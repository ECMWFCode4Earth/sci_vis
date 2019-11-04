# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   instruments/__init__.py
#
#   Define custom nodes to solve specific problems, for example
#   managing time.
# ---------------------------------------------------------------------------------


from ... utilities import *
from .. core import *
from ... import pip_installer


# ----------------------------------------------------------------
#   Multi block leaf
# ----------------------------------------------------------------


class BVTK_NT_MultiBlockLeaf(Node, BVTK_Node):
    """This node breaks down vtkMultiBlock data and outputs one
    user selected block.
    """
    bl_idname = 'BVTK_NT_MultiBlockLeaf'
    bl_label = 'MultiBlockLeaf'

    # Value of enum list in case no blocks
    # are  found in the input data.
    empty_block_list_id = "-1"

    def blocks(self, context):
        """ Returns a list for a dynamic enum. Once verified that
        the input vtk object is decomposable in blocks, the list
        will contain an element for every block, with the following
        information:
        - Block index
        - Block data type (ex. structured grid)
        - Block custom name (if it's defined, in most cases it's not)
        """
        in_node, vtkobj = self.get_input_node("Input")
        if not in_node:
            return [(self.empty_block_list_id, "Input missing", "")]

        elif not vtkobj:
            return [(self.empty_block_list_id, "Input object missing", "")]

        else:
            vtkobj = resolve_algorithm_output(vtkobj)

            if not vtkobj:
                return [(self.empty_block_list_id, "Invalid input", "")]

            if not hasattr(vtkobj, "GetNumberOfBlocks") or not hasattr(vtkobj, "GetBlock"):
                return [(self.empty_block_list_id, "Invalid input object", "")]

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

            if not len(items):
                return [(self.empty_block_list_id, "Empty list of blocks", "")]

            return items

    block = bpy.props.EnumProperty(items=blocks, name="Output block")

    def m_properties(self):
        return []

    def m_connections(self):
        return ["Input"], [], [], ["Output"]

    def draw_buttons(self, context, layout):
        in_node, vtkobj = self.get_input_node("Input")
        if not in_node:
            layout.label("Connect a node")
        elif not vtkobj:
            try_update_box(self, layout, "Input has not vtkobj (try updating).")
        else:
            vtkobj = resolve_algorithm_output(vtkobj)

            if not vtkobj:
                return

            class_name = vtkobj.__class__.__name__
            layout.label("Input: "+class_name)

            if not hasattr(vtkobj, "GetNumberOfBlocks") or not hasattr(vtkobj, "GetBlock"):
                question_box(layout, "Input object does not contain\nmultiple blocks of data.")
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
        in_node, vtkobj = self.get_input_node("Input")
        if in_node:
            if vtkobj:
                vtkobj = resolve_algorithm_output(vtkobj)
                if vtkobj:
                    if hasattr(vtkobj, "GetNumberOfBlocks") or not hasattr(vtkobj, "GetBlock"):
                        if self.block != self.empty_block_list_id:
                            return vtkobj.GetBlock(int(self.block))
        return vtkobj


# ----------------------------------------------------------------
#   Texture editor
# ----------------------------------------------------------------


class BVTK_NT_TextureEditor(Node, BVTK_Node):
    """ """
    bl_idname = 'BVTK_NT_TextureEditor'
    bl_label = 'TextureEditor'

    image = bpy.props.PointerProperty(type=bpy.types.Image)
    texture = bpy.props.PointerProperty(type=bpy.types.Texture)

    def m_properties(self):
        return []

    def m_connections(self):
        return ["Input", "Image"], [], [], ["Output"]

    def draw_buttons(self, context, layout):
        layout.template_ID(self, "texture", new="texture.new")

        if not self.texture:
            question_box(layout, "Select a texture")
            return

        if not self.inputs["Image"].links:
            row = aside_label(layout, "Image")
            row.template_ID(self, "image", open="image.open")

    def apply_properties(self, vtk_obj):
        if self.texture:
            if not self.inputs["Image"].links:
                if self.image:
                    self.texture.image = self.image

    def apply_inputs(self, vtkobj):
        if self.texture:
            if self.inputs["Image"].links:
                image = self.get_input_node("Image")[1]

                try:
                    self.texture.image = image
                except TypeError:
                    log.error("Provided input can't be set as the \n"
                              "texture image.")
                except AttributeError:
                    log.error("Texture is not of image texture type.")

    def get_output(self, socket):
        return self.get_input_node("Input")[1]


# ----------------------------------------------------------------
# TimeSelector
# ----------------------------------------------------------------


try:
    # Import, or install if needed, the 'cftime' package
    # needed to convert the time value to a date
    import cftime
except ImportError:
    if pip_installer.pip_install("cftime", ("numpy", "cython")) == 1:
        import cftime


class BVTK_NT_TimeSelector(Node, BVTK_Node):
    """VTK time management node for time variant data. Display time sets,
    time values and set time.
    """
    bl_idname = 'BVTK_NT_TimeSelector'
    bl_label = 'TimeSelector'

    def check_range(self, context):
        time_steps = self.get_time_steps()
        if time_steps:
            size = len(time_steps)
            if self.time_step < 0:
                self.time_step = 0
            elif self.time_step >= size:
                self.time_step = size-1

    time_step = bpy.props.IntProperty(update=check_range)
    date_format = bpy.props.EnumProperty(name="Date format", items=[
        ("%d/%m/%Y %H:%M", "D/M/Y h:m", "D/M/Y h:m"),
        ("%Y/%m/%d %H:%M", "Y/M/D h:m", "Y/M/D h:m"),
        ("%m/%d/%Y %H:%M", "M/D/Y h:m", "M/D/Y h:m"),
        ("%m/%d/%Y %H:%M", "M/D/Y h:m", "M/D/Y h:m"),
        ("%m/%Y", "M/Y", "M/Y"),
        ("%d/%m/%Y", "D/M/Y", "D/M/Y"),
        ("%Y/%m/%d", "Y/M/D", "Y/M/D"),
        ("%m/%d/%Y", "M/D/Y", "M/D/Y"),
        ("%m/%d/%Y", "M/D/Y", "M/D/Y"),
        ("%Y", "Y", "Y")
    ])

    def m_properties(self):
        return []

    def m_connections(self):
        return ["Input"], ["Output"], [], ["Time Step", "Date"]

    def setup(self):
        self.outputs.new(BVTK_NS_Date.bl_idname, "")

    def draw_buttons(self, context, layout):
        in_node, out_port = self.get_input_node("Input")
        if not in_node:
            question_box(layout, "Connect a node")
        elif not out_port:
            question_box(layout, "Input has not vtkobj, try updating.")
        elif not out_port.IsA("vtkAlgorithmOutput"):
            question_box(layout, "Input is not a vtkAlgorithm.")
        else:
            prod = out_port.GetProducer()
            executive = prod.GetExecutive()
            out_info = prod.GetOutputInformation(out_port.GetIndex())
            if not hasattr(executive, "TIME_STEPS"):
                question_box(layout, "Input executive does not contain\n"
                                     "any information about time steps.")
                return

            time_steps = out_info.Get(executive.TIME_STEPS())
            if not time_steps:
                question_box(layout, "Input contains a time step array\n"
                                     "but it's empty. Try updating.")
                return

            row = layout.row()
            row.prop(self, "time_step", text="Time step")
            size = len(time_steps)
            row.label("Max: "+str(size-1))

            if not 0 <= self.time_step < size:
                error_box(layout, "Index out of time steps range")
                return

            t_val = time_steps[self.time_step]
            layout.label("Time value: {}".format(t_val))

            if not pip_installer.is_loaded("cftime"):
                error_box(layout, "Module cftime not loaded: install\n"
                                  "it to convert the time value\n"
                                  "into a human readable date.\n"
                                  "> pip install cftime")
                return

            time_reader = self.get_time_reader(self)

            if not time_reader:
                return

            layout.prop(self, "date_format")
            t_units = time_reader.GetTimeUnits()
            calendar = time_reader.GetCalendar()
            date = cftime.num2date(t_val, t_units, calendar)

            if date:
                layout.label("Date: {}".format(date.strftime(self.date_format)))
            else:
                layout.label("Time value could not be converted to a date.", icon="ERROR")

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_time_steps(self):
        # Please note: this method is used by the batch scripts,
        # renaming or editing it may compromise them.
        in_node, out_port = self.get_input_node("Input")
        if in_node:
            if out_port:
                if out_port.IsA("vtkAlgorithmOutput"):
                    prod = out_port.GetProducer()
                    executive = prod.GetExecutive()
                    out_info = prod.GetOutputInformation(out_port.GetIndex())
                    if hasattr(executive, "TIME_STEPS"):
                        return out_info.Get(executive.TIME_STEPS())
        return None

    def get_time_reader(self, node):
        """Recursively search the node tree behind the given node for a
        time reader and return it. A node is considerable a time reader
        if its vtk object has 'GetTimeUnits' and 'GetCalendar' methods."""
        if node.get_vtkobj():
            obj = node.get_vtkobj()
            if has_attributes(obj, "GetTimeUnits", "GetCalendar"):
                return obj
        for input in node.inputs:
            for link in input.links:
                in_reader = self.get_time_reader(link.from_node)
                if in_reader:
                    return in_reader
        return None

    def get_text(self, time_value, format_str=None):
        """Convert the given time value in a readable date, if possible."""
        time_reader = self.get_time_reader(self)

        if not time_reader:
            return None

        if not pip_installer.is_loaded("cftime"):
            log.error("Time Selector node can't obtain the date if the 'cftime' library is not loaded")
            return None

        t_units = time_reader.GetTimeUnits()
        calendar = time_reader.GetCalendar()
        date = cftime.num2date(time_value, t_units, calendar)

        if date:
            if not format_str:
                format_str = self.date_format
            return "{}".format(date.strftime(format_str))

        return None

    def get_output(self, socket):
        """Time step socket: return the current time step
        Output socket: check if the input is valid and if the time step can be set.
        If tests pass the time step is updated and the input object is returned,
        otherwise None is returned.
        Date socket: check if it's possible to retrieve a readable date and
        return it as a formatted string.
        """
        if socket.name == "Time Step":
            return self.time_step

        in_node, out_port = self.get_input_node("Input")

        if not in_node:
            return None
        if not out_port:
            return None
        if not out_port.IsA("vtkAlgorithmOutput"):
            return None

        prod = out_port.GetProducer()
        time_steps = self.get_time_steps()
        if time_steps:
            if 0 <= self.time_step < len(time_steps):
                time_value = time_steps[self.time_step]

                if socket.name == "Date":
                    return self.get_text(time_value)

                if socket.bl_idname == BVTK_NS_Date.bl_idname:
                    return self.get_text(time_value, socket.format)

                if hasattr(prod, "UpdateTimeStep"):
                    prod.UpdateTimeStep(time_value)
                else:
                    log.warning("ERROR: {} does not have 'UpdateTimeStep' method."
                                .format(prod.__class__.__name__))
            else:
                log.warning("ERROR: Index out of time steps range")
        return resolve_algorithm_output(out_port)


# ---------------------------------------------------------------------------------
#   Date node socket
# ---------------------------------------------------------------------------------


class BVTK_NS_Date(NodeSocket):
    """BVTK Date Socket"""
    bl_idname = "BVTK_NS_Date"
    bl_label = "BVTK Date Socket"

    format = bpy.props.EnumProperty(items=[
        ("%d", "Day", "Day"),
        ("%m", "Month", "Month"),
        ("%Y", "Year", "Year"),
        ("%H", "Hour", "Hour"),
        ("%M", "Minute", "Minute")
    ])

    def draw(self, context, layout, node, text):
        layout.label(text)
        layout.prop(self, "format", text="")

    def draw_color(self, context, node):
        return 1.0, 0.4, 0.216, 0.5


# ----------------------------------------------------------------


cat = "Instruments"
register.set_category_icon(cat, "GAME")
add_node(BVTK_NT_MultiBlockLeaf, cat)
add_node(BVTK_NT_TimeSelector, cat)
add_node(BVTK_NT_TextureEditor, cat)
register.add_class(BVTK_NS_Date)
