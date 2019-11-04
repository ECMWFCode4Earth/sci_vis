# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   converters/materials.py
#
#   Define functions to create and edit materials and textures.
# ---------------------------------------------------------------------------------


from ... utilities import *


# ---------------------------------------------------------------------------------
#   Naming conventions
# ---------------------------------------------------------------------------------
# User interface names, prefixes and suffixes
# Prefix for solid materials
solid_material_prefix = "BVTK Solid "
# Prefix for blend materials
blend_material_prefix = "BVTK Blend "
# Prefix for image materials
image_material_prefix = "BVTK Image "
# Prefix for volume materials
volume_material_prefix = "BVTK Volume "
# Default uv layer name for BVTK unwraps
default_uv_map = "BVTK UV"
# Name for the customized image texture node
image_node_name = "BVTK Image Texture"
# Name for the customized color ramp node
ramp_node_name = "BVTK Color Ramp"


# ---------------------------------------------------------------------------------
#   Materials
# ---------------------------------------------------------------------------------


def blend_material(mesh, name, ramp, texture, reset=True):
    """Create a blend material and apply it to the given mesh."""
    name = blend_material_prefix + name
    mat, flag = material(mesh, name, reset)
    render_engine = bpy.context.scene.render.engine

    if render_engine == "CYCLES" or render_engine == "BLENDER_EEVEE":
        if not flag or not mat.use_nodes:
            setup_blend_tree(mat, ramp)
        else:
            nodes = mat.node_tree.nodes
            if not update_ramp_nodes(nodes, ramp):
                new_ramp_node(nodes, ramp)
    else:
        if not flag or mat.use_nodes:
            mat.use_nodes = False
            tex, ts = setup_texture(mat, texture, "BLEND")
            ts.texture_coords = "UV"
            ts.uv_layer = default_uv_map
        else:
            add_texture(mat, texture)

    return mat


def image_material(mesh, name, img, reset=True):
    """Create an image material and apply it to the given mesh."""
    name = image_material_prefix + name
    mat, flag = material(mesh, name, reset)
    render_engine = bpy.context.scene.render.engine

    if render_engine == "CYCLES" or render_engine == "BLENDER_EEVEE":
        if not flag or not mat.use_nodes:
            setup_image_tree(mat, img)
        else:
            nodes = mat.node_tree.nodes
            if not update_image_nodes(nodes, img):
                new_image_node(nodes, img)
    else:
        texture = get_item(bpy.data.textures, name, "IMAGE")
        if not flag or mat.use_nodes:
            mat.use_nodes = False
            tex, ts = setup_texture(mat, texture, "IMAGE")
            ts.texture_coords = "UV"
            ts.uv_layer = default_uv_map
        else:
            add_texture(mat, texture)
        texture.image = img

    return mat


def voxel_material(mesh, name, file_path, texture=None, reset=True):
    """Create a voxel material and apply it to the given mesh.
    Works only with blender render engine."""
    name = volume_material_prefix + name
    mat, flag = material(mesh, name, reset, type="VOLUME")
    render_engine = bpy.context.scene.render.engine
    if render_engine == "CYCLES" or render_engine == "BLENDER_EEVEE":
        log.warning("Volumetric rendering is not supported in cycles, use blender render instead.")
        return None
    else:
        if not texture:
            texture = get_item(bpy.data.textures, name, "VOXEL_DATA")
        if not flag or texture.type != "VOXEL_DATA":
            texture, ts = setup_texture(mat, texture, "VOXEL_DATA")
            mat.volume.density = 0
            texture.voxel_data.file_format = "BLENDER_VOXEL"
            texture.voxel_data.filepath = file_path
            ts.texture_coords = "ORCO"
            ts.use_map_density = True
            ts.use_map_emission = True
            ts.use_map_color_emission = True
            mat.type = "VOLUME"
            mat.volume.density = 0
        else:
            add_texture(mat, texture)
            texture.voxel_data.filepath = file_path
    return mat


def solid_material(mesh, name, color=(0, 0, 0), reset=True):
    """Create a blend material and apply it to the given mesh."""
    name = solid_material_prefix + name
    mat, flag = material(mesh, name, reset)
    render_engine = bpy.context.scene.render.engine

    if render_engine == "CYCLES" or render_engine == "BLENDER_EEVEE":
        if not flag or not mat.use_nodes:
            setup_diffuse_tree(mat, color)
    else:
        if not flag or mat.use_nodes:
            mat.use_nodes = False
            mat.diffuse_color = color

    return mat


def material(mesh, name, reset_previous=True, **material_settings):
    """Get or create a material with the given name and
    return a tuple containing the material and a
    boolean set to true if the material already
    existed."""
    if reset_previous:
        # Remove all other materials from the mesh
        mesh.materials.clear()

    mat, existed = seek_item(bpy.data.materials, name)

    for key, value in material_settings.items():
        setattr(mat, key, value)

    apply_material(mesh, mat)

    return mat, existed


def apply_material(mesh, mat):
    if mat.name not in mesh.materials:
        mesh.materials.append(mat)


# ---------------------------------------------------------------------------------
#   Cycles
# ---------------------------------------------------------------------------------


def get_by_attribute(objects, attribute_name, attribute_value):
    for obj in objects:
        if obj.bl_idname:
            if getattr(obj, attribute_name) == attribute_value:
                return obj
    return objects.new(attribute_value)


def get_node_by_idname(nodes, idname):
    return get_by_attribute(nodes, "bl_idname", idname)


def link_nodes(node_a, output_name, node_b, input_name, links):
    from_socket = node_a.outputs[output_name]
    to_socket = node_b.inputs[input_name]
    links.new(to_socket, from_socket)


def setup_diffuse_tree(mat, color=None):
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    out_node = get_node_by_idname(nodes, "ShaderNodeOutputMaterial")
    shader_node = get_node_by_idname(nodes, "ShaderNodeBsdfDiffuse")
    link_nodes(shader_node, "BSDF", out_node, "Surface", links)

    if color is not None:
        if len(color) == 3:
            color = color + (1,)
        shader_node.inputs["Color"].default_value = color


def setup_blend_tree(mat, ramp):
    setup_diffuse_tree(mat)

    # mat.use_nodes = True
    nodes = mat.node_tree.nodes
    out_node = get_node_by_idname(nodes, "ShaderNodeOutputMaterial")
    uv_node = get_node_by_idname(nodes, "ShaderNodeUVMap")
    ramp_node = get_node_by_idname(nodes, "ShaderNodeValToRGB")
    customize_ramp_node(ramp_node)
    shader_node = get_node_by_idname(nodes, "ShaderNodeBsdfDiffuse")
    gradient_node = get_node_by_idname(nodes, "ShaderNodeTexGradient")
    links = mat.node_tree.links
    link_nodes(ramp_node, "Color", shader_node, "Color", links)
    link_nodes(gradient_node, "Fac", ramp_node, "Fac", links)
    # link_nodes(shader_node, "BSDF", out_node, "Surface", links)
    link_nodes(uv_node, "UV", gradient_node, "Vector", links)
    copy_color_ramp(ramp, ramp_node.color_ramp)
    uv_node.uv_map = default_uv_map


def setup_image_tree(mat, image):
    setup_diffuse_tree(mat)

    # mat.use_nodes = True
    nodes = mat.node_tree.nodes
    img_node = get_node_by_idname(nodes, "ShaderNodeTexImage")
    customize_image_node(img_node)
    shader_node = get_node_by_idname(nodes, "ShaderNodeBsdfDiffuse")
    out_node = get_node_by_idname(nodes, "ShaderNodeOutputMaterial")
    uv_node = get_node_by_idname(nodes, "ShaderNodeUVMap")
    links = mat.node_tree.links
    link_nodes(img_node, "Color", shader_node, "Color", links)
    # link_nodes(shader_node, "BSDF", out_node, "Surface", links)
    link_nodes(uv_node, "UV", img_node, "Vector", links)
    img_node.image = image
    uv_node.uv_map = default_uv_map


def new_image_node(nodes, img):
    img_node = nodes.new("ShaderNodeTexImage")
    img_node.image = img
    customize_image_node(img_node)


def new_ramp_node(nodes, ramp):
    ramp_node = nodes.new("ShaderNodeValToRGB")
    copy_color_ramp(ramp, ramp_node.color_ramp)
    customize_ramp_node(ramp_node)


def customize_node(node, node_name):
    node.use_custom_color = True
    node.color = 0.3, 0.4, 0.5
    node.name = node_name
    node.label = node_name


def get_customized_nodes(nodes, node_name):
    c_nodes = []
    for node in nodes:
        if node.name == node_name:
            c_nodes.append(node)
    return c_nodes


def customize_image_node(node):
    customize_node(node, image_node_name)


def update_image_nodes(nodes, img):
    img_nodes = get_customized_nodes(nodes, image_node_name)
    for node in img_nodes:
        node.image = img
    return img_nodes


def customize_ramp_node(node):
    customize_node(node, ramp_node_name)


def update_ramp_nodes(nodes, ramp):
    ramp_nodes = get_customized_nodes(nodes, ramp_node_name)
    for node in ramp_nodes:
        copy_color_ramp(ramp, node.color_ramp)
    return ramp_nodes


# ---------------------------------------------------------------------------------
#   Blender render
# ---------------------------------------------------------------------------------


def setup_texture(mat, texture, texture_type, **texture_settings):
    texture.type = texture_type
    texture = bpy.data.textures[texture.name]
    for key, value in texture_settings.items():
        setattr(texture, key, value)

    ts = set_active_texture(mat, texture)

    return texture, ts


def add_texture(mat, texture):
    if texture.name not in mat.texture_slots:
        ts = mat.texture_slots.add()
        ts.texture = texture
    else:
        ts = mat.texture_slots[texture.name]
    return ts


def set_active_texture(mat, texture):
    for ts in mat.texture_slots:
        if ts:
            ts.use = False
    ts = add_texture(mat, texture)
    ts.use = True
    return ts


def set_active_material():
    pass
