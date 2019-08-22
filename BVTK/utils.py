import bpy
import os
import logging
from math import gcd, log10, pow

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------
# Set up logging of messages using Python logging
# Logging is nicely explained in:
# https://code.blender.org/2016/05/logging-from-python-code-in-blender/
# To see debug messages, configure logging in file
# $HOME/.config/blender/{version}/scripts/startup/setup_logging.py
# add there something like:
# import logging
# logging.basicConfig(format='%(funcName)s: %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)


# -----------------------------------------------------------------------------
# Useful variables
# -----------------------------------------------------------------------------
addon_path = os.path.realpath(__file__).replace('utils.py', '')


# -----------------------------------------------------------------------------
# Useful functions
# -----------------------------------------------------------------------------


def resolve_algorithm_output(vtkobj):
    """Return vtkobj from vtkAlgorithmOutput"""
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


def addon_pref(pref_name):
    pref = bpy.context.user_preferences.addons[__package__].preferences
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
    return (normalize_value(val, data_range) for val in tuple)


# -----------------------------------------------------------------------------
# Layout elements
# -----------------------------------------------------------------------------


def question_box(layout, text):
    """Create a box inside the given layout,
    with the given text and an error icon."""
    layout.box().label(text=str(text), icon="QUESTION")


def error_box(layout, text):
    """Create a box inside the given layout,
    with the given text and an error icon."""
    layout.box().label(text=str(text), icon="ERROR")


def header_box(layout, text):
    """Create a box inside the given layout,
    with the given text."""
    layout.box().label(text=str(text))


def error_icon(layout):
    """Create an error icon inside the given layout."""
    layout.label(text="", icon="ERROR")


# -----------------------------------------------------------------------------
# Cpt file reader
# -----------------------------------------------------------------------------


def read_cpt(file_path=None):
    # Adapted from James Boyle's script
    # https://scipy-cookbook.readthedocs.io/items/Matplotlib_Loading_a_colormap_dynamically.html
    import colorsys
    try:
        f = open(file_path)
    except:
        print("File not found: '{}'".format(file_path))
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
