from . utils import *
from . update import *
from .progress import ChargingBar
import bmesh


# -----------------------------------------------------------------------------
# Converters from VTK to Blender
# -----------------------------------------------------------------------------


class BVTK_NT_ToBlender(Node, BVTK_Node):
    """Convert output from VTK Node to Blender Mesh Object"""
    bl_idname = 'BVTK_NT_ToBlender'
    bl_label = 'ToBlender'

    def start_scan(self, context):
        if context:
            if self.auto_update:
                bpy.ops.bvtk.auto_update_scan(
                    node_name=self.name,
                    tree_name=context.space_data.node_tree.name)

    mesh_name = bpy.props.StringProperty(name="Name", default="mesh")
    auto_update = bpy.props.BoolProperty(default=False, update=start_scan)
    smooth = bpy.props.BoolProperty(name="Smooth", default=False)
    output_type = bpy.props.EnumProperty(name="Output", default="MESH", items=[
        ("MESH", "Mesh", "Generate a mesh as output", "VIEW3D", 0),
        ("VOLUME", "Volume", "Generate a volume as output. Works only in blender render.", "MOD_CAST", 1),
        ("IMAGE", "Image", "Generate image as output.", "IMAGE_DATA", 2),
        ("TEXT", "Text", "Generate a text object as output.", "FONT_DATA", 3)
    ])
    use_probing = bpy.props.BoolProperty(default=True, name="Probe")
    probe_resolution = bpy.props.IntVectorProperty(name="Resolution", default=(250, 250, 250))

    def m_properties(self):
        return ["mesh_name", "smooth", ]

    def m_connections(self):
        return ["Input"], [], [], []

    def draw_buttons(self, context, layout):
        enable_update = True
        layout.prop(self, "mesh_name")
        layout.prop(self, "auto_update", text="Auto update")
        layout.prop(self, "smooth", text="Smooth")
        layout.prop(self, "output_type", text="Output as")

        render_engine = bpy.context.scene.render.engine
        if self.output_type == "VOLUME":
            if render_engine == "CYCLES" or render_engine == "BLENDER_EEVEE":
                enable_update = False
                error_box(layout, "Volume output is supported only by blender render.")
            else:
                layout.prop(self, "use_probing")
                row = layout.row()
                row.enabled = self.use_probing
                row.prop(self, "probe_resolution")

        row = layout.row()
        row.enabled = enable_update
        row.operator("bvtk.node_update", text="Update").node_path = node_path(self)

    def update_cb(self):
        """Update node"""
        input_node, input_obj = self.get_input_node("Input")
        color_node = None
        if input_node and (input_node.bl_idname == "BVTK_NT_ColorMapper" or
                           input_node.bl_idname == "BVTK_NT_ColorToImage"):
            color_node = input_node
            color_node.update()  # setting auto range
            input_node, input_obj = input_node.get_input_node("Input")
        if input_obj is not None:
            input_obj = resolve_algorithm_output(input_obj)
            output_type = self.output_type
            mesh_name = self.mesh_name
            if output_type == "MESH":
                vtk_data_to_mesh(input_obj, mesh_name, color_node, self.smooth)
            elif output_type == "VOLUME":
                vtk_data_to_volume(input_obj, mesh_name, color_node, use_probing=self.use_probing,
                                   probe_resolution=self.probe_resolution)
            elif output_type == "IMAGE":
                vtk_data_to_image(input_obj, mesh_name, color_node)
            elif output_type == "TEXT":
                vtk_data_to_text(input_obj, mesh_name)
            update_3d_view()

    def apply_properties(self, vtkobj):
        pass


# ---------------------------------------------------------------------------------
# Operator Update
# ---------------------------------------------------------------------------------


class BVTK_OT_NodeUpdate(bpy.types.Operator):
    bl_idname = "bvtk.node_update"
    bl_label = "update"
    node_path = bpy.props.StringProperty()
    use_queue = bpy.props.BoolProperty(default=True)

    def execute(self, context):
        check_cache()
        node = eval(self.node_path)
        if node:
            log.info('Updating from {}'.format(node.name))
            cb = None
            if hasattr(node, "update_cb"):
                cb = node.update_cb
            if self.use_queue:
                update(node, cb)
            else:
                no_queue_update(node, cb)
        self.use_queue = True
        return {'FINISHED'}


# -----------------------------------------------------------------------------
# Operator Write
# -----------------------------------------------------------------------------


class BVTK_OT_NodeWrite(Operator):
    """Operator to call VTK Write() for a node"""
    bl_idname = "bvtk.node_write"
    bl_label = "Write"

    id = bpy.props.IntProperty()

    def execute(self, context):
        check_cache()
        # TODO: retrieve the node with the path, not with the id.
        node = get_node(self.id)
        if node:
            def cb():
                node.get_vtkobj().Write()
            update(node, cb)

        return {'FINISHED'}


# ---------------------------------------------------------------------------------
# Auto Update Scan
# ---------------------------------------------------------------------------------


def map(node, pmap=None):
    """Creates a map which represent
    the status (m_properties and inputs) of
    every node connected to the one given.
    """
    # {} map:        node name -> (nodeprops, nodeinputs)
    # {} nodeprops:  property name -> property value
    # {} nodeinputs: input name -> connected node name

    if not pmap:
        pmap = {}
    props = {}
    for prop in node.m_properties():
        val = getattr(node, prop)
        # Special for arrays. Any other type to include?
        if val.__class__.__name__ == 'bpy_prop_array':
            val = [x for x in val]
        props[prop] = val

    if hasattr(node, 'special_properties'):
        # you can add to a node a function called special_properties
        # to make auto update notice differences outside of m_properties
        props['special_properties'] = node.special_properties()

    links = {}
    for input in node.inputs:
        links[input.name] = ''
        for link in input.links:
            links[input.name] = link.from_node.name
            pmap = map(link.from_node, pmap)
    pmap[node.name] = (props, links)
    return pmap


def differences(map1, map2):
    """Generate differences in properties and inputs of argument maps."""
    props = {}   # differences in properties
    inputs = {}  # differences in inputs
    for node in map1:
        nodeprops1, nodeinputs1 = map1[node]
        if node not in map2:
            props[node] = nodeprops1.keys()
            inputs[node] = nodeinputs1.keys()
        else:
            nodeprops2, nodeinputs2 = map2[node]
            props[node] = compare(nodeprops1, nodeprops2)
            if not props[node]:
                props.pop(node)
            inputs[node] = compare(nodeinputs1, nodeinputs2)
            if not inputs[node]:
                inputs.pop(node)
    return props, inputs


def compare(dict1, dict2):
    """Compare two dictionaries. Return a list of mismatching keys."""
    diff = []
    for k in dict1:
        if k not in dict2:
            diff.append(k)
        else:
            val1 = dict1[k]
            val2 = dict2[k]
            if val1 != val2:
                diff.append(k)
    for k in dict2:
        if k not in dict1:
            diff.append(k)
    return diff


class BVTK_OT_AutoUpdateScan(bpy.types.Operator):
    """BVTK Auto Update Scan"""
    bl_idname = "bvtk.auto_update_scan"
    bl_label = "Auto Update"

    _timer = None
    node_name = bpy.props.StringProperty()
    tree_name = bpy.props.StringProperty()

    def modal(self, context, event):
        if event.type == 'TIMER':
            if self.node_is_valid():
                actual_map = map(self.node)
                props, conn = differences(actual_map, self.last_map)
                if props or conn:
                    self.last_map = actual_map
                    check_cache()
                    try:
                        no_queue_update(self.node, self.node.update_cb)
                    except Exception as e:
                        log.error('ERROR UPDATING ' + str(e))
            else:
                self.cancel(context)
                return {'CANCELLED'}
        return {'PASS_THROUGH'}

    def node_is_valid(self):
        """Node validity test. Return false if node has been deleted or auto
        update has been turned off.
        """
        return self.node.name in self.tree and self.node.auto_update

    def execute(self, context):
        self.tree = bpy.data.node_groups[self.tree_name].nodes
        self.node = bpy.data.node_groups[self.tree_name].nodes[self.node_name]
        self.last_map = map(self.node)
        bpy.ops.bvtk.node_update(node_path=node_path(self.node))
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.01, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)


def cut_excess(original_seq, new_len):
    """Take a blender BMElemSeq and remove
    all items that exceed the new length.
    """
    original_len = len(original_seq)
    if original_len > new_len:
        for i, el in enumerate(original_seq):
            if i > (new_len-1):
                original_seq.remove(el)


def check_mesh_data(data):
    """Check data and return true if it's eligible to be
    converted in a mesh.
    """
    if not has_attributes(data, "GetPoints", "GetPoint",
                          "GetNumberOfCells", "GetCell",
                          "GetNumberOfPoints"):
        return False
    try:
        data.GetPoints()
    except TypeError:
        return False

    return True


def apply_geometry_filter(data):
    """Create and apply a vtk geometry filter to the given data.
    Return the resulting geometry.
    """
    geom = vtk.vtkGeometryFilter()
    geom.SetInputData(data)
    geom.Update()
    return geom.GetOutput()


def vtk_data_to_mesh(data, name, color_node=None, smooth=False):
    """Convert the given vtkdata creating or overwriting
    a blender object named 'name'.
    """
    if not data:
        log.error("No data provided.")
        return

    if not check_mesh_data(data):
        log.warning("Input data is not suitable to be converted in a mesh as it is: "
                    "converting to geometry. The process may take a while, consider adding "
                    "a geometry filter in the node tree to avoid repeating this process.")
        data = apply_geometry_filter(data)
        if not check_mesh_data(data):
            log.error("Data can't be converted to a suitable geometry."
                      "Try changing the output type.")
            return

    me, ob = mesh_and_object(name)
    if me.is_editmode:
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    err = 0
    bm = bmesh.new()
    bm.from_mesh(me)  # fill it in from a mesh

    data_p = data.GetPoints()
    n_points = data.GetNumberOfPoints()
    n_faces = data.GetNumberOfCells()
    verts = []

    # Create vertices
    bm.verts.ensure_lookup_table()
    bar = ChargingBar("Creating vertices", max=n_points)
    for i in range(n_points):
        bar.next()
        if i < len(bm.verts):
            bm.verts[i].co = data_p.GetPoint(i)
            vert = bm.verts[i]
        else:
            vert = bm.verts.new(data_p.GetPoint(i))
        verts.append(vert)
    bar.finish()

    # Remove surplus vertices
    log.info("Removing surplus vertices")
    cut_excess(bm.verts, n_points)

    # Creating faces and edges
    bm.faces.ensure_lookup_table()
    bar = ChargingBar("Creating faces", max=n_faces)
    for i in range(n_faces):
        bar.next()
        data_pi = data.GetCell(i).GetPointIds()
        try:
            face_verts = [verts[data_pi.GetId(x)] for x in range(data_pi.GetNumberOfIds())]
            if len(face_verts) == 2:
                e = bm.edges.get(face_verts)
                if not e:
                    e = bm.edges.new(face_verts)
                # Modified edges are marked with a negative index,
                # so that later unmarked edges can be deleted. This
                # approach is suggested by the blender api documentation.
                e.index = -10
            else:
                f = bm.faces.get(face_verts)
                if not f:
                    f = bm.faces.new(face_verts)
                    f.smooth = smooth
                # Modified faces and edges are marked with a negative index,
                # so that later unmarked edges can be deleted. This
                # approach is suggested by the blender api documentation.
                f.index = -10
                for e in f.edges:
                    e.index = -10
        except:
            err += 1
    bar.finish()

    # Removing surplus faces and edges
    log.info("Removing excess faces.")
    for f in bm.faces:
        if f.index == -10:
            continue
        bm.faces.remove(f)
    log.info("Removing excess edges.")
    for e in bm.edges:
        if e.index == -10:
            continue
        bm.edges.remove(e)

    if err:
        log.info('num err', err)

    # Set normals
    log.info("Setting normals.")
    point_normals = data.GetPointData().GetNormals()
    cell_normals = data.GetCellData().GetNormals()
    if cell_normals:
        bm.faces.ensure_lookup_table()
        for i in range(len(bm.faces)):
            bm.faces[i].normal = cell_normals.GetTuple(i)
    if point_normals:
        for i in range(len(verts)):
            verts[i].normal = point_normals.GetTuple(i)

    # Apply colors and create lut
    if color_node:
        bm = apply_colors(color_node, bm, me, data)

    bm.to_mesh(me)  # Store bmesh to mesh

    log.info('Blender mesh created! {} vertices.'.format(len(verts)))


def mesh_and_object(name):
    """Get or create an object and his mesh and return both."""
    me = get_item(bpy.data.meshes, name)
    ob = get_object(name, me)
    return me, ob


def curve_and_object(name, curve_type):
    """Get or create an object and his curve and return both."""
    curve = get_item(bpy.data.curves, name, curve_type)
    ob = get_object(name, curve)
    return curve, ob


def get_item(data, *args):
    """Get or create the item with key args[0] from data and return it."""
    item = data.get(args[0])
    if not item:
        item = data.new(*args)
    return item


def set_link(data, item):
    """Link item to data if it's not already linked."""
    if item.name not in data:
        data.link(item)


def get_object(name, data):
    """Get or create object, set his data, add it to the current scene."""
    ob = get_item(bpy.data.objects, name, data)

    try:
        # Setting data to an object may rise an error if it's not
        # of the correct type, for example trying to set a mesh
        # as the data of a curve object.
        ob.data = data
    except TypeError:
        bpy.data.objects.remove(ob)
        return get_object(name, data)

    set_link(bpy.context.scene.objects, ob)
    return ob


# ---------------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------------


def get_color_array(data, color_node):
    """Retrieve an array from the given data, based on the
    'color by' selection on the provided color node. If the
    color node is not valid then try to retrieve point data
    scalars or face data scalars. Return a tuple with the
    array and a boolean specifying whether it represents or
    not point data."""
    data_array = None
    is_pd = False

    if not color_node:
        pd = data.GetPointData()
        fd = data.GetCellData()
        if pd and hasattr(pd, "GetScalars"):
            data_array = pd.GetScalars()
            is_pd = True
        elif fd and hasattr(fd, "GetScalars"):
            data_array = fd.GetScalars()
            is_pd = False
    elif color_node.color_by[0] == 'P':
        data_array = data.GetPointData().GetArray(int(color_node.color_by[1:]))
        is_pd = True
    else:
        data_array = data.GetCellData().GetArray(int(color_node.color_by[1:]))
        is_pd = False

    return data_array, is_pd


def apply_colors(color_node, bm, me, data):
    if color_node.color_by:
        texture = color_node.get_texture()
        uv_map = default_uv_map
        mat = None
        if color_node.bl_idname == 'BVTK_NT_ColorToImage':  # todo: move color logic inside node classes
            img = color_node.image
            uv_map = color_node.uv_layer
            if not img:
                log.warning("Image not selected in {} node".format(color_node.name))
            else:
                ramp_to_image(texture.color_ramp, image=img)
        else:
            if color_node.texture_type == "IMAGE":
                img = ramp_to_image(texture.color_ramp, name=texture.name + 'IMAGE')
                mat = image_material(me, me.name, img)
            elif color_node.texture_type == "BLEND":
                mat = blend_material(me, me.name, texture.color_ramp, texture)

        s_range = (color_node.range_min, color_node.range_max)
        array, is_point_data = get_color_array(data, color_node)
        if color_node.lut and mat:
            # The lookup table won't work with the color to image node. The support is not
            # granted because the node will be removed in the next add-on versions.
            create_lut(me.name, s_range, 6, mat, font=color_node.font, h=color_node.height)
        if is_point_data:
            bm = point_unwrap(bm, array, s_range, uv_map)
        else:
            bm = face_unwrap(bm, array, s_range, uv_map)
    return bm


blend_material_prefix = "BVTK Blend "
image_material_prefix = "BVTK Image "
volume_material_prefix = "BVTK Volume "


def blend_material(mesh, name, ramp, texture):
    """Create a blend material and apply it to the given mesh."""
    name = blend_material_prefix + name
    mat, flag = material(mesh, name)
    render_engine = bpy.context.scene.render.engine

    if render_engine == "CYCLES" or render_engine == "BLENDER_EEVEE":
        if not flag or not mat.use_nodes:
            setup_blend_tree(mat, ramp)
        else:
            nodes = mat.node_tree.nodes
            if not update_ramp_nodes(nodes, ramp):
                new_ramp_node(nodes, ramp)
    else:
        if not flag or mat.use_nodes:
            mat.use_nodes = False
            tex, ts = setup_texture(mat, texture, "BLEND")
            ts.texture_coords = "UV"
            ts.uv_layer = default_uv_map
        else:
            add_texture(mat, texture)

    return mat


def image_material(mesh, name, img):
    """Create an image material and apply it to the given mesh."""
    name = image_material_prefix + name
    mat, flag = material(mesh, name)
    render_engine = bpy.context.scene.render.engine

    if render_engine == "CYCLES" or render_engine == "BLENDER_EEVEE":
        if not flag or not mat.use_nodes:
            setup_image_tree(mat, img)
        else:
            nodes = mat.node_tree.nodes
            if not update_image_nodes(nodes, img):
                new_image_node(nodes, img)
    else:
        texture = get_item(bpy.data.textures, name, "IMAGE")
        if not flag or mat.use_nodes:
            mat.use_nodes = False
            tex, ts = setup_texture(mat, texture, "IMAGE")
            ts.texture_coords = "UV"
            ts.uv_layer = default_uv_map
        else:
            add_texture(mat, texture)
        texture.image = img

    return mat


def voxel_material(mesh, name, file_path, texture=None):
    """Create a voxel material and apply it to the given mesh.
    Works only with blender render engine."""
    name = volume_material_prefix + name
    mat, flag = material(mesh, name, type="VOLUME")
    render_engine = bpy.context.scene.render.engine
    if render_engine == "CYCLES" or render_engine == "BLENDER_EEVEE":
        log.warning("Volumetric rendering is not supported in cycles, use blender render instead.")
        return None
    else:
        if not texture:
            texture = get_item(bpy.data.textures, name, "VOXEL_DATA")
        if not flag:
            texture, ts = setup_texture(mat, texture, "VOXEL_DATA")
            mat.volume.density = 0
            texture.voxel_data.file_format = "BLENDER_VOXEL"
            texture.voxel_data.filepath = file_path
            ts.texture_coords = "ORCO"
            ts.use_map_density = True
            ts.use_map_emission = True
            ts.use_map_color_emission = True
            mat.type = "VOLUME"
            mat.volume.density = 0
        else:
            add_texture(mat, texture)
            texture.voxel_data.filepath = file_path
    return mat


def material(mesh, name, reset_previous=True, **material_settings):
    """Get or create a material with the given name and
    return a tuple containing the material and a
    boolean set to true if the material already
    existed."""
    if reset_previous:
        # Remove all other materials from the mesh
        mesh.materials.clear()

    mat = bpy.data.materials.get(name)
    flag = True

    if not mat:
        mat = bpy.data.materials.new(name)
        flag = False

    for key, value in material_settings.items():
        setattr(mat, key, value)

    apply_material(mesh, mat)

    return mat, flag


def apply_material(mesh, mat):
    if mat.name not in mesh.materials:
        mesh.materials.append(mat)


def get_by_attribute(objects, attribute_name, attribute_value):
    for obj in objects:
        if obj.bl_idname:
            if getattr(obj, attribute_name) == attribute_value:
                return obj
    return objects.new(attribute_value)


def get_node_by_idname(nodes, idname):
    return get_by_attribute(nodes, "bl_idname", idname)


def link_nodes(node_a, output_name, node_b, input_name, links):
    from_socket = node_a.outputs[output_name]
    to_socket = node_b.inputs[input_name]
    links.new(to_socket, from_socket)


default_uv_map = "BVTK UV"
image_node_label = "BVTK Image Texture"
ramp_node_label = "BVTK Color Ramp"


def setup_blend_tree(mat, ramp):
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    out_node = get_node_by_idname(nodes, "ShaderNodeOutputMaterial")
    uv_node = get_node_by_idname(nodes, "ShaderNodeUVMap")
    ramp_node = get_node_by_idname(nodes, "ShaderNodeValToRGB")
    customize_ramp_node(ramp_node)
    shader_node = get_node_by_idname(nodes, "ShaderNodeBsdfDiffuse")
    gradient_node = get_node_by_idname(nodes, "ShaderNodeTexGradient")
    links = mat.node_tree.links
    link_nodes(ramp_node, "Color", shader_node, "Color", links)
    link_nodes(gradient_node, "Fac", ramp_node, "Fac", links)
    link_nodes(shader_node, "BSDF", out_node, "Surface", links)
    link_nodes(uv_node, "UV", gradient_node, "Vector", links)
    copy_color_ramp(ramp, ramp_node.color_ramp)
    uv_node.uv_map = default_uv_map


def setup_image_tree(mat, image):
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    img_node = get_node_by_idname(nodes, "ShaderNodeTexImage")
    customize_image_node(img_node)
    shader_node = get_node_by_idname(nodes, "ShaderNodeBsdfDiffuse")
    out_node = get_node_by_idname(nodes, "ShaderNodeOutputMaterial")
    uv_node = get_node_by_idname(nodes, "ShaderNodeUVMap")
    links = mat.node_tree.links
    link_nodes(img_node, "Color", shader_node, "Color", links)
    link_nodes(shader_node, "BSDF", out_node, "Surface", links)
    link_nodes(uv_node, "UV", img_node, "Vector", links)
    img_node.image = image
    uv_node.uv_map = default_uv_map


def new_image_node(nodes, img):
    img_node = nodes.new("ShaderNodeTexImage")
    img_node.image = img
    customize_image_node(img_node)


def new_ramp_node(nodes, ramp):
    ramp_node = nodes.new("ShaderNodeValToRGB")
    copy_color_ramp(ramp, ramp_node.color_ramp)
    customize_ramp_node(ramp_node)


def customize_node(node, node_label):
    node.use_custom_color = True
    node.color = 0.3, 0.4, 0.5
    node.bl_label = node_label


def get_customized_nodes(nodes, node_label):
    c_nodes = []
    for node in nodes:
        if node.bl_label == node_label:
            c_nodes.append(node)
    return c_nodes


def customize_image_node(node):
    customize_node(node, image_node_label)


def update_image_nodes(nodes, img):
    img_nodes = get_customized_nodes(nodes, image_node_label)
    for node in img_nodes:
        node.image = img
    return img_nodes


def customize_ramp_node(node):
    customize_node(node, ramp_node_label)


def update_ramp_nodes(nodes, ramp):
    ramp_nodes = get_customized_nodes(nodes, ramp_node_label)
    for node in ramp_nodes:
        copy_color_ramp(ramp, node.color_ramp)
    return ramp_nodes


def setup_texture(mat, texture, texture_type, **texture_settings):
    texture.type = texture_type
    texture = bpy.data.textures[texture.name]
    for key, value in texture_settings.items():
        setattr(texture, key, value)

    ts = set_active_texture(mat, texture)

    return texture, ts


def add_texture(mat, texture):
    if texture.name not in mat.texture_slots:
        ts = mat.texture_slots.add()
        ts.texture = texture
    else:
        ts = mat.texture_slots[texture.name]
    return ts


def set_active_texture(mat, texture):
    for ts in mat.texture_slots:
        if ts:
            ts.use = False
    ts = add_texture(mat, texture)
    ts.use = True
    return ts


def set_active_material():
    pass


def ramp_to_image(ramp, name=None, image=None, w=2000, h=10):
    """Take a color ramp and create a blender image h pixel tall
    and w pixels wide.
    """
    if not image:
        image = get_item(bpy.data.images, name, w, h)
    else:
        w = image.generated_width
        h = image.generated_height
    p = []
    for y in range(h):
        for x in range(w):
            p.extend(ramp.evaluate(x/w))
    image.pixels = p
    # The image could be deleted automatically by blender
    # if it's not used, this must be prevented setting
    # 'use_fake_user' to true
    image.use_fake_user = True
    # The image has to be packed into the file,
    # otherwise it will be deleted after closing blender.
    image.pack(as_png=True)
    return image


def face_unwrap(bm, array, s_range, uv_layer_key=default_uv_map):
    if array:
        r_min, r_max = s_range
        if r_max == r_min:
            log.warning("Can't unwrap: constant range({}, {}).".format(r_min, r_max))
            return bm
        uv_layer = get_item(bm.loops.layers.uv, uv_layer_key)
        bm.faces.index_update()
        for face in bm.faces:
            for loop in face.loops:
                v = (array.GetValue(face.index) - r_min)/(r_max - r_min)
                # Force value inside range.
                v = min(0.999, max(0.001, v))
                loop[uv_layer].uv = (v, 0.5)
    return bm


def point_unwrap(bm, array, s_range, uv_layer_key=default_uv_map):
    if array:
        r_min, r_max = s_range
        if r_max == r_min:
            log.warning("Can't unwrap: constant range({}, {}).".format(r_min, r_max))
            return bm
        uv_layer = get_item(bm.loops.layers.uv, uv_layer_key)
        bm.verts.index_update()
        for face in bm.faces:
            for loop in face.loops:
                v = (array.GetValue(loop.vert.index) - r_min)/(r_max - r_min)
                # Force value inside range.
                v = min(0.999, max(0.001, v))
                loop[uv_layer].uv = (v, 0.5)
    return bm


# -----------------------------------------------------------------------------
# Color legend
# -----------------------------------------------------------------------------


def text(name, body):
    """Get/create a text data block"""
    font = get_item(bpy.data.curves, name, 'FONT')
    ob = get_object(name, font)
    font.body = body

    return ob


def delete_texts(name):
    """Delete text data block"""
    for ob in bpy.data.objects:
        if ob.name.startswith(name):
            curve = ob.data
            bpy.data.objects.remove(ob)
            bpy.data.curves.remove(curve)


def create_lut(name, data_range, n_div, mat, font="", b=0.5, h=5.5, x=5, y=0, z=0, fontsize=0.35, roundto=2):
    """Create value labels and color legends and add to current scene."""
    # Todo: rewrite and optimize this function
    name = name+'_colormap'
    delete_texts(name+'_lab')  # Delete old labels
    # Create plane and UVs
    plane = bmesh.new()  # Todo: use the plane_bmesh function
    plane.faces.new((
        plane.verts.new((0, 0, 0)),
        plane.verts.new((b, 0, 0)),
        plane.verts.new((b, 0, h)),
        plane.verts.new((0, 0, h)),
    ))
    uv_layer = plane.loops.layers.uv.verify()
    plane.faces.ensure_lookup_table()
    plane.faces[0].loops[0][uv_layer].uv = (0, 1)
    plane.faces[0].loops[1][uv_layer].uv = (0, 0)
    plane.faces[0].loops[2][uv_layer].uv = (1, 0)
    plane.faces[0].loops[3][uv_layer].uv = (1, 1)
    me, ob = mesh_and_object(name)
    plane.to_mesh(me)
    apply_material(me, mat)
    r_min, r_max = data_range
    if r_min > r_max or h <= 0:
        log.error('range maximum greater than minimum')
        return
    import math
    ideal_space = (r_max-r_min)/h
    exponent = math.floor(math.log10(ideal_space))
    mantissa = ideal_space/(10**exponent)
    if mantissa < 2.5:
        step = 10 ** exponent
    elif mantissa < 7.5:
        step = 5*10**exponent
    else:
        step = 10*10**exponent
    start = math.ceil(r_min/step)*step
    delta = r_max-r_min
    if step > delta:
        return
    start_h = (h*(start-r_min))/delta
    step_h = (h*step)/delta

    # Add labels as texts
    for i in range(int(math.floor((r_max-start)/step))+1):
        t = text(name+'_lab'+str(i), '{:.15}'.format(float(start+i*step)))
        t.data.size = fontsize
        if font:
            t.data.font = font
        t.rotation_mode = 'XYZ'
        t.rotation_euler = (1.5707963705062866, 0.0, 0.0)
        t.location = b+b/5, 0, start_h+step_h*i
        t.parent = ob


# -----------------------------------------------------------------------------
#  Text data conversion
# -----------------------------------------------------------------------------


def vtk_data_to_text(data, name):
    cur, ob = curve_and_object(name, "FONT")
    data = str(data)
    cur.body = data

    # Set Aileron Regular instead of the default font
    if cur.font.name == "Bfont":
        if "Aileron-Regular" not in bpy.data.fonts:
            f = bpy.data.fonts.load(os.path.join(addon_path, "Aileron-Regular.otf"))
        else:
            f = bpy.data.fonts["Aileron-Regular"]
        cur.font = f

    log.info("Text created: '{}'.".format(data))


# -----------------------------------------------------------------------------
#  Volume data conversion
# -----------------------------------------------------------------------------


def check_append(dict, key, element):
    """Append the given element in the array
    dict[key].
    """
    dict.setdefault(key, []).append(element)


def parallelepiped(dim, pos=(0, 0, 0), layers=2):
    """Create and return a bmesh parallelepiped with
    the given dimensions, in the given position.
    """
    bm = bmesh.new()
    verts = [{}, {}, {}]  # same x, same y, same z
    for i_z in range(layers):
        for i_y in range(2):
            i_y = i_y if i_z == 0 else 1 - i_y
            for i_x in range(2):
                i_x = i_x if i_y == 0 else 1-i_x
                i_x = i_x if i_z == 0 else 1-i_x
                v = bm.verts.new((pos[0] + dim[0]*i_x,
                                  pos[1] + dim[1]*i_y,
                                  pos[2] + dim[2]*i_z))
                check_append(verts[0], i_x, v)
                check_append(verts[1], i_y, v)
                check_append(verts[2], i_z, v)

    faces = []
    for dict in verts:
        for k in dict:
            if len(dict[k]) > 2:
                faces.append(bm.faces.new(dict[k]))

    bmesh.ops.recalc_face_normals(bm, faces=faces)
    return bm


def scan_coordinates(coordinates):
    """Scan a coordinates array to find if the
    grid is uniform and if it's not the optimal number of
    subdivisions.
    """
    size = coordinates.GetNumberOfValues()
    if size < 2:
        return True, 0

    l_c = None  # Last coordinate
    first_step = coordinates.GetValue(1) - coordinates.GetValue(0)
    is_uniform = True
    is_reverse = False
    gdc_step = multi_gcd(*(coordinates.GetValue(i) for i in range(size)))
    divisions = 1

    for i in range(size):
        val = coordinates.GetValue(i)

        if l_c is not None:
            diff = val - l_c
            n_div = abs(int(diff / gdc_step))
            divisions += n_div

            if diff != first_step:
                is_uniform = False

            if diff < 0:
                is_reverse = True

        l_c = val

    return is_uniform, is_reverse, divisions


def scan_rect_grid(grid):
    coord = [
        ("x", grid.GetXCoordinates()),
        ("y", grid.GetYCoordinates()),
        ("z", grid.GetZCoordinates())
    ]
    reverse_coords = []

    for axis, array in coord:
        is_uniform, is_reverse, div = scan_coordinates(array)
        reverse_coords.append(is_reverse)
        if not is_uniform:
            log.warning("Non uniform coordinates in the {}-axis. It is advisable to use probing.".format(axis))

    return reverse_coords


def reverse_index(i, size, condition=True):
    if condition:
        return size - i - 1
    return i


def probe_grid(data, resolution=(250, 250, 250)):
    x0, x1, y0, y1, z0, z1 = data.GetBounds()

    if hasattr(data, "GetDimensions"):
        nx, ny, nz = data.GetDimensions()
        log.warning("The data has specific dimensions ({}, {}, {}): ignoring the provided resolution."
                    .format(nx, ny, nz))
    else:
        nx, ny, nz = resolution

    struct_p = vtk.vtkStructuredPoints()
    struct_p.SetOrigin(x0, y0, z0)

    struct_p.SetDimensions(nx, ny, nz)
    struct_p.SetSpacing((x1 - x0) / nx, (y1 - y0) / ny, (z1 - z0) / nz)

    probe = vtk.vtkProbeFilter()
    probe.SetInputData(struct_p)
    probe.SetSourceData(data)
    log.warning("Starting probe. The process may take a long time.")
    probe.Update()
    log.warning("Probe complete.")

    probe_out = probe.GetOutput()

    return probe_out


def vtk_data_to_volume(data, name, color_node, use_probing=False, probe_resolution=(250, 250, 250)):
    """Convert vtk volumetric data to a Blender object with a volumetric material."""
    from array import array

    if not color_node:
        log.error("Volume rendering requires a color mapper node. Connect one "
                  "before the 'To Blender' to select the data array and the range.")
        return

    data_array = get_color_array(data, color_node)[0]

    if not data_array:
        log.error("Couldn't retrieve the data array from the color mapper: "
                  "make sure there is a valid 'color by' array selected.")
        return

    # Reverse coordinates
    rx, ry, rz = False, False, False

    if use_probing:
        data = probe_grid(data, probe_resolution)
        data_array = data.GetPointData().GetArray(data_array.GetName())
    elif issubclass(data.__class__, vtk.vtkRectilinearGrid):
        rx, ry, rz = scan_rect_grid(data)

    dim = data.GetDimensions()

    min_r, max_r = color_node.range_min, color_node.range_max

    if color_node.auto_range:
        # Update after probing
        min_r, max_r = data_array.GetRange()

    if max_r == min_r:
        log.error("Can't unwrap: the range is constant ({}, {}). "
                  "Define a valid range and try again.".format(max_r, min_r))
        return

    nx, ny, nz = dim[0], dim[1], dim[2]

    nf = 1
    header = [nx, ny, nz, nf]
    vol_data = []
    i = 0

    bar = ChargingBar("Processing volume", max=(nf * nz))
    for t in range(nf):  # frame
        for z in range(nz):  # layer
            bar.next()
            z = reverse_index(z, nz, rz)

            for y in range(ny):  # line
                y = reverse_index(y, ny, ry)

                for x in range(nx):  # value
                    x = reverse_index(x, nx, rx)
                    index = t*(nx*ny*nz) + z*(nx*ny) + y*nx + x
                    val = (data_array.GetValue(index) - min_r) / (max_r - min_r)
                    vol_data.append(val)
                    i += 1
    bar.finish()

    output_dir = addon_pref("output_path")
    file_path = os.path.join(output_dir, name+".bvox")

    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except OSError:
            log.error("Tmp directory to store volume data couldn't "
                      "be created in path '{}'".format(output_dir))
        else:
            log.info("Tmp directory created in '{}'.".format(output_dir))

    bin_file = open(file_path, 'wb')
    header = array("I", header)
    vol_data = array("f", vol_data)
    header.tofile(bin_file)
    vol_data.tofile(bin_file)
    log.info("Volumetric file created in '{}'.".format(file_path))

    me, ob = mesh_and_object(name)
    parallelepiped(dim, layers=2).to_mesh(me)
    texture = color_node.get_texture()
    voxel_material(me, name, file_path, texture)


# -----------------------------------------------------------------------------
#  Image data conversion
# -----------------------------------------------------------------------------


def plane_bmesh(dim, pos=(0, 0, 0)):
    """Create and return a bmesh parallelepiped with
    the given dimensions, in the given position.
    """
    bm = bmesh.new()
    verts = []  # same x, same y, same z

    for i_y in range(2):
        for i_x in range(2):
            i_x = i_x if i_y == 0 else 1 - i_x
            v = bm.verts.new((pos[0] + dim[0] * i_x,
                              pos[1] + dim[1] * i_y,
                              pos[2]))
            verts.append(v)

    f = [bm.faces.new(verts)]

    bmesh.ops.recalc_face_normals(bm, faces=f)

    return bm


def vtk_data_to_image(data, name, color_node):
    """Convert vtkImageData to a Blender image"""

    wm = bpy.context.window_manager
    data_array = get_color_array(data, color_node)[0]

    if not data_array:
        log.error("Couldn't retrieve the data array from the color mapper: "
                  "make sure there is a color mapper node connected, and "
                  "a valid 'color by' array selected.")
        return

    if color_node:
        data_range = color_node.range_min, color_node.range_max
    else:
        data_range = data_array.GetRange()

    if hasattr(data, "GetDimensions"):
        dim = data.GetDimensions()
    else:
        log.error("Input data isn't suitable to become an image. Please change "
                  "the output type or connect data with defined dimensions.")
        return

    if dim[2] > 1:
        log.warning("Input data has more than one dimension in the z-axis. "
                    "You may try to choose volume as an output type.")

    if name in bpy.data.images:
        bpy.data.images.remove(bpy.data.images[name])
    img = bpy.data.images.new(name, dim[0], dim[1])

    array_size = data_array.GetNumberOfTuples()
    p = []

    bar = ChargingBar('Writing image', max=array_size)
    for j in range(array_size):
        bar.next()
        t = data_array.GetTuple(j)
        tuple_size = len(t)
        if tuple_size == 1:
            val = normalize_value(t[0], data_range)
            p.extend((val, val, val, 1))
        else:
            for val in normalize_tuple(t, data_range):
                p.append(val)
            if tuple_size < 4:
                p.append(1)  # Alpha
    bar.finish()

    img.pixels = p
    log.info("Image created, {} pixels.".format(array_size))

    # Create plane mesh with UVs to show the image
    spacing = data.GetSpacing() if hasattr(data, "GetSpacing") else (1,)
    x = dim[0] * spacing[0]
    y = dim[1] * spacing[0]
    plane = plane_bmesh((x, y, 0))
    uv_layer = get_item(plane.loops.layers.uv, default_uv_map)
    plane.faces.ensure_lookup_table()
    plane.faces[0].loops[0][uv_layer].uv = (0, 0)
    plane.faces[0].loops[1][uv_layer].uv = (1, 0)
    plane.faces[0].loops[2][uv_layer].uv = (1, 1)
    plane.faces[0].loops[3][uv_layer].uv = (0, 1)
    me, ob = mesh_and_object(name)
    ob.location = data.GetOrigin() if hasattr(data, "GetOrigin") else (0, 0, 0)
    plane.to_mesh(me)
    mat = image_material(me, name, img)
    mat.use_shadeless = True


# Add classes and menu items
TYPENAMES = []
add_class(BVTK_NT_ToBlender)
TYPENAMES.append('BVTK_NT_ToBlender')
menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Converter", "Converter", items=menu_items))

add_class(BVTK_OT_NodeUpdate)
add_ui_class(BVTK_OT_AutoUpdateScan)
add_ui_class(BVTK_OT_NodeWrite)
