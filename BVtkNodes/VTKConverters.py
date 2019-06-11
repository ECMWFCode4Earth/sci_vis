from .update import *
from .core import *
import bmesh
TYPENAMES = []

# ----------------------------------------------------------------


class VTK2Blender(Node, VTKNode):

    bl_idname = 'VTK2BlenderType'  # type name
    bl_label = 'ToBlender'        # label for nice name display

    def start_scan(self, context):
        if context:
            if self.auto_update:
                bpy.ops.vtk.auto_update_scan(node_name=self.name,
                                             tree_name=context.space_data.node_tree.name)

    m_Name = bpy.props.StringProperty(name='Name', default='mesh')
    auto_update = bpy.props.BoolProperty(default=False, update=start_scan)
    auto_center = bpy.props.BoolProperty(default=False)  # todo: delete this
    smooth = bpy.props.BoolProperty(name='Smooth', default=False)

    def m_properties(self):
        return ['m_Name', 'smooth', ]

    def m_connections(self):
        return ( ['input'],[],[],[] )

    def draw_buttons(self, context, layout):
        layout.prop(self, 'm_Name')
        layout.prop(self, 'auto_update', text='Auto update')
        layout.prop(self, 'smooth', text='Smooth')
        # layout.box().prop(self, "auto_center", text='auto center', expand=True)
        layout.separator()
        layout.operator("node.update", text="update").node_path = node_path(self)

    def update_cb(self):
        input_node, vtkobj = self.get_input_node('input')
        color_node = None
        if input_node and (input_node.bl_idname == 'VTKColorMapperType' or
                           input_node.bl_idname == 'VTKColorToImageType'):
            color_node = input_node
            color_node.update()    # setting auto range
            input_node, vtkobj = input_node.get_input_node('input')
        if vtkobj:
            vtkobj = resolve_algorithm_output(vtkobj)
            vtkdata_to_blender(vtkobj, self.m_Name, color_node, self.smooth)
            update_3d_view()

    def apply_properties(self, vtkobj):
        pass

add_class(  VTK2Blender )
TYPENAMES.append( 'VTK2BlenderType' )


# ----------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory("converters", "converters", items=menu_items) )

# ---------------------------------------------------------------------------------
# OperatorNodeUpdate
# ---------------------------------------------------------------------------------

class OperatorNodeUpdate(bpy.types.Operator):
    bl_idname = "node.update"
    bl_label = "update"
    node_path = bpy.props.StringProperty()
    use_queue = bpy.props.BoolProperty(default = True)

    def execute(self, context):
        check_cache()
        node = eval(self.node_path)
        if node:
            print('Updating from: '+node.name)
            if self.use_queue:
                Update(node, node.update_cb)
            else:
                no_queue_update(node, node.update_cb)
        self.use_queue = True
        return {'FINISHED'}

add_class(OperatorNodeUpdate)

# ---------------------------------------------------------------------------------
# Auto Update Scan
# ---------------------------------------------------------------------------------

def map(node, pmap = None):
    """ returns a map, which represent
    the status (m_properties and inputs) of
    every node connected to the one given.
    {} map:   node name -> (nodeprops, nodeinputs)
    {} nodeprops:  property name -> property value
    {} nodeinputs: input name -> connected node name """
    if not pmap:
        pmap = {}
    props = {}
    for prop in node.m_properties():
        val = getattr(node, prop)
        if val.__class__.__name__ == 'bpy_prop_array':
            # this is for arrays. Is there
            # any other strange bpy type?
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
    """ compares two dictionaries and returns
    a list of mismatching keys """
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


class VTKAutoUpdateScan(bpy.types.Operator):
    """ . """
    bl_idname = "vtk.auto_update_scan"
    bl_label = "auto update"
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
                        print('ERROR UPDATING -- '+str(e))
            else:
                self.cancel(context)
                return {'CANCELLED'}
        return {'PASS_THROUGH'}

    def node_is_valid(self):    # returns false if node has been deleted or auto update has been turned off
        return self.node.name in self.tree and self.node.auto_update

    def execute(self, context):
        self.tree = bpy.data.node_groups[self.tree_name].nodes
        self.node = bpy.data.node_groups[self.tree_name].nodes[self.node_name]
        self.last_map = map(self.node)
        bpy.ops.node.update(node_path=node_path(self.node))
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.01, context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)

add_ui_class(VTKAutoUpdateScan)

# ---------------------------------------------------------------------------------
# vtkdata_to_blender
# ---------------------------------------------------------------------------------


def cut_excess(original_seq, new_len):
    # Takes a blender BMElemSeq (basically an array)
    # and removes all items that exceed the new length
    original_len = len(original_seq)
    if original_len > new_len:
        for i, el in enumerate(original_seq):
            if i > (new_len-1):
                original_seq.remove(el)


def vtkdata_to_blender(data, name, color_node=None, smooth=False):
    """ convert the given vtkdata
    creating or overwriting a blender object named 'name' """
    if not data:
        print('vtkdata_to_blender -- no data!')
        return
    if issubclass(data.__class__, vtk.vtkImageData):
        imgdata_to_blender(data, name)
        return
    me, ob = mesh_and_object(name)
    if me.is_editmode:
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    err = 0
    bm = bmesh.new()
    bm.from_mesh(me)  # fill it in from a Mesh
    # Create vertices
    data_p = data.GetPoints()
    bm.verts.ensure_lookup_table()
    verts = []
    verbose("Creating vertices")
    for i in range(data.GetNumberOfPoints()):
        if i < len(bm.verts):
            bm.verts[i].co = data_p.GetPoint(i)
            vert = bm.verts[i]
        else:
            vert = bm.verts.new(data_p.GetPoint(i))
        verts.append(vert)
    # Remove surplus vertices
    verbose("Removing surplus vertices")
    cut_excess(bm.verts, data.GetNumberOfPoints())
    # Creating faces and edges
    bm.faces.ensure_lookup_table()
    verbose("Creating faces")
    for i in range(data.GetNumberOfCells()):
        data_pi = data.GetCell(i).GetPointIds()
        try:
            face_verts = [verts[data_pi.GetId(x)] for x in range(data_pi.GetNumberOfIds())]
            if len(face_verts) == 2:
                e = bm.edges.get(face_verts)
                if not e:
                    e = bm.edges.new(face_verts)
                e.index = -10
            else:
                f = bm.faces.get(face_verts)
                if not f:
                    f = bm.faces.new(face_verts)
                    f.smooth = smooth
                f.index = -10
                for e in f.edges:
                    e.index = -10
        except:
            err += 1
    # Removing surplus faces and edges
    verbose("Removing excess faces")
    for f in bm.faces:
        if f.index == -10:
            continue
        bm.faces.remove(f)
    verbose("Removing excess edges")
    for e in bm.edges:
        if e.index == -10:
            continue
        bm.edges.remove(e)

    if err:
        print('num err', err)

    # set normals
    point_normals = data.GetPointData().GetNormals()
    cell_normals = data.GetCellData().GetNormals()
    if cell_normals:
        bm.faces.ensure_lookup_table()
        for i in range(len(bm.faces)):
            bm.faces[i].normal = cell_normals.GetTuple(i)
    if point_normals:
        for i in range(len(verts)):
            verts[i].normal = point_normals.GetTuple(i)

    # apply colors and create lut
    if color_node:
        bm = apply_colors(color_node, bm, me, data)

    bm.to_mesh(me)  # store bmesh to mesh

    print('vtkdata_to_blender -- ok!  -- num verts =', len(verts))

    #if (autoCenter):
    #    bpy.data.objects[me.name].select = True
    #    context.scene.objects.active = bpy.data.objects[me.name]
    #    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')


def mesh_and_object(name):
    """ method gets/creates an object and his mesh and returns both """
    me = get_item(bpy.data.meshes, name)
    ob = get_object(name, me)
    return me, ob


def get_item(data, *args):
    """ method gets/creates the item with key args[0] from data and return it """
    item = data.get(args[0])
    if not item:
        item = data.new(*args)
    return item


def set_link(data, item):
    """ method links item to data if item isn't already linked """
    if item.name not in data:
        data.link(item)


def get_object(name, data):
    """ method gets/creates object, sets his data, adds it to current scene """
    ob = get_item(bpy.data.objects, name, data)
    ob.data = data
    set_link(bpy.context.scene.objects, ob)
    return ob

# ---------------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------------


def apply_colors(color_node, bm, me, data):
    if color_node.color_by:
        texture = color_node.get_texture()
        color_by = color_node.color_by
        uv_layer = ""
        if color_node.bl_idname == 'VTKColorToImageType':  # todo: move color logic inside node classes
            img = color_node.image
            uv_layer = color_node.uv_layer
            if not img:
                print("Image not selected in {} node".format(color_node.name))
            else:
                ramp_to_image(texture.color_ramp, image=img)
        else:
            if color_node.texture_type == 'IMAGE':
                img = ramp_to_image(texture.color_ramp, name=texture.name + 'IMAGE')
                texture = get_item(bpy.data.textures, texture.name + 'IMAGE', 'IMAGE')
                texture.image = img
            texture_material(me, 'VTK' + me.name, texture)

        s_range = (color_node.min, color_node.max)
        if color_node.lut:
            create_lut(me.name, s_range, 6, texture, font=color_node.font, h=color_node.height)
        if color_by[0] == 'P':
            bm = point_unwrap(bm, data, int(color_by[1:]), s_range, uv_layer)
        else:
            bm = face_unwrap(bm, data, int(color_by[1:]), s_range, uv_layer)
    return bm


def texture_material(me, name, texture = None, texturetype = 'IMAGE'):
    """ method gets/creates a material and link to it the given texture,
    then apply it to given mesh. If texture isn't given one is created
    """
    if not texture:
        texture = get_item(bpy.data.textures, name, texturetype)
        texture.type = texturetype
    mat = get_item(bpy.data.materials, name)
    if mat.name not in me.materials:
        me.materials.append(mat)
    for ts in mat.texture_slots:  # disabling all other textures
        if ts:
            ts.use = False
    if texture.name not in mat.texture_slots:
        ts = mat.texture_slots.add()
        ts.texture = texture
        ts.texture_coords = 'UV'
    else:
        ts = mat.texture_slots[texture.name]
    ts.use = True
    return texture, mat


def ramp_to_image(ramp, name=None, image=None, w=1000, h=1):
    """ takes a color ramp and creates a blender image h pixel tall
    and w pixels wide. """
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
    return image


def face_unwrap(bm, data, array_index, s_range, uv_layer_key=""):
    scalars = data.GetCellData().GetArray(array_index)
    if scalars is not None:
        min, max = s_range
        if max == min:
            print("Can't unwrap, values are constant: range({},{})!".format(min, max))
            return bm
        uv_layer = bm.loops.layers.uv.get(uv_layer_key)
        if not uv_layer:
            uv_layer = bm.loops.layers.uv.verify()
        bm.faces.index_update()
        for face in bm.faces:
            for loop in face.loops:
                v = (scalars.GetValue(face.index)-min)/(max-min)
                loop[uv_layer].uv = (v, 0.5)
    return bm


def point_unwrap(bm, data, array_index, s_range, uv_layer_key=""):
    scalars = data.GetPointData().GetArray(array_index)
    if scalars is not None:
        min, max = s_range
        if max == min:
            print("Can't unwrap, values are constant: range({},{})!".format(min, max))
            return bm
        uv_layer = bm.loops.layers.uv.get(uv_layer_key)
        if not uv_layer:
            uv_layer = bm.loops.layers.uv.verify()
        bm.verts.index_update()
        for face in bm.faces:
            for loop in face.loops:
                v = (scalars.GetValue(loop.vert.index)-min)/(max-min)
                loop[uv_layer].uv = (v, 0.5)
    return bm


# ---------------------------------------------------------------------------------
# scalarbar to blender
# ---------------------------------------------------------------------------------


def text(name, body):
    """ method gets/creates a text object """
    font = get_item(bpy.data.curves, name, 'FONT')
    ob = get_object(name, font)
    font.body = body
    return ob


def delete_texts(name):
    for ob in bpy.data.objects:
        if ob.name.startswith(name):
            curve = ob.data
            bpy.data.objects.remove(ob)
            bpy.data.curves.remove(curve)


def create_lut(name, Range, n_div, texture, font="", b=0.5, h=5.5, x=5, y=0, z=0, fontsize=0.35, roundto=2):
    """ method creates a lookuptable and adds it to current scene """
    name = name+'_colormap'
    delete_texts(name+'_lab')
    plane = bmesh.new()
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
    # ob.location = x,y,z
    texture_material(me, name, texture)
    min, max = Range
    if min>max or h<=0:
        print('Range maximum greater than minimum')
        return
    import math
    idealspace = (max-min)/(h)
    exponent = math.floor(math.log10(idealspace))
    mantissa = idealspace/(10**exponent)
    if mantissa < 2.5:
        step = 10 ** exponent
    elif mantissa < 7.5:
        step = 5*10**exponent
    else:
        step = 10*10**exponent
    start = math.ceil(min/step)*step
    delta = max-min
    if step>delta:
        return
    starth = (h*(start-min))/delta
    steph = (h*step)/delta
    for i in range(int(math.floor((max-start)/step))+1):
        t = text(name+'_lab'+str(i), '{:.15}'.format(float(start+i*step)))
        t.data.size = fontsize
        if font: t.data.font = font
        t.rotation_mode = 'XYZ'
        t.rotation_euler = (1.5707963705062866, 0.0, 0.0)
        t.location = b+b/5, 0, starth+steph*i
        t.parent = ob


# ---------------------------------------------------------------------------------
#  imgdata_to_blender
# ---------------------------------------------------------------------------------


def imgdata_to_blender(data, name):
    """ Takes a vtkImageData and stores
    it as an image in blender memory
    """
    wm = bpy.context.window_manager
    scalars = data.GetPointData().GetScalars()
    dim = data.GetDimensions()
    z = 0
    wm.progress_begin(0, 100)
    if name in bpy.data.images:
        bpy.data.images.remove(bpy.data.images[name])
    img = bpy.data.images.new(name, dim[0], dim[1])
    l = scalars.GetNumberOfTuples()
    p = []
    prog = 0
    l_prog = 1
    for j in range(l):
        t = scalars.GetTuple(j)
        if len(t) == 1:
            p.extend([t[0] / 255, t[0] / 255, t[0] / 255, 1])
        else:
            alpha = 1 if len(t)<4 else t[3]/255
            p.extend([t[0]/255, t[1]/255, t[2]/255, alpha])

        prog = int(j/l*100)
        if prog != l_prog:
            l_prog = prog
            wm.progress_update(prog)
            print('Converting to img: '+str(prog)+'%', end='\r'),
    img.pixels = p
    wm.progress_end()
    print('imgdata_to_blender -- ok! -- num pixels = '+str(l))
    spacing = data.GetSpacing()
    x = dim[0] * spacing[0]
    y = dim[1] * spacing[0]
    plane = bmesh.new()
    plane.faces.new((
        plane.verts.new((0, 0, 0)),
        plane.verts.new((x, 0, 0)),
        plane.verts.new((x, y, 0)),
        plane.verts.new((0, y, 0)),
    ))
    uv_layer = plane.loops.layers.uv.verify()
    plane.faces.ensure_lookup_table()
    plane.faces[0].loops[0][uv_layer].uv = (0, 0)
    plane.faces[0].loops[1][uv_layer].uv = (1, 0)
    plane.faces[0].loops[2][uv_layer].uv = (1, 1)
    plane.faces[0].loops[3][uv_layer].uv = (0, 1)
    me, ob = mesh_and_object(name)
    ob.location = data.GetOrigin()
    plane.to_mesh(me)
    tex, mat = texture_material(me, 'VTK' + name)
    mat.use_shadeless = True
    tex.image = img

add_ui_class(VTKFunctionQueue)

