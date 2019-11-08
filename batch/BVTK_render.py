import bpy
import os
import sys
from bpy.app.handlers import persistent


# ---------------------------------------------------------------------------------
#   Functions
# ---------------------------------------------------------------------------------

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


def find_nodes(node_tree, bl_idname):
    for node in node_tree.nodes:
        if node.bl_idname == bl_idname:
            yield node


def find_node(node_tree, bl_idname):
    for node in find_nodes(node_tree, bl_idname):
        return node
    print("Could not find '{}' node.".format(bl_idname))


def find_node_couples(node_tree, bl_idname_a, bl_idname_b,
                      k_socket_a, k_socket_b):
    """Find in the node tree all the couple of connected nodes
    with the specified id names, linked from the specified sockets.
    Return each couple as a tuple (node_a, node_b).
     _____________      _____________
    | node_a      |    | node_b      |
    |_____________|    |_____________|
    |             |    |             |
    |   k_socket_a|--->|k_socket_b   |
    |_____________|    |_____________|

    """
    for node in find_nodes(node_tree, bl_idname_a):
        if k_socket_a in node.outputs:
            socket = node.outputs[k_socket_a]
            for link in socket.links:
                if link.to_node.bl_idname == bl_idname_b \
                   and link.to_socket.name == k_socket_b:
                    yield (node, link.to_node)


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


def collapse_node(node):
    """Collapse a node with a single input and a single
    output, connecting the two aside sockets.

    The following situation:
     _____________      _____________      _____________
    | node_a      |    | node        |    | node_b      |
    |_____________|    |_____________|    |_____________|
    |             |    |             |    |             |
    |     socket_a|--->|             |--->|socket_b     |
    |_____________|    |_____________|    |_____________|

    Becomes after collapsing the middle node:
     _____________      _____________
    | node_a      |    | node_b      |
    |_____________|    |_____________|
    |             |    |             |
    |     socket_a|--->|socket_b     |
    |_____________|    |_____________|

    """
    link_1 = None
    socket_1 = None
    link_2 = None
    socket_2 = None

    for socket in node.inputs:
        for link in socket.links:
            link_1 = link
            socket_1 = link.from_socket

    for socket in node.outputs:
        for link in socket.links:
            link_2 = link
            socket_2 = link.to_socket

    tree = node.id_data

    if link_1 and socket_1 and link_2 and socket_2:
        tree.links.remove(link_1)
        tree.links.remove(link_2)
        tree.links.new(socket_1, socket_2)


def insert_between(node, node_a, node_b,
                   k_socket_a, k_socket_in,
                   k_socket_out, k_socket_b):
    """Insert node between node a and node b,
    taking linking the sockets based on the
    provided keys.
     _____________      _____________      _____________
    | node_a      |    | node        |    | node_b      |
    |_____________|    |_____________|    |_____________|
    |             |    |             |    |             |
    |   k_socket_a|--->|k_socket_in  |    |             |
    |             |    | k_socket_out|--->|k_socket_b   |
    |_____________|    |_____________|    |_____________|

    """
    tree = node_a.id_data

    for link in tree.links:
        if link.from_node == node_a and \
           link.to_node == node_b:
            if link.from_socket.name == k_socket_a and \
               link.to_socket.name == k_socket_b:
                tree.links.remove(link)

    if k_socket_a in node_a.outputs:
        if k_socket_b in node_b.inputs:
            if k_socket_in in node.inputs:
                if k_socket_out in node.outputs:
                    tree.links.new(
                        node_a.outputs[k_socket_a],
                        node.inputs[k_socket_in]
                    )
                    tree.links.new(
                        node.outputs[k_socket_out],
                        node_b.inputs[k_socket_b]
                    )


def insert_before(node, node_a, k_socket_in,
                  k_socket_out,  k_socket_a):
    """Insert the given node before node_a, taking care
    of the specified sockets.
             _____________      _____________
            | node        |    | node_a      |
            |_____________|    |_____________|
            |             |    |             |
            | k_socket_out|--->|k_socket_a   |
    ... --->|k_socket_in  |    |             |
            |_____________|    |_____________|

    """
    if k_socket_a not in node_a.inputs:
        return
    if k_socket_in not in node.inputs:
        return
    if k_socket_out not in node.outputs:
        return
    socket = node_a.inputs[k_socket_a]
    for link in socket.links:
        k_socket_x = link.from_socket.name
        insert_between(node, link.from_node, node_a,
                       k_socket_x, k_socket_in,
                       k_socket_out, k_socket_a)


# ---------------------------------------------------------------------------------
#   Read arguments
# ---------------------------------------------------------------------------------
print()
args = {}
separator_found = False

for a in sys.argv:
    if separator_found:
        key, value = a.split(':')
        if value.strip():
            args[key] = value
            print("{}: {}".format(
                key.replace("_", " ").capitalize(),
                value)
            )
    if a == "--":
        separator_found = True

print()


# ---------------------------------------------------------------------------------
#   Validate arguments
# ---------------------------------------------------------------------------------


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

tile_size = None
if "tile_size" in args:
    try:
        tile_size = int(args["tile_size"])
    except ValueError:
        print("Tile size must be an integer, the provided value is invalid "
              "and will be ignored.")

resample_fac = None
if "resample_fac" in args:
    try:
        resample_fac = int(args["resample_fac"])
        if resample_fac < 1:
            print("Resample factor must be greater than or equal to 1, the provided "
                  "value is invalid and will be ignored.")
            resample_fac = None
    except ValueError:
        print("Resample factor must be an integer, the provided value is invalid "
              "and will be ignored.")

res_x = None
if "res_x" in args:
    try:
        res_x = int(args["res_x"])
    except ValueError:
        print("Resolution x must be an integer, the provided value is invalid "
              "and will be ignored.")

res_y = None
if "res_y" in args:
    try:
        res_y = int(args["res_y"])
    except ValueError:
        print("Resolution y must be an integer, the provided value is invalid "
              "and will be ignored.")

color_ramp_path = None
if "color_ramp" in args:
    color_ramp_path = args["color_ramp"]

file_prefix = None
if "file_prefix" in args:
    file_prefix = args["file_prefix"]


# ---------------------------------------------------------------------------------
# Apply arguments
# ---------------------------------------------------------------------------------
# Node bl_idnames
id_reader = "BVTK_NT_NetCDFCFReader"
id_time_sel = "BVTK_NT_TimeSelector"
id_color_mapper = "BVTK_NT_ColorMapper"
id_color_ramp = "BVTK_NT_ColorRamp"
id_temporal_int = "BVTK_NT_TemporalInterpolator"

if bpy.ops.wm.addon_enable(module="BVTK") != {'FINISHED'}:
    quit_msg("Couldn't enable the BVTK add-on, please check if you have installed it."
             "Make sure you have unzipped the folder if you moved BVTK directly"
             "inside the addons folder.")

if "draw_windows" in bpy.context.user_preferences.addons["BVTK"].preferences:
    bpy.context.user_preferences.addons["BVTK"].preferences.draw_windows = False

node_tree = bvtk_node_tree()

if not node_tree:
    quit_msg("Couldn't find a BVTK node tree in the provided blender preset: "
             "please make sure you are using the correct .blend file. "
             "Aborting.")

reader = find_node(node_tree, id_reader)
time_selector = find_node(node_tree, id_time_sel)
color_mapper = find_node(node_tree, id_color_mapper)
color_ramp = find_node(node_tree, id_color_ramp)

if not (reader and color_mapper):
    quit_msg("A required node is missing in the provided blender preset: "
             "please make sure you are using the correct .blend file. "
             "Aborting.")

if not time_selector:
    print("Time selector node is missing. Ignoring temporal data.")
else:
    if resample_fac is None:
        # Removing all temporal interpolator nodes
        for node in find_nodes(node_tree, id_temporal_int):
            collapse_node(node)
    else:
        temporal_int = find_node(node_tree, id_temporal_int)

        if not temporal_int:
            print("Temporal interpolator node could not be found. Creating "
                  "a new one before the time selector.")
            temporal_int = node_tree.nodes.new(id_temporal_int)
            insert_before(temporal_int, time_selector, "Input", "Output", "Input")

        for node in find_nodes(node_tree, id_temporal_int):
            temporal_int.m_ResampleFactor = resample_fac


reader.m_FileName = input_data
bpy.context.scene.render.filepath = output_folder

print("Updating the pipeline to retrieve initial data. Please wait.")
bpy.ops.bvtk.node_update(node_path=node_path(color_mapper), use_queue=False)
print("Update complete.")

if time_selector:
    if not time_end:
        time_steps = time_selector.get_time_steps()
        if not time_steps:
            quit_msg("Could not retrieve the time steps from the given data: "
                     "please make sure that the input data file has some time-related "
                     "information and try again. Aborting.")
        time_end = len(time_steps) - 1
        print("{} time steps.".format(time_end+1))
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
    color_by = get_color_array_name(color_mapper, color_mapper.color_by)
    print("Coloring using '{}' array.".format(color_by))


@persistent
def on_frame_change(scene):
    """Update the blender render output path suffix"""
    fp = file_prefix
    date = time_selector.get_date()

    if date:
        try:
            fp = date.strftime(fp)
        except ValueError as err:
            print("Error while converting date to string "
                  "for the file prefix: {}".format(err))

    fp = fp.replace("{cb}", color_by)
    scene.render.filepath = output_folder + fp


if file_prefix:
    bpy.app.handlers.frame_change_post.append(on_frame_change)


if color_ramp_path:
    if color_ramp:
        bpy.ops.bvtk.import_ramp_from_json(node_path=node_path(color_ramp), filepath=color_ramp_path)
    else:
        print("The color ramp node could not be found, color ramp has not been imported."
              "Open the preset and add a color ramp node to fix this error.")

if not tile_size:
    # Enabling auto tile size add-on
    print("Enabling automatic tile size.")
    bpy.ops.wm.addon_enable(module="render_auto_tile_size")
    if hasattr(bpy.context.scene, "ats_settings"):
        bpy.context.scene.ats_settings.is_enabled = True
    else:
        print("Auto tile size could not be enabled.")
else:
    bpy.context.scene.render.tile_x = tile_size
    bpy.context.scene.render.tile_y = tile_size

if res_x is not None and res_y is not None:
    bpy.context.scene.render.resolution_x = res_x
    bpy.context.scene.render.resolution_y = res_y
else:
    print("Resolution: {}x{}".format(
        bpy.context.scene.render.resolution_x,
        bpy.context.scene.render.resolution_y
    ))

print("Setup complete, starting render.")

if not time_selector:
    # Render a single image
    bpy.context.scene.render.filepath = os.path.join(bpy.context.scene.render.filepath,
                                                     "render.png")
    bpy.ops.render.render(animation=False, write_still=True)
else:
    # Render animation
    bpy.ops.render.render(animation=True)

print("Render complete.")
