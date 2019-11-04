# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   converters/converter.py
#
#   Define functions to convert VTK data into Blender objects.
# ---------------------------------------------------------------------------------


from . materials import *
from mathutils import Euler
import vtk
import bmesh


# ---------------------------------------------------------------------------------
#   Naming conventions
# ---------------------------------------------------------------------------------
# Prefix for color legend meshes
color_leg_prefix = "BVTK Color Legend "
# Prefix for color legend materials
color_leg_mat_prefix = "Color Legend "
# Prefix for color legend labels
label_suffix = " Label "
# Color legend background suffix
background_suffix = "Background"
# Color legend background suffix
contour_suffix = "Contour"


# ---------------------------------------------------------------------------------
#   Polydata conversion
# ---------------------------------------------------------------------------------


def cut_excess(original_seq, new_len):
    """Take a blender BMElemSeq and remove
    all items that exceed the new length.
    """
    original_len = len(original_seq)
    if original_len > new_len:
        for i, el in enumerate(original_seq):
            if i > (new_len-1):
                original_seq.remove(el)
    return original_len-new_len


def check_mesh_data(data):
    """Check data and return true if it's eligible to be
    converted in a mesh.
    """
    if not has_attributes(data, "GetPoints", "GetPoint",
                          "GetNumberOfCells", "GetCell",
                          "GetNumberOfPoints"):
        return False
    try:
        data.GetPoints()
    except TypeError:
        return False

    return True


def apply_geometry_filter(data):
    """Create and apply a vtk geometry filter to the given data.
    Return the resulting geometry.
    """
    geom = vtk.vtkGeometryFilter()
    try:
        geom.SetInputData(data)
    except TypeError:
        return None
    geom.Update()
    return geom.GetOutput()


def apply_colors(color_node, bm, me, data):
    if color_node.color_by:
        texture = color_node.get_texture()
        uv_map = default_uv_map

        if color_node.texture_type == "IMAGE":
            img = ramp_to_image(texture.color_ramp, name=texture.name + 'IMAGE')
            image_material(me, me.name, img, reset=color_node.reset_materials)
        elif color_node.texture_type == "BLEND":
            blend_material(me, me.name, texture.color_ramp, texture, reset=color_node.reset_materials)

        s_range = (color_node.range_min, color_node.range_max)
        array, is_point_data = get_color_array(data, color_node)

        if is_point_data:
            point_unwrap(bm, array, s_range, uv_map)
        else:
            face_unwrap(bm, array, s_range, uv_map)


def vtk_data_to_mesh(data, name, color_node=None, smooth=False):
    """Convert the given vtkdata creating or overwriting
    a blender object named 'name'.
    """
    if not data:
        log.error("No data provided.")
        return

    if not check_mesh_data(data):
        log.warning("Input data is not suitable to be converted in a mesh as it is: "
                    "converting to geometry. The process may take a while, consider adding "
                    "a geometry filter in the node tree to avoid repeating this process.", draw_win=False)
        data = apply_geometry_filter(data)
        if not check_mesh_data(data):
            log.error("Data can't be converted to a suitable geometry.\n"
                      "Try changing the output type.")
            return

    me, ob = mesh_and_object(name)
    if me.is_editmode:
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    err = 0
    bm = bmesh.new()
    bm.from_mesh(me)  # fill it in from a mesh

    data_p = data.GetPoints()
    n_points = data.GetNumberOfPoints()
    n_faces = data.GetNumberOfCells()
    verts = []

    # Create vertices
    bm.verts.ensure_lookup_table()
    bar = ChargingBar("Creating vertices", max=n_points)
    for i in range(n_points):
        bar.next()
        if i < len(bm.verts):
            bm.verts[i].co = data_p.GetPoint(i)
            vert = bm.verts[i]
        else:
            vert = bm.verts.new(data_p.GetPoint(i))
        verts.append(vert)
    bar.finish()

    # Remove surplus vertices
    log.info("Removing surplus vertices.")
    exc = cut_excess(bm.verts, n_points)
    log.debug("{} vertices removed.".format(exc))

    # Creating faces and edges
    bm.faces.ensure_lookup_table()
    bar = ChargingBar("Creating faces", max=n_faces)
    for i in range(n_faces):
        bar.next()
        data_pi = data.GetCell(i).GetPointIds()
        try:
            face_verts = [verts[data_pi.GetId(x)] for x in range(data_pi.GetNumberOfIds())]
            if len(face_verts) == 2:
                e = bm.edges.get(face_verts)
                if not e:
                    e = bm.edges.new(face_verts)
                # Modified edges are marked with a negative index,
                # so that later unmarked edges can be deleted. This
                # approach is suggested by the blender api documentation.
                e.index = -10
            else:
                f = bm.faces.get(face_verts)
                if not f:
                    f = bm.faces.new(face_verts)
                    f.smooth = smooth
                # Modified faces and edges are marked with a negative index,
                # so that later unmarked edges can be deleted. This
                # approach is suggested by the blender api documentation.
                f.index = -10
                for e in f.edges:
                    e.index = -10
        except:
            err += 1
    bar.finish()

    # Removing surplus faces and edges
    log.info("Removing excess faces.")
    for f in bm.faces:
        if f.index == -10:
            continue
        bm.faces.remove(f)
    log.info("Removing excess edges.")
    for e in bm.edges:
        if e.index == -10:
            continue
        bm.edges.remove(e)

    if err:
        log.info('num err', err)

    # Set normals
    log.info("Setting normals.")
    point_normals = data.GetPointData().GetNormals()
    cell_normals = data.GetCellData().GetNormals()

    if cell_normals:
        bm.faces.ensure_lookup_table()
        for i in range(len(bm.faces)):
            bm.faces[i].normal = cell_normals.GetTuple(i)

    if point_normals:
        for i in range(len(verts)):
            verts[i].normal = point_normals.GetTuple(i)

    if color_node:
        apply_colors(color_node, bm, me, data)

    bm.to_mesh(me)
    log.info('Blender mesh created! {} vertices.'.format(len(verts)), draw_win=True)


def mesh_and_object(name):
    """Get or create an object and his mesh and return both."""
    me = get_item(bpy.data.meshes, name)
    ob = get_object(name, me)
    return me, ob


def curve_and_object(name, curve_type):
    """Get or create an object and his curve and return both."""
    curve = get_item(bpy.data.curves, name, curve_type)
    ob = get_object(name, curve)
    return curve, ob


def get_image(name, dim):
    """Get/Create an image and make sure it has the correct dimensions."""
    img, existed = seek_item(bpy.data.images, name, dim[0], dim[1])
    if existed:
        img.source = "GENERATED"
        img.generated_width = dim[0]
        img.generated_height = dim[1]
    return img


def get_object(name, data):
    """Get or create object, set his data, add it to the current scene."""
    ob = get_item(bpy.data.objects, name, data)

    try:
        # Setting data to an object may rise an error if it's not
        # of the correct type, for example trying to set a mesh
        # as the data of a curve object.
        ob.data = data
    except TypeError:
        bpy.data.objects.remove(ob)
        return get_object(name, data)

    set_link(bpy.context.scene.objects, ob)
    return ob


# ---------------------------------------------------------------------------------
#   Colors
# ---------------------------------------------------------------------------------


def get_color_array(data, color_node):
    """Retrieve an array from the given data, based on the
    'color by' selection on the provided color node. If the
    color node is not valid then try to retrieve point data
    scalars or face data scalars. Return a tuple with the
    array and a boolean specifying whether it represents or
    not point data."""
    data_array = None
    is_pd = False

    if not color_node:
        if has_attributes(data, "GetPointData", "GetCellData"):
            pd = data.GetPointData()
            fd = data.GetCellData()
            if pd and hasattr(pd, "GetScalars"):
                data_array = pd.GetScalars()
                is_pd = True
            elif fd and hasattr(fd, "GetScalars"):
                data_array = fd.GetScalars()
                is_pd = False
    elif color_node.color_by[0] == 'P':
        data_array = data.GetPointData().GetArray(int(color_node.color_by[1:]))
        is_pd = True
    else:
        data_array = data.GetCellData().GetArray(int(color_node.color_by[1:]))
        is_pd = False

    return data_array, is_pd


def ramp_to_image(ramp, name=None, image=None, w=2000, h=100):
    """Take a color ramp and create a blender image h pixel tall
    and w pixels wide.
    """
    if not image:
        image = get_image(name, (w, h))
    else:
        w = image.generated_width
        h = image.generated_height

    p = []
    for y in range(h):
        for x in range(w):
            p.extend(ramp.evaluate(x / w))

    image.pixels = p
    # The image could be deleted automatically by blender
    # if it's not used, this must be prevented setting
    # 'use_fake_user' to true
    image.use_fake_user = True
    # The image has to be packed into the file,
    # otherwise it will be deleted after closing blender.
    image.pack(as_png=True)
    return image


def face_unwrap(bm, array, s_range, uv_layer_key=default_uv_map):
    if array:
        r_min, r_max = s_range
        if r_max == r_min:
            log.warning("Can't unwrap: constant range({}, {}).".format(r_min, r_max))
            return bm
        uv_layer = get_item(bm.loops.layers.uv, uv_layer_key)
        bm.faces.index_update()
        for face in bm.faces:
            for loop in face.loops:
                v = (array.GetValue(face.index) - r_min)/(r_max - r_min)
                # Force value inside range.
                v = min(0.999, max(0.001, v))
                loop[uv_layer].uv = (v, 0.5)


def point_unwrap(bm, array, s_range, uv_layer_key=default_uv_map):
    if array:
        r_min, r_max = s_range
        if r_max == r_min:
            log.warning("Can't unwrap: constant range({}, {}).".format(r_min, r_max))
            return bm
        uv_layer = get_item(bm.loops.layers.uv, uv_layer_key)
        bm.verts.index_update()
        for face in bm.faces:
            for loop in face.loops:
                v = (array.GetValue(loop.vert.index) - r_min)/(r_max - r_min)
                # Force value inside range.
                v = min(0.999, max(0.001, v))
                loop[uv_layer].uv = (v, 0.5)


# ---------------------------------------------------------------------------------
#   Color legend
# ---------------------------------------------------------------------------------


def text(name, body, font_size=None):
    """Get/create a text data block"""
    font = get_item(bpy.data.curves, name, 'FONT')
    font.body = body

    if font_size:
        font.size = font_size

    ob = get_object(name, font)
    return font, ob


def delete_texts(name):
    """Delete text data block"""
    for ob in bpy.data.objects:
        if ob.name.startswith(name):
            curve = ob.data
            bpy.data.objects.remove(ob)
            bpy.data.curves.remove(curve)


def rounded_rectangle(name, w, h, rad=0.1, x=0.0, y=0.0):
    curve = get_item(bpy.data.curves, name, "CURVE")
    curve.splines.clear()
    spline = curve.splines.new("NURBS")

    points = [
        (x+w, y-rad/2, 0),
        (x+w+rad, y-rad/2, 0),
        (x+w+rad, y+rad/2, 0),
        (x+w+rad, y+h-rad/2, 0),
        (x+w+rad, y+h+rad/2, 0),
        (x+w, y+h+rad/2, 0),
        (x+rad, y+h+rad/2, 0),
        (x, y+h+rad/2, 0),
        (x, y+h-rad/2, 0),
        (x, y+rad/2, 0),
        (x, y-rad/2, 0),
        (x+rad, y-rad/2, 0)
    ]

    spline.points.add(len(points)-len(spline.points))
    spline.use_cyclic_u = True

    for i, p in enumerate(spline.points):
        p.co = points[i] + (1, )

    ob = get_object(name, curve)

    return curve, ob


def create_color_legend(name, color_node, n_div, font="", w=0.5, h=5.5, fontsize=0.35):
    """Create value labels and color legends and add to current scene."""
    # Todo: rewrite and optimize this function

    cl_name = color_leg_prefix + name
    delete_texts(cl_name+label_suffix)  # Delete old labels
    # Create plane and unwrap it
    plane = plane_bmesh((w, h))
    uv_layer = get_item(plane.loops.layers.uv, default_uv_map)
    plane.faces.ensure_lookup_table()
    plane.faces[0].loops[0][uv_layer].uv = (0.005, 0.995)
    plane.faces[0].loops[1][uv_layer].uv = (0.005, 0.005)
    plane.faces[0].loops[2][uv_layer].uv = (0.995, 0.005)
    plane.faces[0].loops[3][uv_layer].uv = (0.995, 0.995)
    me, ob = mesh_and_object(cl_name)
    plane.to_mesh(me)

    if not color_node:
        log.error("Could not retrieve the color node to create the "
                  "color legend.")
        return

    tex = color_node.get_texture()

    if not tex:
        log.error("Could not retrieve the texture to create the "
                  "color legend.")
        return

    img = ramp_to_image(tex.color_ramp, cl_name)
    image_material(me, color_leg_mat_prefix+name, img)
    r_min, r_max = color_node.range_min, color_node.range_max

    if r_min > r_max:
        log.error("Range maximum greater than minimum.")
        return

    import math
    ideal_space = (r_max-r_min)/n_div
    exponent = math.floor(math.log10(ideal_space))
    mantissa = ideal_space/(10**exponent)

    if mantissa < 2.5:
        step = 10 ** exponent
    elif mantissa < 7.5:
        step = 5 * 10 ** exponent
    else:
        step = 10 * 10 ** exponent

    start = math.ceil(r_min/step)*step
    delta = r_max-r_min

    if step > delta:
        return

    start_h = (h*(start-r_min))/delta
    step_h = (h*step)/delta
    x_offset = 0.1
    padding = 0.1
    text_w = None  # Maximum text width
    z_offset = None

    # Add labels as texts
    for i in range(int(math.floor((r_max-start)/step))+1):
        t_me, t_ob = text(cl_name+label_suffix+str(i), '{:.15}'.format(float(start+i*step)),
                          fontsize)

        solid_material(t_me, color_leg_mat_prefix+name+label_suffix, (0.9, 0.9, 0.9))
        y_axis_i = 1
        x_axis_i = 0
        mesh_offset = 0

        if font:
            t_me.font = font

        bpy.context.scene.update()

        if color_node.cl_horizontal:
            # Horizontal color table, rotate labels
            t_ob.rotation_euler = Euler((0.0, -0.0, 1.570796251296997), 'XYZ')
            y_axis_i = 0
            x_axis_i = 1
            mesh_offset = t_ob.dimensions[x_axis_i]

        if z_offset is None:
            z_offset = -t_ob.dimensions[y_axis_i]/2

        if text_w is None or t_ob.dimensions[x_axis_i] > text_w:
            text_w = t_ob.dimensions[x_axis_i]

        t_ob.location = mesh_offset + w + x_offset, start_h + step_h * i + z_offset, 0
        t_ob.parent = ob

    # Color legend background
    rect_curve, rect_ob = rounded_rectangle(cl_name+" "+background_suffix,
                                            w + text_w + x_offset + padding * 2,
                                            h, x=-padding, rad=0.05)
    rect_ob.location[2] = -0.01
    rect_ob.parent = ob
    # Background border
    rect_c_curve, rect_c_ob = rounded_rectangle(cl_name+" "+contour_suffix,
                                                w + text_w + x_offset + padding * 2,
                                                h, x=-padding, rad=0.05)
    rect_c_curve.fill_mode = "NONE"
    rect_c_curve.bevel_resolution = 10
    rect_c_curve.bevel_depth = 0.008
    rect_c_ob.parent = ob
    # Materials
    solid_material(rect_curve, color_leg_mat_prefix+name+" "+background_suffix, (0, 0, 0))
    solid_material(rect_c_curve, color_leg_mat_prefix+name+" "+contour_suffix, (0.013, 0.013, 0.013))


# ---------------------------------------------------------------------------------
#  Text data conversion
# ---------------------------------------------------------------------------------


def vtk_data_to_text(data, name):
    cur, ob = curve_and_object(name, "FONT")
    data = str(data)
    cur.body = data

    # Set Aileron Regular instead of the default font
    if cur.font.name == "Bfont":
        cur.font = get_aileron_font()

    log.info("Text created: '{}'.".format(data), draw_win=True)


# ---------------------------------------------------------------------------------
#  Volume data conversion
# ---------------------------------------------------------------------------------


def check_append(dict, key, element):
    """Append the given element in the array
    dict[key].
    """
    dict.setdefault(key, []).append(element)


def parallelepiped(dim, pos=(0, 0, 0), layers=2):
    """Create and return a bmesh parallelepiped with
    the given dimensions, in the given position.
    """
    bm = bmesh.new()
    verts = [{}, {}, {}]  # same x, same y, same z
    for i_z in range(layers):
        for i_y in range(2):
            i_y = i_y if i_z == 0 else 1 - i_y
            for i_x in range(2):
                i_x = i_x if i_y == 0 else 1-i_x
                i_x = i_x if i_z == 0 else 1-i_x
                v = bm.verts.new((pos[0] + dim[0]*i_x,
                                  pos[1] + dim[1]*i_y,
                                  pos[2] + dim[2]*i_z))
                check_append(verts[0], i_x, v)
                check_append(verts[1], i_y, v)
                check_append(verts[2], i_z, v)

    faces = []
    for dict in verts:
        for k in dict:
            if len(dict[k]) > 2:
                faces.append(bm.faces.new(dict[k]))

    bmesh.ops.recalc_face_normals(bm, faces=faces)
    return bm


def scan_coordinates(coordinates):
    """Scan a coordinates array to find if the grid is
    uniform, if it's in reverse order and the optimal number
    of subdivisions.
    """
    size = coordinates.GetNumberOfValues()
    if size < 2:
        return True, False, 0

    l_c = None  # Last coordinate
    first_step = coordinates.GetValue(1) - coordinates.GetValue(0)
    is_uniform = True
    is_reverse = False
    gdc_step = multi_gcd(*(coordinates.GetValue(i) for i in range(size)))
    divisions = 1

    for i in range(size):
        val = coordinates.GetValue(i)

        if l_c is not None:
            diff = val - l_c
            n_div = abs(int(diff / gdc_step))
            divisions += n_div

            if diff != first_step:
                is_uniform = False

            if diff < 0:
                is_reverse = True

        l_c = val

    return is_uniform, is_reverse, divisions


def scan_rect_grid(grid, non_uniform_warning="", exclude=()):
    """Scan a rectilinear grid to find out if the coordinate
    arrays are uniform and if they are in reverse order. Return
    two tuples with tree values each which correspond to the
    three axis xyz.
    """
    coord = (
        (grid.GetXCoordinates(), "x"),
        (grid.GetYCoordinates(), "y"),
        (grid.GetZCoordinates(), "z")
    )
    reverse_coords = []
    uniformity = []

    for array, axis in coord:
        if axis not in exclude:
            is_uniform, is_reverse, div = scan_coordinates(array)
            reverse_coords.append(is_reverse)
            uniformity.append(is_uniform)
            if not is_uniform and non_uniform_warning:
                log.warning(non_uniform_warning.format(axis))

    return reverse_coords, uniformity


def probe_grid(data, resolution=(250, 250, 250)):
    x0, x1, y0, y1, z0, z1 = data.GetBounds()

    if hasattr(data, "GetDimensions"):
        nx, ny, nz = data.GetDimensions()
        log.warning("The data has specific dimensions ({}, {}, {}): ignoring the provided resolution."
                    .format(nx, ny, nz))
    else:
        nx, ny, nz = resolution

    struct_p = vtk.vtkStructuredPoints()
    struct_p.SetOrigin(x0, y0, z0)

    struct_p.SetDimensions(nx, ny, nz)
    struct_p.SetSpacing((x1 - x0) / nx, (y1 - y0) / ny, (z1 - z0) / nz)

    probe = vtk.vtkProbeFilter()
    probe.SetInputData(struct_p)
    probe.SetSourceData(data)
    log.warning("Starting probe. The process may take a long time.", draw_win=False)
    probe.Update()
    log.warning("Probe complete.", draw_win=False)

    probe_out = probe.GetOutput()

    return probe_out


def vtk_data_to_volume(data, name, color_node, use_probing=False, probe_resolution=(250, 250, 250),
                       shift=(0, 0), create_box=True):
    """Convert vtk volumetric data to a Blender object with a volumetric material."""
    from array import array

    if not color_node:
        log.error("Volume rendering requires a color mapper node. Connect one "
                  "before the 'To Blender' to select the data array and the range.")
        return

    data_array = get_color_array(data, color_node)[0]

    if not data_array:
        log.error("Couldn't retrieve the data array from the color mapper: "
                  "make sure there is a valid 'color by' array selected.")
        return

    # Reverse coordinates
    rx, ry, rz = False, False, False

    if use_probing:
        data = probe_grid(data, probe_resolution)
        data_array = data.GetPointData().GetArray(data_array.GetName())
    elif issubclass(data.__class__, vtk.vtkRectilinearGrid):
        scan_res = scan_rect_grid(data, non_uniform_warning="Non uniform coordinates in the {}-axis. "
                                                            "It is advisable to use probing.")
        rx, ry, rz = scan_res[0]

    dim = data.GetDimensions()
    min_r, max_r = color_node.range_min, color_node.range_max

    if color_node.auto_range:
        # Update after probing
        min_r, max_r = data_array.GetRange()

    if max_r - min_r == 0:
        log.error("Can't unwrap: the range is constant ({}, {}). "
                  "Define a valid range and try again.".format(max_r, min_r))
        return

    nx, ny, nz = dim[0], dim[1], dim[2]
    nf = 1
    header = [nx, ny, nz, nf]
    vol_data = []
    shift_x = int(nx * shift[0])
    shift_y = int(ny * shift[1])
    bar = ChargingBar("Processing volume", max=(nf * nz))

    for t in range(nf):  # frame
        for z in reverse_range(nz, rz):  # layer
            bar.next()
            for y in shift_reverse_range(ny, shift_y, ry):  # line
                for x in shift_reverse_range(nx, shift_x, rx):  # value
                    # index = t*(nx*ny*nz) + z*(nx*ny) + y*nx + x
                    # val = (data_array.GetValue(index) - min_r) / (max_r - min_r)
                    # vol_data.append(val)
                    #
                    # Compact and faster version
                    vol_data.append(
                        (data_array.GetValue(t * nx * ny * nz + z * nx * ny + y * nx + x) - min_r) / (max_r - min_r)
                    )

    bar.finish()
    output_dir = get_addon_pref("output_path")
    file_path = os.path.join(output_dir, name+".bvox")

    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except OSError:
            log.error("Tmp directory to store volume data couldn't "
                      "be created in path '{}'".format(output_dir))
        else:
            log.info("Tmp directory created in '{}'.".format(output_dir))

    bin_file = open(file_path, 'wb')
    header = array("I", header)
    vol_data = array("f", vol_data)
    header.tofile(bin_file)
    vol_data.tofile(bin_file)
    log.info("Volumetric file created in '{}'.".format(file_path))

    if not create_box:
        texture = color_node.get_texture()
        if hasattr(texture, "voxel_data"):
            texture.voxel_data.filepath = file_path
        else:
            log.warning("The color ramp texture is not of voxel type. You should "
                        "update again checking the option 'create box' to properly "
                        "setup the texture.")
        return

    me, ob = mesh_and_object(name)

    pos = (0, 0, 0)
    if hasattr(data, "GetBounds"):
        bounds = evaluate_bounds(data.GetBounds())
        if bounds:
            pos, dim = bounds

    parallelepiped(dim, layers=2, pos=pos).to_mesh(me)
    texture = color_node.get_texture()
    voxel_material(me, name, file_path, texture, color_node.reset_materials)


# ---------------------------------------------------------------------------------
#   Image data conversion
# ---------------------------------------------------------------------------------


def plane_bmesh(dim, pos=(0, 0, 0)):
    """Create and return a bmesh parallelepiped with
    the given dimensions, in the given position.
    """
    bm = bmesh.new()
    verts = []  # same x, same y, same z

    for i_y in range(2):
        for i_x in range(2):
            i_x = i_x if i_y == 0 else 1 - i_x
            v = bm.verts.new((pos[0] + dim[0] * i_x,
                              pos[1] + dim[1] * i_y,
                              pos[2]))
            verts.append(v)

    f = [bm.faces.new(verts)]

    bmesh.ops.recalc_face_normals(bm, faces=f)

    return bm


def evaluate_bounds(bounds):
    if not bounds or len(bounds) != 6:
        return None
    origin = []
    dim = []
    for i in (0, 2, 4):
        origin.append(bounds[i])
        dim.append(abs(bounds[i+1]-bounds[i]))
    return origin, dim


def vtk_data_to_image(data, name, color_node, shift=(0, 0), create_plane=True, z_level=0):
    """Convert vtkImageData to a Blender image"""
    if issubclass(data.__class__, bpy.types.ColorRamp):
        ramp_to_image(data, name)
        log.info("Color ramp image created: '{}'.".format(name), draw_win=True)
        return

    if hasattr(data, "GetDimensions"):
        dim = data.GetDimensions()
    else:
        log.error("Input data isn't suitable to become an image.\n"
                  "Please change the output type.")
        return

    data_array = get_color_array(data, color_node)[0]

    if not data_array:
        log.error("Couldn't retrieve the data array from the color mapper:\n"
                  "make sure there is a color mapper node connected, and\n"
                  "a valid 'color by' array selected.")
        return

    data_range = data_array.GetRange()
    reset_materials = False
    color_ramp = None

    if color_node:
        reset_materials = color_node.reset_materials
        data_range = color_node.range_min, color_node.range_max
        tex = color_node.get_texture()
        if tex:
            color_ramp = tex.color_ramp

    if data_range[1] - data_range[0] == 0:
        log.error("Range is constant. Please select a proper range.")
        return

    if dim[2] > 1:
        log.warning("Input data has more than one dimension in the z-axis.\n"
                    "You may try to choose volume as an output type.")

    img = get_image(name, dim)

    p = []
    nx, ny, nz = dim[0], dim[1], dim[2]

    # Reverse coordinates
    rx, ry = False, False
    if issubclass(data.__class__, vtk.vtkRectilinearGrid):
        scan_res = scan_rect_grid(data,
                                  non_uniform_warning="Non uniform coordinates in the {}-axis. "
                                                      "The resulting image may not be accurate.",
                                  exclude=("z",))
        rx, ry = scan_res[0]

    bar = ChargingBar("Processing image", max=ny)
    shift_x = int(nx * shift[0])
    shift_y = int(ny * shift[1])
    tuple_size = len(data_array.GetTuple(0))
    n_tuples = data_array.GetNumberOfTuples()
    z_offset = z_level*nx*ny

    if (ny-1) * nx + (nx-1) + z_offset >= n_tuples:
        log.error("Input data isn't suitable to become an image,\n"
                  "maybe due to a three-dimensional structure.\n"
                  "Try to change the output type.")
        return

    for y in shift_reverse_range(ny, shift_y, ry):  # line
        bar.next()

        for x in shift_reverse_range(nx, shift_x, rx):  # value
            t = data_array.GetTuple(y * nx + x + z_offset)
            if tuple_size == 1:
                val = normalize_value(t[0], data_range)
                if color_ramp:
                    p.extend(color_ramp.evaluate(val))
                else:
                    p.extend((val, val, val, 1))
            else:
                for val in normalize_tuple(t, data_range):
                    p.append(val)
                if tuple_size < 4:
                    p.append(1)  # Alpha

    bar.finish()
    img.pixels = p
    log.info("Image created, {} pixels.".format(len(p)), draw_win=True)

    if not create_plane:
        return

    # Create plane mesh with UVs to show the image
    spacing = data.GetSpacing() if hasattr(data, "GetSpacing") else (1,)
    pos = (0, 0, 0)

    if hasattr(data, "GetBounds"):
        bounds = evaluate_bounds(data.GetBounds())
        if bounds:
            pos, dim = bounds

    x = dim[0] * spacing[0]
    y = dim[1] * spacing[0]
    plane = plane_bmesh((x, y), pos)
    uv_layer = get_item(plane.loops.layers.uv, default_uv_map)
    plane.faces.ensure_lookup_table()
    plane.faces[0].loops[0][uv_layer].uv = (0, 0)
    plane.faces[0].loops[1][uv_layer].uv = (1, 0)
    plane.faces[0].loops[2][uv_layer].uv = (1, 1)
    plane.faces[0].loops[3][uv_layer].uv = (0, 1)

    me, ob = mesh_and_object(name)

    if hasattr(data, "GetOrigin"):
        ob.location = data.GetOrigin()

    plane.to_mesh(me)
    image_material(me, name, img, reset_materials)
