# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   __init__.py
#
#   Check if VTK is installed, and if it's not try to install it via pip.
#   Then load (or reload) all the necessary modules and finally require
#   the utilities/register.py module to perform class registration.
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
#   Add-on header section
# ---------------------------------------------------------------------------------

import sys
import importlib
from . utilities import log, node_path
from . import pip_installer
# Crash debugging
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

_modules = [
    "utilities",
    "nodes",
    "layout"
]


def load_modules(module_names, reload=False, recursive=True, prefix=""):
    for mod_name in module_names:
        log.debug("Importing: {}".format("BVTK"+prefix+"."+mod_name))
        mod = importlib.import_module(prefix+"."+mod_name, "BVTK")
        if recursive:
            if hasattr(mod, "_modules"):
                load_modules(mod._modules, reload, recursive, prefix+"."+mod_name)
        if reload:
            log.debug("Reloading: {}".format("BVTK" + prefix + "." + mod_name))
            importlib.reload(mod)


load_modules(_modules, reloading, True)

if not reloading:
    import bpy
    from bpy.app.handlers import persistent

if reloading:
    log.debug("Reloaded modules", draw_win=False)
else:
    log.debug("Initialized modules", draw_win=False)

log.info("Loaded VTK version: {}\n"
         "VTK base path: {}".format(vtk.vtkVersion().GetVTKVersion(), vtk.__file__))


@persistent
def on_file_loaded(scene):
    """Initialize cache after a blender file open"""
    from .nodes import core
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


# ---------------------------------------------------------------------------------


def register():
    # Register is managed by utilities/register.py
    from . utilities import register as r_
    r_.add_handler(bpy.app.handlers.load_post, on_file_loaded)
    r_.add_handler(bpy.app.handlers.frame_change_post, on_frame_change)
    r_.register()


def unregister():
    # Unregister is managed by utilities/register.py
    from .utilities import register as r_
    r_.unregister()
