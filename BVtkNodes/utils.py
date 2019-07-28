import bpy
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
    # For future use
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
