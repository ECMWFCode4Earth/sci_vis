from .core import *
TYPENAMES = []


# --------------------------------------------------------------


class BVTK_NT_SPHInterpolator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SPHInterpolator'
    bl_label = 'vtkSPHInterpolator'
    e_NullPointsStrategy_items = [(x, x, x) for x in ['MaskPoints', 'NullValue']]
    
    m_ComputeShepardSum = bpy.props.BoolProperty(name='ComputeShepardSum', description='Indicate whether to compute the summation of weighting coefficients (the so-called Shepard sum). In the interior of a SPH point cloud, the Shephard summation value should be ~1.0. Towards the boundary, the Shepard summation generally falls off <1.0. If ComputeShepardSum is specified, then the output will contain an array of summed Shepard weights for each output point. On by default', default=True)
    m_CutoffArrayName = bpy.props.StringProperty(name='CutoffArrayName', description='Specify an (optional) cutoff distance for each point in the input P. If not specified, then the kernel cutoff is used', default='')
    m_DensityArrayName = bpy.props.StringProperty(name='DensityArrayName', description='Specify the density array name. This is optional. Typically both the density and mass arrays are specified together (in order to compute the local volume). Both the mass and density arrays must consist of tuples of 1-component. (Note that the density array name specifies a point array found in the Pc source.', default='Rho')
    m_MassArrayName = bpy.props.StringProperty(name='MassArrayName', description='Specify the mass array name. This is optional. Typically both the density and mass arrays are specified together (in order to compute the local volume). Both the mass and density arrays must consist of tuples of 1-component. (Note that the mass array name specifies a point array found in the Pc source.', default='')
    e_NullPointsStrategy = bpy.props.EnumProperty(name='NullPointsStrategy', description='Specify a strategy to use when encountering a "null" point during the interpolation process. Null points occur when the local neighborhood (of nearby points to interpolate from) is empty. If the strategy is set to MaskPoints, then an output array is created that marks points as being valid (=1) or null (invalid =0) (and the NullValue is set as well). If the strategy is set to NullValue, then the output data value(s) are set to the NullPoint value', default='NullValue', items=e_NullPointsStrategy_items)
    m_NullValue = bpy.props.FloatProperty(name='NullValue', description='Specify the null point value. When a null point is encountered then all components of each null tuple are set to this value. By default the null value is set to zero', default=0.0)
    m_PassCellArrays = bpy.props.BoolProperty(name='PassCellArrays', description='Indicate whether to shallow copy the input cell data arrays to the output. On by default', default=True)
    m_PassFieldArrays = bpy.props.BoolProperty(name='PassFieldArrays', description='Indicate whether to pass the field-data arrays from the input to the output. On by default', default=True)
    m_PassPointArrays = bpy.props.BoolProperty(name='PassPointArrays', description='Indicate whether to shallow copy the input point data arrays to the output. On by default', default=True)
    m_PromoteOutputArrays = bpy.props.BoolProperty(name='PromoteOutputArrays', description='If enabled, then input arrays that are non-real types (i.e., not float or double) are promoted to float type on output. This is because the interpolation process may not be well behaved when integral types are combined using interpolation weights', default=True)
    m_ShepardSumArrayName = bpy.props.StringProperty(name='ShepardSumArrayName', description='If ComputeShepardSum is on, then an array is generated with name ShepardSumArrayName for each input point. This vtkFloatArray is placed into the output of the filter, and NullPoints have value =0.0. The default name is "Shepard Summation"', default='Shepard Summation')
    m_ValidPointsMaskArrayName = bpy.props.StringProperty(name='ValidPointsMaskArrayName', description='If the NullPointsStrategy == MASK_POINTS, then an array is generated for each input point. This vtkCharArray is placed into the output of the filter, with a non-zero value for a valid point, and zero otherwise. The name of this masking array is specified here', default='vtkValidPointMask')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeShepardSum', 'm_CutoffArrayName', 'm_DensityArrayName', 'm_MassArrayName', 'e_NullPointsStrategy', 'm_NullValue', 'm_PassCellArrays', 'm_PassFieldArrays', 'm_PassPointArrays', 'm_PromoteOutputArrays', 'm_ShepardSumArrayName', 'm_ValidPointsMaskArrayName', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['Kernel'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SPHInterpolator)
TYPENAMES.append('BVTK_NT_SPHInterpolator' )


# --------------------------------------------------------------


class BVTK_NT_ProbeFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProbeFilter'
    bl_label = 'vtkProbeFilter'
    
    m_CategoricalData = bpy.props.BoolProperty(name='CategoricalData', description='Control whether the source point data is to be treated as categorical. If the data is categorical, then the resultant data will be determined by a nearest neighbor interpolation scheme', default=True)
    m_ComputeTolerance = bpy.props.BoolProperty(name='ComputeTolerance', description='Set whether to use the Tolerance field or precompute the tolerance. When on, the tolerance will be computed and the field value is ignored. Off by default', default=True)
    m_PassCellArrays = bpy.props.BoolProperty(name='PassCellArrays', description='Shallow copy the input cell data arrays to the output. Off by default', default=True)
    m_PassFieldArrays = bpy.props.BoolProperty(name='PassFieldArrays', description='Set whether to pass the field-data arrays from the Input i.e. the input providing the geometry to the output. On by default', default=True)
    m_PassPointArrays = bpy.props.BoolProperty(name='PassPointArrays', description='Shallow copy the input point data arrays to the output Off by default', default=True)
    m_SpatialMatch = bpy.props.BoolProperty(name='SpatialMatch', description='This flag is used only when a piece is requested to update. By default the flag is off. Because no spatial correspondence between input pieces and source pieces is known, all of the source has to be requested no matter what piece of the output is requested. When there is a spatial correspondence, the user/application can set this flag. This hint allows the breakup of the probe operation to be much more efficient. When piece m of n is requested for update by the user, then only n of m needs to be requested of the source', default=True)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Set the tolerance used to compute whether a point in the source is in a cell of the input. This value is only used if ComputeTolerance is off', default=1.0)
    m_ValidPointMaskArrayName = bpy.props.StringProperty(name='ValidPointMaskArrayName', description='Returns the name of the char array added to the output with values 1 for valid points and 0 for invalid points. Set to "vtkValidPointMask" by default', default='vtkValidPointMask')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CategoricalData', 'm_ComputeTolerance', 'm_PassCellArrays', 'm_PassFieldArrays', 'm_PassPointArrays', 'm_SpatialMatch', 'm_Tolerance', 'm_ValidPointMaskArrayName', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProbeFilter)
TYPENAMES.append('BVTK_NT_ProbeFilter' )


# --------------------------------------------------------------


class BVTK_NT_GenericStreamTracer(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GenericStreamTracer'
    bl_label = 'vtkGenericStreamTracer'
    e_InitialIntegrationStepUnit_items = [(x, x, x) for x in ['CellLengthUnit', 'LengthUnit', 'TimeUnit']]
    e_IntegrationDirection_items = [(x, x, x) for x in ['Backward', 'Both', 'Forward']]
    e_IntegratorType_items = [(x, x, x) for x in ['RungeKutta2', 'RungeKutta4', 'RungeKutta45']]
    e_MaximumIntegrationStepUnit_items = [(x, x, x) for x in ['CellLengthUnit', 'LengthUnit', 'TimeUnit']]
    e_MaximumPropagationUnit_items = [(x, x, x) for x in ['CellLengthUnit', 'LengthUnit', 'TimeUnit']]
    e_MinimumIntegrationStepUnit_items = [(x, x, x) for x in ['CellLengthUnit', 'LengthUnit', 'TimeUnit']]
    
    m_ComputeVorticity = bpy.props.BoolProperty(name='ComputeVorticity', description='Turn on/off calculation of vorticity at streamline points (necessary for generating proper streamribbons using the vtkRibbonFilter', default=True)
    m_InitialIntegrationStep = bpy.props.FloatProperty(name='InitialIntegrationStep', description='Specify the initial step used in the integration expressed in one of the: TIME_UNIT = 0 LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 If the integrator is not adaptive, this is the actual step used', default=0.5)
    e_InitialIntegrationStepUnit = bpy.props.EnumProperty(name='InitialIntegrationStepUnit', description='Specify the initial step used in the integration expressed in one of the: TIME_UNIT = 0 LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 If the integrator is not adaptive, this is the actual step used', default='CellLengthUnit', items=e_InitialIntegrationStepUnit_items)
    e_IntegrationDirection = bpy.props.EnumProperty(name='IntegrationDirection', description='Specify whether the streamtrace will be generated in the upstream or downstream direction', default='Forward', items=e_IntegrationDirection_items)
    e_IntegratorType = bpy.props.EnumProperty(name='IntegratorType', description='Set/get the integrator type to be used in the stream line calculation. The object passed is not actually used but is cloned with NewInstance in the process of integration (prototype pattern). The default is 2nd order Runge Kutta. The integrator can also be changed using SetIntegratorType. The recognized solvers are: RUNGE_KUTTA2 = 0 RUNGE_KUTTA4 = 1 RUNGE_KUTTA45 = ', default='RungeKutta2', items=e_IntegratorType_items)
    m_MaximumError = bpy.props.FloatProperty(name='MaximumError', description="Specify the maximum error in the integration. This value is passed to the integrator. Therefore, it's meaning depends on the integrator used", default=1e-06)
    m_MaximumIntegrationStep = bpy.props.FloatProperty(name='MaximumIntegrationStep', description='Specify the maximum step used in the integration expressed in one of the: TIME_UNIT = 0 LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 Only valid when using adaptive integrators', default=1.0)
    e_MaximumIntegrationStepUnit = bpy.props.EnumProperty(name='MaximumIntegrationStepUnit', description='Specify the maximum step used in the integration expressed in one of the: TIME_UNIT = 0 LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 Only valid when using adaptive integrators', default='CellLengthUnit', items=e_MaximumIntegrationStepUnit_items)
    m_MaximumNumberOfSteps = bpy.props.IntProperty(name='MaximumNumberOfSteps', description='Specify the maximum number of steps used in the integration', default=2000)
    m_MaximumPropagation = bpy.props.FloatProperty(name='MaximumPropagation', description='Specify the maximum length of the streamlines expressed in one of the: TIME_UNIT = 0 LENGTH_UNIT = 1 CELL_LENGTH_UNIT = ', default=1.0)
    e_MaximumPropagationUnit = bpy.props.EnumProperty(name='MaximumPropagationUnit', description='Specify the maximum length of the streamlines expressed in one of the: TIME_UNIT = 0 LENGTH_UNIT = 1 CELL_LENGTH_UNIT = ', default='LengthUnit', items=e_MaximumPropagationUnit_items)
    m_MinimumIntegrationStep = bpy.props.FloatProperty(name='MinimumIntegrationStep', description='Specify the minimum step used in the integration expressed in one of the: TIME_UNIT = 0 LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 Only valid when using adaptive integrators', default=0.01)
    e_MinimumIntegrationStepUnit = bpy.props.EnumProperty(name='MinimumIntegrationStepUnit', description='Specify the minimum step used in the integration expressed in one of the: TIME_UNIT = 0 LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 Only valid when using adaptive integrators', default='CellLengthUnit', items=e_MinimumIntegrationStepUnit_items)
    m_RotationScale = bpy.props.FloatProperty(name='RotationScale', description='This can be used to scale the rate with which the streamribbons twist. The default is 1', default=1.0)
    m_StartPosition = bpy.props.FloatVectorProperty(name='StartPosition', description='', default=[0.0, 0.0, 0.0], size=3)
    m_TerminalSpeed = bpy.props.FloatProperty(name='TerminalSpeed', description='If at any point, the speed is below this value, the integration is terminated', default=1e-12)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeVorticity', 'm_InitialIntegrationStep', 'e_InitialIntegrationStepUnit', 'e_IntegrationDirection', 'e_IntegratorType', 'm_MaximumError', 'm_MaximumIntegrationStep', 'e_MaximumIntegrationStepUnit', 'm_MaximumNumberOfSteps', 'm_MaximumPropagation', 'e_MaximumPropagationUnit', 'm_MinimumIntegrationStep', 'e_MinimumIntegrationStepUnit', 'm_RotationScale', 'm_StartPosition', 'm_TerminalSpeed', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['Integrator'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GenericStreamTracer)
TYPENAMES.append('BVTK_NT_GenericStreamTracer' )


# --------------------------------------------------------------


class BVTK_NT_ApplyIcons(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ApplyIcons'
    bl_label = 'vtkApplyIcons'
    e_SelectionMode_items = [(x, x, x) for x in ['AnnotationIcon', 'IgnoreSelection', 'SelectedIcon', 'SelectedOffset']]
    
    m_AttributeType = bpy.props.IntProperty(name='AttributeType', description='The attribute type to append the icon array to, used only if the input array is not specified or does not exist. This is set to one of the AttributeTypes enum in vtkDataObject (e.g. POINT, CELL, VERTEX EDGE, FIELD)', default=4)
    m_DefaultIcon = bpy.props.IntProperty(name='DefaultIcon', description='The default point icon for all unannotated, unselected elements of the data. This is used if UsePointLookupTable is off', default=-1)
    m_IconOutputArrayName = bpy.props.StringProperty(name='IconOutputArrayName', description='The output array name for the point icon index array. Default is "vtkApplyIcons icon"', default='vtkApplyIcons icon')
    m_SelectedIcon = bpy.props.IntProperty(name='SelectedIcon', description='The point icon for all selected elements of the data. This is used if the annotation input has a current selection', default=0)
    e_SelectionMode = bpy.props.EnumProperty(name='SelectionMode', description='Changes the behavior of the icon to use for selected items. SELECTED_ICON uses SelectedIcon as the icon for all selected elements. SELECTED_OFFSET uses SelectedIcon as an offset to add to all selected elements. ANNOTATION_ICON uses the ICON_INDEX() property of the current annotation. IGNORE_SELECTION does not change the icon based on the current selection. The default is IGNORE_SELECTION', default='IgnoreSelection', items=e_SelectionMode_items)
    m_UseLookupTable = bpy.props.BoolProperty(name='UseLookupTable', description='If on, uses the point lookup table to set the colors of unannotated, unselected elements of the data', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AttributeType', 'm_DefaultIcon', 'm_IconOutputArrayName', 'm_SelectedIcon', 'e_SelectionMode', 'm_UseLookupTable', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ApplyIcons)
TYPENAMES.append('BVTK_NT_ApplyIcons' )


# --------------------------------------------------------------


class BVTK_NT_PointInterpolator2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PointInterpolator2D'
    bl_label = 'vtkPointInterpolator2D'
    e_NullPointsStrategy_items = [(x, x, x) for x in ['ClosestPoint', 'MaskPoints', 'NullValue']]
    
    m_InterpolateZ = bpy.props.BoolProperty(name='InterpolateZ', description='Specify whether to take the z-coordinate values of the source points as attributes to be interpolated. This is in addition to any other point attribute data associated with the source. By default this is enabled', default=True)
    e_NullPointsStrategy = bpy.props.EnumProperty(name='NullPointsStrategy', description='Specify a strategy to use when encountering a "null" point during the interpolation process. Null points occur when the local neighborhood (of nearby points to interpolate from) is empty. If the strategy is set to MaskPoints, then an output array is created that marks points as being valid (=1) or null (invalid =0) (and the NullValue is set as well). If the strategy is set to NullValue (this is the default), then the output data value(s) are set to the NullPoint value (specified in the output point data). Finally, the strategy ClosestPoint is to simply use the closest point to perform the interpolation', default='NullValue', items=e_NullPointsStrategy_items)
    m_NullValue = bpy.props.FloatProperty(name='NullValue', description='Specify the null point value. When a null point is encountered then all components of each null tuple are set to this value. By default the null value is set to zero', default=0.0)
    m_PassCellArrays = bpy.props.BoolProperty(name='PassCellArrays', description='Indicate whether to shallow copy the input cell data arrays to the output. On by default', default=True)
    m_PassFieldArrays = bpy.props.BoolProperty(name='PassFieldArrays', description='Indicate whether to pass the field-data arrays from the input to the output. On by default', default=True)
    m_PassPointArrays = bpy.props.BoolProperty(name='PassPointArrays', description='Indicate whether to shallow copy the input point data arrays to the output. On by default', default=True)
    m_PromoteOutputArrays = bpy.props.BoolProperty(name='PromoteOutputArrays', description='If enabled, then input arrays that are non-real types (i.e., not float or double) are promoted to float type on output. This is because the interpolation process may not be well behaved when integral types are combined using interpolation weights', default=True)
    m_ValidPointsMaskArrayName = bpy.props.StringProperty(name='ValidPointsMaskArrayName', description='If the NullPointsStrategy == MASK_POINTS, then an array is generated for each input point. This vtkCharArray is placed into the output of the filter, with a non-zero value for a valid point, and zero otherwise. The name of this masking array is specified here', default='vtkValidPointMask')
    m_ZArrayName = bpy.props.StringProperty(name='ZArrayName', description='Specify the name of the output array containing z values. This method is only applicable when InterpolateZ is enabled. By default the output array name is "Elevation"', default='Elevation')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_InterpolateZ', 'e_NullPointsStrategy', 'm_NullValue', 'm_PassCellArrays', 'm_PassFieldArrays', 'm_PassPointArrays', 'm_PromoteOutputArrays', 'm_ValidPointsMaskArrayName', 'm_ZArrayName', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['Kernel'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PointInterpolator2D)
TYPENAMES.append('BVTK_NT_PointInterpolator2D' )


# --------------------------------------------------------------


class BVTK_NT_PointInterpolator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PointInterpolator'
    bl_label = 'vtkPointInterpolator'
    e_NullPointsStrategy_items = [(x, x, x) for x in ['ClosestPoint', 'MaskPoints', 'NullValue']]
    
    e_NullPointsStrategy = bpy.props.EnumProperty(name='NullPointsStrategy', description='Specify a strategy to use when encountering a "null" point during the interpolation process. Null points occur when the local neighborhood (of nearby points to interpolate from) is empty. If the strategy is set to MaskPoints, then an output array is created that marks points as being valid (=1) or null (invalid =0) (and the NullValue is set as well). If the strategy is set to NullValue (this is the default), then the output data value(s) are set to the NullPoint value (specified in the output point data). Finally, the strategy ClosestPoint is to simply use the closest point to perform the interpolation', default='NullValue', items=e_NullPointsStrategy_items)
    m_NullValue = bpy.props.FloatProperty(name='NullValue', description='Specify the null point value. When a null point is encountered then all components of each null tuple are set to this value. By default the null value is set to zero', default=0.0)
    m_PassCellArrays = bpy.props.BoolProperty(name='PassCellArrays', description='Indicate whether to shallow copy the input cell data arrays to the output. On by default', default=True)
    m_PassFieldArrays = bpy.props.BoolProperty(name='PassFieldArrays', description='Indicate whether to pass the field-data arrays from the input to the output. On by default', default=True)
    m_PassPointArrays = bpy.props.BoolProperty(name='PassPointArrays', description='Indicate whether to shallow copy the input point data arrays to the output. On by default', default=True)
    m_PromoteOutputArrays = bpy.props.BoolProperty(name='PromoteOutputArrays', description='If enabled, then input arrays that are non-real types (i.e., not float or double) are promoted to float type on output. This is because the interpolation process may not be well behaved when integral types are combined using interpolation weights', default=True)
    m_ValidPointsMaskArrayName = bpy.props.StringProperty(name='ValidPointsMaskArrayName', description='If the NullPointsStrategy == MASK_POINTS, then an array is generated for each input point. This vtkCharArray is placed into the output of the filter, with a non-zero value for a valid point, and zero otherwise. The name of this masking array is specified here', default='vtkValidPointMask')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_NullPointsStrategy', 'm_NullValue', 'm_PassCellArrays', 'm_PassFieldArrays', 'm_PassPointArrays', 'm_PromoteOutputArrays', 'm_ValidPointsMaskArrayName', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['Kernel'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PointInterpolator)
TYPENAMES.append('BVTK_NT_PointInterpolator' )


# --------------------------------------------------------------


class BVTK_NT_GenericGlyph3DFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GenericGlyph3DFilter'
    bl_label = 'vtkGenericGlyph3DFilter'
    e_ColorMode_items = [(x, x, x) for x in ['ColorByScalar', 'ColorByScale', 'ColorByVector']]
    e_IndexMode_items = [(x, x, x) for x in ['Off', 'Scalar', 'Vector']]
    e_ScaleMode_items = [(x, x, x) for x in ['DataScalingOff', 'ScaleByScalar', 'ScaleByVector', 'ScaleByVectorComponents']]
    e_VectorMode_items = [(x, x, x) for x in ['UseNormal', 'UseVector', 'VectorRotationOff']]
    
    m_Clamping = bpy.props.BoolProperty(name='Clamping', description='Turn on/off clamping of "scalar" values to range. (Scalar value may be vector magnitude if ScaleByVector() is enabled.', default=True)
    e_ColorMode = bpy.props.EnumProperty(name='ColorMode', description='Either color by scale, scalar or by vector/normal magnitude', default='ColorByScale', items=e_ColorMode_items)
    m_GeneratePointIds = bpy.props.BoolProperty(name='GeneratePointIds', description='Enable/disable the generation of point ids as part of the output. The point ids are the id of the input generating point. The point ids are stored in the output point field data and named "InputPointIds". Point generation is useful for debugging and pick operations', default=True)
    e_IndexMode = bpy.props.EnumProperty(name='IndexMode', description='Index into table of sources by scalar, by vector/normal magnitude, or no indexing. If indexing is turned off, then the first source glyph in the table of glyphs is used', default='Off', items=e_IndexMode_items)
    m_Orient = bpy.props.BoolProperty(name='Orient', description='Turn on/off orienting of input geometry along vector/normal', default=True)
    m_PointIdsName = bpy.props.StringProperty(name='PointIdsName', description='Set/Get the name of the PointIds array if generated. By default the Ids are named "InputPointIds", but this can be changed with this function', default='InputPointIds')
    m_Range = bpy.props.FloatVectorProperty(name='Range', description='Specify range to map scalar values into', default=[0.0, 1.0], size=2)
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Specify scale factor to scale object by', default=1.0)
    e_ScaleMode = bpy.props.EnumProperty(name='ScaleMode', description='Either scale by scalar or by vector/normal magnitude', default='ScaleByScalar', items=e_ScaleMode_items)
    m_Scaling = bpy.props.BoolProperty(name='Scaling', description='Turn on/off scaling of source geometry', default=True)
    e_VectorMode = bpy.props.EnumProperty(name='VectorMode', description='Specify whether to use vector or normal to perform vector operations', default='UseVector', items=e_VectorMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Clamping', 'e_ColorMode', 'm_GeneratePointIds', 'e_IndexMode', 'm_Orient', 'm_PointIdsName', 'm_Range', 'm_ScaleFactor', 'e_ScaleMode', 'm_Scaling', 'e_VectorMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GenericGlyph3DFilter)
TYPENAMES.append('BVTK_NT_GenericGlyph3DFilter' )


# --------------------------------------------------------------


class BVTK_NT_Glyph2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Glyph2D'
    bl_label = 'vtkGlyph2D'
    e_ColorMode_items = [(x, x, x) for x in ['ColorByScalar', 'ColorByScale', 'ColorByVector']]
    e_IndexMode_items = [(x, x, x) for x in ['Off', 'Scalar', 'Vector']]
    e_ScaleMode_items = [(x, x, x) for x in ['DataScalingOff', 'ScaleByScalar', 'ScaleByVector', 'ScaleByVectorComponents']]
    e_VectorMode_items = [(x, x, x) for x in ['UseNormal', 'UseVector', 'VectorRotationOff']]
    
    m_Clamping = bpy.props.BoolProperty(name='Clamping', description='Turn on/off clamping of "scalar" values to range. (Scalar value may be vector magnitude if ScaleByVector() is enabled.', default=True)
    e_ColorMode = bpy.props.EnumProperty(name='ColorMode', description='Either color by scale, scalar or by vector/normal magnitude', default='ColorByScale', items=e_ColorMode_items)
    m_FillCellData = bpy.props.BoolProperty(name='FillCellData', description='Enable/disable the generation of cell data as part of the output. The cell data at each cell will match the point data of the input at the glyphed point', default=True)
    m_GeneratePointIds = bpy.props.BoolProperty(name='GeneratePointIds', description='Enable/disable the generation of point ids as part of the output. The point ids are the id of the input generating point. The point ids are stored in the output point field data and named "InputPointIds". Point generation is useful for debugging and pick operations', default=True)
    e_IndexMode = bpy.props.EnumProperty(name='IndexMode', description='Index into table of sources by scalar, by vector/normal magnitude, or no indexing. If indexing is turned off, then the first source glyph in the table of glyphs is used. Note that indexing mode will only use the InputScalarsSelection array and not the InputColorScalarsSelection as the scalar source if an array is specified', default='Off', items=e_IndexMode_items)
    m_Orient = bpy.props.BoolProperty(name='Orient', description='Turn on/off orienting of input geometry along vector/normal', default=True)
    m_PointIdsName = bpy.props.StringProperty(name='PointIdsName', description='Set/Get the name of the PointIds array if generated. By default the Ids are named "InputPointIds", but this can be changed with this function', default='InputPointIds')
    m_Range = bpy.props.FloatVectorProperty(name='Range', description='Specify range to map scalar values into', default=[0.0, 1.0], size=2)
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Specify scale factor to scale object by', default=1.0)
    e_ScaleMode = bpy.props.EnumProperty(name='ScaleMode', description='Either scale by scalar or by vector/normal magnitude', default='ScaleByScalar', items=e_ScaleMode_items)
    m_Scaling = bpy.props.BoolProperty(name='Scaling', description='Turn on/off scaling of source geometry', default=True)
    e_VectorMode = bpy.props.EnumProperty(name='VectorMode', description='Specify whether to use vector or normal to perform vector operations', default='UseVector', items=e_VectorMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Clamping', 'e_ColorMode', 'm_FillCellData', 'm_GeneratePointIds', 'e_IndexMode', 'm_Orient', 'm_PointIdsName', 'm_Range', 'm_ScaleFactor', 'e_ScaleMode', 'm_Scaling', 'e_VectorMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['SourceTransform'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Glyph2D)
TYPENAMES.append('BVTK_NT_Glyph2D' )


# --------------------------------------------------------------


class BVTK_NT_ExtractSelectedFrustum(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractSelectedFrustum'
    bl_label = 'vtkExtractSelectedFrustum'
    
    m_ContainingCells = bpy.props.IntProperty(name='ContainingCells', description='Sets/gets the intersection test type. Only meaningful when fieldType is vtkSelection::POIN', default=0)
    m_FieldType = bpy.props.IntProperty(name='FieldType', description='Sets/gets the intersection test type', default=0)
    m_InsideOut = bpy.props.BoolProperty(name='InsideOut', description='When on, extracts cells outside the frustum instead of inside', default=True)
    m_PreserveTopology = bpy.props.BoolProperty(name='PreserveTopology', description='This flag tells the extraction filter not to convert the selected output into an unstructured grid, but instead to produce a vtkInsidedness array and add it to the input dataset. Default value is false(0)', default=True)
    m_ShowBounds = bpy.props.BoolProperty(name='ShowBounds', description='When On, this returns an unstructured grid that outlines selection area. Off is the default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ContainingCells', 'm_FieldType', 'm_InsideOut', 'm_PreserveTopology', 'm_ShowBounds', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['Frustum'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractSelectedFrustum)
TYPENAMES.append('BVTK_NT_ExtractSelectedFrustum' )


# --------------------------------------------------------------


class BVTK_NT_GenericProbeFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GenericProbeFilter'
    bl_label = 'vtkGenericProbeFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GenericProbeFilter)
TYPENAMES.append('BVTK_NT_GenericProbeFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageHistogram(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageHistogram'
    bl_label = 'vtkImageHistogram'
    e_HistogramImageScale_items = [(x, x, x) for x in ['Linear', 'Log', 'Sqrt']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_ActiveComponent = bpy.props.IntProperty(name='ActiveComponent', description='Set the component for which to generate a histogram. The default value is -1, which produces a histogram that is the sum of the histograms of the individual components', default=-1)
    m_AutomaticBinning = bpy.props.BoolProperty(name='AutomaticBinning', description='If this is On, then the histogram binning will be done automatically. For char and unsigned char data, there will be 256 bins with unit spacing. For data of type short and larger, there will be between 256 and MaximumNumberOfBins, depending on the range of the data, and the BinOrigin will be set to zero if no negative values are present, or to the smallest negative value if negative values are present. For float data, the MaximumNumberOfBins will always be used. The BinOrigin and BinSpacing will be set so that they provide a mapping from bin index to scalar value', default=True)
    m_BinOrigin = bpy.props.FloatProperty(name='BinOrigin', description='The value for the center of the first bin (default 0). This is automatically computed unless AutomaticBinning is Off', default=0.0)
    m_BinSpacing = bpy.props.FloatProperty(name='BinSpacing', description='The bin spacing (default 1). This is automatically computed unless AutomaticBinning is Off', default=1.0)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GenerateHistogramImage = bpy.props.BoolProperty(name='GenerateHistogramImage', description='If this is On, then a histogram image will be produced as the output. Regardless of this setting, the histogram is always available as a vtkIdTypeArray from the GetHistogram method', default=True)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    e_HistogramImageScale = bpy.props.EnumProperty(name='HistogramImageScale', description='Set the scale to use for the histogram image. The default is a linear scale, but sqrt and log provide better visualization', default='Linear', items=e_HistogramImageScale_items)
    m_HistogramImageSize = bpy.props.IntVectorProperty(name='HistogramImageSize', description='', default=[256, 256], size=2)
    m_MaximumNumberOfBins = bpy.props.IntProperty(name='MaximumNumberOfBins', description='The maximum number of bins to use when AutomaticBinning is On. When AutomaticBinning is On, the size of the output histogram will be set to the full range of the input data values, unless the full range is greater than this value. By default, the max value is 65536, which is large enough to capture the full range of 16-bit integers', default=65536)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfBins = bpy.props.IntProperty(name='NumberOfBins', description='The number of bins in histogram (default 256). This is automatically computed unless AutomaticBinning is Off', default=256)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ActiveComponent', 'm_AutomaticBinning', 'm_BinOrigin', 'm_BinSpacing', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GenerateHistogramImage', 'm_GlobalDefaultEnableSMP', 'e_HistogramImageScale', 'm_HistogramImageSize', 'm_MaximumNumberOfBins', 'm_MinimumPieceSize', 'm_NumberOfBins', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageHistogram)
TYPENAMES.append('BVTK_NT_ImageHistogram' )


# --------------------------------------------------------------


class BVTK_NT_ProgrammableGlyphFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProgrammableGlyphFilter'
    bl_label = 'vtkProgrammableGlyphFilter'
    e_ColorMode_items = [(x, x, x) for x in ['ColorByInput', 'ColorBySource']]
    
    e_ColorMode = bpy.props.EnumProperty(name='ColorMode', description='Either color by the input or source scalar data', default='ColorByInput', items=e_ColorMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ColorMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProgrammableGlyphFilter)
TYPENAMES.append('BVTK_NT_ProgrammableGlyphFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageCheckerboard(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageCheckerboard'
    bl_label = 'vtkImageCheckerboard'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfDivisions = bpy.props.IntVectorProperty(name='NumberOfDivisions', description='Set/Get the number of divisions along each axis', default=[2, 2, 2], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfDivisions', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageCheckerboard)
TYPENAMES.append('BVTK_NT_ImageCheckerboard' )


# --------------------------------------------------------------


class BVTK_NT_ConvertSelection(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ConvertSelection'
    bl_label = 'vtkConvertSelection'
    
    m_AllowMissingArray = bpy.props.BoolProperty(name='AllowMissingArray', description='When enabled, not finding expected array will not return an error. Defaults to OFF', default=False)
    m_ArrayName = bpy.props.StringProperty(name='ArrayName', description='The output array name for value or threshold selections')
    m_InputFieldType = bpy.props.IntProperty(name='InputFieldType', description='The input field type. If this is set to a number other than -1, ignores the input selection field type and instead assumes that all selection nodes have the field type specified. This should be one of the constants defined in vtkSelectionNode.h. Default is -1', default=-1)
    m_MatchAnyValues = bpy.props.BoolProperty(name='MatchAnyValues', description='When on, creates a separate selection node for each array. Defaults to OFF', default=False)
    m_OutputType = bpy.props.IntProperty(name='OutputType', description='The output selection content type. This should be one of the constants defined in vtkSelectionNode.h', default=4)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AllowMissingArray', 'm_ArrayName', 'm_InputFieldType', 'm_MatchAnyValues', 'm_OutputType', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['ArrayNames', 'SelectionExtractor'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ConvertSelection)
TYPENAMES.append('BVTK_NT_ConvertSelection' )


# --------------------------------------------------------------


class BVTK_NT_ImageAccumulate(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageAccumulate'
    bl_label = 'vtkImageAccumulate'
    
    m_ComponentOrigin = bpy.props.FloatVectorProperty(name='ComponentOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    m_ComponentSpacing = bpy.props.FloatVectorProperty(name='ComponentSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_IgnoreZero = bpy.props.BoolProperty(name='IgnoreZero', description='Should the data with value 0 be ignored? Initial value is false', default=True)
    m_ReverseStencil = bpy.props.BoolProperty(name='ReverseStencil', description='Reverse the stencil. Initial value is false', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComponentOrigin', 'm_ComponentSpacing', 'm_IgnoreZero', 'm_ReverseStencil', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageAccumulate)
TYPENAMES.append('BVTK_NT_ImageAccumulate' )


# --------------------------------------------------------------


class BVTK_NT_ProbeSelectedLocations(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProbeSelectedLocations'
    bl_label = 'vtkProbeSelectedLocations'
    
    m_PreserveTopology = bpy.props.BoolProperty(name='PreserveTopology', description='This flag tells the extraction filter not to convert the selected output into an unstructured grid, but instead to produce a vtkInsidedness array and add it to the input dataset. Default value is false(0)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PreserveTopology', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProbeSelectedLocations)
TYPENAMES.append('BVTK_NT_ProbeSelectedLocations' )


# --------------------------------------------------------------


class BVTK_NT_ImageDotProduct(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageDotProduct'
    bl_label = 'vtkImageDotProduct'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageDotProduct)
TYPENAMES.append('BVTK_NT_ImageDotProduct' )


# --------------------------------------------------------------


class BVTK_NT_ParallelCoordinatesHistogramRepresentation(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ParallelCoordinatesHistogramRepresentation'
    bl_label = 'vtkParallelCoordinatesHistogramRepresentation'
    
    m_AngleBrushThreshold = bpy.props.FloatProperty(name='AngleBrushThreshold', description='Maximum angle difference (in degrees) of selection using angle/function brushe', default=0.03)
    m_AxisColor = bpy.props.FloatVectorProperty(name='AxisColor', description='', default=[1.0, 0.8, 0.3], size=3)
    m_AxisLabelColor = bpy.props.FloatVectorProperty(name='AxisLabelColor', description='', default=[1.0, 1.0, 1.0], size=3)
    m_CurveResolution = bpy.props.IntProperty(name='CurveResolution', description='Resolution of the curves displayed, enabled by setting UseCurve', default=20)
    m_FontSize = bpy.props.FloatProperty(name='FontSize', description='Access plot propertie', default=1.0)
    m_FunctionBrushThreshold = bpy.props.FloatProperty(name='FunctionBrushThreshold', description='Maximum angle difference (in degrees) of selection using angle/function brushe', default=0.1)
    m_HistogramLookupTableRange = bpy.props.FloatVectorProperty(name='HistogramLookupTableRange', description='', default=[0.0, 10.0], size=2)
    m_LabelRenderMode = bpy.props.IntProperty(name='LabelRenderMode', description='Set the label render mode. vtkRenderView::QT - Use Qt-based labeler with fitted labeling and unicode support. Requires VTK_USE_QT to be on. vtkRenderView::FREETYPE - Use standard freetype text rendering', default=0)
    m_LineColor = bpy.props.FloatVectorProperty(name='LineColor', description='', default=[1.0, 1.0, 1.0], size=3)
    m_LineOpacity = bpy.props.FloatProperty(name='LineOpacity', description='Access plot propertie', default=1.0)
    m_NumberOfAxisLabels = bpy.props.IntProperty(name='NumberOfAxisLabels', description='Set/Get the number of labels to display on each axi', default=2)
    m_PreferredNumberOfOutliers = bpy.props.IntProperty(name='PreferredNumberOfOutliers', description='Target maximum number of outliers to be drawn, although not guaranteed', default=100)
    m_Selectable = bpy.props.BoolProperty(name='Selectable', description='Whether this representation is able to handle a selection. Default is true', default=True)
    m_SelectionArrayName = bpy.props.StringProperty(name='SelectionArrayName', description='If a VALUES selection, the array used to produce a selection')
    m_SelectionType = bpy.props.IntProperty(name='SelectionType', description='Set the selection type produced by this view. This should be one of the content type constants defined in vtkSelectionNode.h. Common values are vtkSelectionNode::INDICES vtkSelectionNode::PEDIGREEIDS vtkSelectionNode::VALUE', default=4)
    m_ShowOutliers = bpy.props.BoolProperty(name='ShowOutliers', description='Whether to compute and show outlier line', default=True)
    m_UseCurves = bpy.props.BoolProperty(name='UseCurves', description='Whether or not to display using curve', default=True)
    m_UseHistograms = bpy.props.BoolProperty(name='UseHistograms', description="Whether to use the histogram rendering mode or the superclass's line rendering mod", default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AngleBrushThreshold', 'm_AxisColor', 'm_AxisLabelColor', 'm_CurveResolution', 'm_FontSize', 'm_FunctionBrushThreshold', 'm_HistogramLookupTableRange', 'm_LabelRenderMode', 'm_LineColor', 'm_LineOpacity', 'm_NumberOfAxisLabels', 'm_PreferredNumberOfOutliers', 'm_Selectable', 'm_SelectionArrayName', 'm_SelectionType', 'm_ShowOutliers', 'm_UseCurves', 'm_UseHistograms', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['AnnotationLink', 'SelectionArrayNames'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ParallelCoordinatesHistogramRepresentation)
TYPENAMES.append('BVTK_NT_ParallelCoordinatesHistogramRepresentation' )


# --------------------------------------------------------------


class BVTK_NT_ImageToStructuredPoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageToStructuredPoints'
    bl_label = 'vtkImageToStructuredPoints'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageToStructuredPoints)
TYPENAMES.append('BVTK_NT_ImageToStructuredPoints' )


# --------------------------------------------------------------


class BVTK_NT_Glyph3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Glyph3D'
    bl_label = 'vtkGlyph3D'
    e_ColorMode_items = [(x, x, x) for x in ['ColorByScalar', 'ColorByScale', 'ColorByVector']]
    e_IndexMode_items = [(x, x, x) for x in ['Off', 'Scalar', 'Vector']]
    e_ScaleMode_items = [(x, x, x) for x in ['DataScalingOff', 'ScaleByScalar', 'ScaleByVector', 'ScaleByVectorComponents']]
    e_VectorMode_items = [(x, x, x) for x in ['UseNormal', 'UseVector', 'VectorRotationOff']]
    
    m_Clamping = bpy.props.BoolProperty(name='Clamping', description='Turn on/off clamping of "scalar" values to range. (Scalar value may be vector magnitude if ScaleByVector() is enabled.', default=True)
    e_ColorMode = bpy.props.EnumProperty(name='ColorMode', description='Either color by scale, scalar or by vector/normal magnitude', default='ColorByScale', items=e_ColorMode_items)
    m_FillCellData = bpy.props.BoolProperty(name='FillCellData', description='Enable/disable the generation of cell data as part of the output. The cell data at each cell will match the point data of the input at the glyphed point', default=True)
    m_GeneratePointIds = bpy.props.BoolProperty(name='GeneratePointIds', description='Enable/disable the generation of point ids as part of the output. The point ids are the id of the input generating point. The point ids are stored in the output point field data and named "InputPointIds". Point generation is useful for debugging and pick operations', default=True)
    e_IndexMode = bpy.props.EnumProperty(name='IndexMode', description='Index into table of sources by scalar, by vector/normal magnitude, or no indexing. If indexing is turned off, then the first source glyph in the table of glyphs is used. Note that indexing mode will only use the InputScalarsSelection array and not the InputColorScalarsSelection as the scalar source if an array is specified', default='Off', items=e_IndexMode_items)
    m_Orient = bpy.props.BoolProperty(name='Orient', description='Turn on/off orienting of input geometry along vector/normal', default=True)
    m_PointIdsName = bpy.props.StringProperty(name='PointIdsName', description='Set/Get the name of the PointIds array if generated. By default the Ids are named "InputPointIds", but this can be changed with this function', default='InputPointIds')
    m_Range = bpy.props.FloatVectorProperty(name='Range', description='Specify range to map scalar values into', default=[0.0, 1.0], size=2)
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Specify scale factor to scale object by', default=1.0)
    e_ScaleMode = bpy.props.EnumProperty(name='ScaleMode', description='Either scale by scalar or by vector/normal magnitude', default='ScaleByScalar', items=e_ScaleMode_items)
    m_Scaling = bpy.props.BoolProperty(name='Scaling', description='Turn on/off scaling of source geometry', default=True)
    e_VectorMode = bpy.props.EnumProperty(name='VectorMode', description='Specify whether to use vector or normal to perform vector operations', default='UseVector', items=e_VectorMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Clamping', 'e_ColorMode', 'm_FillCellData', 'm_GeneratePointIds', 'e_IndexMode', 'm_Orient', 'm_PointIdsName', 'm_Range', 'm_ScaleFactor', 'e_ScaleMode', 'm_Scaling', 'e_VectorMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['SourceTransform'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Glyph3D)
TYPENAMES.append('BVTK_NT_Glyph3D' )


# --------------------------------------------------------------


class BVTK_NT_ImageDifference(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageDifference'
    bl_label = 'vtkImageDifference'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_AllowShift = bpy.props.BoolProperty(name='AllowShift', description='Specify whether the comparison will allow a shift of one pixel between the images. If set, then the minimum difference between input images will be used to determine the difference. Otherwise, the difference is computed directly between pixels of identical row/column values', default=True)
    m_Averaging = bpy.props.BoolProperty(name='Averaging', description='Specify whether the comparison will include comparison of averaged 3x3 data between the images. For graphics renderings you normally would leave this on. For imaging operations it should be off', default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_Threshold = bpy.props.IntProperty(name='Threshold', description='Specify a threshold tolerance for pixel differences', default=16)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AllowShift', 'm_Averaging', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', 'm_Threshold', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageDifference)
TYPENAMES.append('BVTK_NT_ImageDifference' )


# --------------------------------------------------------------


class BVTK_NT_ImageChangeInformation(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageChangeInformation'
    bl_label = 'vtkImageChangeInformation'
    
    m_CenterImage = bpy.props.BoolProperty(name='CenterImage', description='Set the Origin of the output so that image coordinate (0,0,0) lies at the Center of the data set. This will override SetOutputOrigin. This is often a useful operation to apply before using vtkImageReslice to apply a transformation to an image', default=True)
    m_ExtentTranslation = bpy.props.IntVectorProperty(name='ExtentTranslation', description='', default=[0, 0, 0], size=3)
    m_OriginScale = bpy.props.FloatVectorProperty(name='OriginScale', description='', default=[1.0, 1.0, 1.0], size=3)
    m_OriginTranslation = bpy.props.FloatVectorProperty(name='OriginTranslation', description='', default=[0.0, 0.0, 0.0], size=3)
    m_OutputExtentStart = bpy.props.IntVectorProperty(name='OutputExtentStart', description='', default=[1000000000, 1000000000, 1000000000], size=3)
    m_OutputOrigin = bpy.props.FloatVectorProperty(name='OutputOrigin', description='', default=[1e+30, 1e+30, 1e+30], size=3)
    m_OutputSpacing = bpy.props.FloatVectorProperty(name='OutputSpacing', description='', default=[1e+30, 1e+30, 1e+30], size=3)
    m_SpacingScale = bpy.props.FloatVectorProperty(name='SpacingScale', description='', default=[1.0, 1.0, 1.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CenterImage', 'm_ExtentTranslation', 'm_OriginScale', 'm_OriginTranslation', 'm_OutputExtentStart', 'm_OutputOrigin', 'm_OutputSpacing', 'm_SpacingScale', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageChangeInformation)
TYPENAMES.append('BVTK_NT_ImageChangeInformation' )


# --------------------------------------------------------------


class BVTK_NT_ParticlePathFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ParticlePathFilter'
    bl_label = 'vtkParticlePathFilter'
    
    m_ComputeVorticity = bpy.props.BoolProperty(name='ComputeVorticity', description='Turn on/off vorticity computation at streamline points (necessary for generating proper stream-ribbons using the vtkRibbonFilter', default=True)
    m_DisableResetCache = bpy.props.BoolProperty(name='DisableResetCache', description='Set/Get the flag to disable cache This is off by default and turned on in special circumstances such as in a coprocessing workflo', default=True)
    m_EnableParticleWriting = bpy.props.BoolProperty(name='EnableParticleWriting', description='Set/Get the filename to be used with the particle writer when dumping particles to dis', default=True)
    m_ForceReinjectionEveryNSteps = bpy.props.IntProperty(name='ForceReinjectionEveryNSteps', description='When animating particles, it is nice to inject new ones every Nth step to produce a continuous flow. Setting ForceReinjectionEveryNSteps to a non zero value will cause the particle source to reinject particles every Nth step even if it is otherwise unchanged. Note that if the particle source is also animated, this flag will be redundant as the particles will be reinjected whenever the source changes anywa', default=0)
    m_IgnorePipelineTime = bpy.props.BoolProperty(name='IgnorePipelineTime', description='To get around problems with the Paraview Animation controls we can just animate the time step and ignore the TIME_ request', default=True)
    m_IntegratorType = bpy.props.IntProperty(name='IntegratorType', description='', default=1)
    m_ParticleFileName = bpy.props.StringProperty(name='ParticleFileName', description='Set/Get the filename to be used with the particle writer when dumping particles to dis', subtype='FILE_PATH')
    m_RotationScale = bpy.props.FloatProperty(name='RotationScale', description='This can be used to scale the rate with which the streamribbons twist. The default is 1', default=1.0)
    m_StartTime = bpy.props.FloatProperty(name='StartTime', description='Set the time value for particle tracing to begin. The units of time should be consistent with the primary time variable', default=0.0)
    m_StaticMesh = bpy.props.IntProperty(name='StaticMesh', description='if StaticMesh is set, many optimizations for cell caching can be assumed. if StaticMesh is not set, the algorithm will attempt to find out if optimizations can be used, but setting it to true will force all optimizations. Do not Set StaticMesh to true if a dynamic mesh is being used as this will invalidate all results. The default is that StaticMesh is 0', default=0)
    m_StaticSeeds = bpy.props.IntProperty(name='StaticSeeds', description='if StaticSeeds is set and the mesh is static, then every time particles are injected we can re-use the same injection information. We classify particles according to processor just once before start. If StaticSeeds is set and a moving seed source is specified the motion will be ignored and results will not be as expected. The default is that StaticSeeds is 0', default=0)
    m_TerminalSpeed = bpy.props.FloatProperty(name='TerminalSpeed', description='Specify the terminal speed value, below which integration is terminated', default=1e-12)
    m_TerminationTime = bpy.props.FloatProperty(name='TerminationTime', description='Setting TerminationTime to a positive value will cause particles to terminate when the time is reached. Use a vlue of zero to diable termination. The units of time should be consistent with the primary time variable', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeVorticity', 'm_DisableResetCache', 'm_EnableParticleWriting', 'm_ForceReinjectionEveryNSteps', 'm_IgnorePipelineTime', 'm_IntegratorType', 'm_ParticleFileName', 'm_RotationScale', 'm_StartTime', 'm_StaticMesh', 'm_StaticSeeds', 'm_TerminalSpeed', 'm_TerminationTime', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['Integrator', 'ParticleWriter'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ParticlePathFilter)
TYPENAMES.append('BVTK_NT_ParticlePathFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractSelection(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractSelection'
    bl_label = 'vtkExtractSelection'
    
    m_PreserveTopology = bpy.props.BoolProperty(name='PreserveTopology', description='This flag tells the extraction filter not to convert the selected output into an unstructured grid, but instead to produce a vtkInsidedness array and add it to the input dataset. Default value is false(0)', default=True)
    m_ShowBounds = bpy.props.BoolProperty(name='ShowBounds', description='When On, this returns an unstructured grid that outlines selection area. Off is the default. Applicable only to Frustum selection extraction', default=True)
    m_UseProbeForLocations = bpy.props.BoolProperty(name='UseProbeForLocations', description='When On, vtkProbeSelectedLocations is used for extracting selections of content type vtkSelection::LOCATIONS. Default is off and then vtkExtractSelectedLocations is used', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PreserveTopology', 'm_ShowBounds', 'm_UseProbeForLocations', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractSelection)
TYPENAMES.append('BVTK_NT_ExtractSelection' )


# --------------------------------------------------------------


class BVTK_NT_Delaunay2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Delaunay2D'
    bl_label = 'vtkDelaunay2D'
    
    m_Alpha = bpy.props.FloatProperty(name='Alpha', description='Specify alpha (or distance) value to control output of this filter. For a non-zero alpha value, only edges or triangles contained within a sphere centered at mesh vertices will be output. Otherwise, only triangles will be output', default=0.0)
    m_BoundingTriangulation = bpy.props.BoolProperty(name='BoundingTriangulation', description='Boolean controls whether bounding triangulation points (and associated triangles) are included in the output. (These are introduced as an initial triangulation to begin the triangulation process. This feature is nice for debugging output.', default=True)
    m_Offset = bpy.props.FloatProperty(name='Offset', description='Specify a multiplier to control the size of the initial, bounding Delaunay triangulation', default=1.0)
    m_ProjectionPlaneMode = bpy.props.IntProperty(name='ProjectionPlaneMode', description='Defin', default=0)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Specify a tolerance to control discarding of closely spaced points. This tolerance is specified as a fraction of the diagonal length of the bounding box of the points', default=1e-05)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Alpha', 'm_BoundingTriangulation', 'm_Offset', 'm_ProjectionPlaneMode', 'm_Tolerance', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['Transform'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Delaunay2D)
TYPENAMES.append('BVTK_NT_Delaunay2D' )


# --------------------------------------------------------------


class BVTK_NT_ExtractSelectedPolyDataIds(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractSelectedPolyDataIds'
    bl_label = 'vtkExtractSelectedPolyDataIds'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractSelectedPolyDataIds)
TYPENAMES.append('BVTK_NT_ExtractSelectedPolyDataIds' )


# --------------------------------------------------------------


class BVTK_NT_ExtractSelectedBlock(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractSelectedBlock'
    bl_label = 'vtkExtractSelectedBlock'
    
    m_PreserveTopology = bpy.props.BoolProperty(name='PreserveTopology', description='This flag tells the extraction filter not to convert the selected output into an unstructured grid, but instead to produce a vtkInsidedness array and add it to the input dataset. Default value is false(0)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PreserveTopology', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractSelectedBlock)
TYPENAMES.append('BVTK_NT_ExtractSelectedBlock' )


# --------------------------------------------------------------


class BVTK_NT_TemporalStreamTracer(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TemporalStreamTracer'
    bl_label = 'vtkTemporalStreamTracer'
    e_IntegrationDirection_items = [(x, x, x) for x in ['Backward', 'Both', 'Forward']]
    e_IntegratorType_items = [(x, x, x) for x in ['RungeKutta2', 'RungeKutta4', 'RungeKutta45']]
    e_TerminationTimeUnit_items = [(x, x, x) for x in ['StepUnit', 'TimeUnit']]
    
    m_ComputeVorticity = bpy.props.BoolProperty(name='ComputeVorticity', description='Turn on/off vorticity computation at streamline points (necessary for generating proper stream-ribbons using the vtkRibbonFilter', default=True)
    m_EnableParticleWriting = bpy.props.BoolProperty(name='EnableParticleWriting', description='Set/Get the filename to be used with the particle writer when dumping particles to dis', default=True)
    m_ForceReinjectionEveryNSteps = bpy.props.IntProperty(name='ForceReinjectionEveryNSteps', description='When animating particles, it is nice to inject new ones every Nth step to produce a continuous flow. Setting ForceReinjectionEveryNSteps to a non zero value will cause the particle source to reinject particles every Nth step even if it is otherwise unchanged. Note that if the particle source is also animated, this flag will be redundant as the particles will be reinjected whenever the source changes anywa', default=1)
    m_IgnorePipelineTime = bpy.props.BoolProperty(name='IgnorePipelineTime', description='To get around problems with the Paraview Animation controls we can just animate the time step and ignore the TIME_ request', default=True)
    m_InitialIntegrationStep = bpy.props.FloatProperty(name='InitialIntegrationStep', description='Specify the Initial step size used for line integration, expressed in: LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 (either the starting size for an adaptive integrator, e.g., RK45, or the constant / fixed size for non-adaptive ones, i.e., RK2 and RK4', default=0.5)
    e_IntegrationDirection = bpy.props.EnumProperty(name='IntegrationDirection', description='Specify whether the streamline is integrated in the upstream or downstream direction', default='Forward', items=e_IntegrationDirection_items)
    m_IntegrationStepUnit = bpy.props.IntProperty(name='IntegrationStepUnit', description='Specify a uniform integration step unit for MinimumIntegrationStep, InitialIntegrationStep, and MaximumIntegrationStep. NOTE: The valid unit is now limited to only LENGTH_UNIT (1) and CELL_LENGTH_UNIT (2), EXCLUDING the previously-supported TIME_UNIT', default=1)
    e_IntegratorType = bpy.props.EnumProperty(name='IntegratorType', description='Set/get the integrator type to be used for streamline generation. The object passed is not actually used but is cloned with NewInstance in the process of integration (prototype pattern). The default is Runge-Kutta2. The integrator can also be changed using SetIntegratorType. The recognized solvers are: RUNGE_KUTTA2 = 0 RUNGE_KUTTA4 = 1 RUNGE_KUTTA45 = ', default='RungeKutta4', items=e_IntegratorType_items)
    m_MaximumError = bpy.props.FloatProperty(name='MaximumError', description='Specify the maximum error tolerated throughout streamline integration', default=1e-06)
    m_MaximumIntegrationStep = bpy.props.FloatProperty(name='MaximumIntegrationStep', description='Specify the Maximum step size used for line integration, expressed in: LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 (Only valid for an adaptive integrator, e.g., RK45', default=1.0)
    m_MaximumNumberOfSteps = bpy.props.IntProperty(name='MaximumNumberOfSteps', description='Specify the maximum number of steps for integrating a streamline', default=2000)
    m_MaximumPropagation = bpy.props.FloatProperty(name='MaximumPropagation', description='Specify the maximum length of a streamline expressed in LENGTH_UNIT', default=1.0)
    m_MinimumIntegrationStep = bpy.props.FloatProperty(name='MinimumIntegrationStep', description='Specify the Minimum step size used for line integration, expressed in: LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 (Only valid for an adaptive integrator, e.g., RK45', default=0.01)
    m_ParticleFileName = bpy.props.StringProperty(name='ParticleFileName', description='Set/Get the filename to be used with the particle writer when dumping particles to dis', subtype='FILE_PATH')
    m_RotationScale = bpy.props.FloatProperty(name='RotationScale', description='This can be used to scale the rate with which the streamribbons twist. The default is 1', default=1.0)
    m_StartPosition = bpy.props.FloatVectorProperty(name='StartPosition', description='', default=[0.0, 0.0, 0.0], size=3)
    m_StaticMesh = bpy.props.BoolProperty(name='StaticMesh', description='if StaticMesh is set, many optimizations for cell caching can be assumed. if StaticMesh is not set, the algorithm will attempt to find out if optimizations can be used, but setting it to true will force all optimizations. Do not Set StaticMesh to true if a dynamic mesh is being used as this will invalidate all results', default=True)
    m_StaticSeeds = bpy.props.BoolProperty(name='StaticSeeds', description='if StaticSeeds is set and the mesh is static, then every time particles are injected we can re-use the same injection information. We classify particles according to processor just once before start. If StaticSeeds is set and a moving seed source is specified the motion will be ignored and results will not be as expected', default=True)
    m_SurfaceStreamlines = bpy.props.BoolProperty(name='SurfaceStreamlines', description='Set/Unset the streamlines to be computed on a surfac', default=False)
    m_TerminalSpeed = bpy.props.FloatProperty(name='TerminalSpeed', description='Specify the terminal speed value, below which integration is terminated', default=1e-12)
    m_TerminationTime = bpy.props.FloatProperty(name='TerminationTime', description='Setting TerminationTime to a positive value will cause particles to terminate when the time is reached. Use a vlue of zero to diable termination. The units of time should be consistent with the primary time variable', default=0.0)
    e_TerminationTimeUnit = bpy.props.EnumProperty(name='TerminationTimeUnit', description="The units of TerminationTime may be actual 'Time' units as described by the data, or just TimeSteps of iteration", default='StepUnit', items=e_TerminationTimeUnit_items)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Set/Get the TimeStep. This is the primary means of advancing the particles. The TimeStep should be animated and this will drive the pipeline forcing timesteps to be fetched from upstream', default=0)
    m_TimeStepResolution = bpy.props.FloatProperty(name='TimeStepResolution', description='If the data source does not have the correct time values present on each time step - setting this value to non unity can be used to adjust the time step size from 1s pre step to 1x_TimeStepResolution : Not functional in this version. Broke it @todo, put back time scalin', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=24, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeVorticity', 'm_EnableParticleWriting', 'm_ForceReinjectionEveryNSteps', 'm_IgnorePipelineTime', 'm_InitialIntegrationStep', 'e_IntegrationDirection', 'm_IntegrationStepUnit', 'e_IntegratorType', 'm_MaximumError', 'm_MaximumIntegrationStep', 'm_MaximumNumberOfSteps', 'm_MaximumPropagation', 'm_MinimumIntegrationStep', 'm_ParticleFileName', 'm_RotationScale', 'm_StartPosition', 'm_StaticMesh', 'm_StaticSeeds', 'm_SurfaceStreamlines', 'm_TerminalSpeed', 'm_TerminationTime', 'e_TerminationTimeUnit', 'm_TimeStep', 'm_TimeStepResolution', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['Integrator', 'ParticleWriter'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TemporalStreamTracer)
TYPENAMES.append('BVTK_NT_TemporalStreamTracer' )


# --------------------------------------------------------------


class BVTK_NT_CookieCutter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CookieCutter'
    bl_label = 'vtkCookieCutter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['LoopsConnection'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CookieCutter)
TYPENAMES.append('BVTK_NT_CookieCutter' )


# --------------------------------------------------------------


class BVTK_NT_SmoothPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SmoothPolyDataFilter'
    bl_label = 'vtkSmoothPolyDataFilter'
    
    m_BoundarySmoothing = bpy.props.BoolProperty(name='BoundarySmoothing', description='Turn on/off the smoothing of vertices on the boundary of the mesh', default=True)
    m_Convergence = bpy.props.FloatProperty(name='Convergence', description='Specify a convergence criterion for the iteration process. Smaller numbers result in more smoothing iterations', default=0.0)
    m_EdgeAngle = bpy.props.FloatProperty(name='EdgeAngle', description='Specify the edge angle to control smoothing along edges (either interior or boundary)', default=15.0)
    m_FeatureAngle = bpy.props.FloatProperty(name='FeatureAngle', description='Specify the feature angle for sharp edge identification', default=45.0)
    m_FeatureEdgeSmoothing = bpy.props.BoolProperty(name='FeatureEdgeSmoothing', description='Turn on/off smoothing along sharp interior edges', default=True)
    m_GenerateErrorScalars = bpy.props.BoolProperty(name='GenerateErrorScalars', description='Turn on/off the generation of scalar distance values', default=True)
    m_GenerateErrorVectors = bpy.props.BoolProperty(name='GenerateErrorVectors', description='Turn on/off the generation of error vectors', default=True)
    m_NumberOfIterations = bpy.props.IntProperty(name='NumberOfIterations', description='Specify the number of iterations for Laplacian smoothing', default=20)
    m_RelaxationFactor = bpy.props.FloatProperty(name='RelaxationFactor', description='Specify the relaxation factor for Laplacian smoothing. As in all iterative methods, the stability of the process is sensitive to this parameter. In general, small relaxation factors and large numbers of iterations are more stable than larger relaxation factors and smaller numbers of iterations', default=0.01)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BoundarySmoothing', 'm_Convergence', 'm_EdgeAngle', 'm_FeatureAngle', 'm_FeatureEdgeSmoothing', 'm_GenerateErrorScalars', 'm_GenerateErrorVectors', 'm_NumberOfIterations', 'm_RelaxationFactor', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SmoothPolyDataFilter)
TYPENAMES.append('BVTK_NT_SmoothPolyDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_BlankStructuredGridWithImage(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BlankStructuredGridWithImage'
    bl_label = 'vtkBlankStructuredGridWithImage'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BlankStructuredGridWithImage)
TYPENAMES.append('BVTK_NT_BlankStructuredGridWithImage' )


# --------------------------------------------------------------


class BVTK_NT_ProjectedTerrainPath(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProjectedTerrainPath'
    bl_label = 'vtkProjectedTerrainPath'
    e_ProjectionMode_items = [(x, x, x) for x in ['Hug', 'NonOccluded', 'Simple']]
    
    m_HeightOffset = bpy.props.FloatProperty(name='HeightOffset', description='This is the height above (or below) the terrain that the projected path should be. Positive values indicate distances above the terrain; negative values indicate distances below the terrain', default=10.0)
    m_HeightTolerance = bpy.props.FloatProperty(name='HeightTolerance', description='This is the allowable variation in the altitude of the path with respect to the variation in the terrain. It only comes into play if the hug projection mode is enabled', default=10.0)
    m_MaximumNumberOfLines = bpy.props.IntProperty(name='MaximumNumberOfLines', description='This instance variable can be used to limit the total number of line segments created during subdivision. Note that the number of input line segments will be the minimum number that cab be output', default=1000000000)
    e_ProjectionMode = bpy.props.EnumProperty(name='ProjectionMode', description='Determine how to control the projection process. Simple projection just projects the original polyline points. Non-occluded projection insures that the polyline does not intersect the terrain surface. Hug projection is similar to non-occulded projection except that produces a path that is nearly parallel to the terrain (within the user specified height tolerance)', default='Simple', items=e_ProjectionMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_HeightOffset', 'm_HeightTolerance', 'm_MaximumNumberOfLines', 'e_ProjectionMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProjectedTerrainPath)
TYPENAMES.append('BVTK_NT_ProjectedTerrainPath' )


# --------------------------------------------------------------


class BVTK_NT_ApplyColors(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ApplyColors'
    bl_label = 'vtkApplyColors'
    
    m_CellColorOutputArrayName = bpy.props.StringProperty(name='CellColorOutputArrayName', description='The output array name for the cell color RGBA array. Default is "vtkApplyColors color"', default='vtkApplyColors color')
    m_DefaultCellColor = bpy.props.FloatVectorProperty(name='DefaultCellColor', description='', default=[0.0, 0.0, 0.0], size=3)
    m_DefaultCellOpacity = bpy.props.FloatProperty(name='DefaultCellOpacity', description='The default cell opacity for all unannotated, unselected elements of the data. This is used if UseCellLookupTable is off', default=1.0)
    m_DefaultPointColor = bpy.props.FloatVectorProperty(name='DefaultPointColor', description='', default=[0.0, 0.0, 0.0], size=3)
    m_DefaultPointOpacity = bpy.props.FloatProperty(name='DefaultPointOpacity', description='The default point opacity for all unannotated, unselected elements of the data. This is used if UsePointLookupTable is off', default=1.0)
    m_PointColorOutputArrayName = bpy.props.StringProperty(name='PointColorOutputArrayName', description='The output array name for the point color RGBA array. Default is "vtkApplyColors color"', default='vtkApplyColors color')
    m_ScaleCellLookupTable = bpy.props.BoolProperty(name='ScaleCellLookupTable', description='If on, uses the range of the data to scale the lookup table range. Otherwise, uses the range defined in the lookup table', default=True)
    m_ScalePointLookupTable = bpy.props.BoolProperty(name='ScalePointLookupTable', description='If on, uses the range of the data to scale the lookup table range. Otherwise, uses the range defined in the lookup table', default=True)
    m_SelectedCellColor = bpy.props.FloatVectorProperty(name='SelectedCellColor', description='', default=[0.0, 0.0, 0.0], size=3)
    m_SelectedCellOpacity = bpy.props.FloatProperty(name='SelectedCellOpacity', description='The cell opacity for all selected elements of the data. This is used if the selection input is available', default=1.0)
    m_SelectedPointColor = bpy.props.FloatVectorProperty(name='SelectedPointColor', description='', default=[0.0, 0.0, 0.0], size=3)
    m_SelectedPointOpacity = bpy.props.FloatProperty(name='SelectedPointOpacity', description='The point opacity for all selected elements of the data. This is used if the selection input is available', default=1.0)
    m_UseCellLookupTable = bpy.props.BoolProperty(name='UseCellLookupTable', description='If on, uses the cell lookup table to set the colors of unannotated, unselected elements of the data', default=False)
    m_UseCurrentAnnotationColor = bpy.props.BoolProperty(name='UseCurrentAnnotationColor', description='Use the annotation to color the current annotation (i.e. the current selection). Otherwise use the selection color attributes of this filter', default=False)
    m_UsePointLookupTable = bpy.props.BoolProperty(name='UsePointLookupTable', description='If on, uses the point lookup table to set the colors of unannotated, unselected elements of the data', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CellColorOutputArrayName', 'm_DefaultCellColor', 'm_DefaultCellOpacity', 'm_DefaultPointColor', 'm_DefaultPointOpacity', 'm_PointColorOutputArrayName', 'm_ScaleCellLookupTable', 'm_ScalePointLookupTable', 'm_SelectedCellColor', 'm_SelectedCellOpacity', 'm_SelectedPointColor', 'm_SelectedPointOpacity', 'm_UseCellLookupTable', 'm_UseCurrentAnnotationColor', 'm_UsePointLookupTable', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['CellLookupTable', 'PointLookupTable'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ApplyColors)
TYPENAMES.append('BVTK_NT_ApplyColors' )


# --------------------------------------------------------------


class BVTK_NT_SynchronizeTimeFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SynchronizeTimeFilter'
    bl_label = 'vtkSynchronizeTimeFilter'
    
    m_RelativeTolerance = bpy.props.FloatProperty(name='RelativeTolerance', description='Set/get the relative tolerance for comparing time step values to see if they are close enough to be considered identical', default=1e-05)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_RelativeTolerance', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SynchronizeTimeFilter)
TYPENAMES.append('BVTK_NT_SynchronizeTimeFilter' )


# --------------------------------------------------------------


class BVTK_NT_ProbePolyhedron(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProbePolyhedron'
    bl_label = 'vtkProbePolyhedron'
    
    m_ProbeCellData = bpy.props.BoolProperty(name='ProbeCellData', description='Specify whether to probe (and hence produce) cell data. The interpolated point data of the source will produce the output cell data (output cells are passed from the input cells). Note that the probing of the input uses the centers of the cells as the probe position', default=True)
    m_ProbePointData = bpy.props.BoolProperty(name='ProbePointData', description='Specify whether to probe (and hence produce) point data. The interpolated point data of the source will produce the output point data (output points are passed from the input points)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ProbeCellData', 'm_ProbePointData', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProbePolyhedron)
TYPENAMES.append('BVTK_NT_ProbePolyhedron' )


# --------------------------------------------------------------


class BVTK_NT_PExtractArraysOverTime(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PExtractArraysOverTime'
    bl_label = 'vtkPExtractArraysOverTime'
    
    m_ReportStatisticsOnly = bpy.props.BoolProperty(name='ReportStatisticsOnly', description='Instead of breaking a selection into a separate time-history table for each (block,ID)-tuple, you may call ReportStatisticsOnlyOn(). Then a single table per block of the input dataset will report the minimum, maximum, quartiles, and (for numerical arrays) the average and standard deviation of the selection over time', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ReportStatisticsOnly', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['SelectionExtractor'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PExtractArraysOverTime)
TYPENAMES.append('BVTK_NT_PExtractArraysOverTime' )


# --------------------------------------------------------------


class BVTK_NT_FiberSurface(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FiberSurface'
    bl_label = 'vtkFiberSurface'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FiberSurface)
TYPENAMES.append('BVTK_NT_FiberSurface' )


# --------------------------------------------------------------


class BVTK_NT_StreamTracer(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StreamTracer'
    bl_label = 'vtkStreamTracer'
    e_IntegrationDirection_items = [(x, x, x) for x in ['Backward', 'Both', 'Forward']]
    e_IntegratorType_items = [(x, x, x) for x in ['RungeKutta2', 'RungeKutta4', 'RungeKutta45']]
    
    m_ComputeVorticity = bpy.props.BoolProperty(name='ComputeVorticity', description='Turn on/off vorticity computation at streamline points (necessary for generating proper stream-ribbons using the vtkRibbonFilter', default=True)
    m_InitialIntegrationStep = bpy.props.FloatProperty(name='InitialIntegrationStep', description='Specify the Initial step size used for line integration, expressed in: LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 (either the starting size for an adaptive integrator, e.g., RK45, or the constant / fixed size for non-adaptive ones, i.e., RK2 and RK4', default=0.5)
    e_IntegrationDirection = bpy.props.EnumProperty(name='IntegrationDirection', description='Specify whether the streamline is integrated in the upstream or downstream direction', default='Forward', items=e_IntegrationDirection_items)
    m_IntegrationStepUnit = bpy.props.IntProperty(name='IntegrationStepUnit', description='Specify a uniform integration step unit for MinimumIntegrationStep, InitialIntegrationStep, and MaximumIntegrationStep. NOTE: The valid unit is now limited to only LENGTH_UNIT (1) and CELL_LENGTH_UNIT (2), EXCLUDING the previously-supported TIME_UNIT', default=2)
    e_IntegratorType = bpy.props.EnumProperty(name='IntegratorType', description='Set/get the integrator type to be used for streamline generation. The object passed is not actually used but is cloned with NewInstance in the process of integration (prototype pattern). The default is Runge-Kutta2. The integrator can also be changed using SetIntegratorType. The recognized solvers are: RUNGE_KUTTA2 = 0 RUNGE_KUTTA4 = 1 RUNGE_KUTTA45 = ', default='RungeKutta2', items=e_IntegratorType_items)
    m_MaximumError = bpy.props.FloatProperty(name='MaximumError', description='Specify the maximum error tolerated throughout streamline integration', default=1e-06)
    m_MaximumIntegrationStep = bpy.props.FloatProperty(name='MaximumIntegrationStep', description='Specify the Maximum step size used for line integration, expressed in: LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 (Only valid for an adaptive integrator, e.g., RK45', default=1.0)
    m_MaximumNumberOfSteps = bpy.props.IntProperty(name='MaximumNumberOfSteps', description='Specify the maximum number of steps for integrating a streamline', default=2000)
    m_MaximumPropagation = bpy.props.FloatProperty(name='MaximumPropagation', description='Specify the maximum length of a streamline expressed in LENGTH_UNIT', default=1.0)
    m_MinimumIntegrationStep = bpy.props.FloatProperty(name='MinimumIntegrationStep', description='Specify the Minimum step size used for line integration, expressed in: LENGTH_UNIT = 1 CELL_LENGTH_UNIT = 2 (Only valid for an adaptive integrator, e.g., RK45', default=0.01)
    m_RotationScale = bpy.props.FloatProperty(name='RotationScale', description='This can be used to scale the rate with which the streamribbons twist. The default is 1', default=1.0)
    m_StartPosition = bpy.props.FloatVectorProperty(name='StartPosition', description='', default=[0.0, 0.0, 0.0], size=3)
    m_SurfaceStreamlines = bpy.props.BoolProperty(name='SurfaceStreamlines', description='Set/Unset the streamlines to be computed on a surfac', default=False)
    m_TerminalSpeed = bpy.props.FloatProperty(name='TerminalSpeed', description='Specify the terminal speed value, below which integration is terminated', default=1e-12)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeVorticity', 'm_InitialIntegrationStep', 'e_IntegrationDirection', 'm_IntegrationStepUnit', 'e_IntegratorType', 'm_MaximumError', 'm_MaximumIntegrationStep', 'm_MaximumNumberOfSteps', 'm_MaximumPropagation', 'm_MinimumIntegrationStep', 'm_RotationScale', 'm_StartPosition', 'm_SurfaceStreamlines', 'm_TerminalSpeed', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['Integrator'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StreamTracer)
TYPENAMES.append('BVTK_NT_StreamTracer' )


# --------------------------------------------------------------


class BVTK_NT_VolumeContourSpectrumFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VolumeContourSpectrumFilter'
    bl_label = 'vtkVolumeContourSpectrumFilter'
    
    m_ArcId = bpy.props.IntProperty(name='ArcId', description='Set the arc Id for which the contour signature has to be computed. Default value: ', default=0)
    m_FieldId = bpy.props.IntProperty(name='FieldId', description='Set the scalar field Id Default value: ', default=0)
    m_NumberOfSamples = bpy.props.IntProperty(name='NumberOfSamples', description='Set the number of samples in the output signature Default value: 10', default=100)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArcId', 'm_FieldId', 'm_NumberOfSamples', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VolumeContourSpectrumFilter)
TYPENAMES.append('BVTK_NT_VolumeContourSpectrumFilter' )


# --------------------------------------------------------------


class BVTK_NT_CellDistanceSelector(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CellDistanceSelector'
    bl_label = 'vtkCellDistanceSelector'
    
    m_AddIntermediate = bpy.props.BoolProperty(name='AddIntermediate', description='If set, intermediate cells (between seed cells and the selection boundary) will be included in the final selectio', default=True)
    m_Distance = bpy.props.IntProperty(name='Distance', description='Tells how far (in term of topological distance) away from seed cells to expand the selectio', default=1)
    m_IncludeSeed = bpy.props.BoolProperty(name='IncludeSeed', description='If set, seed cells passed with SetSeedCells will be included in the final selectio', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AddIntermediate', 'm_Distance', 'm_IncludeSeed', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CellDistanceSelector)
TYPENAMES.append('BVTK_NT_CellDistanceSelector' )


# --------------------------------------------------------------


class BVTK_NT_ImageMask(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMask'
    bl_label = 'vtkImageMask'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MaskAlpha = bpy.props.FloatProperty(name='MaskAlpha', description='Set/Get the alpha blending value for the mask The input image is assumed to be at alpha = 1.0 and the mask image uses this alpha to blend using an over operator', default=1.0)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NotMask = bpy.props.BoolProperty(name='NotMask', description='When Not Mask is on, the mask is passed through a boolean not before it is used to mask the image. The effect is to pass the pixels where the input mask is zero, and replace the pixels where the input value is non zero', default=True)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MaskAlpha', 'm_MinimumPieceSize', 'm_NotMask', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMask)
TYPENAMES.append('BVTK_NT_ImageMask' )


# --------------------------------------------------------------


class BVTK_NT_ImageHistogramStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageHistogramStatistics'
    bl_label = 'vtkImageHistogramStatistics'
    e_HistogramImageScale_items = [(x, x, x) for x in ['Linear', 'Log', 'Sqrt']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_ActiveComponent = bpy.props.IntProperty(name='ActiveComponent', description='Set the component for which to generate a histogram. The default value is -1, which produces a histogram that is the sum of the histograms of the individual components', default=-1)
    m_AutoRangeExpansionFactors = bpy.props.FloatVectorProperty(name='AutoRangeExpansionFactors', description='', default=[0.1, 0.1], size=2)
    m_AutoRangePercentiles = bpy.props.FloatVectorProperty(name='AutoRangePercentiles', description='', default=[1.0, 99.0], size=2)
    m_AutomaticBinning = bpy.props.BoolProperty(name='AutomaticBinning', description='If this is On, then the histogram binning will be done automatically. For char and unsigned char data, there will be 256 bins with unit spacing. For data of type short and larger, there will be between 256 and MaximumNumberOfBins, depending on the range of the data, and the BinOrigin will be set to zero if no negative values are present, or to the smallest negative value if negative values are present. For float data, the MaximumNumberOfBins will always be used. The BinOrigin and BinSpacing will be set so that they provide a mapping from bin index to scalar value', default=True)
    m_BinOrigin = bpy.props.FloatProperty(name='BinOrigin', description='The value for the center of the first bin (default 0). This is automatically computed unless AutomaticBinning is Off', default=0.0)
    m_BinSpacing = bpy.props.FloatProperty(name='BinSpacing', description='The bin spacing (default 1). This is automatically computed unless AutomaticBinning is Off', default=1.0)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GenerateHistogramImage = bpy.props.BoolProperty(name='GenerateHistogramImage', description='If this is On, then a histogram image will be produced as the output. Regardless of this setting, the histogram is always available as a vtkIdTypeArray from the GetHistogram method', default=True)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    e_HistogramImageScale = bpy.props.EnumProperty(name='HistogramImageScale', description='Set the scale to use for the histogram image. The default is a linear scale, but sqrt and log provide better visualization', default='Linear', items=e_HistogramImageScale_items)
    m_HistogramImageSize = bpy.props.IntVectorProperty(name='HistogramImageSize', description='', default=[256, 256], size=2)
    m_MaximumNumberOfBins = bpy.props.IntProperty(name='MaximumNumberOfBins', description='The maximum number of bins to use when AutomaticBinning is On. When AutomaticBinning is On, the size of the output histogram will be set to the full range of the input data values, unless the full range is greater than this value. By default, the max value is 65536, which is large enough to capture the full range of 16-bit integers', default=65536)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfBins = bpy.props.IntProperty(name='NumberOfBins', description='The number of bins in histogram (default 256). This is automatically computed unless AutomaticBinning is Off', default=256)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ActiveComponent', 'm_AutoRangeExpansionFactors', 'm_AutoRangePercentiles', 'm_AutomaticBinning', 'm_BinOrigin', 'm_BinSpacing', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GenerateHistogramImage', 'm_GlobalDefaultEnableSMP', 'e_HistogramImageScale', 'm_HistogramImageSize', 'm_MaximumNumberOfBins', 'm_MinimumPieceSize', 'm_NumberOfBins', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageHistogramStatistics)
TYPENAMES.append('BVTK_NT_ImageHistogramStatistics' )


# --------------------------------------------------------------


class BVTK_NT_StreaklineFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StreaklineFilter'
    bl_label = 'vtkStreaklineFilter'
    
    m_ComputeVorticity = bpy.props.BoolProperty(name='ComputeVorticity', description='Turn on/off vorticity computation at streamline points (necessary for generating proper stream-ribbons using the vtkRibbonFilter', default=True)
    m_DisableResetCache = bpy.props.BoolProperty(name='DisableResetCache', description='Set/Get the flag to disable cache This is off by default and turned on in special circumstances such as in a coprocessing workflo', default=True)
    m_EnableParticleWriting = bpy.props.BoolProperty(name='EnableParticleWriting', description='Set/Get the filename to be used with the particle writer when dumping particles to dis', default=True)
    m_ForceReinjectionEveryNSteps = bpy.props.IntProperty(name='ForceReinjectionEveryNSteps', description='When animating particles, it is nice to inject new ones every Nth step to produce a continuous flow. Setting ForceReinjectionEveryNSteps to a non zero value will cause the particle source to reinject particles every Nth step even if it is otherwise unchanged. Note that if the particle source is also animated, this flag will be redundant as the particles will be reinjected whenever the source changes anywa', default=1)
    m_IgnorePipelineTime = bpy.props.BoolProperty(name='IgnorePipelineTime', description='To get around problems with the Paraview Animation controls we can just animate the time step and ignore the TIME_ request', default=True)
    m_IntegratorType = bpy.props.IntProperty(name='IntegratorType', description='', default=1)
    m_ParticleFileName = bpy.props.StringProperty(name='ParticleFileName', description='Set/Get the filename to be used with the particle writer when dumping particles to dis', subtype='FILE_PATH')
    m_RotationScale = bpy.props.FloatProperty(name='RotationScale', description='This can be used to scale the rate with which the streamribbons twist. The default is 1', default=1.0)
    m_StartTime = bpy.props.FloatProperty(name='StartTime', description='Set the time value for particle tracing to begin. The units of time should be consistent with the primary time variable', default=0.0)
    m_StaticMesh = bpy.props.IntProperty(name='StaticMesh', description='if StaticMesh is set, many optimizations for cell caching can be assumed. if StaticMesh is not set, the algorithm will attempt to find out if optimizations can be used, but setting it to true will force all optimizations. Do not Set StaticMesh to true if a dynamic mesh is being used as this will invalidate all results. The default is that StaticMesh is 0', default=0)
    m_StaticSeeds = bpy.props.IntProperty(name='StaticSeeds', description='if StaticSeeds is set and the mesh is static, then every time particles are injected we can re-use the same injection information. We classify particles according to processor just once before start. If StaticSeeds is set and a moving seed source is specified the motion will be ignored and results will not be as expected. The default is that StaticSeeds is 0', default=0)
    m_TerminalSpeed = bpy.props.FloatProperty(name='TerminalSpeed', description='Specify the terminal speed value, below which integration is terminated', default=1e-12)
    m_TerminationTime = bpy.props.FloatProperty(name='TerminationTime', description='Setting TerminationTime to a positive value will cause particles to terminate when the time is reached. Use a vlue of zero to diable termination. The units of time should be consistent with the primary time variable', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeVorticity', 'm_DisableResetCache', 'm_EnableParticleWriting', 'm_ForceReinjectionEveryNSteps', 'm_IgnorePipelineTime', 'm_IntegratorType', 'm_ParticleFileName', 'm_RotationScale', 'm_StartTime', 'm_StaticMesh', 'm_StaticSeeds', 'm_TerminalSpeed', 'm_TerminationTime', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['Integrator', 'ParticleWriter'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StreaklineFilter)
TYPENAMES.append('BVTK_NT_StreaklineFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageThresholdConnectivity(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageThresholdConnectivity'
    bl_label = 'vtkImageThresholdConnectivity'
    
    m_ActiveComponent = bpy.props.IntProperty(name='ActiveComponent', description='For multi-component images, you can set which component will be used for the threshold checks', default=-1)
    m_InValue = bpy.props.FloatProperty(name='InValue', description='If ReplaceIn is set, the filled region will be replaced by this value', default=0.0)
    m_NeighborhoodFraction = bpy.props.FloatProperty(name='NeighborhoodFraction', description='The fraction of the neighborhood that must be within the thresholds. The default value is 0.5', default=0.5)
    m_NeighborhoodRadius = bpy.props.FloatVectorProperty(name='NeighborhoodRadius', description='', default=[0.0, 0.0, 0.0], size=3)
    m_OutValue = bpy.props.FloatProperty(name='OutValue', description='If ReplaceOut is set, outside the fill will be replaced by this value', default=0.0)
    m_ReplaceIn = bpy.props.BoolProperty(name='ReplaceIn', description='Replace the filled region by the value set by SetInValue()', default=True)
    m_ReplaceOut = bpy.props.BoolProperty(name='ReplaceOut', description='Replace the filled region by the value set by SetInValue()', default=True)
    m_SliceRangeX = bpy.props.IntVectorProperty(name='SliceRangeX', description='', default=[-1000000000, 1000000000], size=2)
    m_SliceRangeY = bpy.props.IntVectorProperty(name='SliceRangeY', description='', default=[-1000000000, 1000000000], size=2)
    m_SliceRangeZ = bpy.props.IntVectorProperty(name='SliceRangeZ', description='', default=[-1000000000, 1000000000], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ActiveComponent', 'm_InValue', 'm_NeighborhoodFraction', 'm_NeighborhoodRadius', 'm_OutValue', 'm_ReplaceIn', 'm_ReplaceOut', 'm_SliceRangeX', 'm_SliceRangeY', 'm_SliceRangeZ', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['SeedPoints'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageThresholdConnectivity)
TYPENAMES.append('BVTK_NT_ImageThresholdConnectivity' )


# --------------------------------------------------------------


class BVTK_NT_BinCellDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BinCellDataFilter'
    bl_label = 'vtkBinCellDataFilter'
    
    m_ArrayComponent = bpy.props.IntProperty(name='ArrayComponent', description='Set/get which component of the scalar array to bin; defaults to 0', default=0)
    m_CellOverlapMethod = bpy.props.IntProperty(name='CellOverlapMethod', description='Set whether cell overlap is determined by source cell centroid or by source cell points. Centroid by default', default=0)
    m_ComputeTolerance = bpy.props.BoolProperty(name='ComputeTolerance', description='Set whether to use the Tolerance field or precompute the tolerance. When on, the tolerance will be computed and the field value is ignored. Off by default', default=False)
    m_NumberOfBins = bpy.props.IntProperty(name='NumberOfBins', description='Methods to set / get bin values', default=2)
    m_NumberOfNonzeroBinsArrayName = bpy.props.StringProperty(name='NumberOfNonzeroBinsArrayName', description='Returns the name of the id array added to the output that holds the number of nonzero bins per cell. Set to "NumberOfNonzeroBins" by default', default='NumberOfNonzeroBins')
    m_SpatialMatch = bpy.props.BoolProperty(name='SpatialMatch', description='This flag is used only when a piece is requested to update. By default the flag is off. Because no spatial correspondence between input pieces and source pieces is known, all of the source has to be requested no matter what piece of the output is requested. When there is a spatial correspondence, the user/application can set this flag. This hint allows the breakup of the probe operation to be much more efficient. When piece m of n is requested for update by the user, then only n of m needs to be requested of the source', default=True)
    m_StoreNumberOfNonzeroBins = bpy.props.BoolProperty(name='StoreNumberOfNonzeroBins', description='Set whether to store the number of nonzero bins for each cell. On by default', default=True)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Set the tolerance used to compute whether a cell centroid in the source is in a cell of the input. This value is only used if ComputeTolerance is off', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayComponent', 'm_CellOverlapMethod', 'm_ComputeTolerance', 'm_NumberOfBins', 'm_NumberOfNonzeroBinsArrayName', 'm_SpatialMatch', 'm_StoreNumberOfNonzeroBins', 'm_Tolerance', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['CellLocator'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BinCellDataFilter)
TYPENAMES.append('BVTK_NT_BinCellDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_ParticleTracer(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ParticleTracer'
    bl_label = 'vtkParticleTracer'
    
    m_ComputeVorticity = bpy.props.BoolProperty(name='ComputeVorticity', description='Turn on/off vorticity computation at streamline points (necessary for generating proper stream-ribbons using the vtkRibbonFilter', default=True)
    m_DisableResetCache = bpy.props.BoolProperty(name='DisableResetCache', description='Set/Get the flag to disable cache This is off by default and turned on in special circumstances such as in a coprocessing workflo', default=True)
    m_EnableParticleWriting = bpy.props.BoolProperty(name='EnableParticleWriting', description='Set/Get the filename to be used with the particle writer when dumping particles to dis', default=True)
    m_ForceReinjectionEveryNSteps = bpy.props.IntProperty(name='ForceReinjectionEveryNSteps', description='When animating particles, it is nice to inject new ones every Nth step to produce a continuous flow. Setting ForceReinjectionEveryNSteps to a non zero value will cause the particle source to reinject particles every Nth step even if it is otherwise unchanged. Note that if the particle source is also animated, this flag will be redundant as the particles will be reinjected whenever the source changes anywa', default=0)
    m_IgnorePipelineTime = bpy.props.BoolProperty(name='IgnorePipelineTime', description='To get around problems with the Paraview Animation controls we can just animate the time step and ignore the TIME_ request', default=True)
    m_IntegratorType = bpy.props.IntProperty(name='IntegratorType', description='', default=1)
    m_ParticleFileName = bpy.props.StringProperty(name='ParticleFileName', description='Set/Get the filename to be used with the particle writer when dumping particles to dis', subtype='FILE_PATH')
    m_RotationScale = bpy.props.FloatProperty(name='RotationScale', description='This can be used to scale the rate with which the streamribbons twist. The default is 1', default=1.0)
    m_StartTime = bpy.props.FloatProperty(name='StartTime', description='Set the time value for particle tracing to begin. The units of time should be consistent with the primary time variable', default=0.0)
    m_StaticMesh = bpy.props.IntProperty(name='StaticMesh', description='if StaticMesh is set, many optimizations for cell caching can be assumed. if StaticMesh is not set, the algorithm will attempt to find out if optimizations can be used, but setting it to true will force all optimizations. Do not Set StaticMesh to true if a dynamic mesh is being used as this will invalidate all results. The default is that StaticMesh is 0', default=0)
    m_StaticSeeds = bpy.props.IntProperty(name='StaticSeeds', description='if StaticSeeds is set and the mesh is static, then every time particles are injected we can re-use the same injection information. We classify particles according to processor just once before start. If StaticSeeds is set and a moving seed source is specified the motion will be ignored and results will not be as expected. The default is that StaticSeeds is 0', default=0)
    m_TerminalSpeed = bpy.props.FloatProperty(name='TerminalSpeed', description='Specify the terminal speed value, below which integration is terminated', default=1e-12)
    m_TerminationTime = bpy.props.FloatProperty(name='TerminationTime', description='Setting TerminationTime to a positive value will cause particles to terminate when the time is reached. Use a vlue of zero to diable termination. The units of time should be consistent with the primary time variable', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeVorticity', 'm_DisableResetCache', 'm_EnableParticleWriting', 'm_ForceReinjectionEveryNSteps', 'm_IgnorePipelineTime', 'm_IntegratorType', 'm_ParticleFileName', 'm_RotationScale', 'm_StartTime', 'm_StaticMesh', 'm_StaticSeeds', 'm_TerminalSpeed', 'm_TerminationTime', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['Integrator', 'ParticleWriter'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ParticleTracer)
TYPENAMES.append('BVTK_NT_ParticleTracer' )


# --------------------------------------------------------------


class BVTK_NT_MergeDataObjectFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MergeDataObjectFilter'
    bl_label = 'vtkMergeDataObjectFilter'
    e_OutputField_items = [(x, x, x) for x in ['CellDataField', 'DataObjectField', 'PointDataField']]
    
    e_OutputField = bpy.props.EnumProperty(name='OutputField', description='Specify where to place the field data during the merge process. There are three choices: the field data associated with the vtkDataObject superclass; the point field attribute data; and the cell field attribute data', default='DataObjectField', items=e_OutputField_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_OutputField', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MergeDataObjectFilter)
TYPENAMES.append('BVTK_NT_MergeDataObjectFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractSelectedLocations(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractSelectedLocations'
    bl_label = 'vtkExtractSelectedLocations'
    
    m_PreserveTopology = bpy.props.BoolProperty(name='PreserveTopology', description='This flag tells the extraction filter not to convert the selected output into an unstructured grid, but instead to produce a vtkInsidedness array and add it to the input dataset. Default value is false(0)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PreserveTopology', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractSelectedLocations)
TYPENAMES.append('BVTK_NT_ExtractSelectedLocations' )


# --------------------------------------------------------------


class BVTK_NT_AreaContourSpectrumFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AreaContourSpectrumFilter'
    bl_label = 'vtkAreaContourSpectrumFilter'
    
    m_ArcId = bpy.props.IntProperty(name='ArcId', description='Set the arc Id for which the contour signature has to be computed. Default value: ', default=0)
    m_FieldId = bpy.props.IntProperty(name='FieldId', description='Set the scalar field Id Default value: ', default=0)
    m_NumberOfSamples = bpy.props.IntProperty(name='NumberOfSamples', description='Set the number of samples in the output signature Default value: 10', default=100)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArcId', 'm_FieldId', 'm_NumberOfSamples', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AreaContourSpectrumFilter)
TYPENAMES.append('BVTK_NT_AreaContourSpectrumFilter' )


# --------------------------------------------------------------


class BVTK_NT_ParallelCoordinatesRepresentation(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ParallelCoordinatesRepresentation'
    bl_label = 'vtkParallelCoordinatesRepresentation'
    
    m_AngleBrushThreshold = bpy.props.FloatProperty(name='AngleBrushThreshold', description='Maximum angle difference (in degrees) of selection using angle/function brushe', default=0.03)
    m_AxisColor = bpy.props.FloatVectorProperty(name='AxisColor', description='', default=[1.0, 0.8, 0.3], size=3)
    m_AxisLabelColor = bpy.props.FloatVectorProperty(name='AxisLabelColor', description='', default=[1.0, 1.0, 1.0], size=3)
    m_CurveResolution = bpy.props.IntProperty(name='CurveResolution', description='Resolution of the curves displayed, enabled by setting UseCurve', default=20)
    m_FontSize = bpy.props.FloatProperty(name='FontSize', description='Access plot propertie', default=1.0)
    m_FunctionBrushThreshold = bpy.props.FloatProperty(name='FunctionBrushThreshold', description='Maximum angle difference (in degrees) of selection using angle/function brushe', default=0.1)
    m_LabelRenderMode = bpy.props.IntProperty(name='LabelRenderMode', description='Set the label render mode. vtkRenderView::QT - Use Qt-based labeler with fitted labeling and unicode support. Requires VTK_USE_QT to be on. vtkRenderView::FREETYPE - Use standard freetype text rendering', default=0)
    m_LineColor = bpy.props.FloatVectorProperty(name='LineColor', description='', default=[1.0, 1.0, 1.0], size=3)
    m_LineOpacity = bpy.props.FloatProperty(name='LineOpacity', description='Access plot propertie', default=1.0)
    m_NumberOfAxisLabels = bpy.props.IntProperty(name='NumberOfAxisLabels', description='Set/Get the number of labels to display on each axi', default=2)
    m_Selectable = bpy.props.BoolProperty(name='Selectable', description='Whether this representation is able to handle a selection. Default is true', default=True)
    m_SelectionArrayName = bpy.props.StringProperty(name='SelectionArrayName', description='If a VALUES selection, the array used to produce a selection')
    m_SelectionType = bpy.props.IntProperty(name='SelectionType', description='Set the selection type produced by this view. This should be one of the content type constants defined in vtkSelectionNode.h. Common values are vtkSelectionNode::INDICES vtkSelectionNode::PEDIGREEIDS vtkSelectionNode::VALUE', default=4)
    m_UseCurves = bpy.props.BoolProperty(name='UseCurves', description='Whether or not to display using curve', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AngleBrushThreshold', 'm_AxisColor', 'm_AxisLabelColor', 'm_CurveResolution', 'm_FontSize', 'm_FunctionBrushThreshold', 'm_LabelRenderMode', 'm_LineColor', 'm_LineOpacity', 'm_NumberOfAxisLabels', 'm_Selectable', 'm_SelectionArrayName', 'm_SelectionType', 'm_UseCurves', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['AnnotationLink', 'SelectionArrayNames'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ParallelCoordinatesRepresentation)
TYPENAMES.append('BVTK_NT_ParallelCoordinatesRepresentation' )


# --------------------------------------------------------------


class BVTK_NT_DeformPointSet(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DeformPointSet'
    bl_label = 'vtkDeformPointSet'
    
    m_InitializeWeights = bpy.props.BoolProperty(name='InitializeWeights', description='Specify whether to regenerate interpolation weights or not. Initially the filter will reexecute no matter what this flag is set to (initial weights must be computed). Also, this flag is ignored if the number of input points/cells or the number of control mesh points/cells changes between executions. Thus flag is used to force reexecution and recomputation of weights', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_InitializeWeights', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['ControlMeshData'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DeformPointSet)
TYPENAMES.append('BVTK_NT_DeformPointSet' )


# --------------------------------------------------------------


class BVTK_NT_ImageLogic(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageLogic'
    bl_label = 'vtkImageLogic'
    e_Operation_items = [(x, x, x) for x in ['And', 'Nand', 'Nor', 'Not', 'Or', 'Xor']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_Operation = bpy.props.EnumProperty(name='Operation', description='Set/Get the Operation to perform', default='And', items=e_Operation_items)
    m_OutputTrueValue = bpy.props.FloatProperty(name='OutputTrueValue', description='Set the value to use for true in the output', default=255.0)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_Operation', 'm_OutputTrueValue', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageLogic)
TYPENAMES.append('BVTK_NT_ImageLogic' )


# --------------------------------------------------------------


class BVTK_NT_ImageNonMaximumSuppression(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageNonMaximumSuppression'
    bl_label = 'vtkImageNonMaximumSuppression'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Determines how the input is interpreted (set of 2d slices or a 3D volume', default=2)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_HandleBoundaries = bpy.props.BoolProperty(name='HandleBoundaries', description='If "HandleBoundariesOn" then boundary pixels are duplicated So central differences can get values', default=True)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_HandleBoundaries', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageNonMaximumSuppression)
TYPENAMES.append('BVTK_NT_ImageNonMaximumSuppression' )


# --------------------------------------------------------------


class BVTK_NT_TensorGlyph(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TensorGlyph'
    bl_label = 'vtkTensorGlyph'
    e_ColorMode_items = [(x, x, x) for x in ['Eigenvalues', 'Scalars']]
    
    m_ClampScaling = bpy.props.BoolProperty(name='ClampScaling', description='Turn on/off scalar clamping. If scalar clamping is on, the ivar MaxScaleFactor is used to control the maximum scale factor. (This is useful to prevent uncontrolled scaling near singularities.', default=True)
    m_ColorGlyphs = bpy.props.BoolProperty(name='ColorGlyphs', description='Turn on/off coloring of glyph with input scalar data or eigenvalues. If false, or input scalar data not present, then the scalars from the source object are passed through the filter', default=True)
    e_ColorMode = bpy.props.EnumProperty(name='ColorMode', description='Set the color mode to be used for the glyphs. This can be set to use the input scalars (default) or to use the eigenvalues at the point. If ThreeGlyphs is set and the eigenvalues are chosen for coloring then each glyph is colored by the corresponding eigenvalue and if not set the color corresponding to the largest eigenvalue is chosen. The recognized values are: COLOR_BY_SCALARS = 0 (default) COLOR_BY_EIGENVALUES = ', default='Scalars', items=e_ColorMode_items)
    m_ExtractEigenvalues = bpy.props.BoolProperty(name='ExtractEigenvalues', description='Turn on/off extraction of eigenvalues from tensor', default=True)
    m_Length = bpy.props.FloatProperty(name='Length', description='Set/Get the distance, along x, from the origin to the end of the source glyph. It is used to draw the symmetric glyphs', default=1.0)
    m_MaxScaleFactor = bpy.props.FloatProperty(name='MaxScaleFactor', description='Set/Get the maximum allowable scale factor. This value is compared to the combination of the scale factor times the eigenvalue. If less, the scale factor is reset to the MaxScaleFactor. The boolean ClampScaling has to be "on" for this to work', default=100.0)
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Specify scale factor to scale object by. (Scale factor always affects output even if scaling is off.', default=1.0)
    m_Scaling = bpy.props.BoolProperty(name='Scaling', description='Turn on/off scaling of glyph with eigenvalues', default=True)
    m_Symmetric = bpy.props.BoolProperty(name='Symmetric', description='Turn on/off drawing a mirror of each glyp', default=True)
    m_ThreeGlyphs = bpy.props.BoolProperty(name='ThreeGlyphs', description='Turn on/off drawing three glyph', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClampScaling', 'm_ColorGlyphs', 'e_ColorMode', 'm_ExtractEigenvalues', 'm_Length', 'm_MaxScaleFactor', 'm_ScaleFactor', 'm_Scaling', 'm_Symmetric', 'm_ThreeGlyphs', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TensorGlyph)
TYPENAMES.append('BVTK_NT_TensorGlyph' )


# --------------------------------------------------------------


class BVTK_NT_ResampleWithDataSet(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ResampleWithDataSet'
    bl_label = 'vtkResampleWithDataSet'
    
    m_CategoricalData = bpy.props.BoolProperty(name='CategoricalData', description='Control whether the source point data is to be treated as categorical. If the data is categorical, then the resultant data will be determined by a nearest neighbor interpolation scheme', default=False)
    m_ComputeTolerance = bpy.props.BoolProperty(name='ComputeTolerance', description='Set whether to use the Tolerance field or precompute the tolerance. When on, the tolerance will be computed and the field value is ignored. Off by default', default=True)
    m_MarkBlankPointsAndCells = bpy.props.BoolProperty(name='MarkBlankPointsAndCells', description='Set whether points without resampled values, and their corresponding cells, should be marked as Blank. Default is On', default=True)
    m_PassCellArrays = bpy.props.BoolProperty(name='PassCellArrays', description='Shallow copy the input cell data arrays to the output. Off by default', default=False)
    m_PassFieldArrays = bpy.props.BoolProperty(name='PassFieldArrays', description='Set whether to pass the field-data arrays from the Input i.e. the input providing the geometry to the output. On by default', default=True)
    m_PassPointArrays = bpy.props.BoolProperty(name='PassPointArrays', description='Shallow copy the input point data arrays to the output Off by default', default=False)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Set the tolerance used to compute whether a point in the source is in a cell of the input. This value is only used if ComputeTolerance is off', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CategoricalData', 'm_ComputeTolerance', 'm_MarkBlankPointsAndCells', 'm_PassCellArrays', 'm_PassFieldArrays', 'm_PassPointArrays', 'm_Tolerance', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ResampleWithDataSet)
TYPENAMES.append('BVTK_NT_ResampleWithDataSet' )


# --------------------------------------------------------------


class BVTK_NT_PProbeFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PProbeFilter'
    bl_label = 'vtkPProbeFilter'
    
    m_CategoricalData = bpy.props.BoolProperty(name='CategoricalData', description='Control whether the source point data is to be treated as categorical. If the data is categorical, then the resultant data will be determined by a nearest neighbor interpolation scheme', default=True)
    m_ComputeTolerance = bpy.props.BoolProperty(name='ComputeTolerance', description='Set whether to use the Tolerance field or precompute the tolerance. When on, the tolerance will be computed and the field value is ignored. Off by default', default=True)
    m_PassCellArrays = bpy.props.BoolProperty(name='PassCellArrays', description='Shallow copy the input cell data arrays to the output. Off by default', default=True)
    m_PassFieldArrays = bpy.props.BoolProperty(name='PassFieldArrays', description='Set whether to pass the field-data arrays from the Input i.e. the input providing the geometry to the output. On by default', default=True)
    m_PassPartialArrays = bpy.props.BoolProperty(name='PassPartialArrays', description='When dealing with composite datasets, partial arrays are common i.e. data-arrays that are not available in all of the blocks. By default, this filter only passes those point and cell data-arrays that are available in all the blocks i.e. partial array are removed. When PassPartialArrays is turned on, this behavior is changed to take a union of all arrays present thus partial arrays are passed as well. However, for composite dataset input, this filter still produces a non-composite output. For all those locations in a block of where a particular data array is missing, this filter uses vtkMath::Nan() for double and float arrays, while 0 for all other types of arrays i.e int, char etc', default=False)
    m_PassPointArrays = bpy.props.BoolProperty(name='PassPointArrays', description='Shallow copy the input point data arrays to the output Off by default', default=True)
    m_SpatialMatch = bpy.props.BoolProperty(name='SpatialMatch', description='This flag is used only when a piece is requested to update. By default the flag is off. Because no spatial correspondence between input pieces and source pieces is known, all of the source has to be requested no matter what piece of the output is requested. When there is a spatial correspondence, the user/application can set this flag. This hint allows the breakup of the probe operation to be much more efficient. When piece m of n is requested for update by the user, then only n of m needs to be requested of the source', default=True)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Set the tolerance used to compute whether a point in the source is in a cell of the input. This value is only used if ComputeTolerance is off', default=1.0)
    m_ValidPointMaskArrayName = bpy.props.StringProperty(name='ValidPointMaskArrayName', description='Returns the name of the char array added to the output with values 1 for valid points and 0 for invalid points. Set to "vtkValidPointMask" by default', default='vtkValidPointMask')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CategoricalData', 'm_ComputeTolerance', 'm_PassCellArrays', 'm_PassFieldArrays', 'm_PassPartialArrays', 'm_PassPointArrays', 'm_SpatialMatch', 'm_Tolerance', 'm_ValidPointMaskArrayName', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PProbeFilter)
TYPENAMES.append('BVTK_NT_PProbeFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractSelectedThresholds(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractSelectedThresholds'
    bl_label = 'vtkExtractSelectedThresholds'
    
    m_PreserveTopology = bpy.props.BoolProperty(name='PreserveTopology', description='This flag tells the extraction filter not to convert the selected output into an unstructured grid, but instead to produce a vtkInsidedness array and add it to the input dataset. Default value is false(0)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PreserveTopology', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractSelectedThresholds)
TYPENAMES.append('BVTK_NT_ExtractSelectedThresholds' )


# --------------------------------------------------------------


class BVTK_NT_SelectEnclosedPoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SelectEnclosedPoints'
    bl_label = 'vtkSelectEnclosedPoints'
    
    m_CheckSurface = bpy.props.BoolProperty(name='CheckSurface', description='Specify whether to check the surface for closure. If on, then the algorithm first checks to see if the surface is closed and manifold', default=True)
    m_InsideOut = bpy.props.BoolProperty(name='InsideOut', description='By default, points inside the surface are marked inside or sent to the output. If InsideOut is on, then the points outside the surface are marked inside', default=True)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Specify the tolerance on the intersection. The tolerance is expressed as a fraction of the bounding box of the enclosing surface', default=0.001)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CheckSurface', 'm_InsideOut', 'm_Tolerance', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SelectEnclosedPoints)
TYPENAMES.append('BVTK_NT_SelectEnclosedPoints' )


# --------------------------------------------------------------


class BVTK_NT_SubPixelPositionEdgels(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SubPixelPositionEdgels'
    bl_label = 'vtkSubPixelPositionEdgels'
    
    m_TargetFlag = bpy.props.BoolProperty(name='TargetFlag', description='These methods can make the positioning look for a target scalar value instead of looking for a maximum', default=True)
    m_TargetValue = bpy.props.FloatProperty(name='TargetValue', description='These methods can make the positioning look for a target scalar value instead of looking for a maximum', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_TargetFlag', 'm_TargetValue', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SubPixelPositionEdgels)
TYPENAMES.append('BVTK_NT_SubPixelPositionEdgels' )


# --------------------------------------------------------------


class BVTK_NT_ImageRectilinearWipe(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageRectilinearWipe'
    bl_label = 'vtkImageRectilinearWipe'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    e_Wipe_items = [(x, x, x) for x in ['Horizontal', 'LowerLeft', 'LowerRight', 'Quad', 'UpperLeft', 'UpperRight', 'Vertical']]
    
    m_Axis = bpy.props.IntVectorProperty(name='Axis', description='Set/Get the location of the wipe axes. The default is X,Y (ie vector values of 0 and 1)', default=[0, 1], size=2)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_Position = bpy.props.IntVectorProperty(name='Position', description='Set/Get the location of the image transition. Note that position is specified in pixels', default=[0, 0], size=2)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    e_Wipe = bpy.props.EnumProperty(name='Wipe', description='Specify the wipe mode. This mode determnis how input 0 and input 1 are combined to produce the output. Each mode uses one or both of the values stored in Position. SetWipeToQuad - alternate input 0 and input 1 horizontally and vertically. The Position specifies the location of the quad intersection. SetWipeToLowerLeft{LowerRight,UpperLeft.UpperRight} - 3 of one input and 1 of the other. Select the location of input 0 to the LowerLeft{LowerRight,UpperLeft,UpperRight}. Position selects the location of the corner. SetWipeToHorizontal - alternate input 0 and input 1 with a vertical split. Position[0] specifies the location of the vertical transition between input 0 and input 1. SetWipeToVertical - alternate input 0 and input 1 with a horizontal split. Position[1] specifies the location of the horizonal transition between input 0 and input 1', default='Quad', items=e_Wipe_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Axis', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_Position', 'e_SplitMode', 'e_Wipe', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageRectilinearWipe)
TYPENAMES.append('BVTK_NT_ImageRectilinearWipe' )


# --------------------------------------------------------------


class BVTK_NT_ImageToPoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageToPoints'
    bl_label = 'vtkImageToPoints'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['StencilConnection'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageToPoints)
TYPENAMES.append('BVTK_NT_ImageToPoints' )


# --------------------------------------------------------------


class BVTK_NT_DepthImageToPointCloud(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DepthImageToPointCloud'
    bl_label = 'vtkDepthImageToPointCloud'
    
    m_CullFarPoints = bpy.props.BoolProperty(name='CullFarPoints', description='Indicate whether to cull points that are located on the far clipping plane. These typically are points that are part of the background. By default this is enabled', default=True)
    m_CullNearPoints = bpy.props.BoolProperty(name='CullNearPoints', description='Indicate whether to cull points that are located on the near clipping plane. These typically are points that are part of the clipped foreground. By default this is disabled', default=False)
    m_ProduceColorScalars = bpy.props.BoolProperty(name='ProduceColorScalars', description='Indicate whether to output color scalar values along with the point cloud (assuming that the scalar values are available on input). By default this is enabled', default=True)
    m_ProduceVertexCellArray = bpy.props.BoolProperty(name='ProduceVertexCellArray', description='Indicate whether to output a vertex cell array (i.e., Verts) in the output point cloud. Some filters require this vertex cells to be defined in order to execute properly. For example some mappers will only render points if the vertex cells are defined', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CullFarPoints', 'm_CullNearPoints', 'm_ProduceColorScalars', 'm_ProduceVertexCellArray', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DepthImageToPointCloud)
TYPENAMES.append('BVTK_NT_DepthImageToPointCloud' )


# --------------------------------------------------------------


class BVTK_NT_FastSplatter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FastSplatter'
    bl_label = 'vtkFastSplatter'
    e_LimitMode_items = [(x, x, x) for x in ['Clamp', 'FreezeScale', 'None', 'Scale']]
    
    e_LimitMode = bpy.props.EnumProperty(name='LimitMode', description='Set/get the way voxel values will be limited. If this is set to None (the default), the output can have arbitrarily large values. If set to clamp, the output will be clamped to [MinValue,MaxValue]. If set to scale, the output will be linearly scaled between MinValue and MaxValue', default='None', items=e_LimitMode_items)
    m_MaxValue = bpy.props.FloatProperty(name='MaxValue', description='See the LimitMode method', default=1.0)
    m_MinValue = bpy.props.FloatProperty(name='MinValue', description='See the LimitMode method', default=0.0)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Set / get the (xmin,xmax, ymin,ymax, zmin,zmax) bounding box in which the sampling is performed. If any of the (min,max) bounds values are min >= max, then the bounds will be computed automatically from the input data. Otherwise, the user-specified bounds will be used', default=[0.0, -1.0, 0.0, -1.0, 0.0, -1.0], size=6)
    m_OutputDimensions = bpy.props.IntVectorProperty(name='OutputDimensions', description='', default=[100, 100, 1], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_LimitMode', 'm_MaxValue', 'm_MinValue', 'm_ModelBounds', 'm_OutputDimensions', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FastSplatter)
TYPENAMES.append('BVTK_NT_FastSplatter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractFunctionalBagPlot(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractFunctionalBagPlot'
    bl_label = 'vtkExtractFunctionalBagPlot'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractFunctionalBagPlot)
TYPENAMES.append('BVTK_NT_ExtractFunctionalBagPlot' )


# --------------------------------------------------------------


class BVTK_NT_ExtractSelectedIds(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractSelectedIds'
    bl_label = 'vtkExtractSelectedIds'
    
    m_PreserveTopology = bpy.props.BoolProperty(name='PreserveTopology', description='This flag tells the extraction filter not to convert the selected output into an unstructured grid, but instead to produce a vtkInsidedness array and add it to the input dataset. Default value is false(0)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PreserveTopology', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractSelectedIds)
TYPENAMES.append('BVTK_NT_ExtractSelectedIds' )


# --------------------------------------------------------------


class BVTK_NT_ImageCorrelation(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageCorrelation'
    bl_label = 'vtkImageCorrelation'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Determines how the input is interpreted (set of 2d slices ...). The default is 2', default=2)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageCorrelation)
TYPENAMES.append('BVTK_NT_ImageCorrelation' )


# --------------------------------------------------------------


class BVTK_NT_ImageMathematics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMathematics'
    bl_label = 'vtkImageMathematics'
    e_Operation_items = [(x, x, x) for x in ['ATAN', 'ATAN2', 'AbsoluteValue', 'Add', 'AddConstant', 'ComplexMultiply', 'Conjugate', 'Cos', 'Divide', 'Exp', 'Invert', 'Log', 'Max', 'Min', 'Multiply', 'MultiplyByK', 'ReplaceCByK', 'Sin', 'Square', 'SquareRoot', 'Subtract']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_ConstantC = bpy.props.FloatProperty(name='ConstantC', description='A constant used by some operations (typically additive). Default is 0', default=0.0)
    m_ConstantK = bpy.props.FloatProperty(name='ConstantK', description='A constant used by some operations (typically multiplicative). Default is 1', default=1.0)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_DivideByZeroToC = bpy.props.BoolProperty(name='DivideByZeroToC', description='How to handle divide by zero. Default is 0', default=True)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_Operation = bpy.props.EnumProperty(name='Operation', description='Set/Get the Operation to perform', default='Add', items=e_Operation_items)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ConstantC', 'm_ConstantK', 'm_DesiredBytesPerPiece', 'm_DivideByZeroToC', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_Operation', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMathematics)
TYPENAMES.append('BVTK_NT_ImageMathematics' )


# --------------------------------------------------------------


class BVTK_NT_ExtractArraysOverTime(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractArraysOverTime'
    bl_label = 'vtkExtractArraysOverTime'
    
    m_ReportStatisticsOnly = bpy.props.BoolProperty(name='ReportStatisticsOnly', description='Instead of breaking a selection into a separate time-history table for each (block,ID)-tuple, you may call ReportStatisticsOnlyOn(). Then a single table per block of the input dataset will report the minimum, maximum, quartiles, and (for numerical arrays) the average and standard deviation of the selection over time', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ReportStatisticsOnly', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], ['SelectionExtractor'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractArraysOverTime)
TYPENAMES.append('BVTK_NT_ExtractArraysOverTime' )


# --------------------------------------------------------------


class BVTK_NT_CompositeDataProbeFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CompositeDataProbeFilter'
    bl_label = 'vtkCompositeDataProbeFilter'
    
    m_CategoricalData = bpy.props.BoolProperty(name='CategoricalData', description='Control whether the source point data is to be treated as categorical. If the data is categorical, then the resultant data will be determined by a nearest neighbor interpolation scheme', default=True)
    m_ComputeTolerance = bpy.props.BoolProperty(name='ComputeTolerance', description='Set whether to use the Tolerance field or precompute the tolerance. When on, the tolerance will be computed and the field value is ignored. Off by default', default=True)
    m_PassCellArrays = bpy.props.BoolProperty(name='PassCellArrays', description='Shallow copy the input cell data arrays to the output. Off by default', default=True)
    m_PassFieldArrays = bpy.props.BoolProperty(name='PassFieldArrays', description='Set whether to pass the field-data arrays from the Input i.e. the input providing the geometry to the output. On by default', default=True)
    m_PassPartialArrays = bpy.props.BoolProperty(name='PassPartialArrays', description='When dealing with composite datasets, partial arrays are common i.e. data-arrays that are not available in all of the blocks. By default, this filter only passes those point and cell data-arrays that are available in all the blocks i.e. partial array are removed. When PassPartialArrays is turned on, this behavior is changed to take a union of all arrays present thus partial arrays are passed as well. However, for composite dataset input, this filter still produces a non-composite output. For all those locations in a block of where a particular data array is missing, this filter uses vtkMath::Nan() for double and float arrays, while 0 for all other types of arrays i.e int, char etc', default=False)
    m_PassPointArrays = bpy.props.BoolProperty(name='PassPointArrays', description='Shallow copy the input point data arrays to the output Off by default', default=True)
    m_SpatialMatch = bpy.props.BoolProperty(name='SpatialMatch', description='This flag is used only when a piece is requested to update. By default the flag is off. Because no spatial correspondence between input pieces and source pieces is known, all of the source has to be requested no matter what piece of the output is requested. When there is a spatial correspondence, the user/application can set this flag. This hint allows the breakup of the probe operation to be much more efficient. When piece m of n is requested for update by the user, then only n of m needs to be requested of the source', default=True)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Set the tolerance used to compute whether a point in the source is in a cell of the input. This value is only used if ComputeTolerance is off', default=1.0)
    m_ValidPointMaskArrayName = bpy.props.StringProperty(name='ValidPointMaskArrayName', description='Returns the name of the char array added to the output with values 1 for valid points and 0 for invalid points. Set to "vtkValidPointMask" by default', default='vtkValidPointMask')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CategoricalData', 'm_ComputeTolerance', 'm_PassCellArrays', 'm_PassFieldArrays', 'm_PassPartialArrays', 'm_PassPointArrays', 'm_SpatialMatch', 'm_Tolerance', 'm_ValidPointMaskArrayName', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CompositeDataProbeFilter)
TYPENAMES.append('BVTK_NT_CompositeDataProbeFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageBlend(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageBlend'
    bl_label = 'vtkImageBlend'
    e_BlendMode_items = [(x, x, x) for x in ['Compound', 'Normal']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    e_BlendMode = bpy.props.EnumProperty(name='BlendMode', description='Set the blend mod', default='Normal', items=e_BlendMode_items)
    m_CompoundThreshold = bpy.props.FloatProperty(name='CompoundThreshold', description='Specify a threshold in compound mode. Pixels with opacity*alpha less or equal the threshold are ignored', default=0.0)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_BlendMode', 'm_CompoundThreshold', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageBlend)
TYPENAMES.append('BVTK_NT_ImageBlend' )


# --------------------------------------------------------------


menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append(BVTK_NodeCategory('VTKFilter2', 'Filter2', items=menu_items))