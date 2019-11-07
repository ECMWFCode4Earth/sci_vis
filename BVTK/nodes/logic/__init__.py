# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   logic/__init__.py
#
#   Define nodes to introduce algorithms logic in the pipeline.
# ---------------------------------------------------------------------------------


from ... utilities import *
from .. core import *


# ---------------------------------------------------------------------------------
# Custom filter
# ---------------------------------------------------------------------------------
class BVTK_NT_CustomFilter(Node, BVTK_Node):
    """A node connected to a python script written by the user,
    to create a vtk object and pass it through the pipeline.
    """
    bl_idname = 'BVTK_NT_CustomFilter'
    bl_label = 'CustomFilter'

    def texts(self, context):
        t = []
        i = 0
        for text in bpy.data.texts:
            t.append((text.name, text.name, text.name, 'TEXT', i))
            i += 1
        if not t:
            t.append(('No texts found', 'No texts found', 'No texts found', 'TEXT', i))
        return t

    def functions(self, context=None):
        f = []
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            for func in t.split('def ')[1:]:
                if '(' in func:
                    name = func.split('(')[0].replace(' ','')
                    f.append((name, name, name))
        return f

    text = bpy.props.EnumProperty(items=texts, name='text')
    func = bpy.props.EnumProperty(items=functions, name='function')

    def m_properties(self):
        return []

    def m_connections(self):
        return ["Input"], [], [], ["Output"]

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)
        row.prop(self, "text")
        op = row.operator("bvtk.new_text", icon="ZOOMIN", text="")
        op.name = "customfilter.py"
        op.body = ("# This file is used for vtk custom filter. \n"
                   "# On update all of this file will be executed. \n"
                   "# To the chosen function will be passed: \n"
                   "# - A list of objects, if custom filter node has multiple links in input. \n"
                   "# - A single object, if custom filter node has a single link in input. \n"
                   "# Your function must return a variable which can be set as input of the \n"
                   "# node following custom filter. \n")
        if len(self.functions()):
            layout.prop(self, "func")
        else:
            layout.label("No functions found in specified text")

    def apply_properties(self, vtkobj):
        """Execute user defined function. If something goes wrong,
        print the error and leave the object as it was before.
        """
        # Acquire each input object
        input_objects = [
            resolve_algorithm_output(x[1]) for x in self.get_input_nodes("Input")
        ]

        if len(input_objects) == 1:
            input_objects = input_objects[0]

        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()

            try:
                exec(t, globals(), locals())
            except Exception as e:
                log.info("Error while parsing user defined text: " +
                         str(e).replace("<string>", self.text))
                return self.get_input_node("Input")[1]

            if self.func in locals():
                try:
                    user_output = eval(self.func + "(input_objects)")
                    self.set_vtkobj(user_output)
                except Exception as e:
                    log.info("Error while executing user defined function:" + str(e))

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socket):
        """Execute user defined function. If something goes wrong,
        print the error and return the input object.
        """
        custom_obj = self.get_vtkobj()

        if custom_obj:
            return custom_obj

        in_node, in_obj = self.get_input_node("Input")
        if in_obj:
            return in_obj

        return None

    def setup(self):
        self.inputs["Input"].link_limit = 300

    def export_properties(self):
        """Export node properties"""
        dict = {}
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            dict["text_as_string"] = t
            dict["text_name"] = self.text
        return dict

    def import_properties(self, dict):
        """Import node properties"""
        bpy.ops.bvtk.new_text(body=dict["text_as_string"], name=dict["text_name"])


class BVTK_OT_NewText(bpy.types.Operator):
    """New text operator"""
    bl_idname = "bvtk.new_text"
    bl_label = "Create a new text"

    name = bpy.props.StringProperty(default="New text")
    body = bpy.props.StringProperty()

    def execute(self, context):
        text = bpy.data.texts.new(self.name)
        text.from_string(self.body)
        flag = True
        areas = context.screen.areas
        for area in areas:
            if area.type == "TEXT_EDITOR":
                for space in area.spaces:
                    if space.type == "TEXT_EDITOR":
                        if flag:
                            space.text = text
                            space.top = 0
                            flag = False
        if flag:
            self.report({"INFO"}, "See '{}' in the text editor.".format(text.name))
        return {"FINISHED"}


# ----------------------------------------------------------------
# Baker
# ----------------------------------------------------------------


class BVTK_NT_Baker(Node, BVTK_Node):
    """VTK time management node for time variant data. Display time sets,
    time values and set time.
    """
    bl_idname = 'BVTK_NT_Baker'
    bl_label = 'Baker'

    def m_properties(self):
        return []

    def m_connections(self):
        return ["Input"], [], [], ["Output"]

    def draw_buttons(self, context, layout):
        baked_obj = self.get_vtkobj()
        operator, label, icon = ("bvtk.node_update", "Bake", "MESH_CUBE") if baked_obj is None \
            else ("bvtk.free_bake", "Rebake", "OBJECT_DATA")
        op = layout.operator(operator, text=label, icon=icon)
        op.node_path = node_path(self)
        if baked_obj:
            box = layout.box()
            box.label(type(baked_obj).__name__)

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def update_cb(self):
        in_node, in_obj = self.get_input_node("Input")
        if in_obj:
            self.set_vtkobj(in_obj)
        else:
            log.warning("Input object is invalid and it hasn't been baked.")

    def input_nodes(self):
        """Return input nodes"""
        # When this method is called by the update function,
        # if the baker node has a baked object it will
        # pretend to be the last node of the pipeline, and the
        # the rest of the tree won't be updated.
        if self.get_vtkobj():
            return []
        else:
            # If the node hasn't a valid baked object the
            # pipeline will be executed as normal.
            nodes = []
            for input in self.inputs:
                for link in input.links:
                    nodes.append(link.from_node)
            return nodes

    def get_output(self, socket):
        """Return the baked object, if there is one,
        otherwise return the input object."""
        baked_obj = self.get_vtkobj()
        if baked_obj:
            return baked_obj

        in_node, in_obj = self.get_input_node("Input")
        if in_obj:
            return in_obj

        return None


# ---------------------------------------------------------------------------------
#     Operator free bake
# ---------------------------------------------------------------------------------


class BVTK_OT_FreeBake(bpy.types.Operator):
    bl_idname = "bvtk.free_bake"
    bl_label = "Free Bake"
    node_path = bpy.props.StringProperty()
    use_queue = bpy.props.BoolProperty(default=True)

    def execute(self, context):
        check_cache()
        node = eval(self.node_path)
        if node:
            node.set_vtkobj(None)  # Remove baked object
            bpy.ops.bvtk.node_update(node_path=self.node_path)
        self.use_queue = True
        return {"FINISHED"}


# ----------------------------------------------------------------
#   Switch
# ----------------------------------------------------------------


class BVTK_NT_Switch(Node, BVTK_Node):
    """ """
    bl_idname = 'BVTK_NT_Switch'
    bl_label = 'Switch'

    def add_case(self, context):
        case_sockets = len(self.inputs) - len(self.m_connections()[0])

        print(case_sockets, self.n_cases)

        while case_sockets > self.n_cases:
            print("Deleting")
            bpy.ops.bvtk.remove_socket(
                node_path=node_path(self),
                socket_idname=BVTK_NS_String.bl_idname,
                socket_index=-2
            )
            case_sockets -= 1

        while case_sockets < self.n_cases:
            bpy.ops.bvtk.add_socket(
                node_path=node_path(self),
                socket_idname=BVTK_NS_String.bl_idname,
                socket_name="Case {}".format(self.n_cases),
                socket_index=-2
            )
            case_sockets += 1

    n_cases = bpy.props.IntProperty(update=add_case, min=0, name="Cases")
    conversion = bpy.props.EnumProperty(items=[
        ("Auto", "Auto", "Auto"),
        ("Float", "Float", "Float"),
        ("Integer", "Integer", "Integer"),
        ("String", "String", "String")
    ])

    def convert_value(self, val):
        func = None

        if self.conversion == "Auto":
            if hasattr(val, "isdigit") and val.isdigit():
                return int(val)

            try:
                return float(val)
            except (TypeError, ValueError):
                pass

            return str(val)

        if self.conversion == "Float":
            func = float
        elif self.conversion == "Integer":
            func = int
        elif self.conversion == "String":
            func = str

        try:
            return func(val)
        except (TypeError, ValueError):
            log.error("Error while converting the input\n" 
                      "variable to compare.")
        return val

    def m_properties(self):
        return []

    def m_connections(self):
        return ["Compare", "Default"], [], [], ["Output"]

    def draw_buttons(self, context, layout):
        layout.prop(self, "conversion", text="Type conversion")
        layout.prop(self, "n_cases")

    def apply_properties(self, vtk_obj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socket):
        compare = self.get_input_node("Compare")[1]
        compare = self.convert_value(compare)

        for socket in self.inputs:
            if socket.bl_idname == BVTK_NS_String.bl_idname:
                val = self.convert_value(socket.value)
                if val == compare:
                    return self.get_input_node(socket.name)[1]

        return self.get_input_node("Default")[1]


class BVTK_NS_String(NodeSocket):
    """BVTK String Node Socket"""
    bl_idname = "BVTK_NS_String"
    bl_label = "BVTK String Socket"

    value = bpy.props.StringProperty()

    def draw(self, context, layout, node, text):
        layout.label(text)
        layout.prop(self, "value", text="")

    def draw_color(self, context, node):
        return 1.0, 0.4, 0.216, 0.5


class BVTK_OT_NodeUpdate(bpy.types.Operator):
    bl_idname = "bvtk.node_update"
    bl_label = "update"
    node_path = bpy.props.StringProperty()
    use_queue = bpy.props.BoolProperty(default=True)

    def execute(self, context):
        check_cache()
        node = eval(self.node_path)
        if node:
            pass
        return {'FINISHED'}


# ----------------------------------------------------------------


cat = "Logic"
register.set_category_icon(cat, "SCRIPTWIN")
add_node(BVTK_NT_CustomFilter, cat)
add_node(BVTK_NT_Baker, cat)
add_node(BVTK_NT_Switch, cat)
register.add_class(BVTK_OT_NewText)
register.add_class(BVTK_OT_FreeBake)
register.add_class(BVTK_NS_String)
