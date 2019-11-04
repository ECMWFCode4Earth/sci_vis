# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   converters/__init__.py
#
#   Define nodes to move VTK data to Blender.
# ---------------------------------------------------------------------------------


from . converter import *
from .. update import *

_modules = [
    "converter",
    "materials"
]

# ---------------------------------------------------------------------------------
#   Converters from VTK to Blender
# ---------------------------------------------------------------------------------


class BVTK_NT_ToBlender(bpy.types.Node, BVTK_Node):
    """Convert output from VTK Node to Blender Mesh Object"""
    bl_idname = 'BVTK_NT_ToBlender'
    bl_label = 'ToBlender'

    def start_scan(self, context):
        if context:
            if self.auto_update:
                bpy.ops.bvtk.auto_update_scan(
                    node_name=self.name,
                    tree_name=context.space_data.node_tree.name)

    def update_z_level(self, context):
        data = self.get_input_node("Input")[1]
        data = resolve_algorithm_output(data)

        if hasattr(data, "GetDimensions"):
            z = data.GetDimensions()[2]
            if self.z_level > z:
                self.z_level = z

    mesh_name = bpy.props.StringProperty(name="Name", default="mesh")
    auto_update = bpy.props.BoolProperty(default=False, update=start_scan)
    smooth = bpy.props.BoolProperty(name="Smooth", default=False)
    output_type = bpy.props.EnumProperty(name="Output", default="MESH", items=[
        ("MESH", "Mesh", "Generate a mesh as output", "VIEW3D", 0),
        ("VOLUME", "Volume", "Generate a volume as output. Works only in blender render.", "MOD_CAST", 1),
        ("IMAGE", "Image", "Generate image as output.", "IMAGE_DATA", 2),
        ("TEXT", "Text", "Generate a text object as output.", "FONT_DATA", 3)
    ])

    # Volume output options
    use_probing = bpy.props.BoolProperty(default=True, name="Probe")
    probe_resolution = bpy.props.IntVectorProperty(name="Resolution", default=(250, 250, 250))
    create_box = bpy.props.BoolProperty(default=True, name="Create box",
                                        description="Create a parallelepiped to display the generated volume")

    # Image output options
    create_plane = bpy.props.BoolProperty(default=True, name="Create plane",
                                          description="Create a plane to display the generated image")
    z_level = bpy.props.IntProperty(default=1, min=1, update=update_z_level)

    # Image output and volume output options
    shift_x = bpy.props.FloatProperty(default=0, name="Shift x", subtype="PERCENTAGE", min=-100, max=100, soft_min=0)
    shift_y = bpy.props.FloatProperty(default=0, name="Shift y", subtype="PERCENTAGE", min=-100, max=100, soft_min=0)

    def m_properties(self):
        return ["mesh_name", "smooth",
                "z_level", "smooth",
                "output_type", "use_probing",
                "probe_resolution", "create_box",
                "create_plane", "shift_x",
                "shift_y"]

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

            layout.prop(self, "use_probing")
            row = layout.row()
            row.enabled = self.use_probing
            row.prop(self, "probe_resolution")
            layout.prop(self, "create_box")

        if self.output_type == "VOLUME" or self.output_type == "IMAGE":
            col = layout.column(align=True)
            col.prop(self, "shift_x")
            col.prop(self, "shift_y")

        if self.output_type == "IMAGE":
            data = self.get_input_node("Input")[1]
            data = resolve_algorithm_output(data)

            if hasattr(data, "GetDimensions"):
                z = data.GetDimensions()[2]
                row = layout.split(percentage=0.3)
                row.prop(self, "z_level", text="")
                row.label(text="Max: {}".format(z))

            layout.prop(self, "create_plane")

        row = layout.row()
        row.enabled = enable_update
        high_op(row, "bvtk.node_update", text="Update").node_path = node_path(self)

    def update_cb(self):
        """Update node"""
        input_node, input_obj = self.get_input_node("Input")
        color_node = None

        if input_node and input_node.bl_idname == "BVTK_NT_ColorMapper":
            color_node = input_node
            color_node.update()  # setting auto range
            input_node, input_obj = input_node.get_input_node("Input")

        if input_obj is not None:
            input_obj = resolve_algorithm_output(input_obj)
            output_type = self.output_type
            mesh_name = self.mesh_name
            shift = -self.shift_x/100, self.shift_y/100

            if output_type == "MESH":
                vtk_data_to_mesh(input_obj, mesh_name, color_node, self.smooth)
            elif output_type == "VOLUME":
                vtk_data_to_volume(input_obj, mesh_name, color_node, use_probing=self.use_probing,
                                   probe_resolution=self.probe_resolution, shift=shift,
                                   create_box=self.create_box)
            elif output_type == "IMAGE":
                vtk_data_to_image(input_obj, mesh_name, color_node, shift, self.create_plane,
                                  self.z_level-1)
            elif output_type == "TEXT":
                vtk_data_to_text(input_obj, mesh_name)

            if color_node and color_node.cl_enable:
                create_color_legend(mesh_name, color_node, color_node.cl_div,
                                    color_node.cl_font, color_node.cl_width,
                                    color_node.cl_height, color_node.cl_font_size)

            update_3d_view()

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass


# ---------------------------------------------------------------------------------
#   Operator add socket
# ---------------------------------------------------------------------------------


class BVTK_OT_AddSocket(bpy.types.Operator):
    bl_idname = "bvtk.add_socket"
    bl_label = "Add socket"

    node_path = bpy.props.StringProperty()
    socket_idname = bpy.props.StringProperty()
    socket_name = bpy.props.StringProperty()
    socket_index = bpy.props.IntProperty(default=-1)
    is_output = bpy.props.BoolProperty(default=False)

    def execute(self, context):
        check_cache()
        node = eval(self.node_path)

        if not node:
            return {"CANCELLED"}

        socket_list = node.inputs

        if self.is_output:
            socket_list = node.outputs

        socket_list.new(
            self.socket_idname,
            self.socket_name
        )

        index = self.socket_index

        if index < 0:
            index = len(socket_list) + index

        socket_list.move(len(socket_list)-1, index)

        return {"FINISHED"}


class BVTK_OT_RemoveSocket(bpy.types.Operator):
    bl_idname = "bvtk.remove_socket"
    bl_label = "Remove socket"

    default_index = 52123121

    node_path = bpy.props.StringProperty()
    socket_idname = bpy.props.StringProperty()
    socket_name = bpy.props.StringProperty()
    socket_index = bpy.props.IntProperty(default=default_index)
    is_output = bpy.props.BoolProperty(default=False)

    def execute(self, context):
        check_cache()
        node = eval(self.node_path)

        if not node:
            return {"CANCELLED"}

        socket_list = node.inputs

        if self.is_output:
            socket_list = node.outputs

        index = self.socket_index

        if index < 0:
            index = len(socket_list) + index

        for i, socket in enumerate(socket_list):
            if socket.bl_idname == self.socket_idname or not self.socket_idname:
                if socket.name == self.socket_name or not self.socket_name:
                    if index == i or index == self.default_index:
                        socket_list.remove(socket)

        return {"FINISHED"}


# ---------------------------------------------------------------------------------
#   Operator Update
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


# ---------------------------------------------------------------------------------
#   Operator Write
# ---------------------------------------------------------------------------------


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
#   Auto Update Scan
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


# Add classes and menu items
cat = "Converters"
add_node(BVTK_NT_ToBlender, cat)
register.set_category_icon(cat, "APPEND_BLEND")
register.add_class(BVTK_OT_NodeUpdate)
register.add_class(BVTK_OT_AutoUpdateScan)
register.add_class(BVTK_OT_NodeWrite)
register.add_class(BVTK_OT_AddSocket)
register.add_class(BVTK_OT_RemoveSocket)
