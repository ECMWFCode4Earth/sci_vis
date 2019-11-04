# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   filters/__init__.py
#
#   Import and override default generated filters.
# ---------------------------------------------------------------------------------


from ... utilities import node_prop_path
from . gen_vtk_filters import *
from . gen_vtk_filters1 import *
from . gen_vtk_filters2 import *

_modules = [
    "gen_vtk_filters",
    "gen_vtk_filters1",
    "gen_vtk_filters2"
]

# ---------------------------------------------------------------------------------
#   Contour classes
# ---------------------------------------------------------------------------------


class BVTK_PG_ValueSettings(bpy.types.PropertyGroup):
    """ Actually a float array of variable size """
    value = bpy.props.FloatProperty(default=0)


class BVTK_ContourHelper:
    """Base class for filters which use variable number of discrete
    data values for input, similar to vtkCountourFilter.
    """
    m_ContourValues = bpy.props.CollectionProperty(type=BVTK_PG_ValueSettings)

    def draw_buttons(self, context, layout):
        m_properties = self.m_properties()
        for i in range(len(m_properties)):
            if self.b_properties[i]:
                prop = m_properties[i]
                if prop == 'm_ContourValues':
                    prop = getattr(self, prop)
                    prop_path = node_prop_path(self, 'm_ContourValues')
                    row = layout.row()
                    op = row.operator('bvtk.update_collection', text='', icon='ZOOMIN')
                    op.prop_path = prop_path
                    op.add = True
                    row.label(text='Contour values')
                    for i, item in enumerate(self.m_ContourValues):
                        row = layout.row(align=True)
                        op = row.operator('bvtk.update_collection', text='', icon='ZOOMOUT')
                        op.prop_path = prop_path
                        op.add = False
                        op.index = i
                        row.prop(item, 'value')
                else:
                    layout.prop(self, prop)

    def apply_properties(self, vtkobj):
        m_properties = self.m_properties()
        for x in [m_properties[i] for i in range(len(m_properties)) if self.b_properties[i]]:
            if x == 'm_ContourValues':
                self.contours = vtkobj.SetNumberOfContours(0)
                i = 0
                for item in self.m_ContourValues:
                    vtkobj.SetValue(i, item.value)
                    i += 1
            else:
                cmd = 'vtkobj.Set' + x[2:] + '(self.' + x + ')'
                exec(cmd, globals(), locals())

    def special_properties(self):
        return [x.value for x in self.m_ContourValues]

    def export_properties(self):
        """Export properties"""
        return {'m_ContourValues':[x.value for x in self.m_ContourValues]}

    def import_properties(self, dict):
        """Import properties"""
        values = dict['m_ContourValues']
        for i, val in enumerate(values):
            if i < len(self.m_ContourValues):
                self.m_ContourValues[i].value = val
            else:
                item = self.m_ContourValues.add()
                item.value = val


class BVTK_OT_UpdateCollection(bpy.types.Operator):
    bl_idname = "bvtk.update_collection"
    bl_label = "Update"
    index = bpy.props.IntProperty(default = 0)
    value = bpy.props.FloatProperty()
    prop_path = bpy.props.StringProperty()
    add = bpy.props.BoolProperty(default=True)

    def execute(self, context):
        prop = eval(self.prop_path)
        if self.add:
            item = prop.add()
            item.value = self.value
        else:
            prop.remove(self.index)
        return {'FINISHED'}


class BVTK_NT_ContourFilter(BVTK_ContourHelper, Node, BVTK_Node):
    bl_idname = 'BVTK_NT_ContourFilter'
    bl_label = 'vtkContourFilter'

    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', default=True)
    m_GenerateTriangles = bpy.props.BoolProperty(name='GenerateTriangles', default=True)
    m_ArrayComponent = bpy.props.IntProperty(name='ArrayComponent', default=0)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', default=1)

    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_GenerateTriangles', 'm_ArrayComponent',
                'm_NumberOfContours', 'm_ContourValues']

    def m_connections(self):
        return (['input'], ['output'], [], [])


add_node(BVTK_NT_ContourFilter)


# --------------------------------------------------------------


class BVTK_NT_MarchingCubes(BVTK_ContourHelper, Node, BVTK_Node):
    bl_idname = 'BVTK_NT_MarchingCubes'
    bl_label = 'vtkMarchingCubes'

    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', default=1)

    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars',
                'm_NumberOfContours', 'm_ContourValues']

    def m_connections(self):
        return (['input'], ['output'], [], [])


add_node(BVTK_NT_MarchingCubes)


# --------------------------------------------------------------


class BVTK_NT_AppendFilter(Node, BVTK_Node):
    bl_idname = 'BVTK_NT_AppendFilter'
    bl_label = 'vtkAppendFilter'

    m_MergePoints = bpy.props.BoolProperty(name='MergePoints', default=True)

    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MergePoints', ]

    def m_connections(self):
        return (['input'], ['output'], [], [])

    def setup(self):
        self.inputs['input'].link_limit = 300

    def apply_inputs(self, vtkobj):
        added = [vtkobj.GetInputConnection(0, i) for i in range(vtkobj.GetNumberOfInputConnections(0))]
        toadd = []
        for node, in_obj in self.get_input_nodes('input'):
            toadd.append(in_obj)
            if in_obj not in added:
                vtkobj.AddInputConnection(in_obj)

        for obj in added:
            if obj not in toadd:
                vtkobj.RemoveInputConnection(0, obj)


add_node(BVTK_NT_AppendFilter)


# ---------------------------------------------------------------------------------
#   Array calculator
# ---------------------------------------------------------------------------------


class BVTK_PG_ArrayCalculatorVariable(bpy.types.PropertyGroup):
    """ """
    var_name = bpy.props.StringProperty(name="Variable name")
    array_name = bpy.props.StringProperty(name="Array name")
    component_index = bpy.props.IntProperty(name="Component index", default=0)


class BVTK_OT_UpdateCalculatorVariables(bpy.types.Operator):
    """Add a variable for each array found in the input object.
    Works only for point and cell data
    """
    bl_idname = "bvtk.update_calculator_variables"
    bl_label = "Update variables"
    node_path = bpy.props.StringProperty()

    def execute(self, context):
        node = eval(self.node_path)
        if not node:
            return {"CANCELLED"}

        arr_names = []
        arr_found = True

        if node.e_AttributeType == "CellData" or \
           node.e_AttributeType == "Default":
            arr_names = node.cell_data_arrays()
            arr_found = len(arr_names)
        if node.e_AttributeType == "PointData" or \
           (node.e_AttributeType == "Default" and not arr_found):
            arr_names = node.point_data_arrays()

        for arr_name in arr_names:
            flag = False

            for var in node.variables:
                if arr_name == var.array_name:
                    flag = True

            if not flag:
                var = node.variables.add()
                var.array_name = arr_name
                var.var_name = arr_name

        node.add_variables()

        return {"FINISHED"}


class BVTK_OT_AddCalculatorVariable(bpy.types.Operator):
    """Add a variable to use in the function"""
    bl_idname = "bvtk.add_calculator_variable"
    bl_label = "Add variable"
    node_path = bpy.props.StringProperty()

    def execute(self, context):
        node = eval(self.node_path)
        if not node:
            return {"CANCELLED"}

        node.variables.add()

        return {"FINISHED"}


class BVTK_OT_RemoveCalculatorVariable(bpy.types.Operator):
    """Remove a variable"""
    bl_idname = "bvtk.remove_calculator_variable"
    bl_label = "Reset variable"
    node_path = bpy.props.StringProperty()
    var_index = bpy.props.IntProperty()

    def execute(self, context):
        node = eval(self.node_path)
        if not node:
            return {"CANCELLED"}

        node.variables.remove(self.var_index)

        node.add_variables()

        return {"FINISHED"}


class BVTK_NT_ArrayCalculator(Node, BVTK_NodePanels, BVTK_Node):
    bl_idname = 'BVTK_NT_ArrayCalculator'
    bl_label = 'vtkArrayCalculator'
    e_AttributeType_items = [(x, x, x) for x in
                             ['CellData', 'Default', 'EdgeData', 'PointData', 'RowData', 'VertexData']]

    e_AttributeType = bpy.props.EnumProperty(name='AttributeType',
                                             description="Control which AttributeType the filter operates on (point data or cell data for vtkDataSets). By default the filter uses Point/Vertex/Row data depending on the input data type. The input value for this function should be one of the constants in vtkDataObject::AttributeTypes or DEFAULT_ATTRIBUTE_TYPE for 'default behavior'",
                                             default='Default', items=e_AttributeType_items)
    m_CoordinateResults = bpy.props.BoolProperty(name='CoordinateResults',
                                                 description="Set whether to output results as coordinates. ResultArrayName will be ignored. Outputing as coordinates is only valid with vector results and if the AttributeMode is AttributeModeToUsePointData. If a valid output can't be made, an error will occur",
                                                 default=True)
    m_Function = bpy.props.StringProperty(name='Function', description='Set/Get the function to be evaluated')
    m_ReplaceInvalidValues = bpy.props.BoolProperty(name='ReplaceInvalidValues',
                                                    description='When ReplaceInvalidValues is on, all invalid values (such as sqrt(-2), note that function parser does not handle complex numbers) will be replaced by ReplacementValue. Otherwise an error will be reporte',
                                                    default=True)
    m_ReplacementValue = bpy.props.FloatProperty(name='ReplacementValue',
                                                 description='When ReplaceInvalidValues is on, all invalid values (such as sqrt(-2), note that function parser does not handle complex numbers) will be replaced by ReplacementValue. Otherwise an error will be reporte',
                                                 default=0.0)
    m_ResultArrayName = bpy.props.StringProperty(name='ResultArrayName',
                                                 description='Set the name of the array in which to store the result of evaluating this function. If this is the name of an existing array, that array will be overwritten. Otherwise a new array will be created with the specified name',
                                                 default='resultArray')
    m_ResultArrayType = bpy.props.IntProperty(name='ResultArrayType',
                                              description='Type of the result array. It is ignored if CoordinateResults is true. Initial value is VTK_DOUBLE',
                                              default=11)
    m_ResultNormals = bpy.props.BoolProperty(name='ResultNormals',
                                             description='Set whether to output results as point/cell normals. Outputing as normals is only valid with vector results. Point or cell normals are selected using AttributeMode',
                                             default=False)
    m_ResultTCoords = bpy.props.BoolProperty(name='ResultTCoords',
                                             description='Set whether to output results as point/cell texture coordinates. Point or cell texture coordinates are selected using AttributeMode. 2-component texture coordinates cannot be generated at this time',
                                             default=False)

    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    variables = bpy.props.CollectionProperty(type=BVTK_PG_ArrayCalculatorVariable)

    def draw_buttons(self, context, layout):
        m_properties = self.m_properties()
        for i in range(len(m_properties)):
            if self.b_properties[i]:
                layout.prop(self, m_properties[i])
        self.draw_panels(context, layout)

    def data_array_names(self, method):
        """Analyze the input object and retrieve all the arrays
        available using the given method (passed as a string).
        For example you can pass 'GetPointData' to retrieve
        the list of point data arrays.
        """
        arrays = []
        vtkobj = resolve_algorithm_output(self.get_input_node("Input")[1])
        if vtkobj:
            if hasattr(vtkobj, method):
                arr_data = getattr(vtkobj, method)()
                for i in range(arr_data.GetNumberOfArrays()):
                    arrays.append(str(arr_data.GetArrayName(i)))
        return arrays

    def point_data_arrays(self):
        """Analyze the input object and return a list
        of the names of point data arrays.
        """
        return self.data_array_names("GetPointData")

    def cell_data_arrays(self):
        """Analyze the input object and return a list
        of the names of cell data arrays.
        """
        return self.data_array_names("GetCellData")

    def update_variables(self):
        bpy.ops.bvtk.update_calculator_variables(
            node_path=node_path(self)
        )

    def add_variables(self):
        """Add a variable to the array calculator vtk object."""
        self.reset_variables()
        vtk_obj = self.get_vtkobj()
        if vtk_obj:
            for var in self.variables:
                vtk_obj.AddScalarVariable(var.var_name, var.array_name, var.component_index)

    def reset_variables(self):
        """Remove all variables from the array calculator vtk object."""
        vtk_obj = self.get_vtkobj()
        if vtk_obj:
            vtk_obj.RemoveAllVariables()

    def draw_variables(self, context, layout):
        row = layout.row()
        col_0 = row.column()
        col_1 = row.column()
        col_2 = row.column()
        col_3 = row.column()
        col_0.scale_x = 0.1
        col_3.scale_x = 0.3
        col_0.label(text="")
        col_1.label(text="Variable name")
        col_2.label(text="Array name")
        col_3.label(text="Component")

        for i, var in enumerate(self.variables):
            op = col_0.operator(BVTK_OT_RemoveCalculatorVariable.bl_idname, icon="X", emboss=False, text="")
            op.node_path = node_path(self)
            op.var_index = i
            col_1.prop(var, "var_name", text="")
            col_2.prop(var, "array_name", text="")
            col_3.prop(var, "component_index", text="")

        small_separator(layout)
        col = layout.column(align=True)
        op = col.operator(BVTK_OT_UpdateCalculatorVariables.bl_idname, icon="FILE_REFRESH")
        op.node_path = node_path(self)

        op = col.operator(BVTK_OT_AddCalculatorVariable.bl_idname, icon="ZOOMIN")
        op.node_path = node_path(self)

    def setup(self):
        self.update_variables()

    def apply_properties(self, vtkobj):
        if vtkobj:
            # Reset the calculator function. It seems that if
            # the function doesn't change vtk won't check for
            # changes in the variable names, and this may
            # be a problem while using the node.
            vtkobj.SetFunction("")
        # Check and add the variables
        self.update_variables()
        # Apply as usual all the properties
        super().apply_properties(vtkobj)

    _panels = [
        ("Variables", draw_variables)
    ]

    def m_properties(self):
        return ['e_AttributeType', 'm_CoordinateResults', 'm_Function', 'm_ReplaceInvalidValues', 'm_ReplacementValue',
                'm_ResultArrayName', 'm_ResultArrayType', 'm_ResultNormals', 'm_ResultTCoords', ]

    def m_connections(self):
        return ['Input'], ['Output'], [], []

    def methods(self):
        return []


register.add_class(BVTK_PG_ValueSettings)
register.add_class(BVTK_OT_UpdateCollection)
register.add_class(BVTK_PG_ArrayCalculatorVariable)
register.add_class(BVTK_OT_UpdateCalculatorVariables)
register.add_class(BVTK_OT_RemoveCalculatorVariable)
register.add_class(BVTK_OT_AddCalculatorVariable)
add_node(BVTK_NT_ArrayCalculator)
