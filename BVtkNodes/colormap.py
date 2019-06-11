from  .core import *
TYPENAMES = []


def default_texture(name):
    """ create and return a new texture """
    tex_name = name
    tex = bpy.data.textures.new(tex_name, 'BLEND')
    tex.use_color_ramp = True
    elements = tex.color_ramp.elements
    elements[0].color = (10 / 255, 10 / 255, 180 / 255, 1)
    elements[0].position = 0.05
    elements[1].color = (180 / 255, 10 / 255, 20 / 255, 1)
    elements[1].position = 0.95
    e = elements.new(0.425)
    e.color = (141 / 255, 176 / 255, 254 / 255, 1)
    e = elements.new(0.5)
    e.color = (221 / 255, 221 / 255, 221 / 255, 1)
    e = elements.new(0.575)
    e.color = (243 / 255, 148 / 255, 117 / 255, 1)
    return tex

# ----------------------------------------------------------------


class VTKColorMapper(Node, VTKNode):

    bl_idname = 'VTKColorMapperType'
    bl_label  = 'ColorMapper'

    def array_change(self, context):
        vtkobj = self.get_input_node('input')[1]
        if self.color_by and vtkobj:
            vtkobj = resolve_algorithm_output(vtkobj)
            if self.color_by[0] == 'P':
                d = vtkobj.GetPointData()
            else:
                d = vtkobj.GetCellData()
            if d:
                range = d.GetArray(int(self.color_by[1:])).GetRange()
                self.max = range[1]
                self.min = range[0]

    def color_arrays(self, context):
        items = []
        vtkobj = self.get_input_node('input')[1]
        if vtkobj:
            vtkobj = resolve_algorithm_output(vtkobj)
            if hasattr(vtkobj, 'GetCellData'):
                c_data = vtkobj.GetCellData()
                p_data =  vtkobj.GetPointData()
                c_descr = 'Color by cell data using '
                p_descr = 'Color by point data using '
                for i in range(p_data.GetNumberOfArrays()):
                    arr_name = str(p_data.GetArrayName(i))
                    items.append(('P'+str(i), arr_name, p_descr+arr_name+' array', 'VERTEXSEL', len(items)))
                for i in range(c_data.GetNumberOfArrays()):
                    arr_name = str(c_data.GetArrayName(i))
                    items.append(('C'+str(i), arr_name, c_descr+arr_name+' array', 'FACESEL', len(items)))
        if not len(items):
            items.append(('', '', ''))
        return items

    color_by = bpy.props.EnumProperty(items=color_arrays, name="color by", update=array_change)
    texture_type = bpy.props.EnumProperty(name="texture type",
                                          items=[('BLEND','BLEND','BLEND','TEXTURE_DATA',0),('IMAGE','IMAGE','IMAGE','FILE_IMAGE',1)],
                                          default='BLEND')
    auto_range = bpy.props.BoolProperty(default=True, update=array_change)
    default_texture = bpy.props.StringProperty(default="")
    last_color_by = bpy.props.StringProperty(default='')
    lut = bpy.props.BoolProperty(default=False)
    height = bpy.props.FloatProperty(default=5.5)
    max = bpy.props.FloatProperty(default=0)
    min = bpy.props.FloatProperty(default=0)
    font = bpy.props.PointerProperty(type=bpy.types.VectorFont)

    def m_properties(self):
        return ['color_by', 'texture_type', 'auto_range',
                'lut', 'min', 'max', 'height']

    def m_connections(self):
        return (['input'],[],[],['output'])

    def setup(self):
        self.inputs.new('VTKSocketType', 'lookuptable')

    def update(self):
        if self.last_color_by != self.color_by or self.auto_range:
            self.last_color_by = self.color_by
            self.array_change(None)

    def get_texture(self):
        in_links = self.inputs['lookuptable'].links
        if len(in_links) > 0:
            return in_links[0].from_node.get_texture()
        if self.default_texture:
            if self.default_texture in bpy.data.textures:
                return bpy.data.textures[self.default_texture]
        new_texture = default_texture(self.name)
        self.default_texture = new_texture.name
        return new_texture

    def free(self):
        if self.default_texture:
            if self.default_texture in bpy.data.textures:
                bpy.data.texures.remove(bpy.data.textures[self.default_texture])
        node_deleted(self)

    def draw_buttons(self, context, layout):
        in_node, vtkobj = self.get_input_node('input')
        if not in_node:
            layout.label('Connect a node')
        elif not vtkobj:
            layout.label('Input has not vtkobj (try updating)')
        else:
            vtkobj = resolve_algorithm_output(vtkobj)
            if hasattr(vtkobj, 'GetPointData'):
                layout.prop(self, 'lut', text='Generate scalar bar')
                layout.prop(self, 'texture_type')
                if self.lut:
                    layout.prop(self, 'height', text='scalar bar height')
                    layout.template_ID(self, "font", open="font.open", unlink="font.unlink")
                layout.prop(self, 'color_by', text='color by')
                layout.prop(self, 'auto_range', text='automatic range')
                row = layout.row(align=True)
                row.enabled = not self.auto_range
                row.prop(self, 'min')
                row.prop(self, 'max')
                layout.separator()
            else:
                layout.label('Input has no associated data (try updating)')


add_class(VTKColorMapper)
TYPENAMES.append('VTKColorMapperType')
# ----------------------------------------------------------------


class VTKColorToImage(Node, VTKNode):
    """ This node creates a color ramp using an image selected by the user
    and unwraps the mesh using a specific UV map, also selected by the user.
    The difference with the normal colorMapper node is that this doesn't
    apply any texture or material on the mesh, so it's easier to use with
    cycles, where you can use the color map image and uv as you like.
    """

    bl_idname = 'VTKColorToImageType'
    bl_label = 'ColorToImage'

    def array_change(self, context):
        vtkobj = self.get_input_node('input')[1]
        if self.color_by and vtkobj:
            vtkobj = resolve_algorithm_output(vtkobj)
            if self.color_by[0] == 'P':
                d = vtkobj.GetPointData()
            else:
                d = vtkobj.GetCellData()
            if d:
                range = d.GetArray(int(self.color_by[1:])).GetRange()
                self.max = range[1]
                self.min = range[0]

    def color_arrays(self, context):
        items = []
        vtkobj = self.get_input_node('input')[1]
        if vtkobj:
            vtkobj = resolve_algorithm_output(vtkobj)
            if hasattr(vtkobj, 'GetCellData'):
                c_data = vtkobj.GetCellData()
                p_data = vtkobj.GetPointData()
                c_descr = 'Color by cell data using '
                p_descr = 'Color by point data using '
                for i in range(p_data.GetNumberOfArrays()):
                    arr_name = str(p_data.GetArrayName(i))
                    items.append(('P'+str(i), arr_name, p_descr+arr_name+' array', 'VERTEXSEL', len(items)))
                for i in range(c_data.GetNumberOfArrays()):
                    arr_name = str(c_data.GetArrayName(i))
                    items.append(('C'+str(i), arr_name, c_descr+arr_name+' array', 'FACESEL', len(items)))
        if not len(items):
            items.append(('', '', ''))
        return items

    color_by = bpy.props.EnumProperty(items=color_arrays, name="color by", update=array_change)
    auto_range = bpy.props.BoolProperty(default=True, update=array_change)
    default_texture = bpy.props.StringProperty(default="")
    last_color_by = bpy.props.StringProperty(default='')
    lut = bpy.props.BoolProperty(default=False)
    height = bpy.props.FloatProperty(default=5.5)
    max = bpy.props.FloatProperty(default=0)
    min = bpy.props.FloatProperty(default=0)
    font = bpy.props.PointerProperty(type=bpy.types.VectorFont)
    image = bpy.props.PointerProperty(type=bpy.types.Image)
    mesh = bpy.props.PointerProperty(type=bpy.types.Mesh)
    uv_layer = bpy.props.StringProperty()

    def m_properties(self):
        return ['color_by', 'auto_range',
                'lut', 'min', 'max', 'height']

    def m_connections(self):
        return (['input'],[],[],['output'])

    def setup(self):
        self.inputs.new('VTKSocketType', 'lookuptable')

    def update(self):
        if self.last_color_by != self.color_by or self.auto_range:
            self.last_color_by = self.color_by
            self.array_change(None)

    def free(self):
        if self.default_texture:
            if self.default_texture in bpy.data.textures:
                bpy.data.texures.remove(bpy.data.textures[self.default_texture])
        node_deleted(self)

    def draw_buttons(self, context, layout):
        in_node, vtkobj = self.get_input_node('input')
        if not in_node:
            layout.box().label('Connect a node', icon="QUESTION")
        elif not vtkobj:
            layout.box().label('Input has not vtkobj (try updating)', icon="QUESTION")
        else:
            vtkobj = resolve_algorithm_output(vtkobj)
            if not hasattr(vtkobj, 'GetPointData'):
                layout.box().label('Input has no associated data (try updating)', icon="QUESTION")
            else:
                # Find if node is connected to a 'toBlender' node.
                # If it is, mesh names are compared to the local one
                # to see if they match.
                out_links = self.outputs['output'].links
                flag = False
                # m_flag is False if there isn't a linked ToBlender with a mesh name
                # equal to the mesh stored on this node.
                m_flag = False
                for link in out_links:
                    node = link.to_node
                    if node.bl_idname == 'VTK2BlenderType':
                        flag = True
                        if self.mesh and node.m_Name == self.mesh.name:
                            m_flag = True
                if not flag and len(out_links):
                    layout.box().label('This node must be connected in output with '
                                       'a ToBlender node in order to work properly', icon="ERROR")
                # Image output layout
                box1 = layout.box()
                box1.box().label("Image output")
                box1.template_ID(self, "image", new="image.new", open="image.open")
                box1.prop_search(self, "mesh", bpy.data, "meshes", text="")
                if self.mesh: box1.prop_search(self, "uv_layer", self.mesh, "uv_textures", text="")
                if not m_flag and self.mesh:
                    box1.box().label("The selected mesh won't be unwrapped if it doesn't match "
                                       "the ToBlender's mesh name", icon="QUESTION")
                layout.separator()
                # Coloring layout
                box1 = layout.box()
                box1.box().label("Coloring")
                box1.prop(self, 'color_by', text='Color by')
                box1.prop(self, 'auto_range', text='Automatic range')
                row = box1.row(align=True)
                row.enabled = not self.auto_range
                row.prop(self, 'min')
                row.prop(self, 'max')
                layout.separator()
                # Scalar bar
                box1 = layout.box()
                box1.box().label("Scalar bar")
                box1.prop(self, 'lut', text='Generate scalar bar')
                if self.lut:
                    box1.prop(self, 'height', text='scalar bar height')
                    box1.template_ID(self, "font", open="font.open", unlink="font.unlink")

    def get_texture(self):
        in_links = self.inputs['lookuptable'].links
        if len(in_links) > 0:
            return in_links[0].from_node.get_texture()
        if self.default_texture:
            if self.default_texture in bpy.data.textures:
                return bpy.data.textures[self.default_texture]
        new_texture = default_texture(self.name)
        self.default_texture = new_texture.name
        return new_texture

    def apply_properties(self, vtkobj):
        pass

    def get_output(self, socketname):
        return self.get_input_node('input')[1]

add_class(VTKColorToImage)
TYPENAMES.append('VTKColorToImageType')

# ----------------------------------------------------------------


class VTKColorMap(Node, VTKNode):

    bl_idname = 'VTKColorMapType'  # type name
    bl_label = 'ColorMap'          # label for nice name display

    my_texture = bpy.props.StringProperty()

    def m_properties(self):
        return []

    def m_connections(self):
        return ([],[],[],['lookupTable'])

    def copy_setup(self, node):
        new_texture = default_texture(self.name)
        self.my_texture = new_texture.name
        old_texture = node.get_texture()
        if old_texture:
            elements = new_texture.color_ramp.elements
            new_elements = old_texture.color_ramp.elements
            while len(elements) > len(new_elements):
                elements.remove(elements[0])
            for i, new_el in enumerate(new_elements):
                if i < len(elements):
                    elements[i].color = new_el.color
                    elements[i].position = new_el.position
                else:
                    e = elements.new(new_el.position)
                    e.color = new_el.color

    def setup(self):
        new_texture = default_texture(self.name)
        self.my_texture = new_texture.name

    def get_texture(self):
        if self.my_texture not in bpy.data.textures.keys():
            return None
        return bpy.data.textures[self.my_texture]

    def free(self):
        if self.my_texture in bpy.data.textures:
            bpy.data.textures.remove(bpy.data.textures[self.my_texture])
        node_deleted(self)

    def draw_buttons(self, context, layout):
        if self.my_texture in bpy.data.textures.keys():
            layout.template_color_ramp(bpy.data.textures[self.my_texture], "color_ramp", expand=False)

    def apply_properties(self, vtkobj):
        pass

    def get_output(self, socketname):
        lut = vtk.vtkLookupTable()
        lut.Build()
        return lut

    def special_properties(self):
        """ needed to make auto_update scanner notice
         changes in the color ramp """
        return self.export_properties()['elements']

    def export_properties(self):
        """ called by export operator """
        t = self.get_texture()
        if t:
            elements = t.color_ramp.elements
            e = [[[x for x in e.color], e.position] for e in elements]
        else:
            e = []
        return {'elements': e}

    def import_properties(self, dict):
        """ called by import operator """
        t = self.get_texture()
        new_elements = dict['elements']
        if t:
            elements = t.color_ramp.elements
            while len(elements) > len(new_elements):
                elements.remove(elements[0])
            for i, new_el in enumerate(new_elements):
                if i < len(elements):
                    elements[i].color = new_el[0]
                    elements[i].position = new_el[1]
                else:
                    e = elements.new(new_el[1])
                    e.color = new_el[0]


add_class(VTKColorMap)
TYPENAMES.append('VTKColorMapType')
# ----------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory("color", "color", items=menu_items) )
# ----------------------------------------------------------------
