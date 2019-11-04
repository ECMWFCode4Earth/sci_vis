# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   nodes/core.py
#
#   Contain the base classes for all the nodes, sockets and node categories.
#   Manage the vtk objects cache.
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
#   Modules import
# ---------------------------------------------------------------------------------
import bpy
import vtk
import os
from bpy.types import NodeTree, Node, NodeSocket, Operator, AddonPreferences
from nodeitems_utils import NodeCategory
from .. utilities import *
from . import b_properties  # Boolean properties
b_path = os.path.realpath(b_properties.__file__)  # Boolean properties config file path


# ---------------------------------------------------------------------------------
#   Node Cache and related functions
# ---------------------------------------------------------------------------------
NodesMaxId = 1   # Maximum node id number. 0 means invalid
NodesMap = {}  # node_id -> node
VTKCache = {}  # node_id -> vtkobj


def node_created(node):
    """Add node to Node Cache. Called from node.init() and from
    check_cache. Give the node a unique node_id, then add it in
    NodesMap, and finally instantiate it's vtkobj and store it in
    VTKCache.
    """
    global NodesMaxId, NodesMap, VTKCache  

    # Ensure each node has a node_id
    if node.node_id == 0:
        node.node_id = NodesMaxId
        NodesMaxId += 1
        NodesMap[node.node_id] = node
        VTKCache[node.node_id] = None

    # Create the node vtk_obj if needed
    if node.bl_label.startswith("vtk"):
        vtk_class = getattr(vtk, node.bl_label, None)
        if vtk_class is None:
            log.error("bad classname " + node.bl_label)
            return
        VTKCache[node.node_id] = vtk_class()  # make an instance of node.vtk_class

    log.debug("Node created {} ({})".format(node.bl_label, node.node_id))


def node_deleted(node):
    """Remove node from Node Cache. To be called from node.free().
    Remove node from NodesMap and its vtkobj from VTKCache.
    """
    global NodesMap, VTKCache  
    if node.node_id in NodesMap:
        del NodesMap[node.node_id]

    if node.node_id in VTKCache:
        obj = VTKCache[node.node_id]
        # if obj: 
        #     obj.UnRegister(obj)  # vtkObjects have no Delete in Python -- maybe is not needed
        del VTKCache[node.node_id]
    log.debug("Node deleted {} ({})".format(node.bl_label, node.node_id))


def get_node(node_id):
    """Get node corresponding to node_id."""
    node = NodesMap.get(node_id)
    if node is None:
        log.error("Node not found, node id: {}".format(node_id))
    return node


def get_vtkobj(node):
    """Get the VTK object associated with a node"""
    if node is None:
        log.error("Bad node " + str(node))
        return None

    if node.node_id not in VTKCache:
        log.debug("Node id not in cache: {}".format(node.node_id))
        return None

    return VTKCache[node.node_id]


def set_vtkobj(node, obj):
    """Set the VTK object associated with a node"""
    if node is None:
        log.error("Bad node " + str(node))
        return

    VTKCache[node.node_id] = obj


def init_cache():
    """Initialize Node Cache"""
    global NodesMaxId, NodesMap, VTKCache
    log.debug("Initializing")
    NodesMaxId = 1
    NodesMap = {}
    VTKCache = {}
    check_cache()
    print_nodes()


def check_cache():
    """Rebuild Node Cache. Called by all operators. Cache is out of sync
    if an operator is called and at the same time NodesMaxId=1.
    This happens after reloading addons. Cache is rebuilt, and the
    operator must be interrupted, but the next operator call will work
    OK.
    """
    global NodesMaxId

    # After F8 or FileOpen VTKCache is empty and NodesMaxId == 1
    # any previous node_id must be invalidated
    if NodesMaxId == 1:
        for nt in bpy.data.node_groups:
            if nt.bl_idname == "BVTK_NodeTree":
                for n in nt.nodes:
                    n.node_id = 0

    # For each node check if it has a node_id
    # and if it has a vtk_obj associated
    for nt in bpy.data.node_groups:
        if nt.bl_idname == "BVTK_NodeTree":
            for n in nt.nodes:
                if get_vtkobj(n) is None or n.node_id == 0:
                    node_created(n)


# ---------------------------------------------------------------------------------
#   Add-on preferences
# ---------------------------------------------------------------------------------


class BVTK_AddonPreferences(AddonPreferences):
    """BVTK add-on preferences"""

    bl_idname = "BVTK"
    output_path = bpy.props.StringProperty(default=os.path.join(addon_path, "tmp"),
                                           subtype="FILE_PATH")
    draw_windows = bpy.props.BoolProperty(default=True)

    def get_log_level(self):
        log_lev = log.python_log.getEffectiveLevel()
        lev = logging.CRITICAL
        if log_lev <= logging.DEBUG:
            lev = logging.DEBUG
        elif log_lev <= logging.INFO:
            lev = logging.INFO
        elif log_lev <= logging.WARNING:
            lev = logging.WARNING
        elif log_lev <= logging.ERROR:
            lev = logging.ERROR
        return lev

    def set_log_level(self, value):
        log.python_log.setLevel(value)

    logging_level = bpy.props.EnumProperty(items=[
        (str(logging.DEBUG), "Debug", "Show all types of message", "NONE", logging.DEBUG),
        (str(logging.INFO), "Info", "Show info, warning, error and critical messages", "NONE", logging.INFO),
        (str(logging.WARNING), "Warning", "Show warning, error and critical messages", "NONE", logging.WARNING),
        (str(logging.ERROR), "Error", "Show error and critical messages", "NONE", logging.ERROR),
        (str(logging.CRITICAL), "Critical", "Show only critical messages", "NONE", logging.CRITICAL)
    ], get=get_log_level, set=set_log_level)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "output_path", text="Output directory")
        layout.prop(self, "logging_level", text="Logging detail")
        layout.prop(self, "draw_windows", text="Draw log windows")


# ---------------------------------------------------------------------------------
#   NodeTree
# ---------------------------------------------------------------------------------


class BVTK_NodeTree(NodeTree):
    """BVTK Node Tree"""
    bl_idname = "BVTK_NodeTree"
    bl_label = "BVTK Node Tree"
    bl_icon = "COLOR_RED"


# ---------------------------------------------------------------------------------
#   Custom socket types
# ---------------------------------------------------------------------------------


class BVTK_NodeSocket:
    """Base class for all generated node sockets, for future use."""

    def draw(self, context, layout, node, text):
        layout.label(text)
        a_properties = self.a_properties()
        for arg in a_properties:
            layout.prop(self, arg)

    def draw_color(self, context, node):
        return 0.02, 0.46, 0.64, 0.5


class BVTK_NS_Standard(NodeSocket):
    """BVTK Standard Node Socket"""
    bl_idname = "BVTK_NS_Standard"
    bl_label = "BVTK Node Socket"
    
    def draw(self, context, layout, node, text):
        layout.label(text)

    def draw_color(self, context, node):
        return 1.0, 0.4, 0.216, 0.5


# ---------------------------------------------------------------------------------
#   Base class for all BVTK_Nodes
# ---------------------------------------------------------------------------------
class BVTK_Node:
    """Base class for VTK Nodes"""

    node_id = bpy.props.IntProperty(default=0)

    @classmethod
    def poll(cls, node_tree):
        return node_tree.bl_idname == "BVTK_NodeTree"

    def free(self):
        node_deleted(self)

    def get_output(self, socket):
        """Get output object. Return an object depending on socket
        name. Used to simplify custom node usage such as info
        node and custom filter.
        """
        vtkobj = self.get_vtkobj()
        if socket.bl_idname == "BVTK_NS_Standard":  # socket is not generated
            socketname = socket.name
            if not vtkobj:
                return None
            if socketname == "Self":
                return vtkobj
            if socketname == "Output" or socketname == "Output 0":
                return vtkobj.GetOutputPort()
            if socketname == "Output 1":
                return vtkobj.GetOutputPort(1)
            else:
                log.critical("Bad output link name: '{}'".format(socketname))
                return None
            # TODO: handle output 2,3,....
        else:
            function_name = socket.bl_label  # function to call
            if not hasattr(vtkobj, function_name):
                log.critical("Socket function {} not found!".format(function_name))
                return None
            args = [getattr(socket, prop) for prop in socket.a_properties()]
            return getattr(vtkobj, function_name)(*args)

    def get_input_nodes(self, name):
        """Return inputs of a node. Name argument specifies the type of inputs:
        'Self'                 -> input_node.get_vtkobj()
        'Output' or 'Output 0' -> get_vtkobj().getOutputPort()
        'Output x'             -> get_vtkobj().getOutputPort(x)
        """
        if name not in self.inputs:
            return []
        input = self.inputs[name]
        if len(input.links) < 1:  # is_linked could be true even with 0 links
            return []
        nodes = []
        for link in input.links:
            input_node = link.from_node
            input_socket = link.from_socket
            if not input_node:
                continue
            nodes.append((input_node, input_node.get_output(input_socket)))
        return nodes

    def get_input_node(self, *args):
        """Return input of a node"""
        nodes = self.get_input_nodes(*args)
        if nodes:
            return nodes[0]
        return 0, 0

    def input_nodes(self):
        """Return input nodes"""
        nodes = []
        for input in self.inputs:
            for link in input.links:
                nodes.append(link.from_node)
        return nodes

    def get_vtkobj(self):
        """Shortcut to get vtkobj"""
        return get_vtkobj(self)

    def set_vtkobj(self, obj):
        """Shortcut to set vtkobj"""
        set_vtkobj(self, obj)

    def draw_buttons(self, context, layout):
        m_properties = self.m_properties()
        for i in range(len(m_properties)):
            if self.b_properties[i]:
                layout.prop(self, m_properties[i])
        if self.bl_idname.endswith("Writer"):
            high_op(layout, "bvtk.node_write").id = self.node_id

    def copy(self, node):
        """Copies setup from another node"""
        self.node_id = 0
        check_cache()

        if hasattr(self, 'copy_setup'):
            # some nodes need to set properties (such as color ramp elements)
            # after being copied
            self.copy_setup(node)

    def apply_properties(self, vtk_obj):
        """Sets properties from node to vtk object based on property name"""
        m_properties = self.m_properties()

        for x in [m_properties[i] for i in range(len(m_properties)) if self.b_properties[i]]:

            # SetXFileName(Y)
            if "FileName" in x:
                value = os.path.realpath(bpy.path.abspath(getattr(self, x)))
                cmd = "vtk_obj.Set{}(value)".format(x[2:])

            # SetXToY()
            elif x.startswith("e_"):
                value = getattr(self, x)
                cmd = "vtk_obj.Set{}To{}()".format(x[2:], value)

            # SetX(self.Y)
            else:
                cmd = "vtk_obj.Set{}(self.{})".format(x[2:], x)

            exec(cmd, globals(), locals())

        if hasattr(self, "apply_properties_setup"):
            # some nodes need to set perform special actions
            # after default properties application
            self.apply_properties_setup(vtk_obj)

    def apply_inputs(self, vtk_obj):
        """Set node inputs/connections to vtk object"""
        input_ports, output_ports, extra_input, extra_output = self.m_connections()

        for i, name in enumerate(input_ports):
            input_node, input_obj = self.get_input_node(name)

            if input_node:

                if vtk_obj:

                    if input_obj.IsA("vtkAlgorithmOutput"):
                        vtk_obj.SetInputConnection(i, input_obj)
                    else:
                        # needed for custom filter
                        vtk_obj.SetInputData(i, input_obj)

        for name in extra_input:
            input_node, input_obj = self.get_input_node(name)

            if input_node:

                if vtk_obj:
                    cmd = "vtk_obj.Set{}(resolve_algorithm_output(input_obj))".format(name)
                    exec(cmd, globals(), locals())

    def init(self, context):
        """Initialize node"""
        self.width = 200
        self.use_custom_color = True
        self.color = 0.5, 0.5, 0.5
        check_cache()
        input_ports, output_ports, extra_input, extra_output = self.m_connections()
        input_ports.extend(extra_input)
        output_ports.extend(extra_output)

        for x in input_ports:
            self.inputs.new("BVTK_NS_Standard", x)

        for x in output_ports:
            self.outputs.new("BVTK_NS_Standard", x)

        # Some nodes need to set properties (such as link limit) after creation
        if hasattr(self, "setup"):
            self.setup()

    def get_b(self):
        """Get boolean property"""
        return b_properties.b[self.bl_idname]

    def set_b(self, value):
        """Set boolean property a value and update boolean properties file"""
        b_properties.b[self.bl_idname] = [v for v in value]
        bpy.ops.node.select_all(action="SELECT")
        bpy.ops.node.select_all(action="DESELECT")

        # Write sorted b_properties.b dictionary
        # Note: lambda function used to force sort on dictionary key
        txt = "b={"
        for key, value in sorted(b_properties.b.items(), key=lambda s: str.lower(s[0])):
            txt += " '" + key + "': " + str(value) + ",\n"
        txt += "}\n"
        open(b_path, "w").write(txt)


# ---------------------------------------------------------------------------------
#   Registering
# ---------------------------------------------------------------------------------


def add_node(obj, category=""):
    """Register a node class and check if the number of b_properties is correct
    and matches the number of m_properties. If it's not, fix it.
    """
    if hasattr(obj, "m_properties") and hasattr(obj, "b_properties"):
        np = len(obj.m_properties(obj))
        name = obj.bl_idname
        b = b_properties.b

        if (not name in b) or (name in b and len(b[name]) != np):
            b[name] = [True for i in range(np)]

    register.add_class(obj, obj.bl_idname)

    if category:
        register.node_to_category(category, obj)


# Register classes
register.add_class(BVTK_NodeTree)
register.add_class(BVTK_AddonPreferences)
register.add_class(BVTK_NS_Standard)
register.add_class(BVTK_OT_TogglePanel)


# ---------------------------------------------------------------------------------
#   BVTK Node Category
# ---------------------------------------------------------------------------------


class BVTK_NodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == "BVTK_NodeTree"


register.set_node_category(BVTK_NodeCategory)


# ---------------------------------------------------------------------------------
#   Debug utilities
# ---------------------------------------------------------------------------------


def ls(o):
    log.debug("\n".join(sorted(dir(o))))


def print_cls(obj):
    log.debug("------------------------------")
    log.debug("Class = " + obj.__class__.__name__)
    log.debug("------------------------------")
    for m in sorted(dir(obj)):
        if not m.startswith("__"):
            attr = getattr(obj, m)
            rep = str(attr)
            if len(rep) > 100:
                rep = rep[:100] + "  [...]"
            log.debug(m.ljust(30) + "=" + rep)


def print_nodes(): 
    log.debug("maxid = " + str(NodesMaxId))
    for nt in bpy.data.node_groups:
        if nt.bl_idname == "BVTK_NodeTree":
            log.debug("tree " + nt.name)
            for n in nt.nodes:
                if get_vtkobj(n) is None:
                    x = ""
                else:
                    x = "VTK object"
                log.debug("node " + str(n.node_id) + ": " + n.name.ljust(30, " ") + x)
