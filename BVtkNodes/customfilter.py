from .core import *
TYPENAMES = []

# ----------------------------------------------------------------
# Custom filter
# ----------------------------------------------------------------


class VTKCustomFilter(Node, VTKNode):
    """# This file is used for vtk custom filter.
    # On update all of this file will be executed.
    # To the chosen function will be passed:
    # - A list of objects, if custom filter node has multiple links in input.
    # - A single object, if custom filter node has a single link in input.
    # Your function must return a variable which can be set as input of the
    # node following custom filter.
    """
    bl_idname = 'VTKCustomFilterType'
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
        op = row.operator('vtk.new_text', icon='ZOOMIN', text='')
        op.name = 'customfilter.py'
        op.body = self.__doc__.replace("    ","")
        if len(self.functions()):
            layout.prop(self, 'func')
        else:
            layout.label('No functions found in specified text')

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socketname):
        """ execute user defined function.
         If something goes wrong print the error and
        return the input object.
         """
        input_objects = [x[1] for x in self.get_input_nodes('input')]
        if len(input_objects) == 1:
            input_objects = input_objects[0]
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            try:
                exec(t, globals(), locals())
            except Exception as e:
                print('VTKCustomFilter - error while parsing user defined text:',
                      str(e).replace('<string>', self.text))
                return self.get_input_node('input')[1]
            if self.func not in locals():
                print('VTKCustomFilter - function not found')
            else:
                try:
                    user_output = eval(self.func+'(input_objects)')
                    return user_output
                except Exception as e:
                    print('VTKCustomFilter - error while executing user defined function:',str(e))
        return self.get_input_node('input')[1]

    def setup(self):
        self.inputs['input'].link_limit = 300

    def export_properties(self):
        """ called on export """
        dict = {}
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            dict['text_as_string'] = t
            dict['text_name'] = self.text
        return dict

    def import_properties(self, dict):
        """ called on import """
        bpy.ops.vtk.new_text(body=dict['text_as_string'], name=dict['text_name'])

add_class(VTKCustomFilter)
TYPENAMES.append('VTKCustomFilterType')

# ----------------------------------------------------------------
# New text operator
# ----------------------------------------------------------------


class VTKNewText(bpy.types.Operator):
    bl_idname = 'vtk.new_text'
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
            self.report({'INFO'}, "See '"+text.name+"' in the text editor")
        return {'FINISHED'}


add_ui_class(VTKNewText)


# ----------------------------------------------------------------
# MultiBlockLeaf
# ----------------------------------------------------------------


class VTKMultiBlockLeaf(Node, VTKNode):
    """ This node is useful to break down a vtkMultiBlock
    into the blocks of which it is composed.
    """
    bl_idname = 'VTKMultiBlockLeafType'
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
                    if not custom_name: custom_name = ""
                else:
                    custom_name = ""
                name = str(i) + " " + (block.__class__.__name__ if block else "Empty block") + custom_name
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
                layout.label("Input object does not contain multiple blocks of data (can't find 'GetBlock' method)")
                return
            layout.prop(self, "block")

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socketname):
        """ The function checks if the specified block can be retrieved from the input vtk object,
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


add_class(VTKMultiBlockLeaf)
TYPENAMES.append('VTKMultiBlockLeafType')

# ----------------------------------------------------------------
# MultiBlockLeaf
# ----------------------------------------------------------------


class VTKTimeSetter(Node, VTKNode):
    """ This node provides the possibility o managing time.
    It displays time sets, time values and shows a property to set them.
    """
    bl_idname = 'VTKTimeSetterType'
    bl_label = 'TimeSetter'

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
        else:
            if out_port.IsA('vtkAlgorithmOutput'):
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
            else:
                layout.label('Input is not a vtkAlgorithm. Executive cannot be retrieved and time cannot be set.')

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socketname):
        """ Checks if the input is valid and if the time step can be set.
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
                                    print("ERROR: "+prod.__class__.__name__+" does not have 'UpdateTimeStep' method.")
                                    print("If you can, please document this case and report it to the developers.")
                            else:
                                print('ERROR: Index out of time steps range')
                return resolve_algorithm_output(out_port)
        return None


add_class(VTKTimeSetter)
TYPENAMES.append('VTKTimeSetterType')

# ----------------------------------------------------------------
menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(VTKNodeCategory("custom", "custom", items=menu_items))
# ----------------------------------------------------------------
