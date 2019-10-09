# <pep8 compliant>

# ---------------------------------------------------------------------------------
# ADD-ON HEADER SECTION
# ---------------------------------------------------------------------------------

import sys
from . utils import log, node_path
from . import pip_installer
# Crashes debugging
import faulthandler
faulthandler.enable()

bl_info = {
    "name": "BVTK nodes",
    "author": "Silvano Imboden, Lorenzo Celli, Paul McManus, Tuomo Keskitalo",
    "version": (0, 3),
    "blender": (2, 79,  0),
    "location": "BVTK Node Tree Editor > New",
    "description": "Create and execute VTK pipelines in Blender Node Editor",
    "wiki_url": "https://github.com/esowc/sci_vis",
    "tracker_url": "https://github.com/esowc/sci_vis/issues",
    "support": 'COMMUNITY',
    "category": "Node",
    }

# Note: See core.py on how to set up Python Logging to see debug messages

# OPEN ISSUES
# - generate/vtk_info_modified.py is not used, should it be deleted?
# - continue development of node_tree_from_py at some point?
# - cone.json example raises a lot of vtkInformation request errors on
#   first run, but still works, and later updates do not produce errors
# - Color Mapper color_by produces RNA warnings due to empty list
#   until input nodes generate the list
# - Generate Scalar Bar in Color Mapper is not working correctly.
#
# CURRENTLY UNDER WORK
# - Support for volume rendering in Blender
#
# IDEAS FOR FUTURE DEVELOPMENT
# - Calculator Node: use vtkExpression evaluator
# - FromBlender (Blender To VTK) node: a BVTK node which converts Blender mesh
#   into vtkPolyData. Alternatively add vtkBlendReader to VTK?
#   Or maybe vtkAlembicReader to VTK? https://www.alembic.io/
# - Support for several VTK versions in one add-on. Would require making
#   gen_VTK*.py, VTK*.py and b_properties dependent on specific VTK version
#   and easy switch between versions.
# - Time subranges for temporal averaged analysis
# - Better access to OpenFOAM Reader settings, like selection of
#   regions and different data arrays

vtk_paths = [
    "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages"
]
sys.path.extend(vtk_paths)
log.warning("Import vtk begin.", draw_win=False)
try:
    import vtk
    res_code = 1
    log.warning("Import ok.", draw_win=False)
except ImportError:
    res_code = pip_installer.pip_install("vtk")
    if res_code == 1:
        import vtk

if not pip_installer.is_loaded("vtk"):
    if res_code == -1:
        message = ("\n\n"
                   "BVTK add-on failed to install the VTK library because of the\n"
                   "absence of the internet connection. Please connect to the internet and\n"
                   "try again. Otherwise you can install the VTK library by yourself\n"
                   "and then make sure it is accessible inside Blender.\n")
        raise Exception(message)
    else:
        import bpy
        message = ("\n\n"
                   "BVTK add-on failed to install the VTK library. Usually to solve\n"
                   "this type of error closing and reopen Blender and try again is\n"
                   "enough. Otherwise if it keeps failing you may try to install the\n"
                   "VTK library by yourself on the Blender python, running in\n"
                   "the terminal the following command:\n"
                   "\n"
                   "{} -m pip install vtk\n"
                   "\n"
                   "Then close and reopen Blender. If it still doesn't work you can\n"
                   "open an issue on github: https://github.com/esowc/sci_vis/issues .\n"
                   .format(bpy.app.binary_path_python))

        # Redirect to the troubleshooting web page
        import urllib.parse
        import webbrowser
        params = urllib.parse.urlencode({
            "python_path": bpy.app.binary_path_python,
            "blender_path": bpy.app.binary_path
        })
        webbrowser.open("http://lorenzocelli.me/BVTK/troubleshooting/index.html?"+params)

        raise Exception(message)

reloading = "bpy" in locals()

if not reloading:
    import bpy
    from bpy.app.handlers import persistent
    import nodeitems_utils

    from . import utils
    from . import progress
    from . import core
    from . import b_properties
    from . import showhide_properties
    from . import inspect_panel
    from . import favorites
    from . import examples
    from . import colormap
    from . import customfilter
    from . import info
    from . import converters

    from . import VTKSources
    from . import VTKReaders
    from . import VTKWriters
    from . import VTKFilters

    from . import VTKOthers
else:
    import importlib

    importlib.reload(utils)
    importlib.reload(progress)
    importlib.reload(core)
    importlib.reload(update)
    importlib.reload(converters)
    importlib.reload(b_properties)
    importlib.reload(showhide_properties)
    importlib.reload(examples)
    importlib.reload(inspect_panel)
    importlib.reload(colormap)
    importlib.reload(customfilter)
    importlib.reload(info)
    importlib.reload(favorites_data)
    importlib.reload(favorites)

    importlib.reload(gen_VTKSources)
    importlib.reload(VTKSources)

    importlib.reload(gen_VTKReaders)
    importlib.reload(VTKReaders)

    importlib.reload(gen_VTKWriters)
    importlib.reload(VTKWriters)

    importlib.reload(gen_VTKFilters1)
    importlib.reload(gen_VTKFilters2)
    importlib.reload(gen_VTKFilters)
    importlib.reload(VTKFilters)

    importlib.reload(gen_VTKTransform)
    importlib.reload(gen_VTKImplicitFunc)
    importlib.reload(gen_VTKParametricFunc)
    importlib.reload(gen_VTKIntegrator)

    importlib.reload(VTKOthers)

if reloading:
    log.debug("Reloaded modules", draw_win=False)
else:
    log.debug("Initialized modules", draw_win=False)

log.info("Loaded VTK version: {}\n"
         "VTK base path: {}".format(vtk.vtkVersion().GetVTKVersion(), vtk.__file__))


@persistent
def on_file_loaded(scene):
    """Initialize cache after a blender file open"""
    core.init_cache()


@persistent
def on_frame_change(scene):
    """Update nodes after frame changes by updating all VTK to Blender nodes"""
    for node_group in bpy.data.node_groups:
        for node in node_group.nodes:
            if node.bl_idname == 'BVTK_NT_ToBlender':
                log.debug("Calling update without queue", draw_win=False)
                bpy.ops.bvtk.node_update(
                    node_path=node_path(node),
                    use_queue=False
                )


# -----------------------------------------------------------------------------
# Custom categories
# -----------------------------------------------------------------------------


custom_categories_icons = {
    "Colour": "COLOR",
    "Custom": "SCRIPTWIN",
    "Converter": "APPEND_BLEND",
    "Debug": "VIEWZOOM"
}


def custom_register_node_categories():
    """Custom registering of node categories to prevent node categories to
    be shown on the tool-shelf
    """

    identifier = "BVTK_NODES"
    cat_list = core.CATEGORIES

    if identifier in nodeitems_utils._node_categories:
        raise KeyError("Node categories list '%s' already registered"
                       % identifier)

    def draw_node_item(self, context):
        layout = self.layout
        col = layout.column()
        for item in self.category.items(context):
            item.draw(item, col, context)

    def layout_menu(layout, cat_identifier):
        icon = "NONE" if cat_identifier not in custom_categories_icons \
            else custom_categories_icons[cat_identifier]
        layout.menu("NODE_MT_category_%s" % cat_identifier, icon=icon)

    def draw_add_menu(self, context):
        layout = self.layout
        layout.separator()
        vtk_categories = []
        for cat in cat_list:
            if cat.poll(context):
                if cat.identifier.startswith("VTK"):
                    vtk_categories.append(cat.identifier)
                else:
                    layout_menu(layout, cat.identifier)
        layout.separator()
        for cat_id in vtk_categories:
            layout_menu(layout, cat_id)

    menu_types = []
    for cat in cat_list:
        menu_type = type(
            "NODE_MT_category_" + cat.identifier, (bpy.types.Menu,), {
                "bl_space_type": 'NODE_EDITOR',
                "bl_label": cat.name,
                "category": cat,
                "poll": cat.poll,
                "draw": draw_node_item,
            })
        menu_types.append(menu_type)
        bpy.utils.register_class(menu_type)

    nodeitems_utils._node_categories[identifier] = \
        (cat_list, draw_add_menu, menu_types, [])


# -----------------------------------------------------------------------------


def register():
    """Register function. CLASSES and CATEGORIES are defined in core.py and
    filled in all the gen_VTK*.py and VTK*.py files
    """
    bpy.app.handlers.load_post.append(on_file_loaded)
    bpy.app.handlers.frame_change_post.append(on_frame_change)
    core.check_b_properties()  # delayed to here to allow class overriding
    for c in core.UI_CLASSES:
        try:
            bpy.utils.register_class(c)
        except Exception as e:
            log.critical('error registering: {} , exception: {}'.format(c, e))
    for c in sorted(core.CLASSES.keys()):
        try:
            bpy.utils.register_class(core.CLASSES[c])
        except Exception as e:
            log.critical('error registering: {} , exception: {}'.format(c, e))
    custom_register_node_categories()


def unregister():
    nodeitems_utils.unregister_node_categories("BVTK_NODES")
    for c in reversed(sorted(core.CLASSES.keys())):
        bpy.utils.unregister_class(core.CLASSES[c])
    for c in reversed(core.UI_CLASSES):
        bpy.utils.unregister_class(c)
    for p_c in core.p_collections.values():
        bpy.utils.previews.remove(p_c)
    core.p_collections.clear()
    bpy.app.handlers.load_post.remove(on_file_loaded)
    bpy.app.handlers.frame_change_post.remove(on_frame_change)
