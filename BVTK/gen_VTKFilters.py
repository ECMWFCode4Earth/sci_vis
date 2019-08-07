from .core import *
TYPENAMES = []


# --------------------------------------------------------------


class BVTK_NT_GraphAnnotationLayersFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GraphAnnotationLayersFilter'
    bl_label = 'vtkGraphAnnotationLayersFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GraphAnnotationLayersFilter)
TYPENAMES.append('BVTK_NT_GraphAnnotationLayersFilter' )


# --------------------------------------------------------------


class BVTK_NT_DistancePolyDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DistancePolyDataFilter'
    bl_label = 'vtkDistancePolyDataFilter'
    
    m_ComputeSecondDistance = bpy.props.BoolProperty(name='ComputeSecondDistance', description='Enable/disable computation of a second output poly data with the distance from the first poly data at each point. Defaults to on', default=True)
    m_NegateDistance = bpy.props.BoolProperty(name='NegateDistance', description='Enable/disable negation of the distance values. Defaults to off. Has no effect if SignedDistance is off', default=True)
    m_SignedDistance = bpy.props.BoolProperty(name='SignedDistance', description='Enable/disable computation of the signed distance between the first poly data and the second poly data. Defaults to on', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeSecondDistance', 'm_NegateDistance', 'm_SignedDistance', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DistancePolyDataFilter)
TYPENAMES.append('BVTK_NT_DistancePolyDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_StatisticalOutlierRemoval(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StatisticalOutlierRemoval'
    bl_label = 'vtkStatisticalOutlierRemoval'
    
    m_ComputedMean = bpy.props.FloatProperty(name='ComputedMean', description='After execution, return the value of the computed mean. Before execution the value returned is invalid', default=0.0)
    m_ComputedStandardDeviation = bpy.props.FloatProperty(name='ComputedStandardDeviation', description='After execution, return the value of the computed sigma (standard deviation). Before execution the value returned is invalid', default=0.0)
    m_GenerateOutliers = bpy.props.BoolProperty(name='GenerateOutliers', description='If this method is enabled (true), then a second output will be created that contains the outlier points. By default this is off (false). Note that if enabled, the PointMap is modified as well: the outlier points are listed as well, with similar meaning, except their value is negated and shifted by -1', default=False)
    m_GenerateVertices = bpy.props.BoolProperty(name='GenerateVertices', description='If this method is enabled (true), then the outputs will contain a vertex cells (i.e., a vtkPolyVertex for each output). This takes a lot more memory but some VTK filters need cells to function properly. By default this is off (false)', default=False)
    m_SampleSize = bpy.props.IntProperty(name='SampleSize', description='For each point sampled, specify the number of the closest, surrounding points used to compute statistics. By default 25 points are used. Smaller numbers may speed performance', default=25)
    m_StandardDeviationFactor = bpy.props.FloatProperty(name='StandardDeviationFactor', description='The filter uses this specified standard deviation factor to extract points. By default, points within 1.0 standard deviations (i.e., a StandardDeviationFactor=1.0) of the mean distance to neighboring points are retained', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputedMean', 'm_ComputedStandardDeviation', 'm_GenerateOutliers', 'm_GenerateVertices', 'm_SampleSize', 'm_StandardDeviationFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StatisticalOutlierRemoval)
TYPENAMES.append('BVTK_NT_StatisticalOutlierRemoval' )


# --------------------------------------------------------------


class BVTK_NT_MultiCorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MultiCorrelativeStatistics'
    bl_label = 'vtkMultiCorrelativeStatistics'
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_MedianAbsoluteDeviation = bpy.props.BoolProperty(name='MedianAbsoluteDeviation', description='If set to true, the covariance matrix is replaced by the Median Absolute Deviation matrix. Default is false', default=False)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=1)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_DeriveOption', 'm_LearnOption', 'm_MedianAbsoluteDeviation', 'm_NumberOfPrimaryTables', 'm_TestOption', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MultiCorrelativeStatistics)
TYPENAMES.append('BVTK_NT_MultiCorrelativeStatistics' )


# --------------------------------------------------------------


class BVTK_NT_BoxClipDataSet(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BoxClipDataSet'
    bl_label = 'vtkBoxClipDataSet'
    
    m_GenerateClipScalars = bpy.props.BoolProperty(name='GenerateClipScalars', description='If this flag is enabled, then the output scalar values will be interpolated, and not the input scalar data', default=True)
    m_GenerateClippedOutput = bpy.props.BoolProperty(name='GenerateClippedOutput', description="Control whether a second output is generated. The second output contains the polygonal data that's been clipped away", default=True)
    m_Orientation = bpy.props.IntProperty(name='Orientation', description='Tells if clipping happens with a box parallel with coordinate axis (0) or with an hexahedral box (1). Initial value is 1', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateClipScalars', 'm_GenerateClippedOutput', 'm_Orientation', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BoxClipDataSet)
TYPENAMES.append('BVTK_NT_BoxClipDataSet' )


# --------------------------------------------------------------


class BVTK_NT_SelectPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SelectPolyData'
    bl_label = 'vtkSelectPolyData'
    e_SelectionMode_items = [(x, x, x) for x in ['ClosestPointRegion', 'LargestRegion', 'SmallestRegion']]
    
    m_ClosestPoint = bpy.props.FloatVectorProperty(name='ClosestPoint', description='', default=[0.0, 0.0, 0.0], size=3)
    m_GenerateSelectionScalars = bpy.props.BoolProperty(name='GenerateSelectionScalars', description='Set/Get the flag to control behavior of the filter. If GenerateSelectionScalars is on, then the output of the filter is the same as the input, except that scalars are generated. If off, the filter outputs the cells laying inside the loop, and does not generate scalars', default=True)
    m_GenerateUnselectedOutput = bpy.props.BoolProperty(name='GenerateUnselectedOutput', description="Control whether a second output is generated. The second output contains the polygonal data that's not been selected", default=True)
    m_InsideOut = bpy.props.BoolProperty(name='InsideOut', description='Set/Get the InsideOut flag. When off, the mesh within the loop is extracted. When on, the mesh outside the loop is extracted', default=True)
    e_SelectionMode = bpy.props.EnumProperty(name='SelectionMode', description='Control how inside/outside of loop is defined', default='SmallestRegion', items=e_SelectionMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClosestPoint', 'm_GenerateSelectionScalars', 'm_GenerateUnselectedOutput', 'm_InsideOut', 'e_SelectionMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1', 'Output 2'], ['Loop'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SelectPolyData)
TYPENAMES.append('BVTK_NT_SelectPolyData' )


# --------------------------------------------------------------


class BVTK_NT_ExtractVectorComponents(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractVectorComponents'
    bl_label = 'vtkExtractVectorComponents'
    
    m_ExtractToFieldData = bpy.props.BoolProperty(name='ExtractToFieldData', description="Determines whether the vector components will be put in separate outputs or in the first output's field dat", default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ExtractToFieldData', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1', 'Output 2'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractVectorComponents)
TYPENAMES.append('BVTK_NT_ExtractVectorComponents' )


# --------------------------------------------------------------


class BVTK_NT_ProgrammableSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProgrammableSource'
    bl_label = 'vtkProgrammableSource'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1', 'Output 2', 'Output 3', 'Output 4'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProgrammableSource)
TYPENAMES.append('BVTK_NT_ProgrammableSource' )


# --------------------------------------------------------------


class BVTK_NT_CorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CorrelativeStatistics'
    bl_label = 'vtkCorrelativeStatistics'
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=1)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_DeriveOption', 'm_LearnOption', 'm_NumberOfPrimaryTables', 'm_TestOption', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CorrelativeStatistics)
TYPENAMES.append('BVTK_NT_CorrelativeStatistics' )


# --------------------------------------------------------------


class BVTK_NT_GraphToPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GraphToPolyData'
    bl_label = 'vtkGraphToPolyData'
    
    m_EdgeGlyphOutput = bpy.props.BoolProperty(name='EdgeGlyphOutput', description="Create a second output containing points and orientation vectors for drawing arrows or other glyphs on edges. This output should be set as the first input to vtkGlyph3D to place glyphs on the edges. vtkGlyphSource2D's VTK_EDGEARROW_GLYPH provides a good glyph for drawing arrows. Default value is off", default=False)
    m_EdgeGlyphPosition = bpy.props.FloatProperty(name='EdgeGlyphPosition', description='The position of the glyph point along the edge. 0 puts a glyph point at the source of each edge. 1 puts a glyph point at the target of each edge. An intermediate value will place the glyph point between the source and target. The default value is 1', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_EdgeGlyphOutput', 'm_EdgeGlyphPosition', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GraphToPolyData)
TYPENAMES.append('BVTK_NT_GraphToPolyData' )


# --------------------------------------------------------------


class BVTK_NT_ImageResliceToColors(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageResliceToColors'
    bl_label = 'vtkImageResliceToColors'
    e_InterpolationMode_items = [(x, x, x) for x in ['Cubic', 'Linear', 'NearestNeighbor']]
    e_OutputExtent_items = [(x, x, x) for x in ['Default']]
    e_OutputFormat_items = [(x, x, x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_OutputOrigin_items = [(x, x, x) for x in ['Default']]
    e_OutputSpacing_items = [(x, x, x) for x in ['Default']]
    e_SlabMode_items = [(x, x, x) for x in ['Max', 'Mean', 'Min', 'Sum']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_AutoCropOutput = bpy.props.BoolProperty(name='AutoCropOutput', description='Turn this on if you want to guarantee that the extent of the output will be large enough to ensure that none of the data will be cropped (default: Off)', default=True)
    m_BackgroundColor = bpy.props.FloatVectorProperty(name='BackgroundColor', description='', default=[0.0, 0.0, 0.0, 0.0], size=4)
    m_BackgroundLevel = bpy.props.FloatProperty(name='BackgroundLevel', description='Set background grey level (for single-component images)', default=0.0)
    m_Border = bpy.props.BoolProperty(name='Border', description="Extend the apparent input border by a half voxel (default: On). This changes how interpolation is handled at the borders of the input image: if the center of an output voxel is beyond the edge of the input image, but is within a half voxel width of the edge (using the input voxel width), then the value of the output voxel is calculated as if the input's edge voxels were duplicated past the edges of the input. This has no effect if Mirror or Wrap are on", default=True)
    m_Bypass = bpy.props.BoolProperty(name='Bypass', description='Bypass the color mapping operation and output the scalar values directly. The output values will be float, rather than the input data type', default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GenerateStencilOutput = bpy.props.BoolProperty(name='GenerateStencilOutput', description='Generate an output stencil that defines which pixels were interpolated and which pixels were out-of-bounds of the input', default=True)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Interpolate = bpy.props.BoolProperty(name='Interpolate', description='Convenient methods for switching between nearest-neighbor and linear interpolation. InterpolateOn() is equivalent to SetInterpolationModeToLinear() and InterpolateOff() is equivalent to SetInterpolationModeToNearestNeighbor() You should not use these methods if you use the SetInterpolationMode methods', default=True)
    e_InterpolationMode = bpy.props.EnumProperty(name='InterpolationMode', description='Set interpolation mode (default: nearest neighbor)', default='NearestNeighbor', items=e_InterpolationMode_items)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_Mirror = bpy.props.BoolProperty(name='Mirror', description='Turn on mirror-pad feature (default: Off). This will override the wrap-pad', default=True)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_Optimization = bpy.props.BoolProperty(name='Optimization', description='Turn on and off optimizations (default on, they should only be turned off for testing purposes)', default=True)
    m_OutputDimensionality = bpy.props.IntProperty(name='OutputDimensionality', description='Force the dimensionality of the output to either 1, 2, 3 or 0 (default: 3). If the dimensionality is 2D, then the Z extent of the output is forced to (0,0) and the Z origin of the output is forced to 0.0 (i.e. the output extent is confined to the xy plane). If the dimensionality is 1D, the output extent is confined to the x axis. For 0D, the output extent consists of a single voxel at (0,0,0)', default=3)
    e_OutputExtent = bpy.props.EnumProperty(name='OutputExtent', description='Set the extent for the output data. The default output extent is the input extent permuted through the ResliceAxes', default='Default', items=e_OutputExtent_items)
    e_OutputFormat = bpy.props.EnumProperty(name='OutputFormat', description='Set the output format, the default is RGBA', default='RGBA', items=e_OutputFormat_items)
    e_OutputOrigin = bpy.props.EnumProperty(name='OutputOrigin', description='Set the origin for the output data. The default output origin is the input origin permuted through the ResliceAxes', default='Default', items=e_OutputOrigin_items)
    m_OutputScalarType = bpy.props.IntProperty(name='OutputScalarType', description='Set the scalar type of the output to be different from the input. The default value is -1, which means that the input scalar type will be used to set the output scalar type. Otherwise, this must be set to one of the following types: VTK_CHAR, VTK_SIGNED_CHAR, VTK_UNSIGNED_CHAR, VTK_SHORT, VTK_UNSIGNED_SHORT, VTK_INT, VTK_UNSIGNED_INT, VTK_FLOAT, or VTK_DOUBLE. Other types are not permitted. If the output type is an integer type, the output will be rounded and clamped to the limits of the type', default=-1)
    e_OutputSpacing = bpy.props.EnumProperty(name='OutputSpacing', description='Set the voxel spacing for the output data. The default output spacing is the input spacing permuted through the ResliceAxes', default='Default', items=e_OutputSpacing_items)
    m_ResliceAxesDirectionCosines = bpy.props.FloatVectorProperty(name='ResliceAxesDirectionCosines', description='Specify the direction cosines for the ResliceAxes (i.e. the first three elements of each of the first three columns of the ResliceAxes matrix). This will modify the current ResliceAxes matrix, or create a new matrix if none exists', default=[1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], size=9)
    m_ResliceAxesOrigin = bpy.props.FloatVectorProperty(name='ResliceAxesOrigin', description='Specify the origin for the ResliceAxes (i.e. the first three elements of the final column of the ResliceAxes matrix). This will modify the current ResliceAxes matrix, or create new matrix if none exists', default=[0.0, 0.0, 0.0], size=3)
    m_ScalarScale = bpy.props.FloatProperty(name='ScalarScale', description='Set multiplication factor to apply to all the output voxels. After a sample value has been interpolated from the input image, the equation u = (v + ScalarShift)*ScalarScale will be applied to it before it is written to the output image. The result will always be clamped to the limits of the output data type', default=1.0)
    m_ScalarShift = bpy.props.FloatProperty(name='ScalarShift', description='Set a value to add to all the output voxels. After a sample value has been interpolated from the input image, the equation u = (v + ScalarShift)*ScalarScale will be applied to it before it is written to the output image. The result will always be clamped to the limits of the output data type', default=0.0)
    e_SlabMode = bpy.props.EnumProperty(name='SlabMode', description='Set the slab mode, for generating thick slices. The default is Mean. If SetSlabNumberOfSlices(N) is called with N greater than one, then each output slice will actually be a composite of N slices. This method specifies the compositing mode to be used', default='Mean', items=e_SlabMode_items)
    m_SlabNumberOfSlices = bpy.props.IntProperty(name='SlabNumberOfSlices', description='Set the number of slices that will be combined to create the slab', default=1)
    m_SlabSliceSpacingFraction = bpy.props.FloatProperty(name='SlabSliceSpacingFraction', description='The slab spacing as a fraction of the output slice spacing. When one of the various slab modes is chosen, each output slice is produced by generating several "temporary" output slices and then combining them according to the slab mode. By default, the spacing between these temporary slices is the Z component of the OutputSpacing. This method sets the spacing between these temporary slices to be a fraction of the output spacing', default=1.0)
    m_SlabTrapezoidIntegration = bpy.props.BoolProperty(name='SlabTrapezoidIntegration', description='Use trapezoid integration for slab computation. All this does is weigh the first and last slices by half when doing sum and mean. It is off by default', default=True)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_TransformInputSampling = bpy.props.BoolProperty(name='TransformInputSampling', description='Specify whether to transform the spacing, origin and extent of the Input (or the InformationInput) according to the direction cosines and origin of the ResliceAxes before applying them as the default output spacing, origin and extent (default: On)', default=True)
    m_Wrap = bpy.props.BoolProperty(name='Wrap', description='Turn on wrap-pad feature (default: Off)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=32, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutoCropOutput', 'm_BackgroundColor', 'm_BackgroundLevel', 'm_Border', 'm_Bypass', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GenerateStencilOutput', 'm_GlobalDefaultEnableSMP', 'm_Interpolate', 'e_InterpolationMode', 'm_MinimumPieceSize', 'm_Mirror', 'm_NumberOfThreads', 'm_Optimization', 'm_OutputDimensionality', 'e_OutputExtent', 'e_OutputFormat', 'e_OutputOrigin', 'm_OutputScalarType', 'e_OutputSpacing', 'm_ResliceAxesDirectionCosines', 'm_ResliceAxesOrigin', 'm_ScalarScale', 'm_ScalarShift', 'e_SlabMode', 'm_SlabNumberOfSlices', 'm_SlabSliceSpacingFraction', 'm_SlabTrapezoidIntegration', 'e_SplitMode', 'm_TransformInputSampling', 'm_Wrap', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1'], ['Interpolator', 'LookupTable', 'ResliceAxes', 'ResliceTransform', 'StencilOutput'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageResliceToColors)
TYPENAMES.append('BVTK_NT_ImageResliceToColors' )


# --------------------------------------------------------------


class BVTK_NT_ResliceCursorPolyDataAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ResliceCursorPolyDataAlgorithm'
    bl_label = 'vtkResliceCursorPolyDataAlgorithm'
    e_ReslicePlaneNormal_items = [(x, x, x) for x in ['XAxis', 'YAxis', 'ZAxis']]
    
    e_ReslicePlaneNormal = bpy.props.EnumProperty(name='ReslicePlaneNormal', description='Which of the 3 axes defines the reslice plane normal ', default='XAxis', items=e_ReslicePlaneNormal_items)
    m_SliceBounds = bpy.props.FloatVectorProperty(name='SliceBounds', description='', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ReslicePlaneNormal', 'm_SliceBounds', ]
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1', 'Output 2', 'Output 3'], ['ResliceCursor'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ResliceCursorPolyDataAlgorithm)
TYPENAMES.append('BVTK_NT_ResliceCursorPolyDataAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_StreamingStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StreamingStatistics'
    bl_label = 'vtkStreamingStatistics'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StreamingStatistics)
TYPENAMES.append('BVTK_NT_StreamingStatistics' )


# --------------------------------------------------------------


class BVTK_NT_HighestDensityRegionsStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HighestDensityRegionsStatistics'
    bl_label = 'vtkHighestDensityRegionsStatistics'
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=1)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_DeriveOption', 'm_LearnOption', 'm_NumberOfPrimaryTables', 'm_TestOption', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HighestDensityRegionsStatistics)
TYPENAMES.append('BVTK_NT_HighestDensityRegionsStatistics' )


# --------------------------------------------------------------


class BVTK_NT_PExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PExtractHistogram2D'
    bl_label = 'vtkPExtractHistogram2D'
    e_ScalarType_items = [(x, x, x) for x in ['Double', 'Float', 'UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_ComponentsToProcess = bpy.props.IntVectorProperty(name='ComponentsToProcess', description='', default=[0, 0], size=2)
    m_CustomHistogramExtents = bpy.props.FloatVectorProperty(name='CustomHistogramExtents', description='', default=[0.0, 0.0, 0.0, 0.0], size=4)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_NumberOfBins = bpy.props.IntVectorProperty(name='NumberOfBins', description='', default=[0, 0], size=2)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=1)
    e_ScalarType = bpy.props.EnumProperty(name='ScalarType', description='Control the scalar type of the output histogram. If the input is relatively small, you can save space by using a smaller data type. Defaults to unsigned integer', default='UnsignedInt', items=e_ScalarType_items)
    m_SwapColumns = bpy.props.BoolProperty(name='SwapColumns', description='', default=True)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    m_UseCustomHistogramExtents = bpy.props.BoolProperty(name='UseCustomHistogramExtents', description='Use the extents in CustomHistogramExtents when computing the histogram, rather than the simple range of the input columns', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_ComponentsToProcess', 'm_CustomHistogramExtents', 'm_DeriveOption', 'm_LearnOption', 'm_NumberOfBins', 'm_NumberOfPrimaryTables', 'e_ScalarType', 'm_SwapColumns', 'm_TestOption', 'm_UseCustomHistogramExtents', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2', 'Output 3'], ['RowMask'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PExtractHistogram2D)
TYPENAMES.append('BVTK_NT_PExtractHistogram2D' )


# --------------------------------------------------------------


class BVTK_NT_TableBasedClipDataSet(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TableBasedClipDataSet'
    bl_label = 'vtkTableBasedClipDataSet'
    
    m_GenerateClipScalars = bpy.props.BoolProperty(name='GenerateClipScalars', description='Set/Get flag GenerateClipScalars, with 0 as the default value. With this flag on, the scalar point data values obtained by evaluating the implicit function will be exported to the output. Note that this flag requries that an implicit function be provided', default=True)
    m_GenerateClippedOutput = bpy.props.BoolProperty(name='GenerateClippedOutput', description='Set/Get whether a second output is generated. The second output contains the polygonal data that is clipped away by the iso-surface', default=True)
    m_InsideOut = bpy.props.BoolProperty(name='InsideOut', description='Set/Get the InsideOut flag. With this flag off, a vertex is considered inside (the implicit function or the isosurface) if the (function or scalar) value is greater than IVAR Value. With this flag on, a vertex is considered inside (the implicit function or the isosurface) if the (function or scalar) value is less than or equal to IVAR Value. This flag is off by default', default=True)
    m_MergeTolerance = bpy.props.FloatProperty(name='MergeTolerance', description='Set/Get the tolerance used for merging duplicate points near the clipping intersection cells. This tolerance may prevent the generation of degenerate primitives. Note that only 3D cells actually use this IVAR', default=0.01)
    m_UseValueAsOffset = bpy.props.BoolProperty(name='UseValueAsOffset', description='Set/Get flag UseValueAsOffset, with true as the default value. With this flag on, IVAR Value is used as an offset parameter to the implicit function. Value is used only when clipping using a scalar array', default=True)
    m_Value = bpy.props.FloatProperty(name='Value', description='Set/Get the clipping value of the implicit function (if an implicit function is applied) or scalar data array (if a scalar data array is used), with 0.0 as the default value. This value is ignored if flag UseValueAsOffset is true AND a clip function is defined', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateClipScalars', 'm_GenerateClippedOutput', 'm_InsideOut', 'm_MergeTolerance', 'm_UseValueAsOffset', 'm_Value', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], ['ClipFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TableBasedClipDataSet)
TYPENAMES.append('BVTK_NT_TableBasedClipDataSet' )


# --------------------------------------------------------------


class BVTK_NT_PPairwiseExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PPairwiseExtractHistogram2D'
    bl_label = 'vtkPPairwiseExtractHistogram2D'
    e_ScalarType_items = [(x, x, x) for x in ['UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_NumberOfBins = bpy.props.IntVectorProperty(name='NumberOfBins', description='', default=[0, 0], size=2)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=1)
    e_ScalarType = bpy.props.EnumProperty(name='ScalarType', description='Set the scalar type for each of the computed histograms', default='UnsignedInt', items=e_ScalarType_items)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_DeriveOption', 'm_LearnOption', 'm_NumberOfBins', 'm_NumberOfPrimaryTables', 'e_ScalarType', 'm_TestOption', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2', 'Output 3'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PPairwiseExtractHistogram2D)
TYPENAMES.append('BVTK_NT_PPairwiseExtractHistogram2D' )


# --------------------------------------------------------------


class BVTK_NT_ExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractHistogram2D'
    bl_label = 'vtkExtractHistogram2D'
    e_ScalarType_items = [(x, x, x) for x in ['Double', 'Float', 'UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_ComponentsToProcess = bpy.props.IntVectorProperty(name='ComponentsToProcess', description='', default=[0, 0], size=2)
    m_CustomHistogramExtents = bpy.props.FloatVectorProperty(name='CustomHistogramExtents', description='', default=[0.0, 0.0, 0.0, 0.0], size=4)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_NumberOfBins = bpy.props.IntVectorProperty(name='NumberOfBins', description='', default=[0, 0], size=2)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=1)
    e_ScalarType = bpy.props.EnumProperty(name='ScalarType', description='Control the scalar type of the output histogram. If the input is relatively small, you can save space by using a smaller data type. Defaults to unsigned integer', default='UnsignedInt', items=e_ScalarType_items)
    m_SwapColumns = bpy.props.BoolProperty(name='SwapColumns', description='', default=True)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    m_UseCustomHistogramExtents = bpy.props.BoolProperty(name='UseCustomHistogramExtents', description='Use the extents in CustomHistogramExtents when computing the histogram, rather than the simple range of the input columns', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_ComponentsToProcess', 'm_CustomHistogramExtents', 'm_DeriveOption', 'm_LearnOption', 'm_NumberOfBins', 'm_NumberOfPrimaryTables', 'e_ScalarType', 'm_SwapColumns', 'm_TestOption', 'm_UseCustomHistogramExtents', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2', 'Output 3'], ['RowMask'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractHistogram2D)
TYPENAMES.append('BVTK_NT_ExtractHistogram2D' )


# --------------------------------------------------------------


class BVTK_NT_ExtractSelectedRows(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractSelectedRows'
    bl_label = 'vtkExtractSelectedRows'
    
    m_AddOriginalRowIdsArray = bpy.props.BoolProperty(name='AddOriginalRowIdsArray', description='When set, a column named vtkOriginalRowIds will be added to the output. False by default', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AddOriginalRowIdsArray', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractSelectedRows)
TYPENAMES.append('BVTK_NT_ExtractSelectedRows' )


# --------------------------------------------------------------


class BVTK_NT_KMeansStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_KMeansStatistics'
    bl_label = 'vtkKMeansStatistics'
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_DefaultNumberOfClusters = bpy.props.IntProperty(name='DefaultNumberOfClusters', description='Set/get the DefaultNumberOfClusters, used when no initial cluster coordinates are specified', default=3)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_KValuesArrayName = bpy.props.StringProperty(name='KValuesArrayName', description='Set/get the KValuesArrayName', default='K')
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_MaxNumIterations = bpy.props.IntProperty(name='MaxNumIterations', description='Set/get the MaxNumIterations used to terminate iterations on cluster center coordinates when the relative tolerance can not be met', default=50)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=1)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Set/get the relative Tolerance used to terminate iterations on cluster center coordinates', default=0.01)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_DefaultNumberOfClusters', 'm_DeriveOption', 'm_KValuesArrayName', 'm_LearnOption', 'm_MaxNumIterations', 'm_NumberOfPrimaryTables', 'm_TestOption', 'm_Tolerance', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2'], ['DistanceFunctor'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_KMeansStatistics)
TYPENAMES.append('BVTK_NT_KMeansStatistics' )


# --------------------------------------------------------------


class BVTK_NT_TemporalPathLineFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TemporalPathLineFilter'
    bl_label = 'vtkTemporalPathLineFilter'
    
    m_IdChannelArray = bpy.props.StringProperty(name='IdChannelArray', description='Specify the name of a scalar array which will be used to fetch the index of each point. This is necessary only if the particles change position (Id order) on each time step. The Id can be used to identify particles at each step and hence track them properly. If this array is nullptr, the global point ids are used. If an Id array cannot otherwise be found, the point index is used as the ID')
    m_KeepDeadTrails = bpy.props.IntProperty(name='KeepDeadTrails', description="When a particle 'disappears', the trail belonging to it is removed from the list. When this flag is enabled, dead trails will persist until the next time the list is cleared. Use carefully as it may cause excessive memory consumption if left on by mistake", default=0)
    m_MaskPoints = bpy.props.IntProperty(name='MaskPoints', description='Set the number of particles to track as a ratio of the input example: setting MaskPoints to 10 will track every 10th poin', default=200)
    m_MaxStepDistance = bpy.props.FloatVectorProperty(name='MaxStepDistance', description='', default=[1.0, 1.0, 1.0], size=3)
    m_MaxTrackLength = bpy.props.IntProperty(name='MaxTrackLength', description='If the Particles being traced animate for a long time, the trails or traces will become long and stringy. Setting the MaxTraceTimeLength will limit how much of the trace is displayed. Tracks longer then the Max will disappear and the trace will apppear like a snake of fixed length which progresses as the particle move', default=10)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_IdChannelArray', 'm_KeepDeadTrails', 'm_MaskPoints', 'm_MaxStepDistance', 'm_MaxTrackLength', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TemporalPathLineFilter)
TYPENAMES.append('BVTK_NT_TemporalPathLineFilter' )


# --------------------------------------------------------------


class BVTK_NT_FitImplicitFunction(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FitImplicitFunction'
    bl_label = 'vtkFitImplicitFunction'
    
    m_GenerateOutliers = bpy.props.BoolProperty(name='GenerateOutliers', description='If this method is enabled (true), then a second output will be created that contains the outlier points. By default this is off (false). Note that if enabled, the PointMap is modified as well: the outlier points are listed as well, with similar meaning, except their value is negated and shifted by -1', default=False)
    m_GenerateVertices = bpy.props.BoolProperty(name='GenerateVertices', description='If this method is enabled (true), then the outputs will contain a vertex cells (i.e., a vtkPolyVertex for each output). This takes a lot more memory but some VTK filters need cells to function properly. By default this is off (false)', default=False)
    m_Threshold = bpy.props.FloatProperty(name='Threshold', description='Specify a threshold value which defines a fuzzy extraction surface. Since in this filter the implicit surface is defined as f(x,y,z)=0; the extracted points are (-Threshold <= f(x,y,z) < Threshold)', default=0.01)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateOutliers', 'm_GenerateVertices', 'm_Threshold', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], ['ImplicitFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FitImplicitFunction)
TYPENAMES.append('BVTK_NT_FitImplicitFunction' )


# --------------------------------------------------------------


class BVTK_NT_ClipVolume(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ClipVolume'
    bl_label = 'vtkClipVolume'
    
    m_GenerateClipScalars = bpy.props.BoolProperty(name='GenerateClipScalars', description='If this flag is enabled, then the output scalar values will be interpolated from the implicit function values, and not the input scalar data. If you enable this flag but do not provide an implicit function an error will be reported', default=True)
    m_GenerateClippedOutput = bpy.props.BoolProperty(name='GenerateClippedOutput', description="Control whether a second output is generated. The second output contains the unstructured grid that's been clipped away", default=True)
    m_InsideOut = bpy.props.BoolProperty(name='InsideOut', description='Set/Get the InsideOut flag. When off, a vertex is considered inside the implicit function if its value is greater than the Value ivar. When InsideOutside is turned on, a vertex is considered inside the implicit function if its implicit function value is less than or equal to the Value ivar. InsideOut is off by default', default=True)
    m_MergeTolerance = bpy.props.FloatProperty(name='MergeTolerance', description='Set the tolerance for merging clip intersection points that are near the corners of voxels. This tolerance is used to prevent the generation of degenerate tetrahedra', default=0.01)
    m_Mixed3DCellGeneration = bpy.props.BoolProperty(name='Mixed3DCellGeneration', description='Control whether the filter produces a mix of 3D cell types on output, or whether the output cells are all tetrahedra. By default, a mixed set of cells (e.g., tetrahedra and wedges) is produced. (Note: mixed type generation is faster and less overall data is generated.', default=True)
    m_Value = bpy.props.FloatProperty(name='Value', description='Set the clipping value of the implicit function (if clipping with implicit function) or scalar value (if clipping with scalars). The default value is 0.0', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateClipScalars', 'm_GenerateClippedOutput', 'm_InsideOut', 'm_MergeTolerance', 'm_Mixed3DCellGeneration', 'm_Value', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], ['ClipFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ClipVolume)
TYPENAMES.append('BVTK_NT_ClipVolume' )


# --------------------------------------------------------------


class BVTK_NT_ConvertSelectionDomain(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ConvertSelectionDomain'
    bl_label = 'vtkConvertSelectionDomain'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ConvertSelectionDomain)
TYPENAMES.append('BVTK_NT_ConvertSelectionDomain' )


# --------------------------------------------------------------


class BVTK_NT_PCAStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PCAStatistics'
    bl_label = 'vtkPCAStatistics'
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_BasisScheme = bpy.props.IntProperty(name='BasisScheme', description='This variable controls the dimensionality of output tuples in Assess operation. Consider the case where you have requested a PCA on D columns', default=0)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_FixedBasisEnergy = bpy.props.FloatProperty(name='FixedBasisEnergy', description='The minimum energy the new basis should use, as a fraction. See SetBasisScheme() for more information. When FixedBasisEnergy >= 1 (the default), the fixed basis energy scheme is equivalent to the full basis scheme', default=1.0)
    m_FixedBasisSize = bpy.props.IntProperty(name='FixedBasisSize', description='The number of basis vectors to use. See SetBasisScheme() for more information. When FixedBasisSize <= 0 (the default), the fixed basis size scheme is equivalent to the full basis scheme', default=-1)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_MedianAbsoluteDeviation = bpy.props.BoolProperty(name='MedianAbsoluteDeviation', description='If set to true, the covariance matrix is replaced by the Median Absolute Deviation matrix. Default is false', default=False)
    m_NormalizationScheme = bpy.props.IntProperty(name='NormalizationScheme', description='This determines how (or if) the covariance matrix cov is normalized before PCA', default=0)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=1)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_BasisScheme', 'm_DeriveOption', 'm_FixedBasisEnergy', 'm_FixedBasisSize', 'm_LearnOption', 'm_MedianAbsoluteDeviation', 'm_NormalizationScheme', 'm_NumberOfPrimaryTables', 'm_TestOption', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2', 'Input 3'], ['Output 0', 'Output 1', 'Output 2'], ['SpecifiedNormalization'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PCAStatistics)
TYPENAMES.append('BVTK_NT_PCAStatistics' )


# --------------------------------------------------------------


class BVTK_NT_ContingencyStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ContingencyStatistics'
    bl_label = 'vtkContingencyStatistics'
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=2)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_DeriveOption', 'm_LearnOption', 'm_NumberOfPrimaryTables', 'm_TestOption', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ContingencyStatistics)
TYPENAMES.append('BVTK_NT_ContingencyStatistics' )


# --------------------------------------------------------------


class BVTK_NT_ImageReslice(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageReslice'
    bl_label = 'vtkImageReslice'
    e_InterpolationMode_items = [(x, x, x) for x in ['Cubic', 'Linear', 'NearestNeighbor']]
    e_OutputExtent_items = [(x, x, x) for x in ['Default']]
    e_OutputOrigin_items = [(x, x, x) for x in ['Default']]
    e_OutputSpacing_items = [(x, x, x) for x in ['Default']]
    e_SlabMode_items = [(x, x, x) for x in ['Max', 'Mean', 'Min', 'Sum']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_AutoCropOutput = bpy.props.BoolProperty(name='AutoCropOutput', description='Turn this on if you want to guarantee that the extent of the output will be large enough to ensure that none of the data will be cropped (default: Off)', default=True)
    m_BackgroundColor = bpy.props.FloatVectorProperty(name='BackgroundColor', description='', default=[0.0, 0.0, 0.0, 0.0], size=4)
    m_BackgroundLevel = bpy.props.FloatProperty(name='BackgroundLevel', description='Set background grey level (for single-component images)', default=0.0)
    m_Border = bpy.props.BoolProperty(name='Border', description="Extend the apparent input border by a half voxel (default: On). This changes how interpolation is handled at the borders of the input image: if the center of an output voxel is beyond the edge of the input image, but is within a half voxel width of the edge (using the input voxel width), then the value of the output voxel is calculated as if the input's edge voxels were duplicated past the edges of the input. This has no effect if Mirror or Wrap are on", default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GenerateStencilOutput = bpy.props.BoolProperty(name='GenerateStencilOutput', description='Generate an output stencil that defines which pixels were interpolated and which pixels were out-of-bounds of the input', default=True)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Interpolate = bpy.props.BoolProperty(name='Interpolate', description='Convenient methods for switching between nearest-neighbor and linear interpolation. InterpolateOn() is equivalent to SetInterpolationModeToLinear() and InterpolateOff() is equivalent to SetInterpolationModeToNearestNeighbor() You should not use these methods if you use the SetInterpolationMode methods', default=True)
    e_InterpolationMode = bpy.props.EnumProperty(name='InterpolationMode', description='Set interpolation mode (default: nearest neighbor)', default='NearestNeighbor', items=e_InterpolationMode_items)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_Mirror = bpy.props.BoolProperty(name='Mirror', description='Turn on mirror-pad feature (default: Off). This will override the wrap-pad', default=True)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_Optimization = bpy.props.BoolProperty(name='Optimization', description='Turn on and off optimizations (default on, they should only be turned off for testing purposes)', default=True)
    m_OutputDimensionality = bpy.props.IntProperty(name='OutputDimensionality', description='Force the dimensionality of the output to either 1, 2, 3 or 0 (default: 3). If the dimensionality is 2D, then the Z extent of the output is forced to (0,0) and the Z origin of the output is forced to 0.0 (i.e. the output extent is confined to the xy plane). If the dimensionality is 1D, the output extent is confined to the x axis. For 0D, the output extent consists of a single voxel at (0,0,0)', default=3)
    e_OutputExtent = bpy.props.EnumProperty(name='OutputExtent', description='Set the extent for the output data. The default output extent is the input extent permuted through the ResliceAxes', default='Default', items=e_OutputExtent_items)
    e_OutputOrigin = bpy.props.EnumProperty(name='OutputOrigin', description='Set the origin for the output data. The default output origin is the input origin permuted through the ResliceAxes', default='Default', items=e_OutputOrigin_items)
    m_OutputScalarType = bpy.props.IntProperty(name='OutputScalarType', description='Set the scalar type of the output to be different from the input. The default value is -1, which means that the input scalar type will be used to set the output scalar type. Otherwise, this must be set to one of the following types: VTK_CHAR, VTK_SIGNED_CHAR, VTK_UNSIGNED_CHAR, VTK_SHORT, VTK_UNSIGNED_SHORT, VTK_INT, VTK_UNSIGNED_INT, VTK_FLOAT, or VTK_DOUBLE. Other types are not permitted. If the output type is an integer type, the output will be rounded and clamped to the limits of the type', default=-1)
    e_OutputSpacing = bpy.props.EnumProperty(name='OutputSpacing', description='Set the voxel spacing for the output data. The default output spacing is the input spacing permuted through the ResliceAxes', default='Default', items=e_OutputSpacing_items)
    m_ResliceAxesDirectionCosines = bpy.props.FloatVectorProperty(name='ResliceAxesDirectionCosines', description='Specify the direction cosines for the ResliceAxes (i.e. the first three elements of each of the first three columns of the ResliceAxes matrix). This will modify the current ResliceAxes matrix, or create a new matrix if none exists', default=[1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], size=9)
    m_ResliceAxesOrigin = bpy.props.FloatVectorProperty(name='ResliceAxesOrigin', description='Specify the origin for the ResliceAxes (i.e. the first three elements of the final column of the ResliceAxes matrix). This will modify the current ResliceAxes matrix, or create new matrix if none exists', default=[0.0, 0.0, 0.0], size=3)
    m_ScalarScale = bpy.props.FloatProperty(name='ScalarScale', description='Set multiplication factor to apply to all the output voxels. After a sample value has been interpolated from the input image, the equation u = (v + ScalarShift)*ScalarScale will be applied to it before it is written to the output image. The result will always be clamped to the limits of the output data type', default=1.0)
    m_ScalarShift = bpy.props.FloatProperty(name='ScalarShift', description='Set a value to add to all the output voxels. After a sample value has been interpolated from the input image, the equation u = (v + ScalarShift)*ScalarScale will be applied to it before it is written to the output image. The result will always be clamped to the limits of the output data type', default=0.0)
    e_SlabMode = bpy.props.EnumProperty(name='SlabMode', description='Set the slab mode, for generating thick slices. The default is Mean. If SetSlabNumberOfSlices(N) is called with N greater than one, then each output slice will actually be a composite of N slices. This method specifies the compositing mode to be used', default='Mean', items=e_SlabMode_items)
    m_SlabNumberOfSlices = bpy.props.IntProperty(name='SlabNumberOfSlices', description='Set the number of slices that will be combined to create the slab', default=1)
    m_SlabSliceSpacingFraction = bpy.props.FloatProperty(name='SlabSliceSpacingFraction', description='The slab spacing as a fraction of the output slice spacing. When one of the various slab modes is chosen, each output slice is produced by generating several "temporary" output slices and then combining them according to the slab mode. By default, the spacing between these temporary slices is the Z component of the OutputSpacing. This method sets the spacing between these temporary slices to be a fraction of the output spacing', default=1.0)
    m_SlabTrapezoidIntegration = bpy.props.BoolProperty(name='SlabTrapezoidIntegration', description='Use trapezoid integration for slab computation. All this does is weigh the first and last slices by half when doing sum and mean. It is off by default', default=True)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_TransformInputSampling = bpy.props.BoolProperty(name='TransformInputSampling', description='Specify whether to transform the spacing, origin and extent of the Input (or the InformationInput) according to the direction cosines and origin of the ResliceAxes before applying them as the default output spacing, origin and extent (default: On)', default=True)
    m_Wrap = bpy.props.BoolProperty(name='Wrap', description='Turn on wrap-pad feature (default: Off)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=30, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutoCropOutput', 'm_BackgroundColor', 'm_BackgroundLevel', 'm_Border', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GenerateStencilOutput', 'm_GlobalDefaultEnableSMP', 'm_Interpolate', 'e_InterpolationMode', 'm_MinimumPieceSize', 'm_Mirror', 'm_NumberOfThreads', 'm_Optimization', 'm_OutputDimensionality', 'e_OutputExtent', 'e_OutputOrigin', 'm_OutputScalarType', 'e_OutputSpacing', 'm_ResliceAxesDirectionCosines', 'm_ResliceAxesOrigin', 'm_ScalarScale', 'm_ScalarShift', 'e_SlabMode', 'm_SlabNumberOfSlices', 'm_SlabSliceSpacingFraction', 'm_SlabTrapezoidIntegration', 'e_SplitMode', 'm_TransformInputSampling', 'm_Wrap', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1'], ['Interpolator', 'ResliceAxes', 'ResliceTransform', 'StencilOutput'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageReslice)
TYPENAMES.append('BVTK_NT_ImageReslice' )


# --------------------------------------------------------------


class BVTK_NT_ClipDataSet(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ClipDataSet'
    bl_label = 'vtkClipDataSet'
    
    m_GenerateClipScalars = bpy.props.BoolProperty(name='GenerateClipScalars', description='If this flag is enabled, then the output scalar values will be interpolated from the implicit function values, and not the input scalar data. If you enable this flag but do not provide an implicit function an error will be reported', default=True)
    m_GenerateClippedOutput = bpy.props.BoolProperty(name='GenerateClippedOutput', description="Control whether a second output is generated. The second output contains the polygonal data that's been clipped away", default=True)
    m_InsideOut = bpy.props.BoolProperty(name='InsideOut', description='Set/Get the InsideOut flag. When off, a vertex is considered inside the implicit function if its value is greater than the Value ivar. When InsideOutside is turned on, a vertex is considered inside the implicit function if its implicit function value is less than or equal to the Value ivar. InsideOut is off by default', default=True)
    m_MergeTolerance = bpy.props.FloatProperty(name='MergeTolerance', description='Set the tolerance for merging clip intersection points that are near the vertices of cells. This tolerance is used to prevent the generation of degenerate primitives. Note that only 3D cells actually use this instance variable', default=0.01)
    m_UseValueAsOffset = bpy.props.BoolProperty(name='UseValueAsOffset', description='If UseValueAsOffset is true, Value is used as an offset parameter to the implicit function. Otherwise, Value is used only when clipping using a scalar array. Default is true', default=True)
    m_Value = bpy.props.FloatProperty(name='Value', description='Set the clipping value of the implicit function (if clipping with implicit function) or scalar value (if clipping with scalars). The default value is 0.0. This value is ignored if UseValueAsOffset is true and a clip function is defined', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateClipScalars', 'm_GenerateClippedOutput', 'm_InsideOut', 'm_MergeTolerance', 'm_UseValueAsOffset', 'm_Value', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], ['ClipFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ClipDataSet)
TYPENAMES.append('BVTK_NT_ClipDataSet' )


# --------------------------------------------------------------


class BVTK_NT_AutoCorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AutoCorrelativeStatistics'
    bl_label = 'vtkAutoCorrelativeStatistics'
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=1)
    m_SliceCardinality = bpy.props.IntProperty(name='SliceCardinality', description='Set/get the cardinality of the data set at given time, i.e., of any given time slice. It cannot be negative. The input data set is assumed to have a cardinality which is a multiple of this value. The default is 0, meaning that the user must specify a value that is consistent with the input data set', default=0)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_DeriveOption', 'm_LearnOption', 'm_NumberOfPrimaryTables', 'm_SliceCardinality', 'm_TestOption', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AutoCorrelativeStatistics)
TYPENAMES.append('BVTK_NT_AutoCorrelativeStatistics' )


# --------------------------------------------------------------


class BVTK_NT_OrderStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_OrderStatistics'
    bl_label = 'vtkOrderStatistics'
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_MaximumHistogramSize = bpy.props.IntProperty(name='MaximumHistogramSize', description='Set/Get the maximum histogram size. This maximum size is enforced only when Quantize is TRUE', default=1000)
    m_NumberOfIntervals = bpy.props.IntProperty(name='NumberOfIntervals', description='Set/Get the number of quantiles (with uniform spacing)', default=4)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=-1)
    m_QuantileDefinition = bpy.props.IntProperty(name='QuantileDefinition', description='Set the quantile definition', default=1)
    m_Quantize = bpy.props.BoolProperty(name='Quantize', description='Set/Get whether quantization will be allowed to enforce maximum histogram size', default=False)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_DeriveOption', 'm_LearnOption', 'm_MaximumHistogramSize', 'm_NumberOfIntervals', 'm_NumberOfPrimaryTables', 'm_QuantileDefinition', 'm_Quantize', 'm_TestOption', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_OrderStatistics)
TYPENAMES.append('BVTK_NT_OrderStatistics' )


# --------------------------------------------------------------


class BVTK_NT_IntersectionPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_IntersectionPolyDataFilter'
    bl_label = 'vtkIntersectionPolyDataFilter'
    
    m_CheckInput = bpy.props.BoolProperty(name='CheckInput', description='If on, the normals of the input will be checked. Default: OF', default=True)
    m_CheckMesh = bpy.props.BoolProperty(name='CheckMesh', description='If on, the output remeshed surfaces will be checked for bad cells and free edges. Default: O', default=True)
    m_ComputeIntersectionPointArray = bpy.props.BoolProperty(name='ComputeIntersectionPointArray', description='If on, the output split surfaces will contain information about which points are on the intersection of the two inputs. Default: O', default=True)
    m_RelativeSubtriangleArea = bpy.props.FloatProperty(name='RelativeSubtriangleArea', description='When discretizing polygons, the minimum ratio of the smallest acceptable triangle area w.r.t. the area of the polygo', default=0.0001)
    m_SplitFirstOutput = bpy.props.BoolProperty(name='SplitFirstOutput', description='If on, the second output will be the first input mesh split by the intersection with the second input mesh. Defaults to on', default=True)
    m_SplitSecondOutput = bpy.props.BoolProperty(name='SplitSecondOutput', description='If on, the third output will be the second input mesh split by the intersection with the first input mesh. Defaults to on', default=True)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='The tolerance for geometric tests in the filte', default=1e-06)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CheckInput', 'm_CheckMesh', 'm_ComputeIntersectionPointArray', 'm_RelativeSubtriangleArea', 'm_SplitFirstOutput', 'm_SplitSecondOutput', 'm_Tolerance', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1', 'Output 2'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_IntersectionPolyDataFilter)
TYPENAMES.append('BVTK_NT_IntersectionPolyDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageConnectivityFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageConnectivityFilter'
    bl_label = 'vtkImageConnectivityFilter'
    e_ExtractionMode_items = [(x, x, x) for x in ['AllRegions', 'LargestRegion', 'SeededRegions']]
    e_LabelMode_items = [(x, x, x) for x in ['ConstantValue', 'SeedScalar', 'SizeRank']]
    e_LabelScalarType_items = [(x, x, x) for x in ['Int', 'Short', 'UnsignedChar', 'UnsignedShort']]
    
    m_ActiveComponent = bpy.props.IntProperty(name='ActiveComponent', description='For multi-component input images, select which component to use', default=0)
    e_ExtractionMode = bpy.props.EnumProperty(name='ExtractionMode', description='Set which regions to output from this filter. This can be all the regions, just the seeded regions, or the largest region (which will the the largest seeded region, if there are seeds). The default is to output all the seeded regions, if there are seeds, or to output all the regions, if there are no seeds', default='SeededRegions', items=e_ExtractionMode_items)
    m_GenerateRegionExtents = bpy.props.BoolProperty(name='GenerateRegionExtents', description='Turn this on to request creation of the ExtractedRegionExtents array', default=True)
    m_LabelConstantValue = bpy.props.IntProperty(name='LabelConstantValue', description='The label used when LabelMode is ConstantValue. The default value is 255', default=255)
    e_LabelMode = bpy.props.EnumProperty(name='LabelMode', description='Set the mode for applying labels to the output. Labeling by SeedScalar uses the scalars from the seeds as labels, if present, or the regions will be labeled consecutively starting at 1, if the seeds have no scalars. Labeling by SizeRank means that the largest region is labeled 1 and other regions are labeled consecutively in order of decreasing size (if there is a tie, then the seed point ID is used as a tiebreaker). Finally, Constant means that all regions will have the value of SetLabelConstantValue(). The default is to label using the seed scalars, if present, or to label consecutively, if no seed scalars are present', default='SeedScalar', items=e_LabelMode_items)
    e_LabelScalarType = bpy.props.EnumProperty(name='LabelScalarType', description='Set the scalar type for the output label image. This should be one of UnsignedChar, Short, UnsignedShort, or Int depending on how many labels are expected. The default is UnsignedChar, which allows for 255 label values. If the total number of regions is greater than the maximum label value N, then only the largest N regions will be kept and the rest will be discarded', default='UnsignedChar', items=e_LabelScalarType_items)
    m_ScalarRange = bpy.props.FloatVectorProperty(name='ScalarRange', description='', default=[0.5, 1e+30], size=2)
    m_SizeRange = bpy.props.IntVectorProperty(name='SizeRange', description='', default=[1, 1000000000], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ActiveComponent', 'e_ExtractionMode', 'm_GenerateRegionExtents', 'm_LabelConstantValue', 'e_LabelMode', 'e_LabelScalarType', 'm_ScalarRange', 'm_SizeRange', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output'], ['SeedConnection', 'StencilConnection'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageConnectivityFilter)
TYPENAMES.append('BVTK_NT_ImageConnectivityFilter' )


# --------------------------------------------------------------


class BVTK_NT_LoopBooleanPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LoopBooleanPolyDataFilter'
    bl_label = 'vtkLoopBooleanPolyDataFilter'
    e_Operation_items = [(x, x, x) for x in ['Difference', 'Intersection', 'Union']]
    
    m_NoIntersectionOutput = bpy.props.BoolProperty(name='NoIntersectionOutput', description='ONLY USED IF NO INTERSECTION BETWEEN SURFACES Variable to determine what is output if no intersection occurs. 0 = neither (default), 1 = first, 2 = second, 3 = bot', default=True)
    e_Operation = bpy.props.EnumProperty(name='Operation', description='Set the boolean operation to perform. Defaults to union', default='Union', items=e_Operation_items)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Set the tolerance for geometric test', default=1e-06)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NoIntersectionOutput', 'e_Operation', 'm_Tolerance', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LoopBooleanPolyDataFilter)
TYPENAMES.append('BVTK_NT_LoopBooleanPolyDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_MergeFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MergeFilter'
    bl_label = 'vtkMergeFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2', 'Input 3', 'Input 4', 'Input 5'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MergeFilter)
TYPENAMES.append('BVTK_NT_MergeFilter' )


# --------------------------------------------------------------


class BVTK_NT_PairwiseExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PairwiseExtractHistogram2D'
    bl_label = 'vtkPairwiseExtractHistogram2D'
    e_ScalarType_items = [(x, x, x) for x in ['UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_NumberOfBins = bpy.props.IntVectorProperty(name='NumberOfBins', description='', default=[0, 0], size=2)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=1)
    e_ScalarType = bpy.props.EnumProperty(name='ScalarType', description='Set the scalar type for each of the computed histograms', default='UnsignedInt', items=e_ScalarType_items)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_DeriveOption', 'm_LearnOption', 'm_NumberOfBins', 'm_NumberOfPrimaryTables', 'e_ScalarType', 'm_TestOption', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2', 'Output 3'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PairwiseExtractHistogram2D)
TYPENAMES.append('BVTK_NT_PairwiseExtractHistogram2D' )


# --------------------------------------------------------------


class BVTK_NT_ComputeHistogram2DOutliers(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ComputeHistogram2DOutliers'
    bl_label = 'vtkComputeHistogram2DOutliers'
    
    m_PreferredNumberOfOutliers = bpy.props.IntProperty(name='PreferredNumberOfOutliers', description='', default=10)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PreferredNumberOfOutliers', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ComputeHistogram2DOutliers)
TYPENAMES.append('BVTK_NT_ComputeHistogram2DOutliers' )


# --------------------------------------------------------------


class BVTK_NT_ClipPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ClipPolyData'
    bl_label = 'vtkClipPolyData'
    
    m_GenerateClipScalars = bpy.props.BoolProperty(name='GenerateClipScalars', description='If this flag is enabled, then the output scalar values will be interpolated from the implicit function values, and not the input scalar data. If you enable this flag but do not provide an implicit function an error will be reported. GenerateClipScalars is off by default', default=True)
    m_GenerateClippedOutput = bpy.props.BoolProperty(name='GenerateClippedOutput', description="Control whether a second output is generated. The second output contains the polygonal data that's been clipped away. GenerateClippedOutput is off by default", default=True)
    m_InsideOut = bpy.props.BoolProperty(name='InsideOut', description='Set/Get the InsideOut flag. When off, a vertex is considered inside the implicit function if its value is greater than the Value ivar. When InsideOutside is turned on, a vertex is considered inside the implicit function if its implicit function value is less than or equal to the Value ivar. InsideOut is off by default', default=True)
    m_Value = bpy.props.FloatProperty(name='Value', description='Set the clipping value of the implicit function (if clipping with implicit function) or scalar value (if clipping with scalars). The default value is 0.0', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateClipScalars', 'm_GenerateClippedOutput', 'm_InsideOut', 'm_Value', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], ['ClipFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ClipPolyData)
TYPENAMES.append('BVTK_NT_ClipPolyData' )


# --------------------------------------------------------------


class BVTK_NT_BandedPolyDataContourFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BandedPolyDataContourFilter'
    bl_label = 'vtkBandedPolyDataContourFilter'
    e_ScalarMode_items = [(x, x, x) for x in ['Index', 'Value']]
    
    m_ClipTolerance = bpy.props.FloatProperty(name='ClipTolerance', description='Set/Get the clip tolerance. Warning: setting this too large will certainly cause numerical issues. Change from the default value of FLT_EPSILON at your own risk. The actual internal clip tolerance is computed by multiplying ClipTolerance by the scalar range', default=1.1920928955078125e-07)
    m_Clipping = bpy.props.BoolProperty(name='Clipping', description='Indicate whether to clip outside the range specified by the user. (The range is contour value[0] to contour value[numContours-1].) Clipping means all cells outside of the range specified are not sent to the output', default=True)
    m_Component = bpy.props.IntProperty(name='Component', description='Set/Get the component to use of an input scalars array with more than one component. Default is 0', default=0)
    m_GenerateContourEdges = bpy.props.BoolProperty(name='GenerateContourEdges', description='Turn on/off a flag to control whether contour edges are generated. Contour edges are the edges between bands. If enabled, they are generated from polygons/triangle strips and placed into the second output (the ContourEdgesOutput)', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Methods to set / get contour values. A single value at a time can be set with SetValue(). Multiple contour values can be set with GenerateValues(). Note that GenerateValues() generates n values inclusive of the start and end range values', default=1)
    e_ScalarMode = bpy.props.EnumProperty(name='ScalarMode', description='Control whether the cell scalars are output as an integer index or a scalar value. If an index, the index refers to the bands produced by the clipping range. If a value, then a scalar value which is a value between clip values is used', default='Index', items=e_ScalarMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClipTolerance', 'm_Clipping', 'm_Component', 'm_GenerateContourEdges', 'm_NumberOfContours', 'e_ScalarMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BandedPolyDataContourFilter)
TYPENAMES.append('BVTK_NT_BandedPolyDataContourFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImagePermute(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImagePermute'
    bl_label = 'vtkImagePermute'
    e_InterpolationMode_items = [(x, x, x) for x in ['Cubic', 'Linear', 'NearestNeighbor']]
    e_OutputExtent_items = [(x, x, x) for x in ['Default']]
    e_OutputOrigin_items = [(x, x, x) for x in ['Default']]
    e_OutputSpacing_items = [(x, x, x) for x in ['Default']]
    e_SlabMode_items = [(x, x, x) for x in ['Max', 'Mean', 'Min', 'Sum']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_AutoCropOutput = bpy.props.BoolProperty(name='AutoCropOutput', description='Turn this on if you want to guarantee that the extent of the output will be large enough to ensure that none of the data will be cropped (default: Off)', default=True)
    m_BackgroundColor = bpy.props.FloatVectorProperty(name='BackgroundColor', description='', default=[0.0, 0.0, 0.0, 0.0], size=4)
    m_BackgroundLevel = bpy.props.FloatProperty(name='BackgroundLevel', description='Set background grey level (for single-component images)', default=0.0)
    m_Border = bpy.props.BoolProperty(name='Border', description="Extend the apparent input border by a half voxel (default: On). This changes how interpolation is handled at the borders of the input image: if the center of an output voxel is beyond the edge of the input image, but is within a half voxel width of the edge (using the input voxel width), then the value of the output voxel is calculated as if the input's edge voxels were duplicated past the edges of the input. This has no effect if Mirror or Wrap are on", default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_FilteredAxes = bpy.props.IntVectorProperty(name='FilteredAxes', description='The filtered axes are the input axes that get relabeled to X,Y,Z', default=[0, 1, 2], size=3)
    m_GenerateStencilOutput = bpy.props.BoolProperty(name='GenerateStencilOutput', description='Generate an output stencil that defines which pixels were interpolated and which pixels were out-of-bounds of the input', default=True)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Interpolate = bpy.props.BoolProperty(name='Interpolate', description='Convenient methods for switching between nearest-neighbor and linear interpolation. InterpolateOn() is equivalent to SetInterpolationModeToLinear() and InterpolateOff() is equivalent to SetInterpolationModeToNearestNeighbor() You should not use these methods if you use the SetInterpolationMode methods', default=True)
    e_InterpolationMode = bpy.props.EnumProperty(name='InterpolationMode', description='Set interpolation mode (default: nearest neighbor)', default='NearestNeighbor', items=e_InterpolationMode_items)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_Mirror = bpy.props.BoolProperty(name='Mirror', description='Turn on mirror-pad feature (default: Off). This will override the wrap-pad', default=True)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_Optimization = bpy.props.BoolProperty(name='Optimization', description='Turn on and off optimizations (default on, they should only be turned off for testing purposes)', default=True)
    m_OutputDimensionality = bpy.props.IntProperty(name='OutputDimensionality', description='Force the dimensionality of the output to either 1, 2, 3 or 0 (default: 3). If the dimensionality is 2D, then the Z extent of the output is forced to (0,0) and the Z origin of the output is forced to 0.0 (i.e. the output extent is confined to the xy plane). If the dimensionality is 1D, the output extent is confined to the x axis. For 0D, the output extent consists of a single voxel at (0,0,0)', default=3)
    e_OutputExtent = bpy.props.EnumProperty(name='OutputExtent', description='Set the extent for the output data. The default output extent is the input extent permuted through the ResliceAxes', default='Default', items=e_OutputExtent_items)
    e_OutputOrigin = bpy.props.EnumProperty(name='OutputOrigin', description='Set the origin for the output data. The default output origin is the input origin permuted through the ResliceAxes', default='Default', items=e_OutputOrigin_items)
    m_OutputScalarType = bpy.props.IntProperty(name='OutputScalarType', description='Set the scalar type of the output to be different from the input. The default value is -1, which means that the input scalar type will be used to set the output scalar type. Otherwise, this must be set to one of the following types: VTK_CHAR, VTK_SIGNED_CHAR, VTK_UNSIGNED_CHAR, VTK_SHORT, VTK_UNSIGNED_SHORT, VTK_INT, VTK_UNSIGNED_INT, VTK_FLOAT, or VTK_DOUBLE. Other types are not permitted. If the output type is an integer type, the output will be rounded and clamped to the limits of the type', default=-1)
    e_OutputSpacing = bpy.props.EnumProperty(name='OutputSpacing', description='Set the voxel spacing for the output data. The default output spacing is the input spacing permuted through the ResliceAxes', default='Default', items=e_OutputSpacing_items)
    m_ResliceAxesDirectionCosines = bpy.props.FloatVectorProperty(name='ResliceAxesDirectionCosines', description='Specify the direction cosines for the ResliceAxes (i.e. the first three elements of each of the first three columns of the ResliceAxes matrix). This will modify the current ResliceAxes matrix, or create a new matrix if none exists', default=[1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], size=9)
    m_ResliceAxesOrigin = bpy.props.FloatVectorProperty(name='ResliceAxesOrigin', description='Specify the origin for the ResliceAxes (i.e. the first three elements of the final column of the ResliceAxes matrix). This will modify the current ResliceAxes matrix, or create new matrix if none exists', default=[0.0, 0.0, 0.0], size=3)
    m_ScalarScale = bpy.props.FloatProperty(name='ScalarScale', description='Set multiplication factor to apply to all the output voxels. After a sample value has been interpolated from the input image, the equation u = (v + ScalarShift)*ScalarScale will be applied to it before it is written to the output image. The result will always be clamped to the limits of the output data type', default=1.0)
    m_ScalarShift = bpy.props.FloatProperty(name='ScalarShift', description='Set a value to add to all the output voxels. After a sample value has been interpolated from the input image, the equation u = (v + ScalarShift)*ScalarScale will be applied to it before it is written to the output image. The result will always be clamped to the limits of the output data type', default=0.0)
    e_SlabMode = bpy.props.EnumProperty(name='SlabMode', description='Set the slab mode, for generating thick slices. The default is Mean. If SetSlabNumberOfSlices(N) is called with N greater than one, then each output slice will actually be a composite of N slices. This method specifies the compositing mode to be used', default='Mean', items=e_SlabMode_items)
    m_SlabNumberOfSlices = bpy.props.IntProperty(name='SlabNumberOfSlices', description='Set the number of slices that will be combined to create the slab', default=1)
    m_SlabSliceSpacingFraction = bpy.props.FloatProperty(name='SlabSliceSpacingFraction', description='The slab spacing as a fraction of the output slice spacing. When one of the various slab modes is chosen, each output slice is produced by generating several "temporary" output slices and then combining them according to the slab mode. By default, the spacing between these temporary slices is the Z component of the OutputSpacing. This method sets the spacing between these temporary slices to be a fraction of the output spacing', default=1.0)
    m_SlabTrapezoidIntegration = bpy.props.BoolProperty(name='SlabTrapezoidIntegration', description='Use trapezoid integration for slab computation. All this does is weigh the first and last slices by half when doing sum and mean. It is off by default', default=True)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_TransformInputSampling = bpy.props.BoolProperty(name='TransformInputSampling', description='Specify whether to transform the spacing, origin and extent of the Input (or the InformationInput) according to the direction cosines and origin of the ResliceAxes before applying them as the default output spacing, origin and extent (default: On)', default=True)
    m_Wrap = bpy.props.BoolProperty(name='Wrap', description='Turn on wrap-pad feature (default: Off)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=31, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutoCropOutput', 'm_BackgroundColor', 'm_BackgroundLevel', 'm_Border', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_FilteredAxes', 'm_GenerateStencilOutput', 'm_GlobalDefaultEnableSMP', 'm_Interpolate', 'e_InterpolationMode', 'm_MinimumPieceSize', 'm_Mirror', 'm_NumberOfThreads', 'm_Optimization', 'm_OutputDimensionality', 'e_OutputExtent', 'e_OutputOrigin', 'm_OutputScalarType', 'e_OutputSpacing', 'm_ResliceAxesDirectionCosines', 'm_ResliceAxesOrigin', 'm_ScalarScale', 'm_ScalarShift', 'e_SlabMode', 'm_SlabNumberOfSlices', 'm_SlabSliceSpacingFraction', 'm_SlabTrapezoidIntegration', 'e_SplitMode', 'm_TransformInputSampling', 'm_Wrap', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1'], ['Interpolator', 'ResliceAxes', 'ResliceTransform', 'StencilOutput'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImagePermute)
TYPENAMES.append('BVTK_NT_ImagePermute' )


# --------------------------------------------------------------


class BVTK_NT_PComputeHistogram2DOutliers(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PComputeHistogram2DOutliers'
    bl_label = 'vtkPComputeHistogram2DOutliers'
    
    m_PreferredNumberOfOutliers = bpy.props.IntProperty(name='PreferredNumberOfOutliers', description='', default=10)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PreferredNumberOfOutliers', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PComputeHistogram2DOutliers)
TYPENAMES.append('BVTK_NT_PComputeHistogram2DOutliers' )


# --------------------------------------------------------------


class BVTK_NT_RadiusOutlierRemoval(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RadiusOutlierRemoval'
    bl_label = 'vtkRadiusOutlierRemoval'
    
    m_GenerateOutliers = bpy.props.BoolProperty(name='GenerateOutliers', description='If this method is enabled (true), then a second output will be created that contains the outlier points. By default this is off (false). Note that if enabled, the PointMap is modified as well: the outlier points are listed as well, with similar meaning, except their value is negated and shifted by -1', default=False)
    m_GenerateVertices = bpy.props.BoolProperty(name='GenerateVertices', description='If this method is enabled (true), then the outputs will contain a vertex cells (i.e., a vtkPolyVertex for each output). This takes a lot more memory but some VTK filters need cells to function properly. By default this is off (false)', default=False)
    m_NumberOfNeighbors = bpy.props.IntProperty(name='NumberOfNeighbors', description='Specify the number of neighbors that a point must have, within the specified radius, for the point to not be considered isolated', default=2)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Specify the local search radius', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateOutliers', 'm_GenerateVertices', 'm_NumberOfNeighbors', 'm_Radius', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RadiusOutlierRemoval)
TYPENAMES.append('BVTK_NT_RadiusOutlierRemoval' )


# --------------------------------------------------------------


class BVTK_NT_GenericClip(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GenericClip'
    bl_label = 'vtkGenericClip'
    
    m_GenerateClipScalars = bpy.props.BoolProperty(name='GenerateClipScalars', description='If this flag is enabled, then the output scalar values will be interpolated from the implicit function values, and not the input scalar data. If you enable this flag but do not provide an implicit function an error will be reported', default=True)
    m_GenerateClippedOutput = bpy.props.BoolProperty(name='GenerateClippedOutput', description="Control whether a second output is generated. The second output contains the polygonal data that's been clipped away", default=True)
    m_InsideOut = bpy.props.BoolProperty(name='InsideOut', description='Set/Get the InsideOut flag. When off, a vertex is considered inside the implicit function if its value is greater than the Value ivar. When InsideOutside is turned on, a vertex is considered inside the implicit function if its implicit function value is less than or equal to the Value ivar. InsideOut is off by default', default=True)
    m_MergeTolerance = bpy.props.FloatProperty(name='MergeTolerance', description='Set the tolerance for merging clip intersection points that are near the vertices of cells. This tolerance is used to prevent the generation of degenerate primitives. Note that only 3D cells actually use this instance variable', default=0.01)
    m_Value = bpy.props.FloatProperty(name='Value', description='Set the clipping value of the implicit function (if clipping with implicit function) or scalar value (if clipping with scalars). The default value is 0.0', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateClipScalars', 'm_GenerateClippedOutput', 'm_InsideOut', 'm_MergeTolerance', 'm_Value', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], ['ClipFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GenericClip)
TYPENAMES.append('BVTK_NT_GenericClip' )


# --------------------------------------------------------------


class BVTK_NT_ExtractPoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractPoints'
    bl_label = 'vtkExtractPoints'
    
    m_ExtractInside = bpy.props.BoolProperty(name='ExtractInside', description='Boolean controls whether to extract points that are inside of implicit function (ExtractInside == true) or outside of implicit function (ExtractInside == false). By default, ExtractInside is true', default=True)
    m_GenerateOutliers = bpy.props.BoolProperty(name='GenerateOutliers', description='If this method is enabled (true), then a second output will be created that contains the outlier points. By default this is off (false). Note that if enabled, the PointMap is modified as well: the outlier points are listed as well, with similar meaning, except their value is negated and shifted by -1', default=False)
    m_GenerateVertices = bpy.props.BoolProperty(name='GenerateVertices', description='If this method is enabled (true), then the outputs will contain a vertex cells (i.e., a vtkPolyVertex for each output). This takes a lot more memory but some VTK filters need cells to function properly. By default this is off (false)', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ExtractInside', 'm_GenerateOutliers', 'm_GenerateVertices', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], ['ImplicitFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractPoints)
TYPENAMES.append('BVTK_NT_ExtractPoints' )


# --------------------------------------------------------------


class BVTK_NT_BivariateLinearTableThreshold(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BivariateLinearTableThreshold'
    bl_label = 'vtkBivariateLinearTableThreshold'
    e_LinearThresholdType_items = [(x, x, x) for x in ['Above', 'Below', 'Between', 'Near']]
    
    m_ColumnRanges = bpy.props.FloatVectorProperty(name='ColumnRanges', description='', default=[1.0, 1.0], size=2)
    m_DistanceThreshold = bpy.props.FloatProperty(name='DistanceThreshold', description='The Cartesian distance within which a point will pass the near threshold', default=1.0)
    m_Inclusive = bpy.props.IntProperty(name='Inclusive', description='Include the line in the threshold. Essentially whether the threshold operation uses > versus >=', default=0)
    e_LinearThresholdType = bpy.props.EnumProperty(name='LinearThresholdType', description='Set the threshold type. Above: find all rows that are above the specified lines. Below: find all rows that are below the specified lines. Near: find all rows that are near the specified lines. Between: find all rows that are between the specified lines', default='Near', items=e_LinearThresholdType_items)
    m_UseNormalizedDistance = bpy.props.BoolProperty(name='UseNormalizedDistance', description='Renormalize the space of the data such that the X and Y axes are "square" over the specified ColumnRanges. This essentially scales the data space so that ColumnRanges[1]-ColumnRanges[0] = 1.0 and ColumnRanges[3]-ColumnRanges[2] = 1.0. Used for scatter plot distance calculations. Be sure to set DistanceThreshold accordingly, when used', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ColumnRanges', 'm_DistanceThreshold', 'm_Inclusive', 'e_LinearThresholdType', 'm_UseNormalizedDistance', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BivariateLinearTableThreshold)
TYPENAMES.append('BVTK_NT_BivariateLinearTableThreshold' )


# --------------------------------------------------------------


class BVTK_NT_BooleanOperationPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BooleanOperationPolyDataFilter'
    bl_label = 'vtkBooleanOperationPolyDataFilter'
    e_Operation_items = [(x, x, x) for x in ['Difference', 'Intersection', 'Union']]
    
    e_Operation = bpy.props.EnumProperty(name='Operation', description='Set the boolean operation to perform. Defaults to union', default='Union', items=e_Operation_items)
    m_ReorientDifferenceCells = bpy.props.BoolProperty(name='ReorientDifferenceCells', description='Turn on/off cell reorientation of the intersection portion of the surface when the operation is set to DIFFERENCE. Defaults to on', default=True)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description="Set/get the tolerance used to determine when a point's absolute distance is considered to be zero. Defaults to 1e-6", default=1e-06)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_Operation', 'm_ReorientDifferenceCells', 'm_Tolerance', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BooleanOperationPolyDataFilter)
TYPENAMES.append('BVTK_NT_BooleanOperationPolyDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageStencil(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageStencil'
    bl_label = 'vtkImageStencil'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_BackgroundColor = bpy.props.FloatVectorProperty(name='BackgroundColor', description='', default=[1.0, 1.0, 1.0, 1.0], size=4)
    m_BackgroundValue = bpy.props.FloatProperty(name='BackgroundValue', description='Set the default output value to use when the second input is not set', default=1.0)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_ReverseStencil = bpy.props.BoolProperty(name='ReverseStencil', description='Reverse the stencil', default=True)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BackgroundColor', 'm_BackgroundValue', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_ReverseStencil', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageStencil)
TYPENAMES.append('BVTK_NT_ImageStencil' )


# --------------------------------------------------------------


class BVTK_NT_LagrangianParticleTracker(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LagrangianParticleTracker'
    bl_label = 'vtkLagrangianParticleTracker'
    
    m_AdaptiveStepReintegration = bpy.props.BoolProperty(name='AdaptiveStepReintegration', description='Set/Get the Adaptive Step Reintegration feature. it checks the step size after the integration and if it is too big will retry with a smaller ste', default=False)
    m_CellLengthComputationMode = bpy.props.IntProperty(name='CellLengthComputationMode', description='Set/Get the cell length computation mode. Available modes are : - STEP_LAST_CELL_LENGTH : Compute cell length using getLength method on the last cell the particle was in - STEP_CUR_CELL_LENGTH : Compute cell length using getLength method on the current cell the particle is in - STEP_LAST_CELL_VEL_DIR : Compute cell length using the particle velocity and the edges of the last cell the particle was in. - STEP_CUR_CELL_VEL_DIR : Compute cell length using the particle velocity and the edges of the last cell the particle was in. - STEP_LAST_CELL_DIV_THEO : Compute cell length using the particle velocity and the divergence theorem, not supported with vtkVoxel, fallback to STEP_LAST_CELL_LENGTH - STEP_CUR_CELL_DIV_THEO : Compute cell length using the particle velocity and the divergence theorem, not supported with vtkVoxel, fallback to STEP_CUR_CELL_LENGT', default=0)
    m_CreateOutOfDomainParticle = bpy.props.BoolProperty(name='CreateOutOfDomainParticle', description='Set/Get the Creation of particle initially outside of the domai', default=False)
    m_MaximumNumberOfSteps = bpy.props.IntProperty(name='MaximumNumberOfSteps', description='Set/Get the maximum number of steps', default=100)
    m_ParticlePathsRenderingPointsThreshold = bpy.props.IntProperty(name='ParticlePathsRenderingPointsThreshold', description='Set/Get the Optional Paths Rendering featur', default=100)
    m_StepFactor = bpy.props.FloatProperty(name='StepFactor', description='Set/Get the integration step factor', default=1.0)
    m_StepFactorMax = bpy.props.FloatProperty(name='StepFactorMax', description='Set/Get the integration step factor max', default=1.5)
    m_StepFactorMin = bpy.props.FloatProperty(name='StepFactorMin', description='Set/Get the integration step factor min', default=0.5)
    m_UseParticlePathsRenderingThreshold = bpy.props.BoolProperty(name='UseParticlePathsRenderingThreshold', description='Set/Get the Optional Paths Rendering featur', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AdaptiveStepReintegration', 'm_CellLengthComputationMode', 'm_CreateOutOfDomainParticle', 'm_MaximumNumberOfSteps', 'm_ParticlePathsRenderingPointsThreshold', 'm_StepFactor', 'm_StepFactorMax', 'm_StepFactorMin', 'm_UseParticlePathsRenderingThreshold', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1'], ['IntegrationModel', 'Integrator'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LagrangianParticleTracker)
TYPENAMES.append('BVTK_NT_LagrangianParticleTracker' )


# --------------------------------------------------------------


class BVTK_NT_DescriptiveStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DescriptiveStatistics'
    bl_label = 'vtkDescriptiveStatistics'
    
    m_AssessOption = bpy.props.BoolProperty(name='AssessOption', description='Set/Get the Assess operation', default=False)
    m_DeriveOption = bpy.props.BoolProperty(name='DeriveOption', description='Set/Get the Derive operation', default=True)
    m_G1Skewness = bpy.props.BoolProperty(name='G1Skewness', description='Set/get whether the G1 estimator for the skewness should be used, or if the g1 skewness will be calculated. The default is that the g1 skewness estimator will be used', default=True)
    m_G2Kurtosis = bpy.props.BoolProperty(name='G2Kurtosis', description='Set/get whether the G2 estimator for the kurtosis should be used, or if the g2 kurtosis will be calculated. The default is that the g2 kurtosis estimator will be used', default=True)
    m_LearnOption = bpy.props.BoolProperty(name='LearnOption', description='Set/Get the Learn operation', default=True)
    m_NumberOfPrimaryTables = bpy.props.IntProperty(name='NumberOfPrimaryTables', description='Set/Get the number of tables in the primary model', default=1)
    m_SignedDeviations = bpy.props.BoolProperty(name='SignedDeviations', description='Set/get whether the deviations returned should be signed, or should only have their magnitude reported. The default is that signed deviations will be computed', default=True)
    m_TestOption = bpy.props.BoolProperty(name='TestOption', description='Set/Get the Test operation', default=False)
    m_UnbiasedVariance = bpy.props.BoolProperty(name='UnbiasedVariance', description='Set/get whether the unbiased estimator for the variance should be used, or if the population variance will be calculated. The default is that the unbiased estimator will be used', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AssessOption', 'm_DeriveOption', 'm_G1Skewness', 'm_G2Kurtosis', 'm_LearnOption', 'm_NumberOfPrimaryTables', 'm_SignedDeviations', 'm_TestOption', 'm_UnbiasedVariance', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1', 'Input 2'], ['Output 0', 'Output 1', 'Output 2'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DescriptiveStatistics)
TYPENAMES.append('BVTK_NT_DescriptiveStatistics' )


# --------------------------------------------------------------


class BVTK_NT_AnnotationLink(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AnnotationLink'
    bl_label = 'vtkAnnotationLink'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1', 'Output 2'], ['AnnotationLayers', 'CurrentSelection'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AnnotationLink)
TYPENAMES.append('BVTK_NT_AnnotationLink' )


# --------------------------------------------------------------


class BVTK_NT_ExtractHierarchicalBins(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractHierarchicalBins'
    bl_label = 'vtkExtractHierarchicalBins'
    
    m_Bin = bpy.props.IntProperty(name='Bin', description='Specify the bin number to extract. If a non-negative value, then the points from the bin number specified are extracted. If negative, then entire levels of points are extacted (assuming the Level is non-negative). Note that the bin tree is flattened, a particular bin number may refer to a bin on any level', default=-1)
    m_GenerateOutliers = bpy.props.BoolProperty(name='GenerateOutliers', description='If this method is enabled (true), then a second output will be created that contains the outlier points. By default this is off (false). Note that if enabled, the PointMap is modified as well: the outlier points are listed as well, with similar meaning, except their value is negated and shifted by -1', default=False)
    m_GenerateVertices = bpy.props.BoolProperty(name='GenerateVertices', description='If this method is enabled (true), then the outputs will contain a vertex cells (i.e., a vtkPolyVertex for each output). This takes a lot more memory but some VTK filters need cells to function properly. By default this is off (false)', default=False)
    m_Level = bpy.props.IntProperty(name='Level', description='Specify the level to extract. If non-negative, with a negative bin number, then all points at this level are extracted and sent to the output. If negative, then the points from the specified bin are sent to the output. If both the level and bin number are negative values, then the input is sent to the output. By default the 0th level is extracted', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Bin', 'm_GenerateOutliers', 'm_GenerateVertices', 'm_Level', ]
    
    def m_connections(self):
        return ['Input'], ['Output 0', 'Output 1'], ['BinningFilter'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractHierarchicalBins)
TYPENAMES.append('BVTK_NT_ExtractHierarchicalBins' )


# --------------------------------------------------------------


class BVTK_NT_MaskPointsFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MaskPointsFilter'
    bl_label = 'vtkMaskPointsFilter'
    
    m_EmptyValue = bpy.props.IntProperty(name='EmptyValue', description='Set / get the values indicating whether a voxel is empty. By default, an empty voxel is marked with a zero value. Any point inside a voxel marked empty is not selected for output. All other voxels with a value that is not equal to the empty value are selected for output', default=0)
    m_GenerateOutliers = bpy.props.BoolProperty(name='GenerateOutliers', description='If this method is enabled (true), then a second output will be created that contains the outlier points. By default this is off (false). Note that if enabled, the PointMap is modified as well: the outlier points are listed as well, with similar meaning, except their value is negated and shifted by -1', default=False)
    m_GenerateVertices = bpy.props.BoolProperty(name='GenerateVertices', description='If this method is enabled (true), then the outputs will contain a vertex cells (i.e., a vtkPolyVertex for each output). This takes a lot more memory but some VTK filters need cells to function properly. By default this is off (false)', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_EmptyValue', 'm_GenerateOutliers', 'm_GenerateVertices', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MaskPointsFilter)
TYPENAMES.append('BVTK_NT_MaskPointsFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageResample(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageResample'
    bl_label = 'vtkImageResample'
    e_InterpolationMode_items = [(x, x, x) for x in ['Cubic', 'Linear', 'NearestNeighbor']]
    e_OutputExtent_items = [(x, x, x) for x in ['Default']]
    e_OutputOrigin_items = [(x, x, x) for x in ['Default']]
    e_OutputSpacing_items = [(x, x, x) for x in ['Default']]
    e_SlabMode_items = [(x, x, x) for x in ['Max', 'Mean', 'Min', 'Sum']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_AutoCropOutput = bpy.props.BoolProperty(name='AutoCropOutput', description='Turn this on if you want to guarantee that the extent of the output will be large enough to ensure that none of the data will be cropped (default: Off)', default=True)
    m_BackgroundColor = bpy.props.FloatVectorProperty(name='BackgroundColor', description='', default=[0.0, 0.0, 0.0, 0.0], size=4)
    m_BackgroundLevel = bpy.props.FloatProperty(name='BackgroundLevel', description='Set background grey level (for single-component images)', default=0.0)
    m_Border = bpy.props.BoolProperty(name='Border', description="Extend the apparent input border by a half voxel (default: On). This changes how interpolation is handled at the borders of the input image: if the center of an output voxel is beyond the edge of the input image, but is within a half voxel width of the edge (using the input voxel width), then the value of the output voxel is calculated as if the input's edge voxels were duplicated past the edges of the input. This has no effect if Mirror or Wrap are on", default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Dimensionality is the number of axes which are considered during execution. To process images dimensionality would be set to 2. This has the same effect as setting the magnification of the third axis to 1.', default=3)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GenerateStencilOutput = bpy.props.BoolProperty(name='GenerateStencilOutput', description='Generate an output stencil that defines which pixels were interpolated and which pixels were out-of-bounds of the input', default=True)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Interpolate = bpy.props.BoolProperty(name='Interpolate', description='Convenient methods for switching between nearest-neighbor and linear interpolation. InterpolateOn() is equivalent to SetInterpolationModeToLinear() and InterpolateOff() is equivalent to SetInterpolationModeToNearestNeighbor() You should not use these methods if you use the SetInterpolationMode methods', default=True)
    e_InterpolationMode = bpy.props.EnumProperty(name='InterpolationMode', description='Set interpolation mode (default: nearest neighbor)', default='Linear', items=e_InterpolationMode_items)
    m_MagnificationFactors = bpy.props.FloatVectorProperty(name='MagnificationFactors', description='Set/Get Magnification factors. Zero is a reserved value indicating values have not been computed', default=[1.0, 1.0, 1.0], size=3)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_Mirror = bpy.props.BoolProperty(name='Mirror', description='Turn on mirror-pad feature (default: Off). This will override the wrap-pad', default=True)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_Optimization = bpy.props.BoolProperty(name='Optimization', description='Turn on and off optimizations (default on, they should only be turned off for testing purposes)', default=True)
    m_OutputDimensionality = bpy.props.IntProperty(name='OutputDimensionality', description='Force the dimensionality of the output to either 1, 2, 3 or 0 (default: 3). If the dimensionality is 2D, then the Z extent of the output is forced to (0,0) and the Z origin of the output is forced to 0.0 (i.e. the output extent is confined to the xy plane). If the dimensionality is 1D, the output extent is confined to the x axis. For 0D, the output extent consists of a single voxel at (0,0,0)', default=3)
    e_OutputExtent = bpy.props.EnumProperty(name='OutputExtent', description='Set the extent for the output data. The default output extent is the input extent permuted through the ResliceAxes', default='Default', items=e_OutputExtent_items)
    e_OutputOrigin = bpy.props.EnumProperty(name='OutputOrigin', description='Set the origin for the output data. The default output origin is the input origin permuted through the ResliceAxes', default='Default', items=e_OutputOrigin_items)
    m_OutputScalarType = bpy.props.IntProperty(name='OutputScalarType', description='Set the scalar type of the output to be different from the input. The default value is -1, which means that the input scalar type will be used to set the output scalar type. Otherwise, this must be set to one of the following types: VTK_CHAR, VTK_SIGNED_CHAR, VTK_UNSIGNED_CHAR, VTK_SHORT, VTK_UNSIGNED_SHORT, VTK_INT, VTK_UNSIGNED_INT, VTK_FLOAT, or VTK_DOUBLE. Other types are not permitted. If the output type is an integer type, the output will be rounded and clamped to the limits of the type', default=-1)
    e_OutputSpacing = bpy.props.EnumProperty(name='OutputSpacing', description='Set desired spacing. Zero is a reserved value indicating spacing has not been set', default='Default', items=e_OutputSpacing_items)
    m_ResliceAxesDirectionCosines = bpy.props.FloatVectorProperty(name='ResliceAxesDirectionCosines', description='Specify the direction cosines for the ResliceAxes (i.e. the first three elements of each of the first three columns of the ResliceAxes matrix). This will modify the current ResliceAxes matrix, or create a new matrix if none exists', default=[1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], size=9)
    m_ResliceAxesOrigin = bpy.props.FloatVectorProperty(name='ResliceAxesOrigin', description='Specify the origin for the ResliceAxes (i.e. the first three elements of the final column of the ResliceAxes matrix). This will modify the current ResliceAxes matrix, or create new matrix if none exists', default=[0.0, 0.0, 0.0], size=3)
    m_ScalarScale = bpy.props.FloatProperty(name='ScalarScale', description='Set multiplication factor to apply to all the output voxels. After a sample value has been interpolated from the input image, the equation u = (v + ScalarShift)*ScalarScale will be applied to it before it is written to the output image. The result will always be clamped to the limits of the output data type', default=1.0)
    m_ScalarShift = bpy.props.FloatProperty(name='ScalarShift', description='Set a value to add to all the output voxels. After a sample value has been interpolated from the input image, the equation u = (v + ScalarShift)*ScalarScale will be applied to it before it is written to the output image. The result will always be clamped to the limits of the output data type', default=0.0)
    e_SlabMode = bpy.props.EnumProperty(name='SlabMode', description='Set the slab mode, for generating thick slices. The default is Mean. If SetSlabNumberOfSlices(N) is called with N greater than one, then each output slice will actually be a composite of N slices. This method specifies the compositing mode to be used', default='Mean', items=e_SlabMode_items)
    m_SlabNumberOfSlices = bpy.props.IntProperty(name='SlabNumberOfSlices', description='Set the number of slices that will be combined to create the slab', default=1)
    m_SlabSliceSpacingFraction = bpy.props.FloatProperty(name='SlabSliceSpacingFraction', description='The slab spacing as a fraction of the output slice spacing. When one of the various slab modes is chosen, each output slice is produced by generating several "temporary" output slices and then combining them according to the slab mode. By default, the spacing between these temporary slices is the Z component of the OutputSpacing. This method sets the spacing between these temporary slices to be a fraction of the output spacing', default=1.0)
    m_SlabTrapezoidIntegration = bpy.props.BoolProperty(name='SlabTrapezoidIntegration', description='Use trapezoid integration for slab computation. All this does is weigh the first and last slices by half when doing sum and mean. It is off by default', default=True)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_TransformInputSampling = bpy.props.BoolProperty(name='TransformInputSampling', description='Specify whether to transform the spacing, origin and extent of the Input (or the InformationInput) according to the direction cosines and origin of the ResliceAxes before applying them as the default output spacing, origin and extent (default: On)', default=True)
    m_Wrap = bpy.props.BoolProperty(name='Wrap', description='Turn on wrap-pad feature (default: Off)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=32, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutoCropOutput', 'm_BackgroundColor', 'm_BackgroundLevel', 'm_Border', 'm_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GenerateStencilOutput', 'm_GlobalDefaultEnableSMP', 'm_Interpolate', 'e_InterpolationMode', 'm_MagnificationFactors', 'm_MinimumPieceSize', 'm_Mirror', 'm_NumberOfThreads', 'm_Optimization', 'm_OutputDimensionality', 'e_OutputExtent', 'e_OutputOrigin', 'm_OutputScalarType', 'e_OutputSpacing', 'm_ResliceAxesDirectionCosines', 'm_ResliceAxesOrigin', 'm_ScalarScale', 'm_ScalarShift', 'e_SlabMode', 'm_SlabNumberOfSlices', 'm_SlabSliceSpacingFraction', 'm_SlabTrapezoidIntegration', 'e_SplitMode', 'm_TransformInputSampling', 'm_Wrap', ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], ['Output 0', 'Output 1'], ['Interpolator', 'ResliceAxes', 'ResliceTransform', 'StencilOutput'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageResample)
TYPENAMES.append('BVTK_NT_ImageResample' )


# --------------------------------------------------------------


menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append(BVTK_NodeCategory('VTKFilter', 'Filter', items=menu_items))