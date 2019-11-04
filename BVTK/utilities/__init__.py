# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   utilities/__init__.py
#
#   Define useful functions and classes.
# ---------------------------------------------------------------------------------


import bpy
import os
from pathlib import Path
import logging
import json
from . import register
from . progress import ChargingBar
from math import gcd, log10, pow

_modules = [
    "register",
    "progress"
]

# ---------------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------------
# Set up logging of messages using Python logging
# Logging is nicely explained in:
# https://code.blender.org/2016/05/logging-from-python-code-in-blender/
# To see debug messages, configure logging in file
# $HOME/.config/blender/{version}/scripts/startup/setup_logging.py
# add there something like:
# import logging
# logging.basicConfig(format='%(funcName)s: %(message)s', level=logging.DEBUG)


class BlenderLog:
    """Customized version of the normal python log, to draw a graphical
    window showing the message other than printing in the console.
    Note that sometimes the bpy.context.window_manager.popup_menu function
    can make blender crash: for example if you try to call it when blender
    has been started without gui. This is why there is an option in the user
    preferences to disable the drawing of this windows.
    """
    def __init__(self, python_log_name):
        self.python_log = logging.getLogger(python_log_name)

    def concat(self, *strings):
        """Join multiple strings, separated by single a space."""
        s = ""
        first = True
        for string in strings:
            if not first:
                s += " "
            else:
                first = False
            s += str(string)
        return s

    def disable_draw_win(self):
        set_addon_pref("draw_windows", False)

    def enable_draw_win(self):
        set_addon_pref("draw_windows", True)

    def draw_win(self, msg_type, msg, icon):
        """Draw the message to a blender popup window."""

        def draw(self, context):
            split_labels(self.layout, msg)

        if get_addon_pref("draw_windows"):
            title = "BVTK "+msg_type.capitalize()
            bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

    def _log(self, msg, level, log_method, draw_win, icon, *args, **kwargs):
        if getattr(logging, level) >= self.python_log.getEffectiveLevel():
            msg = self.concat(msg, *args)
            log_method(msg.replace("\n", " "), **kwargs)
            if draw_win and "RestrictContext" not in bpy.context.__class__.__name__:
                self.draw_win(level, msg, icon)

    def debug(self, msg, draw_win=False, *args, **kwargs):
        self._log(
            msg,
            "DEBUG",
            self.python_log.debug,
            draw_win,
            "SCRIPTWIN",
            *args, **kwargs
        )

    def info(self, msg, draw_win=False, *args, **kwargs):
        self._log(
            msg,
            "INFO",
            self.python_log.info,
            draw_win,
            "QUESTION",
            *args, **kwargs
        )

    def warning(self, msg, draw_win=True, *args, **kwargs):
        self._log(
            msg,
            "WARNING",
            self.python_log.warning,
            draw_win,
            "ERROR",
            *args, **kwargs
        )

    def error(self, msg, draw_win=True, *args, **kwargs):
        self._log(
            msg,
            "ERROR",
            self.python_log.error,
            draw_win,
            "ERROR",
            *args, **kwargs
        )

    def critical(self, msg, draw_win=True, *args, **kwargs):
        self._log(
            msg,
            "CRITICAL",
            self.python_log.critical,
            draw_win,
            "ERROR",
            *args, **kwargs
        )


log = BlenderLog(__name__)


# ---------------------------------------------------------------------------------
# Useful variables
# ---------------------------------------------------------------------------------
addon_path = str(Path(os.path.realpath(__file__)).parent.parent)


# ---------------------------------------------------------------------------------
# Useful functions
# ---------------------------------------------------------------------------------
def resolve_algorithm_output(vtkobj):
    """Return vtkobj from vtkAlgorithmOutput"""
    if hasattr(vtkobj, "IsA"):
        if vtkobj.IsA('vtkAlgorithmOutput'):
            vtkobj = vtkobj.GetProducer().GetOutputDataObject(vtkobj.GetIndex())
    return vtkobj


def update_3d_view():
    """Force update of 3D View"""
    screen = bpy.context.screen
    if(screen):
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        # This updates viewport in Blender 2.79, not sure why
                        # space.viewport_shade = space.viewport_shade
                        continue


def node_path(node):
    """Return node path of a node"""
    return 'bpy.data.node_groups['+repr(node.id_data.name)+'].nodes['+repr(node.name)+']'


def node_prop_path(node, propname):
    """Return node property path"""
    return node_path(node)+'.'+propname


def node_hash(node):
    """Return a short and identifying hash for the given node.
    Note that the hash is unreliable and may become invalid."""
    tree_i = -1
    tree = node.id_data
    for i, ng in enumerate(bpy.data.node_groups):
        if ng == tree:
            tree_i = i
    return "T{} {}".format(tree_i, node.name)


def encode_node_path(node):
    id_dict = {
        "tree_name": node.id_data.name,
        "node_name": node.name
    }
    return json.dumps(id_dict)


def decode_node_path(encoded_node):
    try:
        id_dict = json.loads(encoded_node)
        if "tree_name" not in id_dict:
            return None
        if "node_name" not in id_dict:
            return None
        tree_name = id_dict["tree_name"]
        node_name = id_dict["node_name"]

        if tree_name not in bpy.data.node_groups:
            return None
        tree = bpy.data.node_groups[tree_name]

        if node_name not in tree.nodes:
            return None
        node = tree.nodes[node_name]

        return node

    except (json.decoder.JSONDecodeError, TypeError):
        return None


def set_addon_pref(pref_name, value):
    pref = bpy.context.user_preferences.addons["BVTK"].preferences
    if hasattr(pref, pref_name):
        return setattr(pref, pref_name, value)


def get_addon_pref(pref_name):
    pref = bpy.context.user_preferences.addons["BVTK"].preferences
    if hasattr(pref, pref_name):
        return getattr(pref, pref_name)
    return None


def copy_color_ramp(from_ramp, to_ramp):
    elements = to_ramp.elements
    new_elements = from_ramp.elements
    while len(elements) > len(new_elements):
        elements.remove(elements[0])
    for i, new_el in enumerate(new_elements):
        if i < len(elements):
            elements[i].color = new_el.color
            elements[i].position = new_el.position
        else:
            e = elements.new(new_el.position)
            e.color = new_el.color


def float_scale(x):
    """Find and return the number of valid digits
    after the comma for the given float.
    """
    max_digits = 14
    int_part = int(abs(x))
    magnitude = 1 if int_part == 0 else int(log10(int_part)) + 1
    if magnitude >= max_digits:
        return 0
    frac_part = abs(x) - int_part
    multiplier = 10 ** (max_digits - magnitude)
    frac_digits = multiplier + int(multiplier * frac_part + 0.5)
    while frac_digits % 10 == 0:
        frac_digits /= 10
    return int(log10(frac_digits))


def float_gcd(a, b):
    """Find and return the float greatest common divisor."""
    sc = float_scale(a)
    sc_b = float_scale(b)
    sc = sc_b if sc_b > sc else sc
    fac = pow(10, sc)

    a = int(round(a*fac))
    b = int(round(b*fac))

    return round(gcd(a, b)/fac, sc)


def multi_gcd(a, b, *args):
    """Find the greatest common divisor of all the given numbers."""
    f_gcd = float_gcd(a, b)  # Final result
    for n in args:
        f_gcd = float_gcd(f_gcd, n)
    return f_gcd


def normalize_value(value, data_range):
    """Return the position of the value relative to the range,
    from 0 (range min) to 1 (range max).
    """
    min_r, max_r = data_range
    val = (value - min_r) / (max_r - min_r)
    val = min(1, max(0, val))
    return val


def normalize_tuple(tuple, data_range):
    for val in tuple:
        yield normalize_value(val, data_range)


def has_attributes(data, *attributes):
    """Return true if data has all of the specified arguments."""
    for att in attributes:
        if not hasattr(data, att):
            return False
    return True


def shift_reverse_range(n, shift_threshold=0, reverse=False):
    """Yield integers from 0 to n, eventually shifted and/or
    reversed. The indexes may be yielded in a shifted  order,
    based on the provided threshold. Here's a  visual example
    of a shift, with  size  equal to 10.

    Threshold = 0:      0  1  2  3  4  5  6  7  8  9
    Threshold = 5:      5  6  7  8  9  0  1  2  3  4
    """
    if shift_threshold < 0:
        shift_threshold = n+shift_threshold

    if not reverse:
        i = 0
        while i != n:

            if shift_threshold + i >= n:
                yield shift_threshold + i - n
            else:
                yield shift_threshold + i

            i += 1
    else:
        i = n-1
        while i >= 0:

            if shift_threshold + i >= n:
                yield shift_threshold + i - n
            else:
                yield shift_threshold + i

            i -= 1


def reverse_range(n, reverse=False):
    """Yield integers from 0 to n if the reverse
    bool is false, otherwise from n-1 to 0.
    """
    if not reverse:
        i = 0
        while i != n:
            yield i
            i += 1
    else:
        i = n-1
        while i >= 0:
            yield i
            i -= 1


def reverse_index(n, i, reverse=True):
    """Return a reversed index based on the specified
    size n, but only if the reverse variable is true.
    """
    if not reverse:
        return i
    return n - 1 - i


# ---------------------------------------------------------------------------------
#   Blender data
# ---------------------------------------------------------------------------------


def get_item(data, *args):
    """Get or create the item with key args[0] from data and return it."""
    item = data.get(args[0])
    if not item:
        item = data.new(*args)
    return item


def seek_item(data, *args):
    """Get or create the item with key args[0] from data and return it,
    together with a boolean flag to indicate if it already existed.
    """
    item = data.get(args[0])
    if not item:
        return data.new(*args), False
    return item, True


def set_link(data, item):
    """Link item to data if it's not already linked."""
    if item.name not in data:
        data.link(item)


# ---------------------------------------------------------------------------------
#   JSON read from file / write to file
# ---------------------------------------------------------------------------------


def write_JSON(dictionary, file_path):
    """Write JSON dictionary to file."""
    file_path = os.path.realpath(file_path)
    text = json.dumps(dictionary, indent=4, sort_keys=True)

    try:
        f = open(file_path, "w", encoding="utf-8")
    except FileNotFoundError:
        log.error("File not found: '{}'\n"
                  "Can't export JSON.")
        return False

    f.write(text)
    f.close()
    return True


def read_JSON(file_path):
    """Read JSON dictionary from file."""

    try:
        f = open(file_path, "r", encoding="utf-8")
    except FileNotFoundError:
        log.error("File not found: '{}'\n"
                  "Can't import JSON.")
        return None

    text = f.read()
    f.close()
    dic = json.loads(text)
    return dic


# ---------------------------------------------------------------------------------
#   Layout elements
# ---------------------------------------------------------------------------------


def split_labels(layout, text, scale=1.0, initial_scale=0.0):
    """Add a label to the given layout for each
    newline in the given text.
    """
    tot_scale = initial_scale
    for text in text.split("\n"):
        layout.label(text=str(text))
        tot_scale += scale
    return tot_scale


def icon_box(layout, text, icon_code):
    """Create a box inside the given layout,
    with the given text and and the specified icon.
    """
    box = layout.box()
    box = side_spaced_layout(box)

    row = box.row()
    icon = row.column()
    icon.label(text="", icon=icon_code)
    col = row.column()
    col.separator()
    scale = 0.7
    col.scale_y = scale
    tot_scale = split_labels(col, text, scale, scale)
    icon.scale_y = tot_scale
    return box


def question_box(layout, text):
    """Create a box inside the given layout,
    with the given text and an error icon.
    """
    return icon_box(layout, text, "QUESTION")


def error_box(layout, text):
    """Create a box inside the given layout,
    with the given text and an error icon.
    """
    return icon_box(layout, text, "ERROR")


def try_update_box(node, layout, text):
    box = question_box(layout, text)
    box.operator("bvtk.node_update", text="Update").node_path = node_path(node)
    box.separator()


def header_box(layout, text):
    """Create a box inside the given layout,
    with the given text.
    """
    layout.box().label(text=str(text))


def error_icon(layout):
    """Create an error icon inside the given layout."""
    layout.label(text="", icon="ERROR")


def small_separator(layout):
    """Create an empty space in the given layout, smaller
    than the one made using the separator method.
    """
    col = layout.column()
    col.separator()
    col.scale_y = 0.8


def high_op(layout, *args, **kwargs):
    """Create a button for an operator in the given layout,
    a little taller than the default.
    """
    col = layout.column()
    col.scale_y = 1.3
    op = col.operator(*args, **kwargs)
    return op


def aside_label(layout, label, percentage=0.3):
    """Split the given layout and insert a label,
    then return the resulting split layout.
    """
    row = layout.split(percentage=percentage)
    row.label(text=str(label)+":")
    return row


def side_spaced_layout(layout):
    """Return a layout with additional space on the
    left and on the right.
    """
    row = layout.row()
    row.column()
    spaced_layout = row.column()
    row.column()
    return spaced_layout


def get_aileron_font():
    if "Aileron-Regular" not in bpy.data.fonts:
        return bpy.data.fonts.load(os.path.join(addon_path, "Aileron-Regular.otf"))
    return bpy.data.fonts["Aileron-Regular"]


class BVTK_NodePanels:
    """Helper class to create subdivisions similar to panels
    inside node layouts. Child classes should redefine the
    protected class variable '_panels'.
    """

    node_categories = bpy.props.BoolVectorProperty(size=32)
    _panels = []

    def draw_index_panel(self, context, layout, panel_index):
        """Draw the panel at the given index."""
        cat_name, cat_draw = self._panels[panel_index]
        is_open = self.node_categories[panel_index]

        box = layout.box()
        icon = "TRIA_DOWN" if is_open else "TRIA_RIGHT"
        op = box.operator(BVTK_OT_TogglePanel.bl_idname, icon=icon,
                          text=cat_name, emboss=False)
        op.index = panel_index
        op.encoded_path = encode_node_path(self)
        op.property_name = "node_categories"
        op.value = not is_open

        if is_open and cat_draw:
            c_box = side_spaced_layout(box)
            small_separator(box)
            cat_draw(self, context, c_box)

    def draw_panels(self, context, layout):
        """Draw all panels in the given layout."""
        for i, cat in enumerate(self._panels):
            self.draw_index_panel(context, layout, i)

    def draw_panel(self, context, layout, panel_name):
        """Draw the panel with the given name."""
        for i, cat in enumerate(self._panels):
            if cat[0] == panel_name:
                self.draw_index_panel(context, layout, i)


class BVTK_OT_TogglePanel(bpy.types.Operator):
    """Open/close panel"""
    bl_idname = "bvtk.toggle_panel"
    bl_label = "Run a VTK function in queue"
    encoded_path = bpy.props.StringProperty()
    property_name = bpy.props.StringProperty()
    index = bpy.props.IntProperty(default=-1)
    value = bpy.props.BoolProperty()

    def execute(self, context):
        node = decode_node_path(self.encoded_path)
        if not node:
            log.error("Could not set property, invalid node path.")
            return {"CANCELLED"}

        prop = self.property_name
        if not hasattr(node, prop):
            log.error("Could not set property, invalid node property.")
            return {"CANCELLED"}

        if self.index == -1:
            setattr(node, prop, self.value)
        else:
            getattr(node, prop)[self.index] = self.value

        return {'FINISHED'}


# ---------------------------------------------------------------------------------
# Cpt file reader
# ---------------------------------------------------------------------------------
def read_cpt(file_path=None):
    # Adapted from James Boyle's script
    # https://scipy-cookbook.readthedocs.io/items/Matplotlib_Loading_a_colormap_dynamically.html
    import colorsys
    try:
        f = open(file_path)
    except:
        log.error("File not found: '{}'".format(file_path))
        return None

    lines = f.readlines()
    f.close()

    rgb = []
    color_model = "RGB"
    last_color = None

    for l in lines:
        ls = l.split()
        if not ls:
            continue
        if l[0] == "#":
            if ls[-1] == "HSV":
                color_model = "HSV"
                continue
            else:
                continue
        if ls[0] == "B" or ls[0] == "F" or ls[0] == "N":
            pass
        else:

            color1 = (float(ls[1]),
                      float(ls[2]),
                      float(ls[3]))

            if color1 != last_color:
                rgb.append(color1)
                last_color = color1

            color2 = (float(ls[5]),
                      float(ls[6]),
                      float(ls[7]))

            if color2 != last_color:
                rgb.append(color2)
                last_color = color2

    if color_model == "HSV":
        for i in range(len(rgb)):
            color = rgb[i]
            rr, gg, bb = colorsys.hsv_to_rgb(color[0]/360, color[1], color[2])
            rgb[i] = (rr, gg, bb)

    elif color_model == "RGB":
        for i in range(len(rgb)):
            rgb[i] = rgb[i][0] / 255, rgb[i][1] / 255, rgb[i][2] / 255

    return rgb
