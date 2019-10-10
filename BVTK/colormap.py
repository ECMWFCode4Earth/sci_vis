# -----------------------------------------------------------------------------
# Color map nodes and functions
# -----------------------------------------------------------------------------
from . utils import *
from . core import *


def get_default_texture(node):
    """Create and return a new color ramp BLEND type brush texture"""
    name = node_hash(node)
    if name not in bpy.data.textures:
        tex = bpy.data.textures.new(name, 'BLEND')
    else:
        tex = bpy.data.textures[name]
    tex.use_color_ramp = True
    tex.use_fake_user = True

    elements = tex.color_ramp.elements
    elements[0].color = (10 / 255, 10 / 255, 180 / 255, 1)
    elements[0].position = 0.05
    elements[1].color = (180 / 255, 10 / 255, 20 / 255, 1)
    elements[1].position = 0.95
    e = elements.new(0.425)
    e.color = (141 / 255, 176 / 255, 254 / 255, 1)
    e = elements.new(0.5)
    e.color = (221 / 255, 221 / 255, 221 / 255, 1)
    e = elements.new(0.575)
    e.color = (243 / 255, 148 / 255, 117 / 255, 1)
    return tex


# -----------------------------------------------------------------------------
# Color mapper nodes
# -----------------------------------------------------------------------------


class BVTK_NT_ColorMapper(Node, BVTK_NodePanels, BVTK_Node):
    """BVTK Color Mapper Node"""
    bl_idname = "BVTK_NT_ColorMapper"
    bl_label = "Color Mapper"

    def update_range(self, context):
        # Please note: this method is used by the batch scripts,
        # renaming or editing it may compromise them.
        if not self.auto_range:
            return
        vtkobj = self.get_input_node("Input")[1]
        if self.color_by and vtkobj:
            vtkobj = resolve_algorithm_output(vtkobj)
            if self.color_by[0] == "P":
                d = vtkobj.GetPointData()
            else:
                d = vtkobj.GetCellData()
            if d:
                range = d.GetArray(int(self.color_by[1:])).GetRange()
                self.range_max = range[1]
                self.range_min = range[0]

    def color_arrays(self, context=None):
        # Please note: this method is used by the batch scripts,
        # renaming or editing it may compromise them.
        items = []
        vtkobj = self.get_input_node("Input")[1]
        if vtkobj:
            vtkobj = resolve_algorithm_output(vtkobj)
            if hasattr(vtkobj, "GetCellData"):
                c_data = vtkobj.GetCellData()
                p_data = vtkobj.GetPointData()
                c_descr = "Color by cell data using "
                p_descr = "Color by point data using "
                for i in range(p_data.GetNumberOfArrays()):
                    arr_name = str(p_data.GetArrayName(i))
                    items.append(("P"+str(i), arr_name, p_descr+arr_name+" array", "VERTEXSEL", len(items)))
                for i in range(c_data.GetNumberOfArrays()):
                    arr_name = str(c_data.GetArrayName(i))
                    items.append(("C"+str(i), arr_name, c_descr+arr_name+" array", "FACESEL", len(items)))
        if not len(items):
            items.append(("", "", ""))
        return items

    color_by = bpy.props.EnumProperty(items=color_arrays, name="Color by", update=update_range)
    texture_type = bpy.props.EnumProperty(name="Texture",
                                          items=[("BLEND", "BLEND", "BLEND", "TEXTURE_DATA", 0),
                                                 ("IMAGE", "IMAGE", "IMAGE", "FILE_IMAGE", 1)],
                                          default="IMAGE")
    auto_range = bpy.props.BoolProperty(default=True, update=update_range)
    default_texture = bpy.props.StringProperty(default="")
    last_color_by = bpy.props.StringProperty(default='')
    range_max = bpy.props.FloatProperty(default=1, name="Range max")
    range_min = bpy.props.FloatProperty(default=0, name="Range min")
    reset_materials = bpy.props.BoolProperty(name="Reset materials", default=True)

    # Color legend options
    cl_enable = bpy.props.BoolProperty(default=False)
    cl_div = bpy.props.IntProperty(default=10)
    cl_height = bpy.props.FloatProperty(default=5.5, name="Height")
    cl_width = bpy.props.FloatProperty(default=0.2, name="Width")
    cl_font = bpy.props.PointerProperty(type=bpy.types.VectorFont, name="Font")
    cl_font_size = bpy.props.FloatProperty(default=0.3, name="Font size")

    def m_properties(self):
        return ["color_by", "texture_type", "auto_range",
                "cl_enable", "range_min", "range_max", "cl_height",
                "cl_width", "cl_font", "cl_div", "reset_materials"]

    def m_connections(self):
        return ["Input"], [], [], ["Output"]

    def setup(self):
        self.inputs.new("BVTK_NS_Standard", "ColorRamp")
        self.cl_font = get_aileron_font()

    def get_output(self, socket):
        return self.get_input_node("Input")[1]

    def update(self):
        if self.last_color_by != self.color_by or self.auto_range:
            self.last_color_by = self.color_by
            self.update_range(None)

    def get_texture(self):
        in_links = self.inputs["ColorRamp"].links
        if len(in_links) > 0:
            return in_links[0].from_node.get_texture()
        if self.default_texture:
            if self.default_texture in bpy.data.textures:
                return bpy.data.textures[self.default_texture]
        new_texture = get_default_texture(self)
        self.default_texture = new_texture.name
        return new_texture

    def free(self):
        if self.default_texture:
            if self.default_texture in bpy.data.textures:
                bpy.data.texures.remove(bpy.data.textures[self.default_texture])
        node_deleted(self)

    def draw_buttons(self, context, layout):
        in_node, vtk_obj = self.get_input_node("Input")

        if not in_node:
            question_box(layout, "Connect a node")
            return

        if not vtk_obj:
            try_update_box(self, layout, "Input has no vtk object data\nTry to update.")
            return

        vtk_obj = resolve_algorithm_output(vtk_obj)
        if not hasattr(vtk_obj, "GetPointData"):
            try_update_box(self, layout, "Input has no associated data\nTry to update.")
            return

        # Find if node is connected to a 'toBlender' node.
        out_links = self.outputs["Output"].links
        tb_nodes = []
        for link in out_links:
            node = link.to_node
            if node.bl_idname == "BVTK_NT_ToBlender":
                tb_nodes.append(node)

        if not tb_nodes and len(out_links):
            error_box(layout, "This node must be connected in\n"
                              "output with a ToBlender node\n"
                              "in order to work properly.")
            small_separator(layout)

        err = set()
        quest = set()
        for tb in tb_nodes:
            o_type = tb.output_type 
            if self.texture_type == "BLEND":
                if o_type == "IMAGE":
                    err.add("Image output is not compatible\n"
                            "with the blend texture type.")
            elif self.texture_type == "IMAGE":
                if o_type == "VOLUME":
                    err.add("Volume output is not compatible\n"
                            "with the image texture type.")
            if o_type == "TEXT":
                quest.add("The color mapper node won't have\n"
                          "any effect on text output.")
        for e in err:
            error_box(layout, e)
        for q in quest:
            question_box(layout, q)

        layout.prop(self, "texture_type")
        layout.prop(self, "color_by", text="Color by")
        layout.prop(self, "auto_range", text="Automatic range")
        col = layout.column(align=True)
        col.enabled = not self.auto_range
        col.prop(self, "range_min")
        col.prop(self, "range_max")
        small_separator(layout)
        self.draw_panels(context, layout)

    def draw_color_legend(self, context, layout):
        layout.prop(self, "cl_enable", text="Generate color legend")

        if self.cl_enable:
            col = layout.column(align=True)
            col.prop(self, "cl_width")
            col.prop(self, "cl_height")

            row = aside_label(layout, "Divisions")
            row.prop(self, "cl_div", text="")

            row = aside_label(layout, "Font")
            row.template_ID(self, "cl_font", open="font.open", unlink="font.unlink")

            row = aside_label(layout, "Font size")
            row.prop(self, "cl_font_size", text="")

    def draw_options(self, context, layout):
        layout.prop(self, "reset_materials")

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    _panels = [
        ("Color Legend", draw_color_legend),
        ("Options", draw_options)
    ]


# -----------------------------------------------------------------------------
# Color ramp node
# -----------------------------------------------------------------------------


class BVTK_PG_ColorSettings(bpy.types.PropertyGroup):
    """Property used by the color ramp node to allow
    the user to choose the arrangement criteria.
    """
    # Each color has an associated value inside the range
    value = bpy.props.FloatProperty()
    # When the locked property is true the value property
    # is significant and the color ramp element won't move
    # during arrangement.
    locked = bpy.props.BoolProperty(default=False)


class BVTK_NT_ColorRamp(Node, BVTK_NodePanels, BVTK_Node):
    """BVTK Color Ramp Node"""
    bl_idname = "BVTK_NT_ColorRamp"
    bl_label = "ColorRamp"

    my_texture = bpy.props.StringProperty()
    color_settings = bpy.props.CollectionProperty(type=BVTK_PG_ColorSettings)

    def distribute_transparency(self, context):
        bpy.ops.bvtk.distribute_alpha(
            node_path=node_path(self),
            mode=self.transparency_mode,
            factor=self.transparency_factor
        )

    # Transparency options
    transparency_mode = bpy.props.EnumProperty(items=[
        ("Sequential", "Sequential", "Sequential"),
        ("Divergent", "Divergent", "Divergent")
    ], default="Sequential", name="Mode", update=distribute_transparency)
    transparency_factor = bpy.props.FloatProperty(default=1, name="Factor",
                                                  update=distribute_transparency)

    def m_properties(self):
        return []

    def m_connections(self):
        return [], [], [], ["ColorRamp"]

    def copy_setup(self, node):
        new_texture = get_default_texture(self)
        self.my_texture = new_texture.name
        old_texture = node.get_texture()
        if old_texture:
            copy_color_ramp(old_texture.color_ramp,
                            new_texture.color_ramp)

    def setup(self):
        new_texture = get_default_texture(self)
        self.my_texture = new_texture.name
        for i in range(32):
            # Initially add 32 color settings, which is the
            # maximum number of color ramp elements
            self.color_settings.add()

    def get_texture(self):
        if self.my_texture not in bpy.data.textures.keys():
            return None
        return bpy.data.textures[self.my_texture]

    def free(self):
        if self.my_texture in bpy.data.textures:
            bpy.data.textures.remove(bpy.data.textures[self.my_texture])
        node_deleted(self)

    def get_range_set(self):
        """Retrieve a set with all the ranges retrieved from the
        nodes in output, return an empty set if no range could be found
        """
        ranges = set()
        for link in self.outputs[0].links:
            node = link.to_node
            if hasattr(node, "range_max") and hasattr(node, "range_min"):
                ranges.add((node.range_min, node.range_max))
        return ranges

    def get_range(self):
        """Check if a valid range exist and return it, otherwise return none"""
        ranges = self.get_range_set()
        if not ranges:
            return None
        if len(ranges) > 1:
            return None
        return ranges.pop()

    def draw_buttons(self, context, layout):
        if self.my_texture in bpy.data.textures.keys():
            texture = bpy.data.textures[self.my_texture]
            layout.menu("BVTK_MT_ColorRamps")
            layout.template_color_ramp(texture, "color_ramp", expand=False)
            self.draw_panels(context, layout)

    def draw_color_values(self, context, layout):
        if self.my_texture not in bpy.data.textures.keys():
            return

        texture = bpy.data.textures[self.my_texture]
        path = node_path(self)
        errors = set()
        ramp = texture.color_ramp

        ranges = self.get_range_set()
        if not ranges:
            question_box(layout, "Connect a node with a valid range.")
            return
        elif len(ranges) > 1:
            question_box(layout, "Input ranges differ, connect nodes with the same range to edit color values.")
            return

        range_min, range_max = ranges.pop()  # Get the single range item

        box = layout
        # header_box(box, "Color values")
        row = box.row(align=True)
        row.label(text="Range: {}, {}".format(round(range_min, 1), round(range_max, 1)))

        if range_min == range_max:
            error_icon(row)
            errors.add("Range max and min can't be equal!")
        elif range_min > range_max:
            error_icon(row)
            errors.add("Range max must be greater than min!")

        color_settings = self.color_settings
        n_settings = len(color_settings)
        split = box.split()
        color_col = split.column()
        settings_col = split.column()
        last_val = None
        for i, element in enumerate(ramp.elements):
            row = settings_col.row()
            color_col.prop(element, "color", text="")
            if i >= n_settings:
                # If the settings aren't enough to match any color ramp elements, the operator will
                # notice it and add more settings. It's done with an operator because blender doesn't
                # allow to modify data during draw. Anyway after this should not happen unless
                # the maximum number of color ramp element increases in future versions of Blender
                op = row.operator("bvtk.update_color_settings", text="", icon="RADIOBUT_OFF", emboss=False)
                op.el_index = i
                op.node_path = path
            else:
                settings = color_settings[i]
                op = row.operator("bvtk.update_color_settings", text="",
                                  icon="RADIOBUT_ON" if settings.locked else "RADIOBUT_OFF",
                                  emboss=False)
                op.el_index = i
                op.node_path = path
                if settings.locked:
                    prop_row = row.row(align=True)
                    prop_row.prop(settings, "value", text="")
                    op = prop_row.operator("bvtk.apply_ramp_position", text="",
                                           icon="PASTEDOWN")
                    op.el_index = i
                    op.node_path = path
                    if settings.value > range_max or settings.value < range_min:
                        row.label(text="", icon="ERROR")
                        errors.add("Values must be inside range!")
                    if last_val is not None and settings.value < last_val:
                        errors.add("Values must be in ascending order!")
                    last_val = settings.value

        for error in errors:
            error_box(box, error)

        row = box.row()
        row.enabled = len(errors) == 0
        op = row.operator("bvtk.arrange_color_ramp", text="Arrange", icon="ALIGN")
        op.node_path = path

    def draw_transparency(self, context, layout):
        layout.prop(self, "transparency_mode", expand=True)
        row = aside_label(layout, "Factor")
        row.prop(self, "transparency_factor")
        small_separator(layout)
        op = high_op(layout, "bvtk.distribute_alpha",
                     text="Distribute transparency")
        op.mode = self.transparency_mode
        op.factor = self.transparency_factor
        op.node_path = node_path(self)

    _panels = [
        ("Color Values", draw_color_values),
        ("Transparency", draw_transparency)
    ]

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socket):
        tex = self.get_texture()
        if tex:
            return tex.color_ramp

    def special_properties(self):
        """Make auto_update scanner notice changes in the color ramp"""
        return self.export_properties()["elements"]

    def export_properties(self):
        """Export colormap properties. Called by export operator"""
        t = self.get_texture()
        if t:
            elements = t.color_ramp.elements
            e = [[[x for x in e.color], e.position] for e in elements]
        else:
            e = []
        return {"elements": e}

    def import_properties(self, dict):
        """Import colormap properties. Called by import operator"""
        log.debug("importing colormap " + str(self.name))
        t = self.get_texture()
        new_elements = dict["elements"]
        if t:
            elements = t.color_ramp.elements
            while len(elements) > len(new_elements):
                elements.remove(elements[0])
            for i, new_el in enumerate(new_elements):
                if i < len(elements):
                    elements[i].color = new_el[0]
                    elements[i].position = new_el[1]
                else:
                    e = elements.new(new_el[1])
                    e.color = new_el[0]


# -----------------------------------------------------------------------------


class BVTK_OT_UpdateColorSetting(bpy.types.Operator):
    """Lock a color ramp element to a certain value
    during the arrangement."""
    bl_idname = "bvtk.update_color_settings"
    bl_label = "Lock or unlock a color ramp element."
    node_path = bpy.props.StringProperty()
    el_index = bpy.props.IntProperty()

    def execute(self, context):
        node = eval(self.node_path)
        if not node:
            return {"CANCELLED"}
        texture = node.get_texture()
        if not texture:
            return {"CANCELLED"}
        ramp = texture.color_ramp
        color_settings = node.color_settings
        el_index = self.el_index
        if el_index >= len(ramp.elements):
            return {"CANCELLED"}
        elif el_index >= len(color_settings):
            m_settings = el_index-len(color_settings)+1  # Number of missing settings
            for i in range(m_settings):
                color_settings.add()

        color_setting = color_settings[el_index]
        if color_setting.locked:
            color_setting.locked = False
        else:
            bpy.ops.bvtk.apply_ramp_position(node_path=self.node_path, el_index=self.el_index)
            color_setting.locked = True
        return {"FINISHED"}


# -----------------------------------------------------------------------------


class BVTK_OT_ApplyRampPosition(bpy.types.Operator):
    """Retrieve the element position in the color ramp
    and find the corresponding value within the range."""
    bl_idname = "bvtk.apply_ramp_position"
    bl_label = "Apply ramp position"
    node_path = bpy.props.StringProperty()
    el_index = bpy.props.IntProperty()

    def execute(self, context):
        node = eval(self.node_path)
        if not node:
            return {"CANCELLED"}
        texture = node.get_texture()
        if not texture:
            return {"CANCELLED"}
        r = node.get_range()
        if not r:
            return {"CANCELLED"}
        r_min, r_max = r
        r_delta = r_max - r_min  # Range delta
        ramp = texture.color_ramp
        color_settings = node.color_settings
        el_index = self.el_index
        if el_index >= len(ramp.elements) or el_index >= len(color_settings):
            return {"CANCELLED"}
        else:
            el = ramp.elements[el_index]
            color_settings[el_index].value = r_min + el.position * r_delta
        return {"FINISHED"}


# ----------------------------------------------------------------


class ColorRampSubset:
    """Represent a part of a color ramp, delimited
    in two fixed values. For internal use."""
    # Helper class used to arrange the color ramp

    def __init__(self, first_value):
        self.first_value = first_value
        self.last_value = None
        self.last_element = None
        self.elements = []

    def append(self, element):
        self.elements.append(element)

    def close(self, last_element, last_value):
        self.last_element = last_element
        self.last_value = last_value
        return ColorRampSubset(last_value)


class BVTK_OT_ArrangeColorRamp(bpy.types.Operator):
    """Arrange the color ramp, distributing the elements based on the color values"""
    bl_idname = "bvtk.arrange_color_ramp"
    bl_label = "Arrange color ramp elements"
    node_path = bpy.props.StringProperty()

    def execute(self, context):
        node = eval(self.node_path)
        if not node:
            return {"CANCELLED"}
        texture = node.get_texture()
        if not texture:
            return {"CANCELLED"}
        r = node.get_range()
        if not r:
            return {"CANCELLED"}
        r_min, r_max = r
        r_delta = r_max-r_min  # Range delta
        ramp = texture.color_ramp
        color_settings = node.color_settings

        # Find the values defined by the user
        subsets = [ColorRampSubset(r_min)]
        subset_i = 0
        for i, el in enumerate(ramp.elements):
            if i < len(color_settings):
                subset = subsets[subset_i]
                setting = color_settings[i]
                if setting.locked:
                    subsets.append(subset.close(el, setting.value))
                    subset_i += 1
                else:
                    subset.append(el)
        subsets[subset_i].close(None, r_max)

        # Arrange the elements
        for subset in subsets:
            abs_start = (subset.first_value - r_min)/r_delta
            n_elements = len(subset.elements)
            abs_step = (subset.last_value - subset.first_value)/r_delta/(n_elements+1)
            for i, el in enumerate(subset.elements):
                el.position = abs_start+abs_step*(i+1)
            if subset.last_element:
                subset.last_element.position = (subset.last_value - r_min)/r_delta
        return {"FINISHED"}


# ----------------------------------------------------------------


class BVTK_OT_DistributeAlpha(bpy.types.Operator):
    """Distribute transparency between the color ramp elements"""
    bl_idname = "bvtk.distribute_alpha"
    bl_label = "Distribute transparency"

    node_path = bpy.props.StringProperty()
    mode = bpy.props.EnumProperty(items=[
        ("Sequential", "Sequential", "Sequential"),
        ("Divergent", "Divergent", "Divergent")
    ], default="Sequential", name="Mode")
    factor = bpy.props.FloatProperty(default=1, name="Factor")

    def execute(self, context):
        node = eval(self.node_path)
        if not node:
            return {"CANCELLED"}
        texture = node.get_texture()
        if not texture:
            return {"CANCELLED"}

        r = texture.color_ramp
        l_el = len(r.elements) - 1  # Last element index

        if self.factor == 0:
            for el in r.elements:
                el.alpha = 0
            return {"FINISHED"}

        if self.mode == "Sequential":
            for i in range(l_el+1):
                el = r.elements[i]
                i = reverse_index(l_el+1, i, self.factor < 0)
                el.alpha = min(1, pow((i / l_el), abs(1/self.factor)))

        elif self.mode == "Divergent":
            for i in range(l_el+1):
                el = r.elements[i]
                if self.factor < 0:
                    el.alpha = min(1, pow(1 - abs((i / l_el) - 0.5) * 2, abs(1 / self.factor)))
                    continue
                el.alpha = min(1, pow(abs((i / l_el) - 0.5) * 2, abs(1/self.factor)))

        return {"FINISHED"}


# -----------------------------------------------------------------------------
# Cpt color ramps management
# -----------------------------------------------------------------------------

# Generate color bar menus based on the directories in the color_ramps folder;
# a menu is created for each folder; it will contain a button for each .cpt
# file inside the said folder
color_ramp_dir = os.path.join(addon_path, "color_ramps")
color_ramp_menus = []

for dir_name in os.listdir(color_ramp_dir):
    if os.path.isdir(os.path.join(color_ramp_dir, dir_name)):
        def menu_draw(self, context):
            layout = self.layout
            # Scan the folder and add an operator for each .cpt file
            add_cpt_operators(self.dir_path, layout)

        menu_type = type("BVTK_MT_" + dir_name, (bpy.types.Menu,), {
            "bl_idname": "BVTK_MT_" + dir_name,
            "bl_label": dir_name,
            "draw": menu_draw,
            "dir_path": os.path.join(color_ramp_dir, dir_name)
        })

        color_ramp_menus.append(menu_type)
        add_ui_class(menu_type)


class BVTK_MT_ColorRamps(bpy.types.Menu):
    """Color ramps menu"""
    bl_label = "Color ramps"
    ciao = bpy.props.IntProperty()

    def draw(self, context):
        layout = self.layout
        # Scan the color_ramps directory for cpt files
        add_cpt_operators(color_ramp_dir, layout)

        # Display all the menus automatically generated
        # and stored in the color_ramp_menus array
        for em in color_ramp_menus:
            menu_icon = 0
            p_coll = get_p_coll(em.dir_path)
            if p_coll and len(p_coll.keys()):
                # A random icon from his collection is assigned
                # to each menu
                menu_icon = p_coll[list(p_coll)[0]].icon_id
            layout.menu(em.bl_idname, icon_value=menu_icon)


# Load color bar icons: each .cpt may have a png equivalent
# with the same name and in the same folder to be displayed
# as an icon; for example, red_scale.cpt will have the icon
# red_scale.png, if present. A preview collection with the
# icons is created for each directory inside the
# 'color_ramps' folder; all the collections are stored in a
# dictionary (declared in core.py) with the corresponding
# directory absolute path as the key
for dir_name in os.listdir(color_ramp_dir):
    if os.path.isdir(os.path.join(color_ramp_dir, dir_name)):
        dir_path = os.path.join(color_ramp_dir, dir_name)
        p_coll = bpy.utils.previews.new()
        p_collections[dir_path] = p_coll
        for file_name in os.listdir(dir_path):
            if file_name.endswith(".png"):
                img_path = os.path.join(dir_path, file_name)
                p_coll.load(file_name, img_path, "IMAGE")


def get_p_coll(dir_path):
    """Given a directory absolute path, return the
    corresponding preview collection or none.
    """
    if dir_path in p_collections:
        return p_collections[dir_path]
    return None


def get_icon_id(dir_path, img_file_name):
    """Given a directory absolute path and an image
    file name, return the corresponding icon id or 0.
    """
    p_coll = get_p_coll(dir_path)
    if p_coll:
        p_coll = p_collections[dir_path]
        if img_file_name in p_coll:
            return p_coll[img_file_name].icon_id
        else:
            log.debug("Key '{}' not found in the preview collection '{}'.".format(img_file_name, dir_path))
    else:
        log.debug("Key '{}' not found in the preview collection dictionary.".format(dir_path))
    return 0


def cpt_dir_scan(dir_path):
    """Scan a directory to find all the .cpt files, and
    return for each one the absolute path, the file name
    and the corresponding icon id."""
    for file_name in sorted(os.listdir(dir_path)):
        if file_name.endswith(".cpt"):
            file_path = os.path.join(dir_path, file_name)
            icon_file = file_name.replace(".cpt", ".png")
            icon_id = get_icon_id(dir_path, icon_file)
            yield file_path, file_name, icon_id


def add_cpt_operators(dir_path, layout):
    """Search the given directory for .cpt files and the
    corresponding icon then create an operator in the given
    layout to load each of these color ramps.
    """
    for file_path, file_name, icon_id in cpt_dir_scan(dir_path):
        op = layout.operator("bvtk.load_cpt_color_ramp",
                             text=file_name.replace(".cpt", ""),
                             icon_value=icon_id,
                             text_ctxt=bpy.app.translations.contexts.id_nodetree)
        op.file_path = file_path


# ----------------------------------------------------------------


def scale_to(array, n1):
    new_array = []
    n0 = len(array)
    for i in range(n1):
        j = ((n0-1)/(n1-1))*i
        new_array.append(array[round(j)])
    return new_array


class BVTK_OT_LoadCPTColorRamp(bpy.types.Operator):
    """Load a color ramp from a .cpt file."""
    bl_idname = "bvtk.load_cpt_color_ramp"
    bl_label = "Load .cpt color ramp"
    file_path = bpy.props.StringProperty()

    def execute(self, context):
        node = context.node
        if not node:
            log.error("Could not retrieve the color ramp node to load the .cpt file.")
            return {"CANCELLED"}

        texture = node.get_texture()
        if not texture:
            return {"CANCELLED"}

        colors = read_cpt(self.file_path)
        if not colors:
            self.report({"ERROR"}, "Color ramp could not be loaded.")
            return {"CANCELLED"}

        elements = texture.color_ramp.elements
        if len(colors) > 32:
            colors = scale_to(colors, 32)
            self.report({"INFO"}, "Color ramp has been resized to 32 colors.")

        n_colors = len(colors)
        while len(elements) > n_colors:
            elements.remove(elements[0])

        gamma = 2.2  # gamma correction
        for i in range(n_colors):
            position = (1/n_colors)/2 + (1/n_colors)*i
            if i >= len(elements):
                el = elements.new(position)
            else:
                el = elements[i]
                el.position = position
            el.color = (pow(colors[i][0], gamma),
                        pow(colors[i][1], gamma),
                        pow(colors[i][2], gamma), 1)
        return {"FINISHED"}


# ----------------------------------------------------------------


# Add classes and menu items
TYPENAMES = []
add_class(BVTK_NT_ColorMapper)
TYPENAMES.append("BVTK_NT_ColorMapper")
add_class(BVTK_NT_ColorRamp)
TYPENAMES.append("BVTK_NT_ColorRamp")
add_ui_class(BVTK_PG_ColorSettings)
add_ui_class(BVTK_OT_ArrangeColorRamp)
add_ui_class(BVTK_OT_UpdateColorSetting)
add_ui_class(BVTK_OT_ApplyRampPosition)
add_ui_class(BVTK_OT_LoadCPTColorRamp)
add_ui_class(BVTK_OT_DistributeAlpha)
add_ui_class(BVTK_MT_ColorRamps)

menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Colour", "Colour", items=menu_items))
