import bpy
import os
import logging

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
