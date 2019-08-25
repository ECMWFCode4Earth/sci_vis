import bpy
import os
import sys

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


def clean_path(path):
    return os.path.abspath(os.path.realpath(path))


def valid_file(path):
    path = clean_path(path)
    validity = os.path.isfile(path)
    return path, validity


def valid_dir(path):
    path = clean_path(path)
    path = os.path.join(path, "")  # Add trailing slash
    validity = os.path.isdir(path)
    return path, validity


def bvtk_node_tree():
    for tree in bpy.data.node_groups:
        if tree.bl_idname == "BVTK_NodeTree":
            return tree
    return None


def find_node(node_tree, bl_idname):
    for node in node_tree.nodes:
        if node.bl_idname == bl_idname:
            return node
    print("Could not find '{}' node.".format(bl_idname))
    return None


def node_path(node):
    """Return node path of a node"""
    return 'bpy.data.node_groups['+repr(node.id_data.name)+'].nodes['+repr(node.name)+']'


def quit_msg(msg):
    print(msg)
    sys.exit()


def set_color_array_by_name(color_mapper, array_name):
    for arr in color_mapper.color_arrays(None):
        if arr[1] == array_name:
            color_mapper.color_by = arr[0]
            return True
    return False


def available_color_arrays(color_mapper):
    for arr in color_mapper.color_arrays(None):
        yield arr[1]


def get_color_array_name(color_mapper, key):
    for arr in color_mapper.color_arrays(None):
        if arr[0] == key:
            return arr[1]
    return None


# -----------------------------------------------------------------------------
# Setup and render
# -----------------------------------------------------------------------------


# Reads arguments
args = {}
separator_found = False
for a in sys.argv:
    if separator_found:
        key, value = a.split(':')
        if value.strip():
            args[key] = value
    if a == "--":
        separator_found = True


# Validate and retrieve arguments
if "input_data" not in args:
    quit_msg("No input given, render process aborted.")
else:
    input_data, is_valid = valid_file(args["input_data"])
    if not is_valid:
        quit_msg("Invalid input path given, render process aborted.")

if "output_folder" not in args:
    quit_msg("No output folder given, render process aborted.")
else:
    output_folder, is_valid = valid_dir(args["output_folder"])
    if not is_valid:
        quit_msg("Invalid output folder path given {}, render process aborted. "
                 "Make sure it's an existing directory and try again.".format(output_folder))


if "time_start" not in args:
    print("No time start given, using the first time step, 0.")
    time_start = 0
else:
    try:
        time_start = int(args["time_start"])
    except ValueError:
        quit_msg("The time start value must be an integer. Aborting.")

if "time_end" not in args:
    print("No time end given, using the last time step.")
    time_end = None
else:
    try:
        time_end = int(args["time_end"])
    except ValueError:
        quit_msg("The time end value must be an integer. Aborting.")

color_by = None
if "color_by" in args:
    color_by = args["color_by"]

if "range_min" in args and "range_max" in args:
    try:
        data_range = float(args["range_min"]), float(args["range_max"])
    except ValueError:
        quit_msg("Range min and max values must be floats. Aborting.")
else:
    data_range = None
    print("Range min and max not provided, automatic range will be used. "
          "Please note that this is not desirable to produce scientifically "
          "reliable animations.")

node_tree = bvtk_node_tree()

if not node_tree:
    quit_msg("Couldn't find a BVTK node tree in the provided blender preset: "
             "please make sure you are using the correct .blend file. "
             "Aborting.")

reader = find_node(node_tree, "BVTK_NT_NetCDFCFReader")
time_selector = find_node(node_tree, "BVTK_NT_TimeSelector")
color_mapper = find_node(node_tree, "BVTK_NT_ColorMapper")

if not (reader and time_selector and color_mapper):
    quit_msg("A required node is missing in the provided blender preset: "
             "please make sure you are using the correct .blend file. "
             "Aborting.")

reader.m_FileName = input_data
bpy.context.scene.render.filepath = output_folder

print("Updating the pipeline to retrieve initial data. Please wait.")
bpy.ops.bvtk.node_update(node_path=node_path(color_mapper), use_queue=False)
print("Update complete.")

if not time_end:
    time_steps = time_selector.get_time_steps()
    if not time_steps:
        quit_msg("Could not retrieve the time steps from the given data: "
                 "please make sure that the input data file has some time-related "
                 "information and try again. Aborting.")
    time_end = len(time_steps) - 1
    print("Last time step: {}.".format(time_end))

bpy.context.scene.frame_start = time_start
bpy.context.scene.frame_end = time_end

time_selector.time_step = time_end
time_selector.keyframe_insert("time_step", frame=time_end)
time_selector.time_step = time_start
time_selector.keyframe_insert("time_step", frame=time_start)

if not data_range:
    color_mapper.auto_range = True
    color_mapper.update_range(None)
    color_mapper.auto_range = False
    print("Detected range: ({}, {})".format(
        color_mapper.range_min, color_mapper.range_max
    ))
else:
    color_mapper.auto_range = False
    color_mapper.range_min, color_mapper.range_max = data_range

if color_by:
    if not set_color_array_by_name(color_mapper, color_by):
        print("Specified color array not found (the name is case sensitive). "
              "Available color arrays are the following: ")
        for arr_name in available_color_arrays(color_mapper):
            print("- {}".format(arr_name))
        quit_msg("Aborting.")
else:
    print("Coloring using '{}' array.".format(get_color_array_name(color_mapper, color_mapper.color_by)))

# Enabling auto tile size add-on
bpy.ops.wm.addon_enable(module="render_auto_tile_size")
if hasattr(bpy.context.scene, "ats_settings"):
    bpy.context.scene.ats_settings.is_enabled = True
else:
    print("Auto tile size could not be enabled.")


print("Setup complete, starting render.")
bpy.ops.render.render(animation=True)
print("Render complete.")
