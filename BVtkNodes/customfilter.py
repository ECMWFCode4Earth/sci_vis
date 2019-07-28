from . utils import resolve_algorithm_output, log, node_path, header_box
from . core import *

# -----------------------------------------------------------------------------
# Custom filter
# -----------------------------------------------------------------------------


class BVTK_NT_CustomFilter(Node, BVTK_Node):
    """# This file is used for vtk custom filter.
    # On update all of this file will be executed.
    # To the chosen function will be passed:
    # - A list of objects, if custom filter node has multiple links in input.
    # - A single object, if custom filter node has a single link in input.
    # Your function must return a variable which can be set as input of the
    # node following custom filter.
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
        return (['input'], [], [], ['output'])

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)
        row.prop(self, 'text')
        op = row.operator('bvtk.new_text', icon='ZOOMIN', text='')
        op.name = 'customfilter.py'
        op.body = ('# This file is used for vtk custom filter.'
                   '# On update all of this file will be executed.'
                   '# To the chosen function will be passed:'
                   '# - A list of objects, if custom filter node has multiple links in input.'
                   '# - A single object, if custom filter node has a single link in input.'
                   '# Your function must return a variable which can be set as input of the'
                   '# node following custom filter.')
        if len(self.functions()):
            layout.prop(self, 'func')
        else:
            layout.label('No functions found in specified text')

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socket):
        """Execute user defined function. If something goes wrong,
        print the error and return the input object.
        """
        input_objects = [x[1] for x in self.get_input_nodes('input')]
        if len(input_objects) == 1:
            input_objects = input_objects[0]
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            try:
                exec(t, globals(), locals())
            except Exception as e:
                log.error('error while parsing user defined text: ' +
                          str(e).replace('<string>', self.text))
                return self.get_input_node('input')[1]
            if self.func not in locals():
                log.error('function not found')
            else:
                try:
                    user_output = eval(self.func+'(input_objects)')
                    return user_output
                except Exception as e:
                    log.error('error while executing user defined function:' + str(e))
        return self.get_input_node('input')[1]

    def setup(self):
        self.inputs['input'].link_limit = 300

    def export_properties(self):
        """Export node properties"""
        dict = {}
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            dict['text_as_string'] = t
            dict['text_name'] = self.text
        return dict

    def import_properties(self, dict):
        """Import node properties"""
        bpy.ops.bvtk.new_text(body=dict['text_as_string'], name=dict['text_name'])


class BVTK_OT_NewText(bpy.types.Operator):
    """New text operator"""
    bl_idname = 'bvtk.new_text'
    bl_label = 'Create a new text'

    name = bpy.props.StringProperty(default='New text')
    body = bpy.props.StringProperty()

    def execute(self, context):
        text = bpy.data.texts.new(self.name)
        text.from_string(self.body)
        flag = True
        areas = context.screen.areas
        for area in areas:
            if area.type == 'TEXT_EDITOR':
                for space in area.spaces:
                    if space.type == 'TEXT_EDITOR':
                        if flag:
                            space.text = text
                            space.top = 0
                            flag = False
        if flag:
            self.report({'INFO'}, "See '" + text.name + "' in the text editor")
        return {'FINISHED'}


# ----------------------------------------------------------------
# MultiBlockLeaf
# ----------------------------------------------------------------

class BVTK_NT_MultiBlockLeaf(Node, BVTK_Node):
    """This node breaks down vtkMultiBlock data and outputs one
    user selected block.
    """
    bl_idname = 'BVTK_NT_MultiBlockLeaf'
    bl_label = 'MultiBlockLeaf'

    def blocks(self, context):
        """ Returns a list for a dynamic enum. Once verified that
        the input vtk object is decomposable in blocks, the list
        will contain an element for every block, with the following
        information:
        - Block index
        - Block data type (ex. structured grid)
        - Block custom name (if it's defined, in most cases it's not)
        """
        in_node, vtkobj = self.get_input_node('input')
        if not in_node:
            return []
        elif not vtkobj:
            return []
        else:
            vtkobj = resolve_algorithm_output(vtkobj)
            if not vtkobj:
                return []
            if not hasattr(vtkobj, "GetNumberOfBlocks") or not hasattr(vtkobj, "GetBlock"):
                return []
            items = []
            meta_flag = True if hasattr(vtkobj, "GetMetaData") else False
            for i in range(vtkobj.GetNumberOfBlocks()):
                block = vtkobj.GetBlock(i)
                meta_data = vtkobj.GetMetaData(i) if meta_flag else None
                if meta_data:
                    custom_name = meta_data.Get(vtk.vtkCompositeDataSet.NAME())
                    if not custom_name:
                        custom_name = ""
                else:
                    custom_name = ""
                name = "[" + str(i) + "]: " + custom_name + " (" + \
                       (block.__class__.__name__ if block else "Empty Block") + ")"
                items.append((str(i), name, ""))
            return items

    block = bpy.props.EnumProperty(items=blocks, name="Output block")

    def m_properties(self):
        return []

    def m_connections(self):
        return (['input'], [], [], ['output'])

    def draw_buttons(self, context, layout):
        in_node, vtkobj = self.get_input_node('input')
        if not in_node:
            layout.label('Connect a node')
        elif not vtkobj:
            layout.label('Input has not vtkobj (try updating)')
        else:
            vtkobj = resolve_algorithm_output(vtkobj)
            if not vtkobj:
                return
            class_name = vtkobj.__class__.__name__
            layout.label("Input: "+class_name)
            if not hasattr(vtkobj, "GetNumberOfBlocks") or not hasattr(vtkobj, "GetBlock"):
                layout.label("Input object does not contain multiple blocks of data")
                return
            layout.prop(self, "block")

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socket):
        """Check if the specified block can be retrieved from the input vtk object,
        in case it's possible the said block is returned.
        """
        in_node, vtkobj = self.get_input_node('input')
        if in_node:
            if vtkobj:
                vtkobj = resolve_algorithm_output(vtkobj)
                if vtkobj:
                    if hasattr(vtkobj, "GetNumberOfBlocks") or not hasattr(vtkobj, "GetBlock"):
                        return vtkobj.GetBlock(int(self.block))
        return None


# ----------------------------------------------------------------
# TimeSelector
# ----------------------------------------------------------------


class BVTK_NT_TimeSelector(Node, BVTK_Node):
    """VTK time management node for time variant data. Display time sets,
    time values and set time.
    """
    bl_idname = 'BVTK_NT_TimeSelector'
    bl_label = 'TimeSelector'

    def check_range(self, context):
        in_node, out_port = self.get_input_node('input')
        if in_node:
            if out_port:
                if out_port.IsA('vtkAlgorithmOutput'):
                    prod = out_port.GetProducer()
                    executive = prod.GetExecutive()
                    out_info = prod.GetOutputInformation(out_port.GetIndex())
                    if hasattr(executive, "TIME_STEPS"):
                        time_steps = out_info.Get(executive.TIME_STEPS())
                        if time_steps:
                            size = len(time_steps)
                            if self.time_step < -size:
                                self.time_step = -size
                            elif self.time_step >= size:
                                self.time_step = size-1

    time_step = bpy.props.IntProperty(update=check_range)

    def m_properties(self):
        return []

    def m_connections(self):
        return (['input'], [], [], ['output'])

    def draw_buttons(self, context, layout):
        in_node, out_port = self.get_input_node('input')
        if not in_node:
            layout.label('Connect a node')
        elif not out_port:
            layout.label('Input has not vtkobj (try updating)')
        elif not out_port.IsA('vtkAlgorithmOutput'):
            layout.label('Input is not a vtkAlgorithm.')
        else:
            prod = out_port.GetProducer()
            executive = prod.GetExecutive()
            out_info = prod.GetOutputInformation(out_port.GetIndex())
            if hasattr(executive, "TIME_STEPS"):
                time_steps = out_info.Get(executive.TIME_STEPS())
                if time_steps:
                    row = layout.row()
                    row.prop(self, 'time_step', text="Time step")
                    size = len(time_steps)
                    row.label("Max: "+str(size-1))
                    if -size <= self.time_step < size:
                        layout.label("Time: "+str(time_steps[self.time_step]))
                    else:
                        layout.label('Index out of time steps range', icon='ERROR')
                else:
                    layout.label('Input executive contains a time steps array but it\'s empty.')
            else:
                layout.label('Input executive does not contain any information about time steps.')

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socket):
        """ Check if the input is valid and if the time step can be set.
        If tests pass the time step is updated and the input object is returned,
        otherwise None is returned.
        """
        in_node, out_port = self.get_input_node('input')
        if in_node:
            if out_port:
                if out_port.IsA('vtkAlgorithmOutput'):
                    prod = out_port.GetProducer()
                    executive = prod.GetExecutive()
                    out_info = prod.GetOutputInformation(out_port.GetIndex())
                    if hasattr(executive, "TIME_STEPS"):
                        time_steps = out_info.Get(executive.TIME_STEPS())
                        if time_steps:
                            size = len(time_steps)
                            if -size <= self.time_step < size:
                                if hasattr(prod, "UpdateTimeStep"):
                                    prod.UpdateTimeStep(time_steps[self.time_step])
                                else:
                                    log.warning("ERROR: {} does not have 'UpdateTimeStep' method."
                                                .format(prod.__class__.__name__))
                                    log.warning("If you can, please document this case and report it to the developers.")
                            else:
                                log.warning('ERROR: Index out of time steps range')
                return resolve_algorithm_output(out_port)
        return None


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
        return (['Input'], [], [], ['Output'])

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
        in_node, in_obj = self.get_input_node('Input')
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

        in_node, in_obj = self.get_input_node('Input')
        if in_obj:
            return in_obj

        return None


# ---------------------------------------------------------------------------------
# Operator free bake
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
        return {'FINISHED'}


# ----------------------------------------------------------------


TYPENAMES = []
add_class(BVTK_NT_CustomFilter)
TYPENAMES.append('BVTK_NT_CustomFilter')
add_class(BVTK_NT_MultiBlockLeaf)
TYPENAMES.append('BVTK_NT_MultiBlockLeaf')
add_class(BVTK_NT_TimeSelector)
TYPENAMES.append('BVTK_NT_TimeSelector')
add_class(BVTK_NT_Baker)
TYPENAMES.append('BVTK_NT_Baker')
add_ui_class(BVTK_OT_NewText)
add_ui_class(BVTK_OT_FreeBake)


menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Custom", "Custom", items=menu_items))
