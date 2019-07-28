from .core import *
TYPENAMES = []


# --------------------------------------------------------------


class BVTK_NT_StructuredGridOutlineFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StructuredGridOutlineFilter'
    bl_label = 'vtkStructuredGridOutlineFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StructuredGridOutlineFilter)
TYPENAMES.append('BVTK_NT_StructuredGridOutlineFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageContinuousDilate3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageContinuousDilate3D'
    bl_label = 'vtkImageContinuousDilate3D'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageContinuousDilate3D)
TYPENAMES.append('BVTK_NT_ImageContinuousDilate3D' )


# --------------------------------------------------------------


class BVTK_NT_ImageShiftScale(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageShiftScale'
    bl_label = 'vtkImageShiftScale'
    e_OutputScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Long', 'Short', 'UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_ClampOverflow = bpy.props.BoolProperty(name='ClampOverflow', description='When the ClampOverflow flag is on, the data is thresholded so that the output value does not exceed the max or min of the data type. Clamping is safer because otherwise you might invoke undefined behavior (and may crash) if the type conversion is out of range of the data type. On the other hand, clamping is slower. By default, ClampOverflow is off', default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_OutputScalarType = bpy.props.EnumProperty(name='OutputScalarType', description='Set the desired output scalar type. The result of the shift and scale operations is cast to the type specified', items=e_OutputScalarType_items)
    m_Scale = bpy.props.FloatProperty(name='Scale', description='Set/Get the scale value. Each pixel is multiplied by this value', default=1.0)
    m_Shift = bpy.props.FloatProperty(name='Shift', description='Set/Get the shift value. This value is added to each pixe', default=0.0)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClampOverflow', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_OutputScalarType', 'm_Scale', 'm_Shift', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageShiftScale)
TYPENAMES.append('BVTK_NT_ImageShiftScale' )


# --------------------------------------------------------------


class BVTK_NT_MoleculeToAtomBallFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MoleculeToAtomBallFilter'
    bl_label = 'vtkMoleculeToAtomBallFilter'
    
    m_RadiusScale = bpy.props.FloatProperty(name='RadiusScale', description='', default=0.8)
    m_RadiusSource = bpy.props.IntProperty(name='RadiusSource', description='', default=0)
    m_Resolution = bpy.props.IntProperty(name='Resolution', description='', default=50)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_RadiusScale', 'm_RadiusSource', 'm_Resolution', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MoleculeToAtomBallFilter)
TYPENAMES.append('BVTK_NT_MoleculeToAtomBallFilter' )


# --------------------------------------------------------------


class BVTK_NT_AppendSelection(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AppendSelection'
    bl_label = 'vtkAppendSelection'
    
    m_AppendByUnion = bpy.props.BoolProperty(name='AppendByUnion', description='When set to true, all the selections are combined together to form a single vtkSelection output. When set to false, the output is a composite selection with input selections as the children of the composite selection. This allows for selections with different content types and properties. Default is true', default=True)
    m_UserManagedInputs = bpy.props.BoolProperty(name='UserManagedInputs', description='UserManagedInputs allows the user to set inputs by number instead of using the AddInput/RemoveInput functions. Calls to SetNumberOfInputs/SetInputByNumber should not be mixed with calls to AddInput/RemoveInput. By default, UserManagedInputs is false', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AppendByUnion', 'm_UserManagedInputs', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AppendSelection)
TYPENAMES.append('BVTK_NT_AppendSelection' )


# --------------------------------------------------------------


class BVTK_NT_Threshold(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Threshold'
    bl_label = 'vtkThreshold'
    e_AttributeMode_items = [(x, x, x) for x in ['Default', 'UseCellData', 'UsePointData']]
    e_ComponentMode_items = [(x, x, x) for x in ['UseAll', 'UseAny', 'UseSelected']]
    e_PointsDataType_items = [(x, x, x) for x in ['Double', 'Float']]
    
    m_AllScalars = bpy.props.BoolProperty(name='AllScalars', description='If using scalars from point data, all scalars for all points in a cell must satisfy the threshold criterion if AllScalars is set. Otherwise, just a single scalar value satisfying the threshold criterion enables will extract the cell', default=True)
    e_AttributeMode = bpy.props.EnumProperty(name='AttributeMode', description='Control how the filter works with scalar point data and cell attribute data. By default (AttributeModeToDefault), the filter will use point data, and if no point data is available, then cell data is used. Alternatively you can explicitly set the filter to use point data (AttributeModeToUsePointData) or cell data (AttributeModeToUseCellData)', items=e_AttributeMode_items)
    e_ComponentMode = bpy.props.EnumProperty(name='ComponentMode', description='Control how the decision of in / out is made with multi-component data. The choices are to use the selected component (specified in the SelectedComponent ivar), or to look at all components. When looking at all components, the evaluation can pass if all the components satisfy the rule (UseAll) or if any satisfy is (UseAny). The default value is UseSelected', default='UseSelected', items=e_ComponentMode_items)
    e_PointsDataType = bpy.props.EnumProperty(name='PointsDataType', description='Set the data type of the output points (See the data types defined in vtkType.h). The default data type is float', items=e_PointsDataType_items)
    m_SelectedComponent = bpy.props.IntProperty(name='SelectedComponent', description='When the component mode is UseSelected, this ivar indicated the selected component. The default value is 0', default=0)
    m_UseContinuousCellRange = bpy.props.BoolProperty(name='UseContinuousCellRange', description='If this is on (default is off), we will use the continuous interval [minimum cell scalar, maxmimum cell scalar] to intersect the threshold bound , rather than the set of discrete scalar values from the vertices *WARNING*: For higher order cells, the scalar range of the cell is not the same as the vertex scalar interval used here, so the result will not be accurate', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AllScalars', 'e_AttributeMode', 'e_ComponentMode', 'e_PointsDataType', 'm_SelectedComponent', 'm_UseContinuousCellRange', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Threshold)
TYPENAMES.append('BVTK_NT_Threshold' )


# --------------------------------------------------------------


class BVTK_NT_MultiBlockMergeFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MultiBlockMergeFilter'
    bl_label = 'vtkMultiBlockMergeFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MultiBlockMergeFilter)
TYPENAMES.append('BVTK_NT_MultiBlockMergeFilter' )


# --------------------------------------------------------------


class BVTK_NT_HierarchicalDataExtractLevel(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HierarchicalDataExtractLevel'
    bl_label = 'vtkHierarchicalDataExtractLevel'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HierarchicalDataExtractLevel)
TYPENAMES.append('BVTK_NT_HierarchicalDataExtractLevel' )


# --------------------------------------------------------------


class BVTK_NT_TransmitImageDataPiece(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransmitImageDataPiece'
    bl_label = 'vtkTransmitImageDataPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty(name='CreateGhostCells', description='Turn on/off creating ghost cells (on by default)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CreateGhostCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransmitImageDataPiece)
TYPENAMES.append('BVTK_NT_TransmitImageDataPiece' )


# --------------------------------------------------------------


class BVTK_NT_ExtractSurface(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractSurface'
    bl_label = 'vtkExtractSurface'
    
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_HoleFilling = bpy.props.BoolProperty(name='HoleFilling', description='Enable hole filling. This generates separating surfaces between the empty and unseen portions of the volume', default=False)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Specify the radius of influence of the signed distance function. Data values (which are distances) that are greater than the radius (i.e., d > Radius) are considered empty voxels; those voxel data values d < -Radius are considered unseen voxels', default=0.1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_HoleFilling', 'm_Radius', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractSurface)
TYPENAMES.append('BVTK_NT_ExtractSurface' )


# --------------------------------------------------------------


class BVTK_NT_CellSizeFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CellSizeFilter'
    bl_label = 'vtkCellSizeFilter'
    
    m_AreaArrayName = bpy.props.StringProperty(name='AreaArrayName', description='Set/Get the name of the computed arrays. Default names are VertexCount, Length, Area and Volume', default='Area')
    m_ComputeArea = bpy.props.BoolProperty(name='ComputeArea', description='Specify whether or not to compute sizes for 2D cells cells. The computed value is the area of the cell. This option is enabled by default', default=True)
    m_ComputeLength = bpy.props.BoolProperty(name='ComputeLength', description='Specify whether or not to compute sizes for 1D cells cells. The computed value is the length of the cell. This option is enabled by default', default=True)
    m_ComputeSum = bpy.props.BoolProperty(name='ComputeSum', description='Specify whether to sum the computed sizes and put the result in a field data array. This option is disabled by default', default=False)
    m_ComputeVertexCount = bpy.props.BoolProperty(name='ComputeVertexCount', description='Specify whether or not to compute sizes for vertex and polyvertex cells. The computed value is the number of points in the cell. This option is enabled by default', default=True)
    m_ComputeVolume = bpy.props.BoolProperty(name='ComputeVolume', description='Specify whether or not to compute sizes for 3D cells cells. The computed value is the volume of the cell. This option is enabled by default', default=True)
    m_LengthArrayName = bpy.props.StringProperty(name='LengthArrayName', description='Set/Get the name of the computed arrays. Default names are VertexCount, Length, Area and Volume', default='Length')
    m_VertexCountArrayName = bpy.props.StringProperty(name='VertexCountArrayName', description='Set/Get the name of the computed arrays. Default names are VertexCount, Length, Area and Volume', default='VertexCount')
    m_VolumeArrayName = bpy.props.StringProperty(name='VolumeArrayName', description='Set/Get the name of the computed arrays. Default names are VertexCount, Length, Area and Volume', default='Volume')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AreaArrayName', 'm_ComputeArea', 'm_ComputeLength', 'm_ComputeSum', 'm_ComputeVertexCount', 'm_ComputeVolume', 'm_LengthArrayName', 'm_VertexCountArrayName', 'm_VolumeArrayName', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CellSizeFilter)
TYPENAMES.append('BVTK_NT_CellSizeFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageFFT(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageFFT'
    bl_label = 'vtkImageFFT'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Dimensionality is the number of axes which are considered during execution. To process images dimensionality would be set to 2', default=3)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageFFT)
TYPENAMES.append('BVTK_NT_ImageFFT' )


# --------------------------------------------------------------


class BVTK_NT_ExtractPolyDataPiece(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractPolyDataPiece'
    bl_label = 'vtkExtractPolyDataPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty(name='CreateGhostCells', description='Turn on/off creating ghost cells (on by default)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CreateGhostCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractPolyDataPiece)
TYPENAMES.append('BVTK_NT_ExtractPolyDataPiece' )


# --------------------------------------------------------------


class BVTK_NT_PCellDataToPointData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PCellDataToPointData'
    bl_label = 'vtkPCellDataToPointData'
    
    m_ContributingCellOption = bpy.props.IntProperty(name='ContributingCellOption', description='Option to specify what cells to include in the gradient computation. Options are all cells (All, Patch and DataSetMax). The default is All', default=0)
    m_PassCellData = bpy.props.BoolProperty(name='PassCellData', description='Control whether the input cell data is to be passed to the output. If on, then the input cell data is passed through to the output; otherwise, only generated point data is placed into the output', default=True)
    m_PieceInvariant = bpy.props.BoolProperty(name='PieceInvariant', description='To get piece invariance, this filter has to request an extra ghost level. By default piece invariance is on', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ContributingCellOption', 'm_PassCellData', 'm_PieceInvariant', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PCellDataToPointData)
TYPENAMES.append('BVTK_NT_PCellDataToPointData' )


# --------------------------------------------------------------


class BVTK_NT_ProjectedTexture(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProjectedTexture'
    bl_label = 'vtkProjectedTexture'
    e_CameraMode_items = [(x, x, x) for x in ['Pinhole', 'TwoMirror']]
    
    m_AspectRatio = bpy.props.FloatVectorProperty(name='AspectRatio', description="Set/Get the aspect ratio of a perpendicular cross-section of the the projector's frustum. The aspect ratio consists of three numbers: (x, y, z), where x is the width of the frustum, y is the height, and z is the perpendicular distance from the focus of the projector", default=[1.0, 1.0, 1.0], size=3)
    e_CameraMode = bpy.props.EnumProperty(name='CameraMode', description='Set/Get the camera mode of the projection -- pinhole projection or two mirror projection', default='Pinhole', items=e_CameraMode_items)
    m_MirrorSeparation = bpy.props.FloatProperty(name='MirrorSeparation', description='Set/Get the mirror separation for the two mirror system', default=1.0)
    m_Position = bpy.props.FloatVectorProperty(name='Position', description='Set/Get the position of the focus of the projector', default=[0.0, 0.0, 1.0], size=3)
    m_SRange = bpy.props.FloatVectorProperty(name='SRange', description='Specify s-coordinate range for texture s-t coordinate pair', default=[0.0, 1.0], size=2)
    m_TRange = bpy.props.FloatVectorProperty(name='TRange', description='Specify t-coordinate range for texture s-t coordinate pair', default=[0.0, 1.0], size=2)
    m_Up = bpy.props.FloatVectorProperty(name='Up', description='Set/Get the up vector of the projector', default=[0.0, 1.0, 0.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AspectRatio', 'e_CameraMode', 'm_MirrorSeparation', 'm_Position', 'm_SRange', 'm_TRange', 'm_Up', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProjectedTexture)
TYPENAMES.append('BVTK_NT_ProjectedTexture' )


# --------------------------------------------------------------


class BVTK_NT_LinkEdgels(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LinkEdgels'
    bl_label = 'vtkLinkEdgels'
    
    m_GradientThreshold = bpy.props.FloatProperty(name='GradientThreshold', description='Set/Get the threshold for image gradient thresholding', default=0.1)
    m_LinkThreshold = bpy.props.FloatProperty(name='LinkThreshold', description='Set/Get the threshold for Phi vs. Alpha link thresholding', default=90.0)
    m_PhiThreshold = bpy.props.FloatProperty(name='PhiThreshold', description='Set/get the threshold for Phi vs. Phi link thresholding', default=90.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GradientThreshold', 'm_LinkThreshold', 'm_PhiThreshold', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LinkEdgels)
TYPENAMES.append('BVTK_NT_LinkEdgels' )


# --------------------------------------------------------------


class BVTK_NT_SplitByCellScalarFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SplitByCellScalarFilter'
    bl_label = 'vtkSplitByCellScalarFilter'
    
    m_PassAllPoints = bpy.props.BoolProperty(name='PassAllPoints', description='Specify if input points array must be passed to output blocks. If so, filter processing is faster but outblocks will contains more points than what is needed by the cells it owns. If not, a new points array is created for every block and it will only contains points for copied cells. Note that this function is only possible for PointSet datasets. The default is true', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PassAllPoints', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SplitByCellScalarFilter)
TYPENAMES.append('BVTK_NT_SplitByCellScalarFilter' )


# --------------------------------------------------------------


class BVTK_NT_RectilinearGridPartitioner(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RectilinearGridPartitioner'
    bl_label = 'vtkRectilinearGridPartitioner'
    
    m_DuplicateNodes = bpy.props.BoolProperty(name='DuplicateNodes', description='', default=True)
    m_NumberOfGhostLayers = bpy.props.IntProperty(name='NumberOfGhostLayers', description='Set/Get macro for the number of ghost layers', default=0)
    m_NumberOfPartitions = bpy.props.IntProperty(name='NumberOfPartitions', description='Set/Get macro for the number of subdivisions', default=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DuplicateNodes', 'm_NumberOfGhostLayers', 'm_NumberOfPartitions', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RectilinearGridPartitioner)
TYPENAMES.append('BVTK_NT_RectilinearGridPartitioner' )


# --------------------------------------------------------------


class BVTK_NT_ImageHSVToRGB(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageHSVToRGB'
    bl_label = 'vtkImageHSVToRGB'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Maximum = bpy.props.FloatProperty(name='Maximum', description='Hue is an angle. Maximum specifies when it maps back to 0. HueMaximum defaults to 255 instead of 2PI, because unsigned char is expected as input. Maximum also specifies the maximum of the Saturation, and R, G, B', default=255.0)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Maximum', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageHSVToRGB)
TYPENAMES.append('BVTK_NT_ImageHSVToRGB' )


# --------------------------------------------------------------


class BVTK_NT_QuadraturePointInterpolator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_QuadraturePointInterpolator'
    bl_label = 'vtkQuadraturePointInterpolator'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_QuadraturePointInterpolator)
TYPENAMES.append('BVTK_NT_QuadraturePointInterpolator' )


# --------------------------------------------------------------


class BVTK_NT_GenericCutter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GenericCutter'
    bl_label = 'vtkGenericCutter'
    
    m_GenerateCutScalars = bpy.props.BoolProperty(name='GenerateCutScalars', description='If this flag is enabled, then the output scalar values will be interpolated from the implicit function values, and not the input scalar data', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Set the number of contours to place into the list. You only really need to use this method to reduce list size. The method SetValue() will automatically increase list size as needed', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateCutScalars', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['CutFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GenericCutter)
TYPENAMES.append('BVTK_NT_GenericCutter' )


# --------------------------------------------------------------


class BVTK_NT_MultiBlockDataSetAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MultiBlockDataSetAlgorithm'
    bl_label = 'vtkMultiBlockDataSetAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MultiBlockDataSetAlgorithm)
TYPENAMES.append('BVTK_NT_MultiBlockDataSetAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_VoxelGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VoxelGrid'
    bl_label = 'vtkVoxelGrid'
    e_ConfigurationStyle_items = [(x, x, x) for x in ['Automatic', 'LeafSize', 'Manual']]
    
    e_ConfigurationStyle = bpy.props.EnumProperty(name='ConfigurationStyle', description='Configure how the filter is to operate. The user can choose to manually specify the binning volume (by setting its dimensions via MANUAL style); or specify a leaf bin size in the x-y-z directions (SPECIFY_LEAF_SIZE); or in AUTOMATIC style, use a rough average number of points in each bin guide the bin size and binning volume dimensions. By default, AUTOMATIC configuration style is used', default='Automatic', items=e_ConfigurationStyle_items)
    m_Divisions = bpy.props.IntVectorProperty(name='Divisions', description='Set the number of divisions in x-y-z directions (the binning volume dimensions). This data member is used when the configuration style is set to MANUAL. Note that these values may be adjusted if <1 or too large', default=[50, 50, 50], size=3)
    m_LeafSize = bpy.props.FloatVectorProperty(name='LeafSize', description='Set the bin size in the x-y-z directions. This data member is used when the configuration style is set to SPECIFY_LEAF_SIZE. The class will use these x-y-z lengths, within the bounding box of the point cloud, to determine the binning dimensions', default=[1.0, 1.0, 1.0], size=3)
    m_NumberOfPointsPerBin = bpy.props.IntProperty(name='NumberOfPointsPerBin', description='Specify the average number of points in each bin. Larger values result in higher rates of subsampling. This data member is used when the configuration style is set to AUTOMATIC. The class will automatically determine the binning dimensions in the x-y-z directions', default=10)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ConfigurationStyle', 'm_Divisions', 'm_LeafSize', 'm_NumberOfPointsPerBin', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Kernel'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VoxelGrid)
TYPENAMES.append('BVTK_NT_VoxelGrid' )


# --------------------------------------------------------------


class BVTK_NT_Stripper(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Stripper'
    bl_label = 'vtkStripper'
    
    m_JoinContiguousSegments = bpy.props.BoolProperty(name='JoinContiguousSegments', description='If on, the output polygonal segments will be joined if they are contiguous. This is useful after slicing a surface. The default is off', default=True)
    m_MaximumLength = bpy.props.IntProperty(name='MaximumLength', description='Specify the maximum number of triangles in a triangle strip, and/or the maximum number of lines in a poly-line', default=1000)
    m_PassCellDataAsFieldData = bpy.props.BoolProperty(name='PassCellDataAsFieldData', description='Enable/Disable passing of the CellData in the input to the output as FieldData. Note the field data is transformed', default=True)
    m_PassThroughCellIds = bpy.props.BoolProperty(name='PassThroughCellIds', description='If on, the output polygonal dataset will have a celldata array that holds the cell index of the original 3D cell that produced each output cell. This is useful for picking. The default is off to conserve memory', default=True)
    m_PassThroughPointIds = bpy.props.BoolProperty(name='PassThroughPointIds', description='If on, the output polygonal dataset will have a pointdata array that holds the point index of the original vertex that produced each output vertex. This is useful for picking. The default is off to conserve memory', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_JoinContiguousSegments', 'm_MaximumLength', 'm_PassCellDataAsFieldData', 'm_PassThroughCellIds', 'm_PassThroughPointIds', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Stripper)
TYPENAMES.append('BVTK_NT_Stripper' )


# --------------------------------------------------------------


class BVTK_NT_PointConnectivityFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PointConnectivityFilter'
    bl_label = 'vtkPointConnectivityFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PointConnectivityFilter)
TYPENAMES.append('BVTK_NT_PointConnectivityFilter' )


# --------------------------------------------------------------


class BVTK_NT_MarchingSquares(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MarchingSquares'
    bl_label = 'vtkMarchingSquares'
    
    m_ImageRange = bpy.props.IntVectorProperty(name='ImageRange', description='Set/Get the i-j-k index range which define a plane on which to generate contour lines. Using this ivar it is possible to input a 3D volume directly and then generate contour lines on one of the i-j-k planes, or a portion of a plane', default=[0, 1000000000, 0, 1000000000, 0, 0], size=6)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Methods to set contour value', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ImageRange', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MarchingSquares)
TYPENAMES.append('BVTK_NT_MarchingSquares' )


# --------------------------------------------------------------


class BVTK_NT_ThresholdTextureCoords(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ThresholdTextureCoords'
    bl_label = 'vtkThresholdTextureCoords'
    
    m_InTextureCoord = bpy.props.FloatVectorProperty(name='InTextureCoord', description='Set the texture coordinate value for point satisfying threshold criterion', default=[0.75, 0.0, 0.0], size=3)
    m_OutTextureCoord = bpy.props.FloatVectorProperty(name='OutTextureCoord', description='Set the texture coordinate value for point NOT satisfying threshold criterion', default=[0.25, 0.0, 0.0], size=3)
    m_TextureDimension = bpy.props.IntProperty(name='TextureDimension', description='Set the desired dimension of the texture map', default=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_InTextureCoord', 'm_OutTextureCoord', 'm_TextureDimension', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ThresholdTextureCoords)
TYPENAMES.append('BVTK_NT_ThresholdTextureCoords' )


# --------------------------------------------------------------


class BVTK_NT_ImageMaskBits(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMaskBits'
    bl_label = 'vtkImageMaskBits'
    e_Operation_items = [(x, x, x) for x in ['And', 'Nand', 'Nor', 'Or', 'Xor']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Masks = bpy.props.IntVectorProperty(name='Masks', description='', default=[1000000000, 1000000000, 1000000000, 1000000000], size=4)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_Operation = bpy.props.EnumProperty(name='Operation', description='Set/Get the boolean operator. Default is AND', default='And', items=e_Operation_items)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Masks', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_Operation', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMaskBits)
TYPENAMES.append('BVTK_NT_ImageMaskBits' )


# --------------------------------------------------------------


class BVTK_NT_UncertaintyTubeFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_UncertaintyTubeFilter'
    bl_label = 'vtkUncertaintyTubeFilter'
    
    m_NumberOfSides = bpy.props.IntProperty(name='NumberOfSides', description='Set / get the number of sides for the tube. At a minimum, the number of sides is 3', default=12)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NumberOfSides', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_UncertaintyTubeFilter)
TYPENAMES.append('BVTK_NT_UncertaintyTubeFilter' )


# --------------------------------------------------------------


class BVTK_NT_QuadricClustering(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_QuadricClustering'
    bl_label = 'vtkQuadricClustering'
    
    m_AutoAdjustNumberOfDivisions = bpy.props.BoolProperty(name='AutoAdjustNumberOfDivisions', description='Enable automatic adjustment of number of divisions. If off, the number of divisions specified by the user is always used (as long as it is valid). The default is O', default=True)
    m_CopyCellData = bpy.props.BoolProperty(name='CopyCellData', description='This flag makes the filter copy cell data from input to output (the best it can). It uses input cells that trigger the addition of output cells (no averaging). This is off by default, and does not work when append is being called explicitly (non-pipeline usage)', default=True)
    m_FeaturePointsAngle = bpy.props.FloatProperty(name='FeaturePointsAngle', description='Set/Get the angle to use in determining whether a point on a boundary / feature edge is a feature point', default=30.0)
    m_NumberOfXDivisions = bpy.props.IntProperty(name='NumberOfXDivisions', description='Set/Get the number of divisions along each axis for the spatial bins. The number of spatial bins is NumberOfXDivisions*NumberOfYDivisions* NumberOfZDivisions. The filter may choose to ignore large numbers of divisions if the input has few points and AutoAdjustNumberOfDivisions is enabled', default=50)
    m_NumberOfYDivisions = bpy.props.IntProperty(name='NumberOfYDivisions', description='Set/Get the number of divisions along each axis for the spatial bins. The number of spatial bins is NumberOfXDivisions*NumberOfYDivisions* NumberOfZDivisions. The filter may choose to ignore large numbers of divisions if the input has few points and AutoAdjustNumberOfDivisions is enabled', default=50)
    m_NumberOfZDivisions = bpy.props.IntProperty(name='NumberOfZDivisions', description='Set/Get the number of divisions along each axis for the spatial bins. The number of spatial bins is NumberOfXDivisions*NumberOfYDivisions* NumberOfZDivisions. The filter may choose to ignore large numbers of divisions if the input has few points and AutoAdjustNumberOfDivisions is enabled', default=50)
    m_PreventDuplicateCells = bpy.props.BoolProperty(name='PreventDuplicateCells', description='Specify a boolean indicating whether to remove duplicate cells (i.e. triangles). This is a little slower, and takes more memory, but in some cases can reduce the number of cells produced by an order of magnitude. By default, this flag is true', default=True)
    m_UseFeatureEdges = bpy.props.BoolProperty(name='UseFeatureEdges', description='By default, this flag is off. When "UseFeatureEdges" is on, then quadrics are computed for boundary edges/feature edges. They influence the quadrics (position of points), but not the mesh. Which features to use can be controlled by the filter "FeatureEdges"', default=True)
    m_UseFeaturePoints = bpy.props.BoolProperty(name='UseFeaturePoints', description='By default, this flag is off. It only has an effect when "UseFeatureEdges" is also on. When "UseFeaturePoints" is on, then quadrics are computed for boundary / feature points used in the boundary / feature edges. They influence the quadrics (position of points), but not the mesh', default=True)
    m_UseInputPoints = bpy.props.BoolProperty(name='UseInputPoints', description='Normally the point that minimizes the quadric error function is used as the output of the bin. When this flag is on, the bin point is forced to be one of the points from the input (the one with the smallest error). This option does not work (i.e., input points cannot be used) when the append methods (StartAppend(), Append(), EndAppend()) are being called directly', default=True)
    m_UseInternalTriangles = bpy.props.BoolProperty(name='UseInternalTriangles', description='When this flag is on (and it is on by default), then triangles that are completely contained in a bin are added to the bin quadrics. When the the flag is off the filter operates faster, but the surface may not be as well behaved', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutoAdjustNumberOfDivisions', 'm_CopyCellData', 'm_FeaturePointsAngle', 'm_NumberOfXDivisions', 'm_NumberOfYDivisions', 'm_NumberOfZDivisions', 'm_PreventDuplicateCells', 'm_UseFeatureEdges', 'm_UseFeaturePoints', 'm_UseInputPoints', 'm_UseInternalTriangles', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_QuadricClustering)
TYPENAMES.append('BVTK_NT_QuadricClustering' )


# --------------------------------------------------------------


class BVTK_NT_ExtractPolyDataGeometry(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractPolyDataGeometry'
    bl_label = 'vtkExtractPolyDataGeometry'
    
    m_ExtractBoundaryCells = bpy.props.BoolProperty(name='ExtractBoundaryCells', description='Boolean controls whether to extract cells that are partially inside. By default, ExtractBoundaryCells is off', default=True)
    m_ExtractInside = bpy.props.BoolProperty(name='ExtractInside', description='Boolean controls whether to extract cells that are inside of implicit function (ExtractInside == 1) or outside of implicit function (ExtractInside == 0)', default=True)
    m_PassPoints = bpy.props.BoolProperty(name='PassPoints', description='Boolean controls whether points are culled or simply passed through to the output', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ExtractBoundaryCells', 'm_ExtractInside', 'm_PassPoints', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['ImplicitFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractPolyDataGeometry)
TYPENAMES.append('BVTK_NT_ExtractPolyDataGeometry' )


# --------------------------------------------------------------


class BVTK_NT_CellCenters(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CellCenters'
    bl_label = 'vtkCellCenters'
    
    m_VertexCells = bpy.props.BoolProperty(name='VertexCells', description='Enable/disable the generation of vertex cells. The default is Off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_VertexCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CellCenters)
TYPENAMES.append('BVTK_NT_CellCenters' )


# --------------------------------------------------------------


class BVTK_NT_WeightedTransformFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_WeightedTransformFilter'
    bl_label = 'vtkWeightedTransformFilter'
    
    m_AddInputValues = bpy.props.BoolProperty(name='AddInputValues', description='If AddInputValues is true, the output values of this filter will be offset from the input values. The effect is exactly equivalent to having an identity transform of weight 1 added into each output point', default=True)
    m_CellDataTransformIndexArray = bpy.props.StringProperty(name='CellDataTransformIndexArray', description='The CellDataTransformIndexArray is like a TransformIndexArray, except for cell data. The array must have type UnsignedShort')
    m_CellDataWeightArray = bpy.props.StringProperty(name='CellDataWeightArray', description="The CellDataWeightArray is analogous to the WeightArray, except for CellData. The array is searched for first in the CellData FieldData, then in the input's FieldData. The data array must have a tuple for each cell. This array is used to transform only normals and vectors")
    m_NumberOfTransforms = bpy.props.IntProperty(name='NumberOfTransforms', description='Set the number of transforms for the filter. References to non-existent filter numbers in the data array is equivalent to a weight of zero (i.e., no contribution of that filter or weight). The maximum number of transforms is limited to 65536 if transform index arrays are used', default=0)
    m_TransformIndexArray = bpy.props.StringProperty(name='TransformIndexArray', description="TransformIndexArray is the string name of the DataArray in the input's FieldData that holds the indices for the transforms for each point. These indices are used to select which transforms each weight of the DataArray refers. If the TransformIndexArray is not specified, the weights of each point are assumed to map directly to a transform. This DataArray must be of type UnsignedShort, which effectively limits the number of transforms to 65536 if a transform index array is used")
    m_WeightArray = bpy.props.StringProperty(name='WeightArray', description="WeightArray is the string name of the DataArray in the input's FieldData that holds the weighting coefficients for each point. The filter will first look for the array in the input's PointData FieldData. If the array isn't there, the filter looks in the input's FieldData. The WeightArray can have tuples of any length, but must have a tuple for every point in the input data set. This array transforms points, normals, and vectors")
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AddInputValues', 'm_CellDataTransformIndexArray', 'm_CellDataWeightArray', 'm_NumberOfTransforms', 'm_TransformIndexArray', 'm_WeightArray', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_WeightedTransformFilter)
TYPENAMES.append('BVTK_NT_WeightedTransformFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageWrapPad(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageWrapPad'
    bl_label = 'vtkImageWrapPad'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_OutputNumberOfScalarComponents = bpy.props.IntProperty(name='OutputNumberOfScalarComponents', description='Set/Get the number of output scalar components', default=-1)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_OutputNumberOfScalarComponents', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageWrapPad)
TYPENAMES.append('BVTK_NT_ImageWrapPad' )


# --------------------------------------------------------------


class BVTK_NT_FieldDataToAttributeDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FieldDataToAttributeDataFilter'
    bl_label = 'vtkFieldDataToAttributeDataFilter'
    e_InputField_items = [(x, x, x) for x in ['CellDataField', 'DataObjectField', 'PointDataField']]
    e_OutputAttributeData_items = [(x, x, x) for x in ['CellData', 'PointData']]
    
    m_DefaultNormalize = bpy.props.BoolProperty(name='DefaultNormalize', description='Set the default Normalize() flag for those methods setting a default Normalize value (e.g., SetScalarComponents)', default=True)
    e_InputField = bpy.props.EnumProperty(name='InputField', description='Specify which field data to use to generate the output attribute data. There are three choices: the field data associated with the vtkDataObject superclass; the point field attribute data; and the cell field attribute data', default='DataObjectField', items=e_InputField_items)
    e_OutputAttributeData = bpy.props.EnumProperty(name='OutputAttributeData', description='Specify which attribute data to output: point or cell data attributes', default='PointData', items=e_OutputAttributeData_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DefaultNormalize', 'e_InputField', 'e_OutputAttributeData', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FieldDataToAttributeDataFilter)
TYPENAMES.append('BVTK_NT_FieldDataToAttributeDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_FlyingEdges3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FlyingEdges3D'
    bl_label = 'vtkFlyingEdges3D'
    
    m_ArrayComponent = bpy.props.IntProperty(name='ArrayComponent', description='Set/get which component of the scalar array to contour on; defaults to 0', default=0)
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_InterpolateAttributes = bpy.props.BoolProperty(name='InterpolateAttributes', description='Indicate whether to interpolate other attribute data. That is, as the isosurface is generated, interpolate all point attribute data across the edge. This is independent of scalar interpolation, which is controlled by the ComputeScalars flag', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Set the number of contours to place into the list. You only really need to use this method to reduce list size. The method SetValue() will automatically increase list size as needed', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayComponent', 'm_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_InterpolateAttributes', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FlyingEdges3D)
TYPENAMES.append('BVTK_NT_FlyingEdges3D' )


# --------------------------------------------------------------


class BVTK_NT_PassThroughFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PassThroughFilter'
    bl_label = 'vtkPassThroughFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PassThroughFilter)
TYPENAMES.append('BVTK_NT_PassThroughFilter' )


# --------------------------------------------------------------


class BVTK_NT_TransformTextureCoords(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransformTextureCoords'
    bl_label = 'vtkTransformTextureCoords'
    
    m_FlipR = bpy.props.BoolProperty(name='FlipR', description='Boolean indicates whether the texture map should be flipped around the s-axis. Note that the flips occur around the texture origin', default=True)
    m_FlipS = bpy.props.BoolProperty(name='FlipS', description='Boolean indicates whether the texture map should be flipped around the s-axis. Note that the flips occur around the texture origin', default=True)
    m_FlipT = bpy.props.BoolProperty(name='FlipT', description='Boolean indicates whether the texture map should be flipped around the t-axis. Note that the flips occur around the texture origin', default=True)
    m_Origin = bpy.props.FloatVectorProperty(name='Origin', description='Set/Get the origin of the texture map. This is the point about which the texture map is flipped (e.g., rotated). Since a typical texture map ranges from (0,1) in the r-s-t coordinates, the default origin is set at (0.5,0.5,0.5)', default=[0.5, 0.5, 0.5], size=3)
    m_Position = bpy.props.FloatVectorProperty(name='Position', description='Set/Get the position of the texture map. Setting the position translates the texture map by the amount specified', default=[0.0, 0.0, 0.0], size=3)
    m_Scale = bpy.props.FloatVectorProperty(name='Scale', description='Set/Get the scale of the texture map. Scaling in performed independently on the r, s and t axes', default=[1.0, 1.0, 1.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FlipR', 'm_FlipS', 'm_FlipT', 'm_Origin', 'm_Position', 'm_Scale', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransformTextureCoords)
TYPENAMES.append('BVTK_NT_TransformTextureCoords' )


# --------------------------------------------------------------


class BVTK_NT_LoopSubdivisionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LoopSubdivisionFilter'
    bl_label = 'vtkLoopSubdivisionFilter'
    
    m_CheckForTriangles = bpy.props.BoolProperty(name='CheckForTriangles', description='Set/get CheckForTriangles Should subdivision check that the dataset only contains triangles? Default is On (1)', default=True)
    m_NumberOfSubdivisions = bpy.props.IntProperty(name='NumberOfSubdivisions', description='Set/get the number of subdivisions. Default is 1', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CheckForTriangles', 'm_NumberOfSubdivisions', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LoopSubdivisionFilter)
TYPENAMES.append('BVTK_NT_LoopSubdivisionFilter' )


# --------------------------------------------------------------


class BVTK_NT_FlyingEdgesPlaneCutter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FlyingEdgesPlaneCutter'
    bl_label = 'vtkFlyingEdgesPlaneCutter'
    
    m_ArrayComponent = bpy.props.IntProperty(name='ArrayComponent', description='Set/get which component of the scalar array to contour on; defaults to 0', default=0)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. The normal generated is simply the cut plane normal. By default this is disabled', default=True)
    m_InterpolateAttributes = bpy.props.BoolProperty(name='InterpolateAttributes', description='Indicate whether to interpolate other attribute data besides the input scalars (which are required). That is, as the isosurface is generated, interpolate all other point attribute data across intersected edges', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayComponent', 'm_ComputeNormals', 'm_InterpolateAttributes', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Plane'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FlyingEdgesPlaneCutter)
TYPENAMES.append('BVTK_NT_FlyingEdgesPlaneCutter' )


# --------------------------------------------------------------


class BVTK_NT_AssignAttribute(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AssignAttribute'
    bl_label = 'vtkAssignAttribute'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AssignAttribute)
TYPENAMES.append('BVTK_NT_AssignAttribute' )


# --------------------------------------------------------------


class BVTK_NT_ImageDataStreamer(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageDataStreamer'
    bl_label = 'vtkImageDataStreamer'
    
    m_NumberOfStreamDivisions = bpy.props.IntProperty(name='NumberOfStreamDivisions', description='Set how many pieces to divide the input into. void SetNumberOfStreamDivisions(int num); int GetNumberOfStreamDivisions()', default=10)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NumberOfStreamDivisions', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['ExtentTranslator'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageDataStreamer)
TYPENAMES.append('BVTK_NT_ImageDataStreamer' )


# --------------------------------------------------------------


class BVTK_NT_AMRCutPlane(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AMRCutPlane'
    bl_label = 'vtkAMRCutPlane'
    
    m_LevelOfResolution = bpy.props.IntProperty(name='LevelOfResolution', description='Sets the level of resolutio', default=0)
    m_UseNativeCutter = bpy.props.BoolProperty(name='UseNativeCutter', description='', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_LevelOfResolution', 'm_UseNativeCutter', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AMRCutPlane)
TYPENAMES.append('BVTK_NT_AMRCutPlane' )


# --------------------------------------------------------------


class BVTK_NT_PolyDataAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PolyDataAlgorithm'
    bl_label = 'vtkPolyDataAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PolyDataAlgorithm)
TYPENAMES.append('BVTK_NT_PolyDataAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_ImageEuclideanDistance(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageEuclideanDistance'
    bl_label = 'vtkImageEuclideanDistance'
    e_Algorithm_items = [(x, x, x) for x in ['Saito', 'SaitoCached']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    e_Algorithm = bpy.props.EnumProperty(name='Algorithm', description='Selects a Euclidean DT algorithm. 1. Saito 2. Saito-cached More algorithms will be added later on', default='Saito', items=e_Algorithm_items)
    m_ConsiderAnisotropy = bpy.props.BoolProperty(name='ConsiderAnisotropy', description='Used to define whether Spacing should be used in the computation of the distance', default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Dimensionality is the number of axes which are considered during execution. To process images dimensionality would be set to 2', default=3)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Initialize = bpy.props.BoolProperty(name='Initialize', description='Used to set all non-zero voxels to MaximumDistance before starting the distance transformation. Setting Initialize off keeps the current value in the input image as starting point. This allows to superimpose several distance maps', default=True)
    m_MaximumDistance = bpy.props.FloatProperty(name='MaximumDistance', description='Any distance bigger than this->MaximumDistance will not ne computed but set to this->MaximumDistance instead', default=2147483647.0)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_Algorithm', 'm_ConsiderAnisotropy', 'm_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Initialize', 'm_MaximumDistance', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageEuclideanDistance)
TYPENAMES.append('BVTK_NT_ImageEuclideanDistance' )


# --------------------------------------------------------------


class BVTK_NT_PlaneCutter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PlaneCutter'
    bl_label = 'vtkPlaneCutter'
    
    m_BuildHierarchy = bpy.props.BoolProperty(name='BuildHierarchy', description='Indicate whether to build tree hierarchy. Computing the tree hierarchy can take some time on the first computation but if the input does not change, the computation of all further slice will be faster. Default is on', default=True)
    m_BuildTree = bpy.props.BoolProperty(name='BuildTree', description='Indicate whether to build the sphere tree. Computing the sphere will take some time on the first computation but if the input does not change, the computation of all further slice will be much faster. Default is on', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. The normal generated is simply the cut plane normal. The normal, if generated, is defined by cell data associated with the output polygons. By default computing of normals is disabled', default=False)
    m_GeneratePolygons = bpy.props.BoolProperty(name='GeneratePolygons', description='Indicate whether to generate polygons instead of triangles when cutting structured and rectilinear grid. No effect with other kinds of inputs, enabled by default', default=True)
    m_InterpolateAttributes = bpy.props.BoolProperty(name='InterpolateAttributes', description='Indicate whether to interpolate attribute data. By default this is enabled. Note that both cell data and point data is interpolated and outputted, except for image data input where only point data are outputted', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BuildHierarchy', 'm_BuildTree', 'm_ComputeNormals', 'm_GeneratePolygons', 'm_InterpolateAttributes', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Plane'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PlaneCutter)
TYPENAMES.append('BVTK_NT_PlaneCutter' )


# --------------------------------------------------------------


class BVTK_NT_ProjectSphereFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProjectSphereFilter'
    bl_label = 'vtkProjectSphereFilter'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set the center of the sphere to be split. Default is 0,0,0', default=[0.0, 0.0, 0.0], size=3)
    m_KeepPolePoints = bpy.props.BoolProperty(name='KeepPolePoints', description='Specify whether or not to keep the cells using a point at a pole. The default is false', default=False)
    m_TranslateZ = bpy.props.BoolProperty(name='TranslateZ', description='Specify whether (true) or not to translate the points in the projected transformation such that the input point with the smallest radius is at 0. The default is false', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_KeepPolePoints', 'm_TranslateZ', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProjectSphereFilter)
TYPENAMES.append('BVTK_NT_ProjectSphereFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageShrink3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageShrink3D'
    bl_label = 'vtkImageShrink3D'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_Averaging = bpy.props.BoolProperty(name='Averaging', description='Choose Mean, Minimum, Maximum, Median or sub sampling. The neighborhood operations are not centered on the sampled pixel. This may cause a half pixel shift in your output image. You can changed "Shift" to get around this. vtkImageGaussianSmooth or vtkImageMean with strides', default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Maximum = bpy.props.BoolProperty(name='Maximum', description='', default=True)
    m_Mean = bpy.props.BoolProperty(name='Mean', description='', default=True)
    m_Median = bpy.props.BoolProperty(name='Median', description='', default=True)
    m_Minimum = bpy.props.BoolProperty(name='Minimum', description='', default=True)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_Shift = bpy.props.IntVectorProperty(name='Shift', description='', default=[0, 0, 0], size=3)
    m_ShrinkFactors = bpy.props.IntVectorProperty(name='ShrinkFactors', description='', default=[1, 1, 1], size=3)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Averaging', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Maximum', 'm_Mean', 'm_Median', 'm_Minimum', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_Shift', 'm_ShrinkFactors', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageShrink3D)
TYPENAMES.append('BVTK_NT_ImageShrink3D' )


# --------------------------------------------------------------


class BVTK_NT_FeatureEdges(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FeatureEdges'
    bl_label = 'vtkFeatureEdges'
    
    m_BoundaryEdges = bpy.props.BoolProperty(name='BoundaryEdges', description='Turn on/off the extraction of boundary edges', default=True)
    m_Coloring = bpy.props.BoolProperty(name='Coloring', description='Turn on/off the coloring of edges by type', default=True)
    m_FeatureAngle = bpy.props.FloatProperty(name='FeatureAngle', description='Specify the feature angle for extracting feature edges', default=30.0)
    m_FeatureEdges = bpy.props.BoolProperty(name='FeatureEdges', description='Turn on/off the extraction of feature edges', default=True)
    m_ManifoldEdges = bpy.props.BoolProperty(name='ManifoldEdges', description='Turn on/off the extraction of manifold edges', default=True)
    m_NonManifoldEdges = bpy.props.BoolProperty(name='NonManifoldEdges', description='Turn on/off the extraction of non-manifold edges', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BoundaryEdges', 'm_Coloring', 'm_FeatureAngle', 'm_FeatureEdges', 'm_ManifoldEdges', 'm_NonManifoldEdges', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FeatureEdges)
TYPENAMES.append('BVTK_NT_FeatureEdges' )


# --------------------------------------------------------------


class BVTK_NT_RotationFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RotationFilter'
    bl_label = 'vtkRotationFilter'
    e_Axis_items = [(x, x, x) for x in ['X', 'Y', 'Z']]
    
    m_Angle = bpy.props.FloatProperty(name='Angle', description='Set the rotation angle to use', default=0.0)
    e_Axis = bpy.props.EnumProperty(name='Axis', description='Set the axis of rotation to use. It is set by default to Z', default='Z', items=e_Axis_items)
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='', default=[0.0, 0.0, 0.0], size=3)
    m_CopyInput = bpy.props.BoolProperty(name='CopyInput', description='If on (the default), copy the input geometry to the output. If off, the output will only contain the rotation', default=True)
    m_NumberOfCopies = bpy.props.IntProperty(name='NumberOfCopies', description='Set the number of copies to create. The source will be rotated N times and a new polydata copy of the original created at each angular position All copies will be appended to form a single outpu', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Angle', 'e_Axis', 'm_Center', 'm_CopyInput', 'm_NumberOfCopies', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RotationFilter)
TYPENAMES.append('BVTK_NT_RotationFilter' )


# --------------------------------------------------------------


class BVTK_NT_AppendFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AppendFilter'
    bl_label = 'vtkAppendFilter'
    
    m_MergePoints = bpy.props.BoolProperty(name='MergePoints', description="Set the filter to merge coincidental points. Note: The filter will only merge points if the ghost cell array doesn't exist Defaults to Of", default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MergePoints', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AppendFilter)
TYPENAMES.append('BVTK_NT_AppendFilter' )


# --------------------------------------------------------------


class BVTK_NT_TransmitUnstructuredGridPiece(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransmitUnstructuredGridPiece'
    bl_label = 'vtkTransmitUnstructuredGridPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty(name='CreateGhostCells', description='Turn on/off creating ghost cells (on by default)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CreateGhostCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransmitUnstructuredGridPiece)
TYPENAMES.append('BVTK_NT_TransmitUnstructuredGridPiece' )


# --------------------------------------------------------------


class BVTK_NT_CastToConcrete(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CastToConcrete'
    bl_label = 'vtkCastToConcrete'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CastToConcrete)
TYPENAMES.append('BVTK_NT_CastToConcrete' )


# --------------------------------------------------------------


class BVTK_NT_DecimatePolylineFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DecimatePolylineFilter'
    bl_label = 'vtkDecimatePolylineFilter'
    
    m_TargetReduction = bpy.props.FloatProperty(name='TargetReduction', description='Specify the desired reduction in the total number of polygons (e.g., if TargetReduction is set to 0.9, this filter will try to reduce the data set to 10% of its original size)', default=0.9)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_TargetReduction', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DecimatePolylineFilter)
TYPENAMES.append('BVTK_NT_DecimatePolylineFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageSobel2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageSobel2D'
    bl_label = 'vtkImageSobel2D'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageSobel2D)
TYPENAMES.append('BVTK_NT_ImageSobel2D' )


# --------------------------------------------------------------


class BVTK_NT_GenericOutlineFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GenericOutlineFilter'
    bl_label = 'vtkGenericOutlineFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GenericOutlineFilter)
TYPENAMES.append('BVTK_NT_GenericOutlineFilter' )


# --------------------------------------------------------------


class BVTK_NT_PiecewiseFunctionAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PiecewiseFunctionAlgorithm'
    bl_label = 'vtkPiecewiseFunctionAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PiecewiseFunctionAlgorithm)
TYPENAMES.append('BVTK_NT_PiecewiseFunctionAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_ImageToImageStencil(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageToImageStencil'
    bl_label = 'vtkImageToImageStencil'
    
    m_LowerThreshold = bpy.props.FloatProperty(name='LowerThreshold', description='Get the Upper and Lower thresholds', default=-1e+30)
    m_UpperThreshold = bpy.props.FloatProperty(name='UpperThreshold', description='Get the Upper and Lower thresholds', default=1e+30)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_LowerThreshold', 'm_UpperThreshold', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageToImageStencil)
TYPENAMES.append('BVTK_NT_ImageToImageStencil' )


# --------------------------------------------------------------


class BVTK_NT_PolyDataSilhouette(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PolyDataSilhouette'
    bl_label = 'vtkPolyDataSilhouette'
    e_Direction_items = [(x, x, x) for x in ['CameraOrigin', 'CameraVector', 'SpecifiedOrigin', 'SpecifiedVector']]
    
    m_BorderEdges = bpy.props.BoolProperty(name='BorderEdges', description='Enables or Disables generation of border edges. Note: borders exist only in case of non closed surfac', default=True)
    e_Direction = bpy.props.EnumProperty(name='Direction', description='Specify how view direction is computed. By default, the camera origin (eye) is used', default='CameraOrigin', items=e_Direction_items)
    m_EnableFeatureAngle = bpy.props.IntProperty(name='EnableFeatureAngle', description='Enables or Disables generation of silhouette edges along sharp edge', default=1)
    m_FeatureAngle = bpy.props.FloatProperty(name='FeatureAngle', description='Sets/Gets minimal angle for sharp edges detection. Default is 6', default=60.0)
    m_Origin = bpy.props.FloatVectorProperty(name='Origin', description="Set/Get the sort origin. This ivar only has effect if the sort direction is set to SetDirectionToSpecifiedOrigin(). The edge detection occurs in the direction of the origin to each edge's center", default=[0.0, 0.0, 0.0], size=3)
    m_PieceInvariant = bpy.props.BoolProperty(name='PieceInvariant', description='Enables or Disables piece invariance. This is useful when dealing with multi-block data sets. Note: requires one level of ghost cell', default=True)
    m_Vector = bpy.props.FloatVectorProperty(name='Vector', description='Set/Get the sort direction. This ivar only has effect if the sort direction is set to SetDirectionToSpecifiedVector(). The edge detection occurs in the direction of the vector', default=[0.0, 0.0, 0.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BorderEdges', 'e_Direction', 'm_EnableFeatureAngle', 'm_FeatureAngle', 'm_Origin', 'm_PieceInvariant', 'm_Vector', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Prop3D'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PolyDataSilhouette)
TYPENAMES.append('BVTK_NT_PolyDataSilhouette' )


# --------------------------------------------------------------


class BVTK_NT_ExtractTensorComponents(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractTensorComponents'
    bl_label = 'vtkExtractTensorComponents'
    e_ScalarMode_items = [(x, x, x) for x in ['Component', 'Determinant', 'EffectiveStress']]
    
    m_ExtractNormals = bpy.props.BoolProperty(name='ExtractNormals', description='Boolean controls whether normal data is extracted from tensor', default=True)
    m_ExtractScalars = bpy.props.BoolProperty(name='ExtractScalars', description='Boolean controls whether scalar data is extracted from tensor', default=True)
    m_ExtractTCoords = bpy.props.BoolProperty(name='ExtractTCoords', description='Boolean controls whether texture coordinates are extracted from tensor', default=True)
    m_ExtractVectors = bpy.props.BoolProperty(name='ExtractVectors', description='Boolean controls whether vector data is extracted from tensor', default=True)
    m_NormalComponents = bpy.props.IntVectorProperty(name='NormalComponents', description='Specify the ((row,column)0,(row,column)1,(row,column)2) tensor components to extract as a vector', default=[0, 1, 1, 1, 2, 1], size=6)
    m_NormalizeNormals = bpy.props.BoolProperty(name='NormalizeNormals', description='Boolean controls whether normal vector is converted to unit normal after extraction', default=True)
    m_NumberOfTCoords = bpy.props.IntProperty(name='NumberOfTCoords', description='Set the dimension of the texture coordinates to extract', default=2)
    m_PassTensorsToOutput = bpy.props.BoolProperty(name='PassTensorsToOutput', description='Boolean controls whether tensor data is passed through to output', default=True)
    m_ScalarComponents = bpy.props.IntVectorProperty(name='ScalarComponents', description='Specify the (row,column) tensor component to extract as a scalar', default=[0, 0], size=2)
    e_ScalarMode = bpy.props.EnumProperty(name='ScalarMode', description='Specify how to extract the scalar. You can extract it as one of the components of the tensor, as effective stress, or as the determinant of the tensor. If you extract a component make sure that you set the ScalarComponents ivar', default='Component', items=e_ScalarMode_items)
    m_TCoordComponents = bpy.props.IntVectorProperty(name='TCoordComponents', description='Specify the ((row,column)0,(row,column)1,(row,column)2) tensor components to extract as a vector. Up to NumberOfTCoords components are extracted', default=[0, 2, 1, 2, 2, 2], size=6)
    m_VectorComponents = bpy.props.IntVectorProperty(name='VectorComponents', description='Specify the ((row,column)0,(row,column)1,(row,column)2) tensor components to extract as a vector', default=[0, 0, 1, 0, 2, 0], size=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ExtractNormals', 'm_ExtractScalars', 'm_ExtractTCoords', 'm_ExtractVectors', 'm_NormalComponents', 'm_NormalizeNormals', 'm_NumberOfTCoords', 'm_PassTensorsToOutput', 'm_ScalarComponents', 'e_ScalarMode', 'm_TCoordComponents', 'm_VectorComponents', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractTensorComponents)
TYPENAMES.append('BVTK_NT_ExtractTensorComponents' )


# --------------------------------------------------------------


class BVTK_NT_KdTreeSelector(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_KdTreeSelector'
    bl_label = 'vtkKdTreeSelector'
    
    m_SelectionAttribute = bpy.props.IntProperty(name='SelectionAttribute', description='The field attribute to use when generating the selection. If set, creates a PEDIGREEIDS or GLOBALIDS selection. If not set (or is set to -1), creates a INDICES selection. By default this is not set. NOTE: This should be set a constant in vtkDataSetAttributes, not vtkSelection', default=-1)
    m_SelectionBounds = bpy.props.FloatVectorProperty(name='SelectionBounds', description='', default=[0.0, -1.0, 0.0, -1.0, -1e+30, 1e+30], size=6)
    m_SelectionFieldName = bpy.props.StringProperty(name='SelectionFieldName', description='The field name to use when generating the selection. If set, creates a VALUES selection. If not set (or is set to nullptr), creates a INDICES selection. By default this is not set')
    m_SingleSelection = bpy.props.BoolProperty(name='SingleSelection', description='Whether to only allow up to one value in the result. The item selected is closest to the center of the bounds, if there are any points within the selection threshold. Default is off', default=False)
    m_SingleSelectionThreshold = bpy.props.FloatProperty(name='SingleSelectionThreshold', description='The threshold for the single selection. A single point is added to the selection if it is within this threshold from the bounds center. Default is 1', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_SelectionAttribute', 'm_SelectionBounds', 'm_SelectionFieldName', 'm_SingleSelection', 'm_SingleSelectionThreshold', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['KdTree'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_KdTreeSelector)
TYPENAMES.append('BVTK_NT_KdTreeSelector' )


# --------------------------------------------------------------


class BVTK_NT_UndirectedGraphAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_UndirectedGraphAlgorithm'
    bl_label = 'vtkUndirectedGraphAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_UndirectedGraphAlgorithm)
TYPENAMES.append('BVTK_NT_UndirectedGraphAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_HyperTreeGridAxisCut(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperTreeGridAxisCut'
    bl_label = 'vtkHyperTreeGridAxisCut'
    
    m_PlaneNormalAxis = bpy.props.IntProperty(name='PlaneNormalAxis', description='Normal axis: 0=X, 1=Y, 2=Z. Default is ', default=0)
    m_PlanePosition = bpy.props.FloatProperty(name='PlanePosition', description='Position of plane: Axis constant. Default is 0.', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PlaneNormalAxis', 'm_PlanePosition', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperTreeGridAxisCut)
TYPENAMES.append('BVTK_NT_HyperTreeGridAxisCut' )


# --------------------------------------------------------------


class BVTK_NT_OverlappingAMRAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_OverlappingAMRAlgorithm'
    bl_label = 'vtkOverlappingAMRAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_OverlappingAMRAlgorithm)
TYPENAMES.append('BVTK_NT_OverlappingAMRAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_WarpLens(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_WarpLens'
    bl_label = 'vtkWarpLens'
    
    m_FormatHeight = bpy.props.FloatProperty(name='FormatHeight', description='Specify the imager format width / height in m', default=1.0)
    m_FormatWidth = bpy.props.FloatProperty(name='FormatWidth', description='Specify the imager format width / height in m', default=1.0)
    m_ImageHeight = bpy.props.IntProperty(name='ImageHeight', description='Specify the image width / height in pixel', default=1)
    m_ImageWidth = bpy.props.IntProperty(name='ImageWidth', description='Specify the image width / height in pixel', default=1)
    m_K1 = bpy.props.FloatProperty(name='K1', description='Specify the symmetric radial distortion parameters for the len', default=-1e-06)
    m_K2 = bpy.props.FloatProperty(name='K2', description='Specify the symmetric radial distortion parameters for the len', default=0.0)
    m_Kappa = bpy.props.FloatProperty(name='Kappa', description='Specify second order symmetric radial lens distortion parameter. This is obsoleted by newer instance variables', default=-1e-06)
    m_P1 = bpy.props.FloatProperty(name='P1', description='Specify the decentering distortion parameters for the len', default=0.0)
    m_P2 = bpy.props.FloatProperty(name='P2', description='Specify the decentering distortion parameters for the len', default=0.0)
    m_PrincipalPoint = bpy.props.FloatVectorProperty(name='PrincipalPoint', description='Specify the calibrated principal point of the camera/len', default=[0.0, 0.0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FormatHeight', 'm_FormatWidth', 'm_ImageHeight', 'm_ImageWidth', 'm_K1', 'm_K2', 'm_Kappa', 'm_P1', 'm_P2', 'm_PrincipalPoint', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_WarpLens)
TYPENAMES.append('BVTK_NT_WarpLens' )


# --------------------------------------------------------------


class BVTK_NT_DataSetAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataSetAlgorithm'
    bl_label = 'vtkDataSetAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataSetAlgorithm)
TYPENAMES.append('BVTK_NT_DataSetAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_SplineFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SplineFilter'
    bl_label = 'vtkSplineFilter'
    e_GenerateTCoords_items = [(x, x, x) for x in ['NormalizedLength', 'Off', 'UseLength', 'UseScalars']]
    e_Subdivide_items = [(x, x, x) for x in ['Length', 'Specified']]
    
    e_GenerateTCoords = bpy.props.EnumProperty(name='GenerateTCoords', description='Control whether and how texture coordinates are produced. This is useful for striping the output polyline. The texture coordinates can be generated in three ways: a normalized (0,1) generation; based on the length (divided by the texture length); and by using the input scalar values', default='NormalizedLength', items=e_GenerateTCoords_items)
    m_Length = bpy.props.FloatProperty(name='Length', description='Control the number of subdivisions that are created for the polyline based on an absolute length. The length of the spline is divided by this length to determine the number of subdivisions', default=0.1)
    m_MaximumNumberOfSubdivisions = bpy.props.IntProperty(name='MaximumNumberOfSubdivisions', description='Set the maximum number of subdivisions that are created for each polyline', default=1000000000)
    m_NumberOfSubdivisions = bpy.props.IntProperty(name='NumberOfSubdivisions', description='Set the number of subdivisions that are created for the polyline. This method only has effect if Subdivisions is set to SetSubdivisionsToSpecify()', default=100)
    e_Subdivide = bpy.props.EnumProperty(name='Subdivide', description='Specify how the number of subdivisions is determined', default='Specified', items=e_Subdivide_items)
    m_TextureLength = bpy.props.FloatProperty(name='TextureLength', description='Control the conversion of units during the texture coordinates calculation. The TextureLength indicates what length (whether calculated from scalars or length) is mapped to the [0,1) texture space', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_GenerateTCoords', 'm_Length', 'm_MaximumNumberOfSubdivisions', 'm_NumberOfSubdivisions', 'e_Subdivide', 'm_TextureLength', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Spline'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SplineFilter)
TYPENAMES.append('BVTK_NT_SplineFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageStencilAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageStencilAlgorithm'
    bl_label = 'vtkImageStencilAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageStencilAlgorithm)
TYPENAMES.append('BVTK_NT_ImageStencilAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_ImageRGBToHSI(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageRGBToHSI'
    bl_label = 'vtkImageRGBToHSI'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Maximum = bpy.props.FloatProperty(name='Maximum', description='Hue is an angle. Maximum specifies when it maps back to 0. HueMaximum defaults to 255 instead of 2PI, because unsigned char is expected as input. Maximum also specifies the maximum of the Saturation', default=255.0)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Maximum', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageRGBToHSI)
TYPENAMES.append('BVTK_NT_ImageRGBToHSI' )


# --------------------------------------------------------------


class BVTK_NT_ImageVariance3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageVariance3D'
    bl_label = 'vtkImageVariance3D'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageVariance3D)
TYPENAMES.append('BVTK_NT_ImageVariance3D' )


# --------------------------------------------------------------


class BVTK_NT_TemporalInterpolator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TemporalInterpolator'
    bl_label = 'vtkTemporalInterpolator'
    
    m_CacheData = bpy.props.BoolProperty(name='CacheData', description='Controls whether input data is cached to avoid updating input when multiple interpolations are asked between 2 time steps', default=True)
    m_DiscreteTimeStepInterval = bpy.props.FloatProperty(name='DiscreteTimeStepInterval', description="If you require a discrete number of outputs steps, to be generated from an input source - for example, you required N steps separated by T, then set DiscreteTimeStepInterval to T and you will get TIME_RANGE/DiscreteTimeStepInterval steps This is a useful option to use if you have a dataset with one missing time step and wish to 'fill-in' the missing data with an interpolated value from the steps either sid", default=0.0)
    m_ResampleFactor = bpy.props.IntProperty(name='ResampleFactor', description='When ResampleFactor is a non zero positive integer, each pair of input time steps will be interpolated between with the number of steps specified. For example an input of 1,2,3,4,5 and a resample factor of 10, will produce steps 0f 1.0, 1.1, 1.2.....1.9, 2.0 etc NB. Irregular input steps will produce irregular output steps. Resample factor wuill only be used if DiscreteTimeStepInterval is zero otherwise the DiscreteTimeStepInterval takes precedenc', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CacheData', 'm_DiscreteTimeStepInterval', 'm_ResampleFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TemporalInterpolator)
TYPENAMES.append('BVTK_NT_TemporalInterpolator' )


# --------------------------------------------------------------


class BVTK_NT_Delaunay3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Delaunay3D'
    bl_label = 'vtkDelaunay3D'
    
    m_Alpha = bpy.props.FloatProperty(name='Alpha', description='Specify alpha (or distance) value to control output of this filter. For a non-zero alpha value, only verts, edges, faces, or tetra contained within the circumsphere (of radius alpha) will be output. Otherwise, only tetrahedra will be output. Note that the flags AlphaTets, AlphaTris, AlphaLines, and AlphaVerts control whether these primitives are output when Alpha is non-zero. (By default all tets, triangles, lines and verts satisfying the alpha shape criterion are output.', default=0.0)
    m_AlphaLines = bpy.props.BoolProperty(name='AlphaLines', description='Boolean controls whether lines are output for non-zero alpha values', default=True)
    m_AlphaTets = bpy.props.BoolProperty(name='AlphaTets', description='Boolean controls whether tetrahedra are output for non-zero alpha values', default=True)
    m_AlphaTris = bpy.props.BoolProperty(name='AlphaTris', description='Boolean controls whether triangles are output for non-zero alpha values', default=True)
    m_AlphaVerts = bpy.props.BoolProperty(name='AlphaVerts', description='Boolean controls whether vertices are output for non-zero alpha values', default=True)
    m_BoundingTriangulation = bpy.props.BoolProperty(name='BoundingTriangulation', description='Boolean controls whether bounding triangulation points (and associated triangles) are included in the output. (These are introduced as an initial triangulation to begin the triangulation process. This feature is nice for debugging output.', default=True)
    m_Offset = bpy.props.FloatProperty(name='Offset', description='Specify a multiplier to control the size of the initial, bounding Delaunay triangulation', default=2.5)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Specify a tolerance to control discarding of closely spaced points. This tolerance is specified as a fraction of the diagonal length of the bounding box of the points', default=0.001)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Alpha', 'm_AlphaLines', 'm_AlphaTets', 'm_AlphaTris', 'm_AlphaVerts', 'm_BoundingTriangulation', 'm_Offset', 'm_Tolerance', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Delaunay3D)
TYPENAMES.append('BVTK_NT_Delaunay3D' )


# --------------------------------------------------------------


class BVTK_NT_TransformPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransformPolyDataFilter'
    bl_label = 'vtkTransformPolyDataFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Transform'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransformPolyDataFilter)
TYPENAMES.append('BVTK_NT_TransformPolyDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_HyperTreeGridToUnstructuredGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperTreeGridToUnstructuredGrid'
    bl_label = 'vtkHyperTreeGridToUnstructuredGrid'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperTreeGridToUnstructuredGrid)
TYPENAMES.append('BVTK_NT_HyperTreeGridToUnstructuredGrid' )


# --------------------------------------------------------------


class BVTK_NT_TriangleMeshPointNormals(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TriangleMeshPointNormals'
    bl_label = 'vtkTriangleMeshPointNormals'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TriangleMeshPointNormals)
TYPENAMES.append('BVTK_NT_TriangleMeshPointNormals' )


# --------------------------------------------------------------


class BVTK_NT_ImageGradientMagnitude(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageGradientMagnitude'
    bl_label = 'vtkImageGradientMagnitude'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Determines how the input is interpreted (set of 2d slices ...', default=2)
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageGradientMagnitude)
TYPENAMES.append('BVTK_NT_ImageGradientMagnitude' )


# --------------------------------------------------------------


class BVTK_NT_UnsignedDistance(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_UnsignedDistance'
    bl_label = 'vtkUnsignedDistance'
    e_OutputScalarType_items = [(x, x, x) for x in ['Double', 'Float']]
    
    m_AdjustBounds = bpy.props.BoolProperty(name='AdjustBounds', description='Control how the model bounds are computed. If the ivar AdjustBounds is set, then the bounds specified (or computed automatically) is modified by the fraction given by AdjustDistance. This means that the model bounds is expanded in each of the x-y-z directions', default=True)
    m_AdjustDistance = bpy.props.FloatProperty(name='AdjustDistance', description='Specify the amount to grow the model bounds (if the ivar AdjustBounds is set). The value is a fraction of the maximum length of the sides of the box specified by the model bounds', default=0.0125)
    m_Bounds = bpy.props.FloatVectorProperty(name='Bounds', description='Set / get the region in space in which to perform the sampling. If not specified, it will be computed automatically', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6)
    m_CapValue = bpy.props.FloatProperty(name='CapValue', description='Specify the capping value to use. The CapValue is also used as an initial distance value at each point in the dataset. By default, the CapValue is VTK_FLOAT_MAX', default=1e+30)
    m_Capping = bpy.props.BoolProperty(name='Capping', description='The outer boundary of the volume can be assigned a particular value after distances are computed. This can be used to close or "cap" all surfaces during isocontouring', default=True)
    e_OutputScalarType = bpy.props.EnumProperty(name='OutputScalarType', description='Set the desired output scalar type. Currently only real types are supported. By default, VTK_FLOAT scalars are created', default='Float', items=e_OutputScalarType_items)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set / get the radius of influence of each point. Smaller values generally improve performance markedly', default=0.1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AdjustBounds', 'm_AdjustDistance', 'm_Bounds', 'm_CapValue', 'm_Capping', 'e_OutputScalarType', 'm_Radius', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_UnsignedDistance)
TYPENAMES.append('BVTK_NT_UnsignedDistance' )


# --------------------------------------------------------------


class BVTK_NT_TextureMapToPlane(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TextureMapToPlane'
    bl_label = 'vtkTextureMapToPlane'
    
    m_AutomaticPlaneGeneration = bpy.props.BoolProperty(name='AutomaticPlaneGeneration', description='Turn on/off automatic plane generation', default=True)
    m_Normal = bpy.props.FloatVectorProperty(name='Normal', description='Specify plane normal. An alternative way to specify a map plane. Using this method, the object will scale the resulting texture coordinate between the SRange and TRange specified', default=[0.0, 0.0, 1.0], size=3)
    m_Origin = bpy.props.FloatVectorProperty(name='Origin', description='Specify a point defining the origin of the plane. Used in conjunction with the Point1 and Point2 ivars to specify a map plane', default=[0.0, 0.0, 0.0], size=3)
    m_Point1 = bpy.props.FloatVectorProperty(name='Point1', description='Specify a point defining the first axis of the plane', default=[0.0, 0.0, 0.0], size=3)
    m_Point2 = bpy.props.FloatVectorProperty(name='Point2', description='Specify a point defining the second axis of the plane', default=[0.0, 0.0, 0.0], size=3)
    m_SRange = bpy.props.FloatVectorProperty(name='SRange', description='Specify s-coordinate range for texture s-t coordinate pair', default=[0.0, 1.0], size=2)
    m_TRange = bpy.props.FloatVectorProperty(name='TRange', description='Specify t-coordinate range for texture s-t coordinate pair', default=[0.0, 1.0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutomaticPlaneGeneration', 'm_Normal', 'm_Origin', 'm_Point1', 'm_Point2', 'm_SRange', 'm_TRange', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TextureMapToPlane)
TYPENAMES.append('BVTK_NT_TextureMapToPlane' )


# --------------------------------------------------------------


class BVTK_NT_ConnectivityFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ConnectivityFilter'
    bl_label = 'vtkConnectivityFilter'
    e_ExtractionMode_items = [(x, x, x) for x in ['AllRegions', 'CellSeededRegions', 'ClosestPointRegion', 'LargestRegion', 'PointSeededRegions', 'SpecifiedRegions']]
    
    m_ClosestPoint = bpy.props.FloatVectorProperty(name='ClosestPoint', description='Use to specify x-y-z point coordinates when extracting the region closest to a specified point', default=[0.0, 0.0, 0.0], size=3)
    m_ColorRegions = bpy.props.BoolProperty(name='ColorRegions', description='Turn on/off the coloring of connected regions', default=True)
    e_ExtractionMode = bpy.props.EnumProperty(name='ExtractionMode', description='Control the extraction of connected surfaces', default='LargestRegion', items=e_ExtractionMode_items)
    m_ScalarConnectivity = bpy.props.BoolProperty(name='ScalarConnectivity', description='Turn on/off connectivity based on scalar value. If on, cells are connected only if they share points AND one of the cells scalar values falls in the scalar range specified', default=True)
    m_ScalarRange = bpy.props.FloatVectorProperty(name='ScalarRange', description='', default=[0.0, 1.0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClosestPoint', 'm_ColorRegions', 'e_ExtractionMode', 'm_ScalarConnectivity', 'm_ScalarRange', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ConnectivityFilter)
TYPENAMES.append('BVTK_NT_ConnectivityFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageYIQToRGB(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageYIQToRGB'
    bl_label = 'vtkImageYIQToRGB'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Maximum = bpy.props.FloatProperty(name='Maximum', description='', default=255.0)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Maximum', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageYIQToRGB)
TYPENAMES.append('BVTK_NT_ImageYIQToRGB' )


# --------------------------------------------------------------


class BVTK_NT_DataSetRegionSurfaceFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataSetRegionSurfaceFilter'
    bl_label = 'vtkDataSetRegionSurfaceFilter'
    
    m_InterfaceIDsName = bpy.props.StringProperty(name='InterfaceIDsName', description='The name of the field array that has material interface type identifiers in it Default is "interface_ids', default='interface_ids')
    m_MaterialIDsName = bpy.props.StringProperty(name='MaterialIDsName', description='The name of the field array that has material type identifiers in it Default is "material_ids', default='material_ids')
    m_MaterialPIDsName = bpy.props.StringProperty(name='MaterialPIDsName', description='The name of the output field array that records parent materials of each interface Default is "material_ancestors', default='material_ancestors')
    m_MaterialPropertiesName = bpy.props.StringProperty(name='MaterialPropertiesName', description='The name of the field array that has characteristics of each material Default is "material_properties', default='material_properties')
    m_NonlinearSubdivisionLevel = bpy.props.IntProperty(name='NonlinearSubdivisionLevel', description='If the input is an unstructured grid with nonlinear faces, this parameter determines how many times the face is subdivided into linear faces. If 0, the output is the equivalent of its linear couterpart (and the midpoints determining the nonlinear interpolation are discarded). If 1 (the default), the nonlinear face is triangulated based on the midpoints. If greater than 1, the triangulated pieces are recursively subdivided to reach the desired subdivision. Setting the value to greater than 1 may cause some point data to not be passed even if no nonlinear faces exist. This option has no effect if the input is not an unstructured grid', default=1)
    m_OriginalCellIdsName = bpy.props.StringProperty(name='OriginalCellIdsName', description='If PassThroughCellIds or PassThroughPointIds is on, then these ivars control the name given to the field in which the ids are written into. If set to nullptr, then vtkOriginalCellIds or vtkOriginalPointIds (the default) is used, respectively', default='vtkOriginalCellIds')
    m_OriginalPointIdsName = bpy.props.StringProperty(name='OriginalPointIdsName', description='If PassThroughCellIds or PassThroughPointIds is on, then these ivars control the name given to the field in which the ids are written into. If set to nullptr, then vtkOriginalCellIds or vtkOriginalPointIds (the default) is used, respectively', default='vtkOriginalPointIds')
    m_PassThroughCellIds = bpy.props.BoolProperty(name='PassThroughCellIds', description='If on, the output polygonal dataset will have a celldata array that holds the cell index of the original 3D cell that produced each output cell. This is useful for cell picking. The default is off to conserve memory. Note that PassThroughCellIds will be ignored if UseStrips is on, since in that case each tringle strip can represent more than on of the input cells', default=True)
    m_PassThroughPointIds = bpy.props.BoolProperty(name='PassThroughPointIds', description='If on, the output polygonal dataset will have a celldata array that holds the cell index of the original 3D cell that produced each output cell. This is useful for cell picking. The default is off to conserve memory. Note that PassThroughCellIds will be ignored if UseStrips is on, since in that case each tringle strip can represent more than on of the input cells', default=True)
    m_PieceInvariant = bpy.props.IntProperty(name='PieceInvariant', description='If PieceInvariant is true, vtkDataSetSurfaceFilter requests 1 ghost level from input in order to remove internal surface that are between processes. False by default', default=0)
    m_RegionArrayName = bpy.props.StringProperty(name='RegionArrayName', description='The name of the cell based array that we use to extract interfaces from Default is "Regions', default='material')
    m_SingleSided = bpy.props.BoolProperty(name='SingleSided', description='Whether to return single sided material interfaces or double sided Default is singl', default=True)
    m_UseStrips = bpy.props.BoolProperty(name='UseStrips', description='When input is structured data, this flag will generate faces with triangle strips. This should render faster and use less memory, but no cell data is copied. By default, UseStrips is Off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_InterfaceIDsName', 'm_MaterialIDsName', 'm_MaterialPIDsName', 'm_MaterialPropertiesName', 'm_NonlinearSubdivisionLevel', 'm_OriginalCellIdsName', 'm_OriginalPointIdsName', 'm_PassThroughCellIds', 'm_PassThroughPointIds', 'm_PieceInvariant', 'm_RegionArrayName', 'm_SingleSided', 'm_UseStrips', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataSetRegionSurfaceFilter)
TYPENAMES.append('BVTK_NT_DataSetRegionSurfaceFilter' )


# --------------------------------------------------------------


class BVTK_NT_AngularPeriodicFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AngularPeriodicFilter'
    bl_label = 'vtkAngularPeriodicFilter'
    e_IterationMode_items = [(x, x, x) for x in ['DirectNb', 'Max']]
    e_RotationAxis_items = [(x, x, x) for x in ['X', 'Y', 'Z']]
    e_RotationMode_items = [(x, x, x) for x in ['ArrayValue', 'DirectAngle']]
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='', default=[0.0, 0.0, 0.0], size=3)
    m_ComputeRotationsOnTheFly = bpy.props.BoolProperty(name='ComputeRotationsOnTheFly', description='Set/Get whether the rotated array values should be computed on-the-fly (default), which is compute-intensive, or the arrays should be explicitly generated and stored, at the cost of using more memory', default=True)
    e_IterationMode = bpy.props.EnumProperty(name='IterationMode', description='Set/Get Iteration mode. VTK_ITERATION_MODE_DIRECT_NB to specify the number of periods, VTK_ITERATION_MODE_MAX to generate a full period (default)', default='Max', items=e_IterationMode_items)
    m_NumberOfPeriods = bpy.props.IntProperty(name='NumberOfPeriods', description='Set/Get Number of periods. Used only with ITERATION_MODE_DIRECT_NB', default=1)
    m_RotationAngle = bpy.props.FloatProperty(name='RotationAngle', description='Set/Get Rotation angle, in degrees. Used only with VTK_ROTATION_MODE_DIRECT_ANGLE. Default is 180', default=180.0)
    m_RotationArrayName = bpy.props.StringProperty(name='RotationArrayName', description='Set/Get Name of array to get the angle from. Used only with VTK_ROTATION_MODE_ARRAY_VALUE')
    e_RotationAxis = bpy.props.EnumProperty(name='RotationAxis', description='Set/Get Rotation Axis, 0 for X, 1 for Y, 2 for ', default='X', items=e_RotationAxis_items)
    e_RotationMode = bpy.props.EnumProperty(name='RotationMode', description='Set/Get The rotation mode. VTK_ROTATION_MODE_DIRECT_ANGLE to specifiy a angle value (default), VTK_ROTATION_MODE_ARRAY_VALUE to use value from an array in the input dataset', default='DirectAngle', items=e_RotationMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_ComputeRotationsOnTheFly', 'e_IterationMode', 'm_NumberOfPeriods', 'm_RotationAngle', 'm_RotationArrayName', 'e_RotationAxis', 'e_RotationMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AngularPeriodicFilter)
TYPENAMES.append('BVTK_NT_AngularPeriodicFilter' )


# --------------------------------------------------------------


class BVTK_NT_EvenlySpacedStreamlines2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EvenlySpacedStreamlines2D'
    bl_label = 'vtkEvenlySpacedStreamlines2D'
    e_IntegratorType_items = [(x, x, x) for x in ['RungeKutta2', 'RungeKutta4']]
    
    m_ClosedLoopMaximumDistance = bpy.props.FloatProperty(name='ClosedLoopMaximumDistance', description='Loops are considered closed if the have two points at distance less than this. This is expressed in IntegrationStepUnit', default=1e-06)
    m_ComputeVorticity = bpy.props.BoolProperty(name='ComputeVorticity', description='Turn on/off vorticity computation at streamline points (necessary for generating proper stream-ribbons using the vtkRibbonFilter', default=True)
    m_InitialIntegrationStep = bpy.props.FloatProperty(name='InitialIntegrationStep', description='Specify the Initial step size used for line integration, expressed in IntegrationStepUni', default=0.5)
    m_IntegrationStepUnit = bpy.props.IntProperty(name='IntegrationStepUnit', description='Specify a uniform integration step unit for InitialIntegrationStep, and SeparatingDistance. Valid units are LENGTH_UNIT (1) (value is in global coordinates) and CELL_LENGTH_UNIT (2) (the value is in number of cell lengths', default=2)
    e_IntegratorType = bpy.props.EnumProperty(name='IntegratorType', description='Set/get the integrator type to be used for streamline generation. The object passed is not actually used but is cloned with NewInstance in the process of integration (prototype pattern). The default is Runge-Kutta2. The integrator can also be changed using SetIntegratorType. The recognized solvers are: RUNGE_KUTTA2 = 0 RUNGE_KUTTA4 = ', default='RungeKutta2', items=e_IntegratorType_items)
    m_LoopAngle = bpy.props.FloatProperty(name='LoopAngle', description='The angle (in radians) between the vector created by p0p1 and the velocity in the point closing the loop. p0 is the current point and p1 is the point before that. Default value is 20 degrees in radians', default=0.349066)
    m_MaximumNumberOfSteps = bpy.props.IntProperty(name='MaximumNumberOfSteps', description='Specify the maximum number of steps for integrating a streamline', default=2000)
    m_MinimumNumberOfLoopPoints = bpy.props.IntProperty(name='MinimumNumberOfLoopPoints', description="We don't try to eliminate loops with fewer points than this. Default value is 4", default=4)
    m_SeparatingDistance = bpy.props.FloatProperty(name='SeparatingDistance', description='Specify the separation distance between streamlines expressed in IntegrationStepUnit', default=1.0)
    m_SeparatingDistanceRatio = bpy.props.FloatProperty(name='SeparatingDistanceRatio', description='Streamline integration is stoped if streamlines are closer than SeparatingDistance*SeparatingDistanceRatio to other streamlines', default=0.5)
    m_StartPosition = bpy.props.FloatVectorProperty(name='StartPosition', description='', default=[0.0, 0.0, 0.0], size=3)
    m_TerminalSpeed = bpy.props.FloatProperty(name='TerminalSpeed', description='Specify the terminal speed value, below which integration is terminated', default=1e-12)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClosedLoopMaximumDistance', 'm_ComputeVorticity', 'm_InitialIntegrationStep', 'm_IntegrationStepUnit', 'e_IntegratorType', 'm_LoopAngle', 'm_MaximumNumberOfSteps', 'm_MinimumNumberOfLoopPoints', 'm_SeparatingDistance', 'm_SeparatingDistanceRatio', 'm_StartPosition', 'm_TerminalSpeed', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Integrator'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EvenlySpacedStreamlines2D)
TYPENAMES.append('BVTK_NT_EvenlySpacedStreamlines2D' )


# --------------------------------------------------------------


class BVTK_NT_AdaptiveSubdivisionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AdaptiveSubdivisionFilter'
    bl_label = 'vtkAdaptiveSubdivisionFilter'
    
    m_MaximumEdgeLength = bpy.props.FloatProperty(name='MaximumEdgeLength', description='Specify the maximum edge length that a triangle may have. Edges longer than this value are split in half and the associated triangles are modified accordingly', default=1.0)
    m_MaximumNumberOfPasses = bpy.props.IntProperty(name='MaximumNumberOfPasses', description='Set a limit on the number of passes (i.e., levels of subdivision). If the limit is hit, then the subdivision process stops and additional passes (needed to meet other criteria) are aborted. The default limit is set to a very large number (i.e., no effective limit)', default=1000000000)
    m_MaximumNumberOfTriangles = bpy.props.IntProperty(name='MaximumNumberOfTriangles', description='Set a limit on the maximum number of triangles that can be created. If the limit is hit, it may result in premature termination of the algorithm and the results may be less than satisfactory (for example non-watertight meshes may be created). By default, the limit is set to a very large number (i.e., no effective limit)', default=1000000000)
    m_MaximumTriangleArea = bpy.props.FloatProperty(name='MaximumTriangleArea', description='Specify the maximum area that a triangle may have. Triangles larger than this value are subdivided to meet this threshold. Note that if this criterion is used it may produce non-watertight meshes as a result', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MaximumEdgeLength', 'm_MaximumNumberOfPasses', 'm_MaximumNumberOfTriangles', 'm_MaximumTriangleArea', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AdaptiveSubdivisionFilter)
TYPENAMES.append('BVTK_NT_AdaptiveSubdivisionFilter' )


# --------------------------------------------------------------


class BVTK_NT_RectilinearGridClip(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RectilinearGridClip'
    bl_label = 'vtkRectilinearGridClip'
    
    m_ClipData = bpy.props.BoolProperty(name='ClipData', description="By default, ClipData is off, and only the WholeExtent is modified. the data's extent may actually be larger. When this flag is on, the data extent will be no more than the OutputWholeExtent", default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClipData', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RectilinearGridClip)
TYPENAMES.append('BVTK_NT_RectilinearGridClip' )


# --------------------------------------------------------------


class BVTK_NT_ComputeQuartiles(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ComputeQuartiles'
    bl_label = 'vtkComputeQuartiles'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ComputeQuartiles)
TYPENAMES.append('BVTK_NT_ComputeQuartiles' )


# --------------------------------------------------------------


class BVTK_NT_MaskFields(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MaskFields'
    bl_label = 'vtkMaskFields'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MaskFields)
TYPENAMES.append('BVTK_NT_MaskFields' )


# --------------------------------------------------------------


class BVTK_NT_GraphAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GraphAlgorithm'
    bl_label = 'vtkGraphAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GraphAlgorithm)
TYPENAMES.append('BVTK_NT_GraphAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_RecursiveDividingCubes(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RecursiveDividingCubes'
    bl_label = 'vtkRecursiveDividingCubes'
    
    m_Distance = bpy.props.FloatProperty(name='Distance', description='Specify sub-voxel size at which to generate point', default=0.1)
    m_Increment = bpy.props.IntProperty(name='Increment', description='Every "Increment" point is added to the list of points. This parameter, if set to a large value, can be used to limit the number of points while retaining good accuracy', default=1)
    m_Value = bpy.props.FloatProperty(name='Value', description='Set isosurface value', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Distance', 'm_Increment', 'm_Value', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RecursiveDividingCubes)
TYPENAMES.append('BVTK_NT_RecursiveDividingCubes' )


# --------------------------------------------------------------


class BVTK_NT_GraphLayoutFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GraphLayoutFilter'
    bl_label = 'vtkGraphLayoutFilter'
    
    m_AutomaticBoundsComputation = bpy.props.BoolProperty(name='AutomaticBoundsComputation', description="Turn on/off automatic graph bounds calculation. If this boolean is off, then the manually specified GraphBounds is used. If on, then the input's bounds us used as the graph bounds", default=True)
    m_CoolDownRate = bpy.props.FloatProperty(name='CoolDownRate', description='Set/Get the Cool-down rate. The higher this number is, the longer it will take to "cool-down", and thus, the more the graph will be modified', default=10.0)
    m_GraphBounds = bpy.props.FloatVectorProperty(name='GraphBounds', description='Set / get the region in space in which to place the final graph. The GraphBounds only affects the results if AutomaticBoundsComputation is off', default=[-0.5, 0.5, -0.5, 0.5, -0.5, 0.5], size=6)
    m_MaxNumberOfIterations = bpy.props.IntProperty(name='MaxNumberOfIterations', description='Set/Get the maximum number of iterations to be used. The higher this number, the more iterations through the algorithm is possible, and thus, the more the graph gets modified', default=50)
    m_ThreeDimensionalLayout = bpy.props.BoolProperty(name='ThreeDimensionalLayout', description='', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutomaticBoundsComputation', 'm_CoolDownRate', 'm_GraphBounds', 'm_MaxNumberOfIterations', 'm_ThreeDimensionalLayout', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GraphLayoutFilter)
TYPENAMES.append('BVTK_NT_GraphLayoutFilter' )


# --------------------------------------------------------------


class BVTK_NT_TessellatorFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TessellatorFilter'
    bl_label = 'vtkTessellatorFilter'
    
    m_ChordError = bpy.props.FloatProperty(name='ChordError', description="These are convenience routines for setting properties maintained by the tessellator and subdivider. They are implemented here for ParaView's sake", default=0.001)
    m_MaximumNumberOfSubdivisions = bpy.props.IntProperty(name='MaximumNumberOfSubdivisions', description="These are convenience routines for setting properties maintained by the tessellator and subdivider. They are implemented here for ParaView's sake", default=3)
    m_MergePoints = bpy.props.BoolProperty(name='MergePoints', description='The adaptive tessellation will output vertices that are not shared among cells, even where they should be. This can be corrected to some extents with a vtkMergeFilter. By default, the filter is off and vertices will not be shared', default=True)
    m_OutputDimension = bpy.props.IntProperty(name='OutputDimension', description="Set the dimension of the output tessellation. Cells in dimensions higher than the given value will have their boundaries of dimension OutputDimension tessellated. For example, if OutputDimension is 2, a hexahedron's quadrilateral faces would be tessellated rather than its interior", default=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ChordError', 'm_MaximumNumberOfSubdivisions', 'm_MergePoints', 'm_OutputDimension', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Subdivider', 'Tessellator'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TessellatorFilter)
TYPENAMES.append('BVTK_NT_TessellatorFilter' )


# --------------------------------------------------------------


class BVTK_NT_StructuredGridClip(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StructuredGridClip'
    bl_label = 'vtkStructuredGridClip'
    
    m_ClipData = bpy.props.BoolProperty(name='ClipData', description="By default, ClipData is off, and only the WholeExtent is modified. the data's extent may actually be larger. When this flag is on, the data extent will be no more than the OutputWholeExtent", default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClipData', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StructuredGridClip)
TYPENAMES.append('BVTK_NT_StructuredGridClip' )


# --------------------------------------------------------------


class BVTK_NT_PolyDataPointSampler(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PolyDataPointSampler'
    bl_label = 'vtkPolyDataPointSampler'
    
    m_Distance = bpy.props.FloatProperty(name='Distance', description='Set/Get the approximate distance between points. This is an absolute distance measure. The default is 0.01', default=0.01)
    m_GenerateEdgePoints = bpy.props.BoolProperty(name='GenerateEdgePoints', description='Specify/retrieve a boolean flag indicating whether cell edges should be sampled to produce output points. The default is true', default=True)
    m_GenerateInteriorPoints = bpy.props.BoolProperty(name='GenerateInteriorPoints', description='Specify/retrieve a boolean flag indicating whether cell interiors should be sampled to produce output points. The default is true', default=True)
    m_GenerateVertexPoints = bpy.props.BoolProperty(name='GenerateVertexPoints', description='Specify/retrieve a boolean flag indicating whether cell vertex points should be output', default=True)
    m_GenerateVertices = bpy.props.BoolProperty(name='GenerateVertices', description='Specify/retrieve a boolean flag indicating whether cell vertices should be generated. Cell vertices are useful if you actually want to display the points (that is, for each point generated, a vertex is generated). Recall that VTK only renders vertices and not points. The default is true', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Distance', 'm_GenerateEdgePoints', 'm_GenerateInteriorPoints', 'm_GenerateVertexPoints', 'm_GenerateVertices', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PolyDataPointSampler)
TYPENAMES.append('BVTK_NT_PolyDataPointSampler' )


# --------------------------------------------------------------


class BVTK_NT_InterpolateDataSetAttributes(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_InterpolateDataSetAttributes'
    bl_label = 'vtkInterpolateDataSetAttributes'
    
    m_T = bpy.props.FloatProperty(name='T', description='Specify interpolation parameter t', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_T', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_InterpolateDataSetAttributes)
TYPENAMES.append('BVTK_NT_InterpolateDataSetAttributes' )


# --------------------------------------------------------------


class BVTK_NT_AttributeDataToFieldDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AttributeDataToFieldDataFilter'
    bl_label = 'vtkAttributeDataToFieldDataFilter'
    
    m_PassAttributeData = bpy.props.BoolProperty(name='PassAttributeData', description='Turn on/off the passing of point and cell non-field attribute data to the output of the filter', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PassAttributeData', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AttributeDataToFieldDataFilter)
TYPENAMES.append('BVTK_NT_AttributeDataToFieldDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_StructuredGridGhostDataGenerator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StructuredGridGhostDataGenerator'
    bl_label = 'vtkStructuredGridGhostDataGenerator'
    
    m_NumberOfGhostLayers = bpy.props.IntProperty(name='NumberOfGhostLayers', description='Set/Get for number of ghost layers to generate', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NumberOfGhostLayers', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StructuredGridGhostDataGenerator)
TYPENAMES.append('BVTK_NT_StructuredGridGhostDataGenerator' )


# --------------------------------------------------------------


class BVTK_NT_ImageLaplacian(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageLaplacian'
    bl_label = 'vtkImageLaplacian'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Determines how the input is interpreted (set of 2d slices ...', default=2)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageLaplacian)
TYPENAMES.append('BVTK_NT_ImageLaplacian' )


# --------------------------------------------------------------


class BVTK_NT_VoxelContoursToSurfaceFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VoxelContoursToSurfaceFilter'
    bl_label = 'vtkVoxelContoursToSurfaceFilter'
    
    m_MemoryLimitInBytes = bpy.props.IntProperty(name='MemoryLimitInBytes', description='Set / Get the memory limit in bytes for this filter. This is the limit of the size of the structured points data set that is created for intermediate processing. The data will be streamed through this volume in as many pieces as necessary', default=10000000)
    m_Spacing = bpy.props.FloatVectorProperty(name='Spacing', description='', default=[1.0, 1.0, 1.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MemoryLimitInBytes', 'm_Spacing', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VoxelContoursToSurfaceFilter)
TYPENAMES.append('BVTK_NT_VoxelContoursToSurfaceFilter' )


# --------------------------------------------------------------


class BVTK_NT_PProjectSphereFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PProjectSphereFilter'
    bl_label = 'vtkPProjectSphereFilter'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set the center of the sphere to be split. Default is 0,0,0', default=[0.0, 0.0, 0.0], size=3)
    m_KeepPolePoints = bpy.props.BoolProperty(name='KeepPolePoints', description='Specify whether or not to keep the cells using a point at a pole. The default is false', default=False)
    m_TranslateZ = bpy.props.BoolProperty(name='TranslateZ', description='Specify whether (true) or not to translate the points in the projected transformation such that the input point with the smallest radius is at 0. The default is false', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_KeepPolePoints', 'm_TranslateZ', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PProjectSphereFilter)
TYPENAMES.append('BVTK_NT_PProjectSphereFilter' )


# --------------------------------------------------------------


class BVTK_NT_IdFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_IdFilter'
    bl_label = 'vtkIdFilter'
    
    m_CellIds = bpy.props.BoolProperty(name='CellIds', description='Enable/disable the generation of point ids. Default is on', default=True)
    m_FieldData = bpy.props.BoolProperty(name='FieldData', description='Set/Get the flag which controls whether to generate scalar data or field data. If this flag is off, scalar data is generated. Otherwise, field data is generated. Default is off', default=True)
    m_IdsArrayName = bpy.props.StringProperty(name='IdsArrayName', description='Set/Get the name of the Ids array if generated. By default the Ids are named "vtkIdFilter_Ids", but this can be changed with this function', default='vtkIdFilter_Ids')
    m_PointIds = bpy.props.BoolProperty(name='PointIds', description='Enable/disable the generation of point ids. Default is on', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CellIds', 'm_FieldData', 'm_IdsArrayName', 'm_PointIds', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_IdFilter)
TYPENAMES.append('BVTK_NT_IdFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageSlab(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageSlab'
    bl_label = 'vtkImageSlab'
    e_Operation_items = [(x, x, x) for x in ['Max', 'Mean', 'Min', 'Sum']]
    e_Orientation_items = [(x, x, x) for x in ['X', 'Y', 'Z']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_MultiSliceOutput = bpy.props.BoolProperty(name='MultiSliceOutput', description="Turn on multi-slice output. Each slice of the output will be a projection through the specified range of input slices, e.g. if the SliceRange is [0,3] then slice 'i' of the output will be a projection through slices 'i' through '3+i' of the input. This flag is off by default", default=True)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_Operation = bpy.props.EnumProperty(name='Operation', description='Set the operation to use when combining slices. The choices are "Mean", "Sum", "Min", "Max". The default is "Mean"', default='Mean', items=e_Operation_items)
    e_Orientation = bpy.props.EnumProperty(name='Orientation', description='Set the slice direction: zero for x, 1 for y, 2 for z. The default is the Z direction', default='Z', items=e_Orientation_items)
    m_SliceRange = bpy.props.IntVectorProperty(name='SliceRange', description='', default=[-1000000000, 1000000000], size=2)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_TrapezoidIntegration = bpy.props.BoolProperty(name='TrapezoidIntegration', description='Use trapezoid integration for slab computation. This weighs the first and last slices by half when doing sum and mean, as compared to the default midpoint integration that weighs all slices equally. It is off by default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_MultiSliceOutput', 'm_NumberOfThreads', 'e_Operation', 'e_Orientation', 'm_SliceRange', 'e_SplitMode', 'm_TrapezoidIntegration', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageSlab)
TYPENAMES.append('BVTK_NT_ImageSlab' )


# --------------------------------------------------------------


class BVTK_NT_PPolyDataNormals(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PPolyDataNormals'
    bl_label = 'vtkPPolyDataNormals'
    
    m_AutoOrientNormals = bpy.props.BoolProperty(name='AutoOrientNormals', description='Turn on/off the automatic determination of correct normal orientation. NOTE: This assumes a completely closed surface (i.e. no boundary edges) and no non-manifold edges. If these constraints do not hold, all bets are off. This option adds some computational complexity, and is useful if you don\'t want to have to inspect the rendered image to determine whether to turn on the FlipNormals flag. However, this flag can work with the FlipNormals flag, and if both are set, all the normals in the output will point "inward"', default=True)
    m_ComputeCellNormals = bpy.props.BoolProperty(name='ComputeCellNormals', description='Turn on/off the computation of cell normals', default=True)
    m_ComputePointNormals = bpy.props.BoolProperty(name='ComputePointNormals', description='Turn on/off the computation of point normals', default=True)
    m_Consistency = bpy.props.BoolProperty(name='Consistency', description='Turn on/off the enforcement of consistent polygon ordering', default=True)
    m_FeatureAngle = bpy.props.FloatProperty(name='FeatureAngle', description='Specify the angle that defines a sharp edge. If the difference in angle across neighboring polygons is greater than this value, the shared edge is considered "sharp"', default=30.0)
    m_FlipNormals = bpy.props.BoolProperty(name='FlipNormals', description="Turn on/off the global flipping of normal orientation. Flipping reverves the meaning of front and back for Frontface and Backface culling in vtkProperty. Flipping modifies both the normal direction and the order of a cell's points", default=True)
    m_NonManifoldTraversal = bpy.props.BoolProperty(name='NonManifoldTraversal', description='Turn on/off traversal across non-manifold edges. This will prevent problems where the consistency of polygonal ordering is corrupted due to topological loops', default=True)
    m_PieceInvariant = bpy.props.BoolProperty(name='PieceInvariant', description='To get piece invariance, this filter has to request an extra ghost level. By default piece invariance is on', default=True)
    m_Splitting = bpy.props.BoolProperty(name='Splitting', description='Turn on/off the splitting of sharp edges', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutoOrientNormals', 'm_ComputeCellNormals', 'm_ComputePointNormals', 'm_Consistency', 'm_FeatureAngle', 'm_FlipNormals', 'm_NonManifoldTraversal', 'm_PieceInvariant', 'm_Splitting', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PPolyDataNormals)
TYPENAMES.append('BVTK_NT_PPolyDataNormals' )


# --------------------------------------------------------------


class BVTK_NT_DataSetTriangleFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataSetTriangleFilter'
    bl_label = 'vtkDataSetTriangleFilter'
    
    m_TetrahedraOnly = bpy.props.BoolProperty(name='TetrahedraOnly', description='When On this filter will cull all 1D and 2D cells from the output. The default is Off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_TetrahedraOnly', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataSetTriangleFilter)
TYPENAMES.append('BVTK_NT_DataSetTriangleFilter' )


# --------------------------------------------------------------


class BVTK_NT_VertexGlyphFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VertexGlyphFilter'
    bl_label = 'vtkVertexGlyphFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VertexGlyphFilter)
TYPENAMES.append('BVTK_NT_VertexGlyphFilter' )


# --------------------------------------------------------------


class BVTK_NT_PolyDataConnectivityFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PolyDataConnectivityFilter'
    bl_label = 'vtkPolyDataConnectivityFilter'
    e_ExtractionMode_items = [(x, x, x) for x in ['AllRegions', 'CellSeededRegions', 'ClosestPointRegion', 'LargestRegion', 'PointSeededRegions', 'SpecifiedRegions']]
    
    m_ClosestPoint = bpy.props.FloatVectorProperty(name='ClosestPoint', description='Use to specify x-y-z point coordinates when extracting the region closest to a specified point', default=[0.0, 0.0, 0.0], size=3)
    m_ColorRegions = bpy.props.BoolProperty(name='ColorRegions', description='Turn on/off the coloring of connected regions', default=True)
    e_ExtractionMode = bpy.props.EnumProperty(name='ExtractionMode', description='Control the extraction of connected surfaces', default='LargestRegion', items=e_ExtractionMode_items)
    m_FullScalarConnectivity = bpy.props.BoolProperty(name='FullScalarConnectivity', description="Turn on/off the use of Fully connected scalar connectivity. This is off by default. The flag is used only if ScalarConnectivity is on. If FullScalarConnectivity is ON, all the cell's points must lie in the scalar range specified for the cell to qualify as being connected. If FullScalarConnectivity is OFF, any one of the cell's points may lie in the user specified scalar range for the cell to qualify as being connected", default=True)
    m_MarkVisitedPointIds = bpy.props.BoolProperty(name='MarkVisitedPointIds', description='Mark visited point ids ? It may be useful to extract the visited point ids for use by a downstream filter. Default is OFF', default=True)
    m_ScalarConnectivity = bpy.props.BoolProperty(name='ScalarConnectivity', description='Turn on/off connectivity based on scalar value. If on, cells are connected only if they share points AND one of the cells scalar values falls in the scalar range specified', default=True)
    m_ScalarRange = bpy.props.FloatVectorProperty(name='ScalarRange', description='', default=[0.0, 1.0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClosestPoint', 'm_ColorRegions', 'e_ExtractionMode', 'm_FullScalarConnectivity', 'm_MarkVisitedPointIds', 'm_ScalarConnectivity', 'm_ScalarRange', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PolyDataConnectivityFilter)
TYPENAMES.append('BVTK_NT_PolyDataConnectivityFilter' )


# --------------------------------------------------------------


class BVTK_NT_WindowedSincPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_WindowedSincPolyDataFilter'
    bl_label = 'vtkWindowedSincPolyDataFilter'
    
    m_BoundarySmoothing = bpy.props.BoolProperty(name='BoundarySmoothing', description='Turn on/off the smoothing of vertices on the boundary of the mesh', default=True)
    m_EdgeAngle = bpy.props.FloatProperty(name='EdgeAngle', description='Specify the edge angle to control smoothing along edges (either interior or boundary)', default=15.0)
    m_FeatureAngle = bpy.props.FloatProperty(name='FeatureAngle', description='Specify the feature angle for sharp edge identification', default=45.0)
    m_FeatureEdgeSmoothing = bpy.props.BoolProperty(name='FeatureEdgeSmoothing', description='Turn on/off smoothing along sharp interior edges', default=True)
    m_GenerateErrorScalars = bpy.props.BoolProperty(name='GenerateErrorScalars', description='Turn on/off the generation of scalar distance values', default=True)
    m_GenerateErrorVectors = bpy.props.BoolProperty(name='GenerateErrorVectors', description='Turn on/off the generation of error vectors', default=True)
    m_NonManifoldSmoothing = bpy.props.BoolProperty(name='NonManifoldSmoothing', description='Smooth non-manifold vertices', default=True)
    m_NormalizeCoordinates = bpy.props.BoolProperty(name='NormalizeCoordinates', description='Turn on/off coordinate normalization. The positions can be translated and scaled such that they fit within a [-1, 1] prior to the smoothing computation. The default is off. The numerical stability of the solution can be improved by turning normalization on. If normalization is on, the coordinates will be rescaled to the original coordinate system after smoothing has completed', default=True)
    m_NumberOfIterations = bpy.props.IntProperty(name='NumberOfIterations', description='Specify the number of iterations (or degree of the polynomial approximating the windowed sinc function)', default=20)
    m_PassBand = bpy.props.FloatProperty(name='PassBand', description='Set the passband value for the windowed sinc filte', default=0.1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BoundarySmoothing', 'm_EdgeAngle', 'm_FeatureAngle', 'm_FeatureEdgeSmoothing', 'm_GenerateErrorScalars', 'm_GenerateErrorVectors', 'm_NonManifoldSmoothing', 'm_NormalizeCoordinates', 'm_NumberOfIterations', 'm_PassBand', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_WindowedSincPolyDataFilter)
TYPENAMES.append('BVTK_NT_WindowedSincPolyDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageRGBToHSV(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageRGBToHSV'
    bl_label = 'vtkImageRGBToHSV'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Maximum = bpy.props.FloatProperty(name='Maximum', description='', default=255.0)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Maximum', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageRGBToHSV)
TYPENAMES.append('BVTK_NT_ImageRGBToHSV' )


# --------------------------------------------------------------


class BVTK_NT_RandomAttributeGenerator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RandomAttributeGenerator'
    bl_label = 'vtkRandomAttributeGenerator'
    
    m_AttributesConstantPerBlock = bpy.props.BoolProperty(name='AttributesConstantPerBlock', description='Indicate that the generated attributes are constant within a block. This can be used to highlight blocks in a composite dataset', default=False)
    m_GenerateCellArray = bpy.props.BoolProperty(name='GenerateCellArray', description='Indicate that an arbitrary cell array is to be generated. Note that the specified number of components is used to create the array', default=True)
    m_GenerateCellNormals = bpy.props.BoolProperty(name='GenerateCellNormals', description='Indicate that cell normals are to be generated. Note that the number of components is always equal to three', default=True)
    m_GenerateCellScalars = bpy.props.BoolProperty(name='GenerateCellScalars', description='Indicate that cell scalars are to be generated. Note that the specified number of components is used to create the scalar', default=True)
    m_GenerateCellTCoords = bpy.props.BoolProperty(name='GenerateCellTCoords', description='Indicate that cell texture coordinates are to be generated. Note that the specified number of components is used to create the texture coordinates (but must range between one and three)', default=True)
    m_GenerateCellTensors = bpy.props.BoolProperty(name='GenerateCellTensors', description='Indicate that cell tensors are to be generated. Note that the number of components is always equal to nine', default=True)
    m_GenerateCellVectors = bpy.props.BoolProperty(name='GenerateCellVectors', description='Indicate that cell vectors are to be generated. Note that the number of components is always equal to three', default=True)
    m_GenerateFieldArray = bpy.props.BoolProperty(name='GenerateFieldArray', description='Indicate that an arbitrary field data array is to be generated. Note that the specified number of components is used to create the scalar', default=True)
    m_GeneratePointArray = bpy.props.BoolProperty(name='GeneratePointArray', description='Indicate that an arbitrary point array is to be generated. Note that the specified number of components is used to create the array', default=True)
    m_GeneratePointNormals = bpy.props.BoolProperty(name='GeneratePointNormals', description='Indicate that point normals are to be generated. Note that the number of components is always equal to three', default=True)
    m_GeneratePointScalars = bpy.props.BoolProperty(name='GeneratePointScalars', description='Indicate that point scalars are to be generated. Note that the specified number of components is used to create the scalar', default=True)
    m_GeneratePointTCoords = bpy.props.BoolProperty(name='GeneratePointTCoords', description='Indicate that point texture coordinates are to be generated. Note that the specified number of components is used to create the texture coordinates (but must range between one and three)', default=True)
    m_GeneratePointTensors = bpy.props.BoolProperty(name='GeneratePointTensors', description='Indicate that point tensors are to be generated. Note that the number of components is always equal to nine', default=True)
    m_GeneratePointVectors = bpy.props.BoolProperty(name='GeneratePointVectors', description='Indicate that point vectors are to be generated. Note that the number of components is always equal to three', default=True)
    m_MaximumComponentValue = bpy.props.FloatProperty(name='MaximumComponentValue', description='Set the maximum component value. This applies to all data that is generated, although normals and tensors have internal constraints that must be observed', default=1.0)
    m_MinimumComponentValue = bpy.props.FloatProperty(name='MinimumComponentValue', description='Set the minimum component value. This applies to all data that is generated, although normals and tensors have internal constraints that must be observed', default=0.0)
    m_NumberOfComponents = bpy.props.IntProperty(name='NumberOfComponents', description='Specify the number of components to generate. This value only applies to those attribute types that take a variable number of components. For example, a vector is only three components so the number of components is not applicable; whereas a scalar may support multiple, varying number of components', default=1)
    m_NumberOfTuples = bpy.props.IntProperty(name='NumberOfTuples', description='Specify the number of tuples to generate. This value only applies when creating general field data. In all other cases (i.e., point data or cell data), the number of tuples is controlled by the number of points and cells, respectively', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AttributesConstantPerBlock', 'm_GenerateCellArray', 'm_GenerateCellNormals', 'm_GenerateCellScalars', 'm_GenerateCellTCoords', 'm_GenerateCellTensors', 'm_GenerateCellVectors', 'm_GenerateFieldArray', 'm_GeneratePointArray', 'm_GeneratePointNormals', 'm_GeneratePointScalars', 'm_GeneratePointTCoords', 'm_GeneratePointTensors', 'm_GeneratePointVectors', 'm_MaximumComponentValue', 'm_MinimumComponentValue', 'm_NumberOfComponents', 'm_NumberOfTuples', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RandomAttributeGenerator)
TYPENAMES.append('BVTK_NT_RandomAttributeGenerator' )


# --------------------------------------------------------------


class BVTK_NT_PolyDataToImageStencil(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PolyDataToImageStencil'
    bl_label = 'vtkPolyDataToImageStencil'
    
    m_OutputOrigin = bpy.props.FloatVectorProperty(name='OutputOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    m_OutputSpacing = bpy.props.FloatVectorProperty(name='OutputSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_OutputWholeExtent = bpy.props.IntVectorProperty(name='OutputWholeExtent', description='', default=[0, -1, 0, -1, 0, -1], size=6)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='The tolerance for including a voxel inside the stencil. This is in fractions of a voxel, and must be between 0 and 1. Tolerance is only applied in the x and y directions, not in z. Setting the tolerance to zero disables all tolerance checks and might result in faster performance', default=7.62939453125e-06)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_OutputOrigin', 'm_OutputSpacing', 'm_OutputWholeExtent', 'm_Tolerance', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PolyDataToImageStencil)
TYPENAMES.append('BVTK_NT_PolyDataToImageStencil' )


# --------------------------------------------------------------


class BVTK_NT_AnnotationLayersAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AnnotationLayersAlgorithm'
    bl_label = 'vtkAnnotationLayersAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AnnotationLayersAlgorithm)
TYPENAMES.append('BVTK_NT_AnnotationLayersAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_AppendPoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AppendPoints'
    bl_label = 'vtkAppendPoints'
    
    m_InputIdArrayName = bpy.props.StringProperty(name='InputIdArrayName', description='Sets the output array name to fill with the input connection index for each point. This provides a way to trace a point back to a particular input. If this is nullptr (the default), the array is not generated')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_InputIdArrayName', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AppendPoints)
TYPENAMES.append('BVTK_NT_AppendPoints' )


# --------------------------------------------------------------


class BVTK_NT_ResampleToImage(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ResampleToImage'
    bl_label = 'vtkResampleToImage'
    
    m_SamplingBounds = bpy.props.FloatVectorProperty(name='SamplingBounds', description='', default=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0], size=6)
    m_SamplingDimensions = bpy.props.IntVectorProperty(name='SamplingDimensions', description='', default=[10, 10, 10], size=3)
    m_UseInputBounds = bpy.props.BoolProperty(name='UseInputBounds', description='Set/Get if the filter should use Input bounds to sub-sample the data. By default it is set to 1', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_SamplingBounds', 'm_SamplingDimensions', 'm_UseInputBounds', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ResampleToImage)
TYPENAMES.append('BVTK_NT_ResampleToImage' )


# --------------------------------------------------------------


class BVTK_NT_TemporalArrayOperatorFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TemporalArrayOperatorFilter'
    bl_label = 'vtkTemporalArrayOperatorFilter'
    
    m_FirstTimeStepIndex = bpy.props.IntProperty(name='FirstTimeStepIndex', description='Set/Get the first time step', default=0)
    m_Operator = bpy.props.IntProperty(name='Operator', description='Set/Get the operator to apply. Default is ADD (0)', default=0)
    m_OutputArrayNameSuffix = bpy.props.StringProperty(name='OutputArrayNameSuffix', description="Set/Get the suffix to be append to the output array name. If not specified, output will be suffixed with '_' and the operation type (eg. myarrayname_add)")
    m_SecondTimeStepIndex = bpy.props.IntProperty(name='SecondTimeStepIndex', description='Set/Get the second time step', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FirstTimeStepIndex', 'm_Operator', 'm_OutputArrayNameSuffix', 'm_SecondTimeStepIndex', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TemporalArrayOperatorFilter)
TYPENAMES.append('BVTK_NT_TemporalArrayOperatorFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageCast(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageCast'
    bl_label = 'vtkImageCast'
    e_OutputScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Long', 'Short', 'UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_ClampOverflow = bpy.props.BoolProperty(name='ClampOverflow', description='When the ClampOverflow flag is on, the data is thresholded so that the output value does not exceed the max or min of the data type. Clamping is safer because otherwise you might invoke undefined behavior (and may crash) if the type conversion is out of range of the data type. On the other hand, clamping is slower. By default ClampOverflow is off', default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_OutputScalarType = bpy.props.EnumProperty(name='OutputScalarType', description='Set the desired output scalar type to cast to', default='Float', items=e_OutputScalarType_items)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClampOverflow', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_OutputScalarType', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageCast)
TYPENAMES.append('BVTK_NT_ImageCast' )


# --------------------------------------------------------------


class BVTK_NT_ExtractPointCloudPiece(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractPointCloudPiece'
    bl_label = 'vtkExtractPointCloudPiece'
    
    m_ModuloOrdering = bpy.props.BoolProperty(name='ModuloOrdering', description='Turn on or off modulo sampling of the points. By default this is on and the points in a given piece will be reordered in an attempt to reduce spatial coherency', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ModuloOrdering', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractPointCloudPiece)
TYPENAMES.append('BVTK_NT_ExtractPointCloudPiece' )


# --------------------------------------------------------------


class BVTK_NT_HyperTreeGridCellCenters(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperTreeGridCellCenters'
    bl_label = 'vtkHyperTreeGridCellCenters'
    
    m_VertexCells = bpy.props.BoolProperty(name='VertexCells', description='Enable/disable the generation of vertex cells. The default is Off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_VertexCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperTreeGridCellCenters)
TYPENAMES.append('BVTK_NT_HyperTreeGridCellCenters' )


# --------------------------------------------------------------


class BVTK_NT_DataObjectAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataObjectAlgorithm'
    bl_label = 'vtkDataObjectAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataObjectAlgorithm)
TYPENAMES.append('BVTK_NT_DataObjectAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_VolumeRayCastSpaceLeapingImageFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VolumeRayCastSpaceLeapingImageFilter'
    bl_label = 'vtkVolumeRayCastSpaceLeapingImageFilter'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_ComputeGradientOpacity = bpy.props.BoolProperty(name='ComputeGradientOpacity', description='Compute gradient opacity ', default=True)
    m_ComputeMinMax = bpy.props.BoolProperty(name='ComputeMinMax', description='Compute the min max structure ?', default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_IndependentComponents = bpy.props.IntProperty(name='IndependentComponents', description='Do we use independent components, or dependent components ', default=1)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_TableScale = bpy.props.FloatVectorProperty(name='TableScale', description='', default=[1.0, 1.0, 1.0, 1.0], size=4)
    m_TableShift = bpy.props.FloatVectorProperty(name='TableShift', description='', default=[0.0, 0.0, 0.0, 0.0], size=4)
    m_TableSize = bpy.props.IntVectorProperty(name='TableSize', description='', default=[0, 0, 0, 0], size=4)
    m_UpdateGradientOpacityFlags = bpy.props.BoolProperty(name='UpdateGradientOpacityFlags', description='Update the gradient opacity flags. (The scalar opacity flags are always updated upon execution of this filter.', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradientOpacity', 'm_ComputeMinMax', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_IndependentComponents', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', 'm_TableScale', 'm_TableShift', 'm_TableSize', 'm_UpdateGradientOpacityFlags', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['CurrentScalars'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VolumeRayCastSpaceLeapingImageFilter)
TYPENAMES.append('BVTK_NT_VolumeRayCastSpaceLeapingImageFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageOpenClose3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageOpenClose3D'
    bl_label = 'vtkImageOpenClose3D'
    
    m_CloseValue = bpy.props.FloatProperty(name='CloseValue', description='Determines the value that will closed. Close value is first dilated, and then erode', default=255.0)
    m_OpenValue = bpy.props.FloatProperty(name='OpenValue', description='Determines the value that will opened. Open value is first eroded, and then dilated', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CloseValue', 'm_OpenValue', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageOpenClose3D)
TYPENAMES.append('BVTK_NT_ImageOpenClose3D' )


# --------------------------------------------------------------


class BVTK_NT_NonOverlappingAMRAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_NonOverlappingAMRAlgorithm'
    bl_label = 'vtkNonOverlappingAMRAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_NonOverlappingAMRAlgorithm)
TYPENAMES.append('BVTK_NT_NonOverlappingAMRAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_PassThrough(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PassThrough'
    bl_label = 'vtkPassThrough'
    
    m_AllowNullInput = bpy.props.BoolProperty(name='AllowNullInput', description='', default=False)
    m_DeepCopyInput = bpy.props.BoolProperty(name='DeepCopyInput', description="Whether or not to deep copy the input. This can be useful if you want to create a copy of a data object. You can then disconnect this filter's input connections and it will act like a source. Defaults to OFF", default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AllowNullInput', 'm_DeepCopyInput', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PassThrough)
TYPENAMES.append('BVTK_NT_PassThrough' )


# --------------------------------------------------------------


class BVTK_NT_ImageExtractComponents(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageExtractComponents'
    bl_label = 'vtkImageExtractComponents'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageExtractComponents)
TYPENAMES.append('BVTK_NT_ImageExtractComponents' )


# --------------------------------------------------------------


class BVTK_NT_ImageDivergence(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageDivergence'
    bl_label = 'vtkImageDivergence'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageDivergence)
TYPENAMES.append('BVTK_NT_ImageDivergence' )


# --------------------------------------------------------------


class BVTK_NT_MoleculeAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MoleculeAlgorithm'
    bl_label = 'vtkMoleculeAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MoleculeAlgorithm)
TYPENAMES.append('BVTK_NT_MoleculeAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_ContourGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ContourGrid'
    bl_label = 'vtkContourGrid'
    
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description="Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off. @deprecated ComputeGradients is not used so these methods don't affect anything (VTK 6.0)", default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_GenerateTriangles = bpy.props.BoolProperty(name='GenerateTriangles', description='If this is enabled (by default), the output will be triangles otherwise, the output will be the intersection polygons WARNING: if the cutting function is not a plane, the output will be 3D poygons, which might be nice to look at but hard to compute with downstream', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Methods to set / get contour values', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_GenerateTriangles', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ContourGrid)
TYPENAMES.append('BVTK_NT_ContourGrid' )


# --------------------------------------------------------------


class BVTK_NT_StructuredGridAppend(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StructuredGridAppend'
    bl_label = 'vtkStructuredGridAppend'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StructuredGridAppend)
TYPENAMES.append('BVTK_NT_StructuredGridAppend' )


# --------------------------------------------------------------


class BVTK_NT_QuantizePolyDataPoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_QuantizePolyDataPoints'
    bl_label = 'vtkQuantizePolyDataPoints'
    
    m_AbsoluteTolerance = bpy.props.FloatProperty(name='AbsoluteTolerance', description='Specify tolerance in absolute terms. Default is 1.0', default=1.0)
    m_ConvertLinesToPoints = bpy.props.BoolProperty(name='ConvertLinesToPoints', description='Turn on/off conversion of degenerate lines to points. Default is On', default=True)
    m_ConvertPolysToLines = bpy.props.BoolProperty(name='ConvertPolysToLines', description='Turn on/off conversion of degenerate polys to lines. Default is On', default=True)
    m_ConvertStripsToPolys = bpy.props.BoolProperty(name='ConvertStripsToPolys', description='Turn on/off conversion of degenerate strips to polys. Default is On', default=True)
    m_PieceInvariant = bpy.props.BoolProperty(name='PieceInvariant', description='', default=True)
    m_PointMerging = bpy.props.BoolProperty(name='PointMerging', description='Set/Get a boolean value that controls whether point merging is performed. If on, a locator will be used, and points laying within the appropriate tolerance may be merged. If off, points are never merged. By default, merging is on', default=True)
    m_QFactor = bpy.props.FloatProperty(name='QFactor', description='Specify quantization grain size. Default is 0.2', default=0.25)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Specify tolerance in terms of fraction of bounding box length. Default is 0.0', default=0.0)
    m_ToleranceIsAbsolute = bpy.props.BoolProperty(name='ToleranceIsAbsolute', description='By default ToleranceIsAbsolute is false and Tolerance is a fraction of Bounding box diagonal, if true, AbsoluteTolerance is used when adding points to locator (merging', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AbsoluteTolerance', 'm_ConvertLinesToPoints', 'm_ConvertPolysToLines', 'm_ConvertStripsToPolys', 'm_PieceInvariant', 'm_PointMerging', 'm_QFactor', 'm_Tolerance', 'm_ToleranceIsAbsolute', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_QuantizePolyDataPoints)
TYPENAMES.append('BVTK_NT_QuantizePolyDataPoints' )


# --------------------------------------------------------------


class BVTK_NT_ButterflySubdivisionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ButterflySubdivisionFilter'
    bl_label = 'vtkButterflySubdivisionFilter'
    
    m_CheckForTriangles = bpy.props.BoolProperty(name='CheckForTriangles', description='Set/get CheckForTriangles Should subdivision check that the dataset only contains triangles? Default is On (1)', default=True)
    m_NumberOfSubdivisions = bpy.props.IntProperty(name='NumberOfSubdivisions', description='Set/get the number of subdivisions. Default is 1', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CheckForTriangles', 'm_NumberOfSubdivisions', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ButterflySubdivisionFilter)
TYPENAMES.append('BVTK_NT_ButterflySubdivisionFilter' )


# --------------------------------------------------------------


class BVTK_NT_RectilinearGridToPointSet(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RectilinearGridToPointSet'
    bl_label = 'vtkRectilinearGridToPointSet'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RectilinearGridToPointSet)
TYPENAMES.append('BVTK_NT_RectilinearGridToPointSet' )


# --------------------------------------------------------------


class BVTK_NT_ShrinkFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ShrinkFilter'
    bl_label = 'vtkShrinkFilter'
    
    m_ShrinkFactor = bpy.props.FloatProperty(name='ShrinkFactor', description='Get/Set the fraction of shrink for each cell. The default is 0.5', default=0.5)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ShrinkFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ShrinkFilter)
TYPENAMES.append('BVTK_NT_ShrinkFilter' )


# --------------------------------------------------------------


class BVTK_NT_ElevationFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ElevationFilter'
    bl_label = 'vtkElevationFilter'
    
    m_HighPoint = bpy.props.FloatVectorProperty(name='HighPoint', description='Define other end of the line (large scalar values). Default is (0,0,1)', default=[0.0, 0.0, 1.0], size=3)
    m_LowPoint = bpy.props.FloatVectorProperty(name='LowPoint', description='Define one end of the line (small scalar values). Default is (0,0,0)', default=[0.0, 0.0, 0.0], size=3)
    m_ScalarRange = bpy.props.FloatVectorProperty(name='ScalarRange', description='Specify range to map scalars into. Default is [0, 1]', default=[0.0, 1.0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_HighPoint', 'm_LowPoint', 'm_ScalarRange', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ElevationFilter)
TYPENAMES.append('BVTK_NT_ElevationFilter' )


# --------------------------------------------------------------


class BVTK_NT_UnstructuredGridGeometryFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_UnstructuredGridGeometryFilter'
    bl_label = 'vtkUnstructuredGridGeometryFilter'
    
    m_CellClipping = bpy.props.BoolProperty(name='CellClipping', description='Turn on/off selection of geometry by cell id', default=True)
    m_CellMaximum = bpy.props.IntProperty(name='CellMaximum', description='Specify the maximum cell id for point id selection', default=1000000000)
    m_CellMinimum = bpy.props.IntProperty(name='CellMinimum', description='Specify the minimum cell id for point id selection', default=0)
    m_DuplicateGhostCellClipping = bpy.props.BoolProperty(name='DuplicateGhostCellClipping', description='Turn on/off clipping of ghost cells with type vtkDataSetAttributes::DUPLICATECELL. Defaults to on', default=True)
    m_ExtentClipping = bpy.props.BoolProperty(name='ExtentClipping', description='Turn on/off selection of geometry via bounding box', default=True)
    m_Merging = bpy.props.BoolProperty(name='Merging', description='Turn on/off merging of coincident points. Note that is merging is on, points with different point attributes (e.g., normals) are merged, which may cause rendering artifacts', default=True)
    m_OriginalCellIdsName = bpy.props.StringProperty(name='OriginalCellIdsName', description='If PassThroughCellIds or PassThroughPointIds is on, then these ivars control the name given to the field in which the ids are written into. If set to nullptr, then vtkOriginalCellIds or vtkOriginalPointIds (the default) is used, respectively', default='vtkOriginalCellIds')
    m_OriginalPointIdsName = bpy.props.StringProperty(name='OriginalPointIdsName', description='If PassThroughCellIds or PassThroughPointIds is on, then these ivars control the name given to the field in which the ids are written into. If set to nullptr, then vtkOriginalCellIds or vtkOriginalPointIds (the default) is used, respectively', default='vtkOriginalPointIds')
    m_PassThroughCellIds = bpy.props.BoolProperty(name='PassThroughCellIds', description='If on, the output polygonal dataset will have a celldata array that holds the cell index of the original 3D cell that produced each output cell. This is useful for cell picking. The default is off to conserve memory. Note that PassThroughCellIds will be ignored if UseStrips is on, since in that case each tringle strip can represent more than on of the input cells', default=True)
    m_PassThroughPointIds = bpy.props.BoolProperty(name='PassThroughPointIds', description='If on, the output polygonal dataset will have a celldata array that holds the cell index of the original 3D cell that produced each output cell. This is useful for cell picking. The default is off to conserve memory. Note that PassThroughCellIds will be ignored if UseStrips is on, since in that case each tringle strip can represent more than on of the input cells', default=True)
    m_PointClipping = bpy.props.BoolProperty(name='PointClipping', description='Turn on/off selection of geometry by point id', default=True)
    m_PointMaximum = bpy.props.IntProperty(name='PointMaximum', description='Specify the maximum point id for point id selection', default=1000000000)
    m_PointMinimum = bpy.props.IntProperty(name='PointMinimum', description='Specify the minimum point id for point id selection', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CellClipping', 'm_CellMaximum', 'm_CellMinimum', 'm_DuplicateGhostCellClipping', 'm_ExtentClipping', 'm_Merging', 'm_OriginalCellIdsName', 'm_OriginalPointIdsName', 'm_PassThroughCellIds', 'm_PassThroughPointIds', 'm_PointClipping', 'm_PointMaximum', 'm_PointMinimum', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_UnstructuredGridGeometryFilter)
TYPENAMES.append('BVTK_NT_UnstructuredGridGeometryFilter' )


# --------------------------------------------------------------


class BVTK_NT_TransmitStructuredDataPiece(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransmitStructuredDataPiece'
    bl_label = 'vtkTransmitStructuredDataPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty(name='CreateGhostCells', description='Turn on/off creating ghost cells (on by default)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CreateGhostCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransmitStructuredDataPiece)
TYPENAMES.append('BVTK_NT_TransmitStructuredDataPiece' )


# --------------------------------------------------------------


class BVTK_NT_GraphWeightEuclideanDistanceFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GraphWeightEuclideanDistanceFilter'
    bl_label = 'vtkGraphWeightEuclideanDistanceFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GraphWeightEuclideanDistanceFilter)
TYPENAMES.append('BVTK_NT_GraphWeightEuclideanDistanceFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractArray(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractArray'
    bl_label = 'vtkExtractArray'
    
    m_Index = bpy.props.IntProperty(name='Index', description='Controls which array will be extracted', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Index', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractArray)
TYPENAMES.append('BVTK_NT_ExtractArray' )


# --------------------------------------------------------------


class BVTK_NT_ImageStencilSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageStencilSource'
    bl_label = 'vtkImageStencilSource'
    
    m_OutputOrigin = bpy.props.FloatVectorProperty(name='OutputOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    m_OutputSpacing = bpy.props.FloatVectorProperty(name='OutputSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_OutputWholeExtent = bpy.props.IntVectorProperty(name='OutputWholeExtent', description='', default=[0, -1, 0, -1, 0, -1], size=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_OutputOrigin', 'm_OutputSpacing', 'm_OutputWholeExtent', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageStencilSource)
TYPENAMES.append('BVTK_NT_ImageStencilSource' )


# --------------------------------------------------------------


class BVTK_NT_CollectTable(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CollectTable'
    bl_label = 'vtkCollectTable'
    
    m_PassThrough = bpy.props.BoolProperty(name='PassThrough', description='To collect or just copy input to output. Off (collect) by default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PassThrough', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CollectTable)
TYPENAMES.append('BVTK_NT_CollectTable' )


# --------------------------------------------------------------


class BVTK_NT_SignedDistance(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SignedDistance'
    bl_label = 'vtkSignedDistance'
    
    m_Bounds = bpy.props.FloatVectorProperty(name='Bounds', description='Set / get the region in space in which to perform the sampling. If not specified, it will be computed automatically', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set / get the radius of influence of each point. Smaller values generally improve performance markedly. Note that after the signed distance function is computed, any voxel taking on the value >= Radius is presumed to be "unseen" or uninitialized', default=0.1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Bounds', 'm_Radius', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SignedDistance)
TYPENAMES.append('BVTK_NT_SignedDistance' )


# --------------------------------------------------------------


class BVTK_NT_ImageToAMR(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageToAMR'
    bl_label = 'vtkImageToAMR'
    
    m_MaximumNumberOfBlocks = bpy.props.IntProperty(name='MaximumNumberOfBlocks', description='Set the maximun number of blocks in the outpu', default=100)
    m_NumberOfLevels = bpy.props.IntProperty(name='NumberOfLevels', description='Set the maximum number of levels in the generated Overlapping-AMR', default=2)
    m_RefinementRatio = bpy.props.IntProperty(name='RefinementRatio', description='Set the refinement ratio for levels. This refinement ratio is used for all levels', default=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MaximumNumberOfBlocks', 'm_NumberOfLevels', 'm_RefinementRatio', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageToAMR)
TYPENAMES.append('BVTK_NT_ImageToAMR' )


# --------------------------------------------------------------


class BVTK_NT_ImageDataToUniformGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageDataToUniformGrid'
    bl_label = 'vtkImageDataToUniformGrid'
    
    m_Reverse = bpy.props.BoolProperty(name='Reverse', description='By default, values of 0 (i.e. Reverse = 0) in the array will result in that point or cell to be blanked. Set Reverse to 1 to make points or cells to not be blanked for array values of 0', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Reverse', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageDataToUniformGrid)
TYPENAMES.append('BVTK_NT_ImageDataToUniformGrid' )


# --------------------------------------------------------------


class BVTK_NT_MatrixMathFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MatrixMathFilter'
    bl_label = 'vtkMatrixMathFilter'
    e_Operation_items = [(x, x, x) for x in ['Determinant', 'Eigenvalue', 'Eigenvector', 'Inverse']]
    
    e_Operation = bpy.props.EnumProperty(name='Operation', description='Set/Get the particular estimator used to function the quality of query', items=e_Operation_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_Operation', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MatrixMathFilter)
TYPENAMES.append('BVTK_NT_MatrixMathFilter' )


# --------------------------------------------------------------


class BVTK_NT_Curvatures(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Curvatures'
    bl_label = 'vtkCurvatures'
    e_CurvatureType_items = [(x, x, x) for x in ['Gaussian', 'Maximum', 'Mean', 'Minimum']]
    
    e_CurvatureType = bpy.props.EnumProperty(name='CurvatureType', description='Set/Get Curvature type VTK_CURVATURE_GAUSS: Gaussian curvature, stored as DataArray "Gauss_Curvature" VTK_CURVATURE_MEAN : Mean curvature, stored as DataArray "Mean_Curvature', default='Gaussian', items=e_CurvatureType_items)
    m_InvertMeanCurvature = bpy.props.BoolProperty(name='InvertMeanCurvature', description='Set/Get the flag which inverts the mean curvature calculation for meshes with inward pointing normals (default false', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_CurvatureType', 'm_InvertMeanCurvature', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Curvatures)
TYPENAMES.append('BVTK_NT_Curvatures' )


# --------------------------------------------------------------


class BVTK_NT_LinearExtrusionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LinearExtrusionFilter'
    bl_label = 'vtkLinearExtrusionFilter'
    e_ExtrusionType_items = [(x, x, x) for x in ['NormalExtrusion', 'PointExtrusion', 'VectorExtrusion']]
    
    m_Capping = bpy.props.BoolProperty(name='Capping', description='Turn on/off the capping of the skirt', default=True)
    m_ExtrusionPoint = bpy.props.FloatVectorProperty(name='ExtrusionPoint', description='Set/Get extrusion point. Only needs to be set if PointExtrusion is turned on. This is the point towards which extrusion occurs', default=[0.0, 0.0, 0.0], size=3)
    e_ExtrusionType = bpy.props.EnumProperty(name='ExtrusionType', description='Set/Get the type of extrusion', default='NormalExtrusion', items=e_ExtrusionType_items)
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Set/Get extrusion scale factor', default=1.0)
    m_Vector = bpy.props.FloatVectorProperty(name='Vector', description='Set/Get extrusion vector. Only needs to be set if VectorExtrusion is turned on', default=[0.0, 0.0, 1.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Capping', 'm_ExtrusionPoint', 'e_ExtrusionType', 'm_ScaleFactor', 'm_Vector', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LinearExtrusionFilter)
TYPENAMES.append('BVTK_NT_LinearExtrusionFilter' )


# --------------------------------------------------------------


class BVTK_NT_DirectedGraphAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DirectedGraphAlgorithm'
    bl_label = 'vtkDirectedGraphAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DirectedGraphAlgorithm)
TYPENAMES.append('BVTK_NT_DirectedGraphAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_StructuredGridAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StructuredGridAlgorithm'
    bl_label = 'vtkStructuredGridAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StructuredGridAlgorithm)
TYPENAMES.append('BVTK_NT_StructuredGridAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_ImageToPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageToPolyDataFilter'
    bl_label = 'vtkImageToPolyDataFilter'
    e_ColorMode_items = [(x, x, x) for x in ['LUT', 'Linear256']]
    e_OutputStyle_items = [(x, x, x) for x in ['Pixelize', 'Polygonalize', 'RunLength']]
    
    e_ColorMode = bpy.props.EnumProperty(name='ColorMode', description='Specify how to quantize color', default='Linear256', items=e_ColorMode_items)
    m_Decimation = bpy.props.BoolProperty(name='Decimation', description='Turn on/off whether the final polygons should be decimated. whether to smooth boundaries', default=True)
    m_DecimationError = bpy.props.FloatProperty(name='DecimationError', description='Specify the error to use for decimation (if decimation is on). The error is an absolute number--the image spacing and dimensions are used to create points so the error should be consistent with the image size', default=1.5)
    m_Error = bpy.props.IntProperty(name='Error', description='Specify the error value between two colors where the colors are considered the same. Only use this if the color mode uses the default 256 table', default=100)
    m_NumberOfSmoothingIterations = bpy.props.IntProperty(name='NumberOfSmoothingIterations', description='Specify the number of smoothing iterations to smooth polygons. (Only in effect if output style is Polygonalize and smoothing is on.', default=40)
    e_OutputStyle = bpy.props.EnumProperty(name='OutputStyle', description='Specify how to create the output. Pixelize means converting the image to quad polygons with a constant color per quad. Polygonalize means merging colors together into polygonal regions, and then smoothing the regions (if smoothing is turned on). RunLength means creating quad polygons that may encompass several pixels on a scan line. The default behavior is Polygonalize', default='Polygonalize', items=e_OutputStyle_items)
    m_Smoothing = bpy.props.BoolProperty(name='Smoothing', description='If the output style is set to polygonalize, then you can control whether to smooth boundaries', default=True)
    m_SubImageSize = bpy.props.IntProperty(name='SubImageSize', description='Specify the size (n by n pixels) of the largest region to polygonalize. When the OutputStyle is set to VTK_STYLE_POLYGONALIZE, large amounts of memory are used. In order to process large images, the image is broken into pieces that are at most Size pixels in width and height', default=250)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ColorMode', 'm_Decimation', 'm_DecimationError', 'm_Error', 'm_NumberOfSmoothingIterations', 'e_OutputStyle', 'm_Smoothing', 'm_SubImageSize', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['LookupTable'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageToPolyDataFilter)
TYPENAMES.append('BVTK_NT_ImageToPolyDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_SubdivideTetra(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SubdivideTetra'
    bl_label = 'vtkSubdivideTetra'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SubdivideTetra)
TYPENAMES.append('BVTK_NT_SubdivideTetra' )


# --------------------------------------------------------------


class BVTK_NT_ImageAnisotropicDiffusion3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageAnisotropicDiffusion3D'
    bl_label = 'vtkImageAnisotropicDiffusion3D'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_Corners = bpy.props.BoolProperty(name='Corners', description='Choose neighbors to diffuse (6 faces, 12 edges, 8 corners)', default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_DiffusionFactor = bpy.props.FloatProperty(name='DiffusionFactor', description='Set/Get the difference facto', default=1.0)
    m_DiffusionThreshold = bpy.props.FloatProperty(name='DiffusionThreshold', description='Set/Get the difference threshold that stops diffusion. when the difference between two pixel is greater than this threshold, the pixels are not diffused. This causes diffusion to avoid sharp edges. If the GradientMagnitudeThreshold is set, then gradient magnitude is used for comparison instead of pixel differences', default=5.0)
    m_Edges = bpy.props.BoolProperty(name='Edges', description='Choose neighbors to diffuse (6 faces, 12 edges, 8 corners)', default=True)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_Faces = bpy.props.BoolProperty(name='Faces', description='Choose neighbors to diffuse (6 faces, 12 edges, 8 corners)', default=True)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_GradientMagnitudeThreshold = bpy.props.BoolProperty(name='GradientMagnitudeThreshold', description='Switch between gradient magnitude threshold and pixel gradient threshold', default=True)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfIterations = bpy.props.IntProperty(name='NumberOfIterations', description='This method sets the number of interations which also affects the input neighborhood needed to compute one output pixel. Each iterations requires an extra pixel layer on the neighborhood. This is only relavent when you are trying to stream or are requesting a sub extent of the "wholeExtent"', default=4)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Corners', 'm_DesiredBytesPerPiece', 'm_DiffusionFactor', 'm_DiffusionThreshold', 'm_Edges', 'm_EnableSMP', 'm_Faces', 'm_GlobalDefaultEnableSMP', 'm_GradientMagnitudeThreshold', 'm_MinimumPieceSize', 'm_NumberOfIterations', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageAnisotropicDiffusion3D)
TYPENAMES.append('BVTK_NT_ImageAnisotropicDiffusion3D' )


# --------------------------------------------------------------


class BVTK_NT_UnstructuredGridAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_UnstructuredGridAlgorithm'
    bl_label = 'vtkUnstructuredGridAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_UnstructuredGridAlgorithm)
TYPENAMES.append('BVTK_NT_UnstructuredGridAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_SimpleImageFilterExample(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SimpleImageFilterExample'
    bl_label = 'vtkSimpleImageFilterExample'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SimpleImageFilterExample)
TYPENAMES.append('BVTK_NT_SimpleImageFilterExample' )


# --------------------------------------------------------------


class BVTK_NT_ImageConvolve(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageConvolve'
    bl_label = 'vtkImageConvolve'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageConvolve)
TYPENAMES.append('BVTK_NT_ImageConvolve' )


# --------------------------------------------------------------


class BVTK_NT_LinearSubdivisionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LinearSubdivisionFilter'
    bl_label = 'vtkLinearSubdivisionFilter'
    
    m_CheckForTriangles = bpy.props.BoolProperty(name='CheckForTriangles', description='Set/get CheckForTriangles Should subdivision check that the dataset only contains triangles? Default is On (1)', default=True)
    m_NumberOfSubdivisions = bpy.props.IntProperty(name='NumberOfSubdivisions', description='Set/get the number of subdivisions. Default is 1', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CheckForTriangles', 'm_NumberOfSubdivisions', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LinearSubdivisionFilter)
TYPENAMES.append('BVTK_NT_LinearSubdivisionFilter' )


# --------------------------------------------------------------


class BVTK_NT_WarpScalar(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_WarpScalar'
    bl_label = 'vtkWarpScalar'
    
    m_Normal = bpy.props.FloatVectorProperty(name='Normal', description='Normal (i.e., direction) along which to warp geometry. Only used if UseNormal boolean set to true or no normals available in data', default=[0.0, 0.0, 1.0], size=3)
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Specify value to scale displacement', default=1.0)
    m_UseNormal = bpy.props.BoolProperty(name='UseNormal', description='Turn on/off use of user specified normal. If on, data normals will be ignored and instance variable Normal will be used instead', default=True)
    m_XYPlane = bpy.props.BoolProperty(name='XYPlane', description='Turn on/off flag specifying that input data is x-y plane. If x-y plane, then the z value is used to warp the surface in the z-axis direction (times the scale factor) and scalars are used to color the surface', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Normal', 'm_ScaleFactor', 'm_UseNormal', 'm_XYPlane', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_WarpScalar)
TYPENAMES.append('BVTK_NT_WarpScalar' )


# --------------------------------------------------------------


class BVTK_NT_ImageMapToWindowLevelColors(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMapToWindowLevelColors'
    bl_label = 'vtkImageMapToWindowLevelColors'
    e_OutputFormat_items = [(x, x, x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_ActiveComponent = bpy.props.IntProperty(name='ActiveComponent', description='Set the component to map for multi-component images (default: 0', default=0)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Level = bpy.props.FloatProperty(name='Level', description='Set / Get the Level to use -> modulation will be performed on the color based on (S - (L - W/2))/W where S is the scalar value, L is the level and W is the window', default=127.5)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NaNColor = bpy.props.IntVectorProperty(name='NaNColor', description='', default=[0, 0, 0, 0], size=4)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_OutputFormat = bpy.props.EnumProperty(name='OutputFormat', description='Set the output format, the default is RGBA', default='RGBA', items=e_OutputFormat_items)
    m_PassAlphaToOutput = bpy.props.BoolProperty(name='PassAlphaToOutput', description='Use the alpha component of the input when computing the alpha component of the output (useful when converting monochrome+alpha data to RGBA', default=True)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_Window = bpy.props.FloatProperty(name='Window', description='Set / Get the Window to use -> modulation will be performed on the color based on (S - (L - W/2))/W where S is the scalar value, L is the level and W is the window', default=255.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ActiveComponent', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Level', 'm_MinimumPieceSize', 'm_NaNColor', 'm_NumberOfThreads', 'e_OutputFormat', 'm_PassAlphaToOutput', 'e_SplitMode', 'm_Window', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['LookupTable'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMapToWindowLevelColors)
TYPENAMES.append('BVTK_NT_ImageMapToWindowLevelColors' )


# --------------------------------------------------------------


class BVTK_NT_TransmitRectilinearGridPiece(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransmitRectilinearGridPiece'
    bl_label = 'vtkTransmitRectilinearGridPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty(name='CreateGhostCells', description='Turn on/off creating ghost cells (on by default)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CreateGhostCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransmitRectilinearGridPiece)
TYPENAMES.append('BVTK_NT_TransmitRectilinearGridPiece' )


# --------------------------------------------------------------


class BVTK_NT_CellQuality(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CellQuality'
    bl_label = 'vtkCellQuality'
    e_QualityMeasure_items = [(x, x, x) for x in ['Area', 'AspectBeta', 'AspectFrobenius', 'AspectGamma', 'AspectRatio', 'CollapseRatio', 'Condition', 'Diagonal', 'Dimension', 'Distortion', 'Jacobian', 'MaxAngle', 'MaxAspectFrobenius', 'MaxEdgeRatio', 'MedAspectFrobenius', 'MinAngle', 'Oddy', 'RadiusRatio', 'RelativeSizeSquared', 'ScaledJacobian', 'Shape', 'ShapeAndSize', 'Shear', 'ShearAndSize', 'Skew', 'Stretch', 'Taper', 'Volume', 'Warpage']]
    
    e_QualityMeasure = bpy.props.EnumProperty(name='QualityMeasure', description='Set/Get the particular estimator used to function the quality of all supported geometries. For qualities that are not defined for certain geometries, later program logic ensures that CellQualityNone static function will be used so that a predefined value is returned for the request. There is no default value for this call and valid values include all possible qualities supported by this class', items=e_QualityMeasure_items)
    m_UndefinedQuality = bpy.props.FloatProperty(name='UndefinedQuality', description='Set/Get the return value for undefined quality. Undefined quality are qualities that could be addressed by this filter but is not well defined for the particular geometry of cell in question, e.g. a volume query for a triangle. Undefined quality will always be undefined. The default value for UndefinedQuality is -1', default=-1.0)
    m_UnsupportedGeometry = bpy.props.FloatProperty(name='UnsupportedGeometry', description='Set/Get the return value for unsupported geometry. Unsupported geometry are geometries that are not supported by this filter currently, future implementation might include support for them. The defalut value for UnsupportedGeometry is -1', default=-1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_QualityMeasure', 'm_UndefinedQuality', 'm_UnsupportedGeometry', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CellQuality)
TYPENAMES.append('BVTK_NT_CellQuality' )


# --------------------------------------------------------------


class BVTK_NT_MatricizeArray(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MatricizeArray'
    bl_label = 'vtkMatricizeArray'
    
    m_SliceDimension = bpy.props.IntProperty(name='SliceDimension', description='Sets the 0-numbered dimension that will be mapped to columns in the outpu', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_SliceDimension', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MatricizeArray)
TYPENAMES.append('BVTK_NT_MatricizeArray' )


# --------------------------------------------------------------


class BVTK_NT_CellDataToPointData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CellDataToPointData'
    bl_label = 'vtkCellDataToPointData'
    
    m_ContributingCellOption = bpy.props.IntProperty(name='ContributingCellOption', description='Option to specify what cells to include in the gradient computation. Options are all cells (All, Patch and DataSetMax). The default is All', default=0)
    m_PassCellData = bpy.props.BoolProperty(name='PassCellData', description='Control whether the input cell data is to be passed to the output. If on, then the input cell data is passed through to the output; otherwise, only generated point data is placed into the output', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ContributingCellOption', 'm_PassCellData', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CellDataToPointData)
TYPENAMES.append('BVTK_NT_CellDataToPointData' )


# --------------------------------------------------------------


class BVTK_NT_TransposeTable(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransposeTable'
    bl_label = 'vtkTransposeTable'
    
    m_AddIdColumn = bpy.props.BoolProperty(name='AddIdColumn', description='This flag indicates if a column must be inserted at index 0 with the names (ids) of the input columns. Default: tru', default=True)
    m_IdColumnName = bpy.props.StringProperty(name='IdColumnName', description='Get/Set the name of the id column added by option AddIdColumn. Default: ColNam', default='ColName')
    m_UseIdColumn = bpy.props.BoolProperty(name='UseIdColumn', description='This flag indicates if the output column must be named using the names listed in the index 0 column. Default: fals', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AddIdColumn', 'm_IdColumnName', 'm_UseIdColumn', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransposeTable)
TYPENAMES.append('BVTK_NT_TransposeTable' )


# --------------------------------------------------------------


class BVTK_NT_RectilinearGridGeometryFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RectilinearGridGeometryFilter'
    bl_label = 'vtkRectilinearGridGeometryFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RectilinearGridGeometryFilter)
TYPENAMES.append('BVTK_NT_RectilinearGridGeometryFilter' )


# --------------------------------------------------------------


class BVTK_NT_MultiThreshold(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MultiThreshold'
    bl_label = 'vtkMultiThreshold'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MultiThreshold)
TYPENAMES.append('BVTK_NT_MultiThreshold' )


# --------------------------------------------------------------


class BVTK_NT_TreeAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TreeAlgorithm'
    bl_label = 'vtkTreeAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TreeAlgorithm)
TYPENAMES.append('BVTK_NT_TreeAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_ForceTime(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ForceTime'
    bl_label = 'vtkForceTime'
    
    m_ForcedTime = bpy.props.FloatProperty(name='ForcedTime', description='Replace the pipeline time by this one', default=0.0)
    m_IgnorePipelineTime = bpy.props.BoolProperty(name='IgnorePipelineTime', description='Use the ForcedTime. If disabled, use usual pipeline time', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ForcedTime', 'm_IgnorePipelineTime', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ForceTime)
TYPENAMES.append('BVTK_NT_ForceTime' )


# --------------------------------------------------------------


class BVTK_NT_ExtractCells(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractCells'
    bl_label = 'vtkExtractCells'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractCells)
TYPENAMES.append('BVTK_NT_ExtractCells' )


# --------------------------------------------------------------


class BVTK_NT_ImageGradient(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageGradient'
    bl_label = 'vtkImageGradient'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Determines how the input is interpreted (set of 2d slices ...', default=2)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_HandleBoundaries = bpy.props.BoolProperty(name='HandleBoundaries', description='Get/Set whether to handle boundaries. If enabled, boundary pixels are treated as duplicated so that central differencing works for the boundary pixels. If disabled, the output whole extent of the image is reduced by one pixel', default=True)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_HandleBoundaries', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageGradient)
TYPENAMES.append('BVTK_NT_ImageGradient' )


# --------------------------------------------------------------


class BVTK_NT_RemoveGhosts(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RemoveGhosts'
    bl_label = 'vtkRemoveGhosts'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RemoveGhosts)
TYPENAMES.append('BVTK_NT_RemoveGhosts' )


# --------------------------------------------------------------


class BVTK_NT_DecimatePro(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DecimatePro'
    bl_label = 'vtkDecimatePro'
    
    m_AbsoluteError = bpy.props.FloatProperty(name='AbsoluteError', description='Same as MaximumError, but to be used when ErrorIsAbsolute is ', default=1e+30)
    m_AccumulateError = bpy.props.BoolProperty(name='AccumulateError', description='The computed error can either be computed directly from the mesh or the error may be accumulated as the mesh is modified. If the error is accumulated, then it represents a global error bounds, and the ivar MaximumError becomes a global bounds on mesh error. Accumulating the error requires extra memory proportional to the number of vertices in the mesh. If AccumulateError is off, then the error is not accumulated', default=True)
    m_BoundaryVertexDeletion = bpy.props.BoolProperty(name='BoundaryVertexDeletion', description='Turn on/off the deletion of vertices on the boundary of a mesh. This may limit the maximum reduction that may be achieved', default=True)
    m_Degree = bpy.props.IntProperty(name='Degree', description='If the number of triangles connected to a vertex exceeds "Degree", then the vertex will be split. (NOTE: the complexity of the triangulation algorithm is proportional to Degree^2. Setting degree small can improve the performance of the algorithm.', default=25)
    m_ErrorIsAbsolute = bpy.props.IntProperty(name='ErrorIsAbsolute', description='The MaximumError is normally defined as a fraction of the dataset bounding diagonal. By setting ErrorIsAbsolute to 1, the error is instead defined as that specified by AbsoluteError. By default ErrorIsAbsolute=0', default=0)
    m_FeatureAngle = bpy.props.FloatProperty(name='FeatureAngle', description='Specify the mesh feature angle. This angle is used to define what an edge is (i.e., if the surface normal between two adjacent triangles is >= FeatureAngle, an edge exists)', default=15.0)
    m_InflectionPointRatio = bpy.props.FloatProperty(name='InflectionPointRatio', description='Specify the inflection point ratio. An inflection point occurs when the ratio of reduction error between two iterations is greater than or equal to the InflectionPointRatio', default=10.0)
    m_MaximumError = bpy.props.FloatProperty(name='MaximumError', description='Set the largest decimation error that is allowed during the decimation process. This may limit the maximum reduction that may be achieved. The maximum error is specified as a fraction of the maximum length of the input data bounding box', default=1e+30)
    m_PreSplitMesh = bpy.props.BoolProperty(name='PreSplitMesh', description='In some cases you may wish to split the mesh prior to algorithm execution. This separates the mesh into semi-planar patches, which are disconnected from each other. This can give superior results in some cases. If the ivar PreSplitMesh ivar is enabled, the mesh is split with the specified SplitAngle. Otherwise mesh splitting is deferred as long as possible', default=True)
    m_PreserveTopology = bpy.props.BoolProperty(name='PreserveTopology', description='Turn on/off whether to preserve the topology of the original mesh. If on, mesh splitting and hole elimination will not occur. This may limit the maximum reduction that may be achieved', default=True)
    m_SplitAngle = bpy.props.FloatProperty(name='SplitAngle', description='Specify the mesh split angle. This angle is used to control the splitting of the mesh. A split line exists when the surface normals between two edge connected triangles are >= SplitAngle', default=75.0)
    m_Splitting = bpy.props.BoolProperty(name='Splitting', description='Turn on/off the splitting of the mesh at corners, along edges, at non-manifold points, or anywhere else a split is required. Turning splitting off will better preserve the original topology of the mesh, but you may not obtain the requested reduction', default=True)
    m_TargetReduction = bpy.props.FloatProperty(name='TargetReduction', description='Specify the desired reduction in the total number of polygons (e.g., if TargetReduction is set to 0.9, this filter will try to reduce the data set to 10% of its original size). Because of various constraints, this level of reduction may not be realized. If you want to guarantee a particular reduction, you must turn off PreserveTopology, turn on SplitEdges and BoundaryVertexDeletion, and set the MaximumError to VTK_DOUBLE_MAX (these ivars are initialized this way when the object is instantiated)', default=0.9)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AbsoluteError', 'm_AccumulateError', 'm_BoundaryVertexDeletion', 'm_Degree', 'm_ErrorIsAbsolute', 'm_FeatureAngle', 'm_InflectionPointRatio', 'm_MaximumError', 'm_PreSplitMesh', 'm_PreserveTopology', 'm_SplitAngle', 'm_Splitting', 'm_TargetReduction', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DecimatePro)
TYPENAMES.append('BVTK_NT_DecimatePro' )


# --------------------------------------------------------------


class BVTK_NT_HyperTreeGridAxisClip(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperTreeGridAxisClip'
    bl_label = 'vtkHyperTreeGridAxisClip'
    e_ClipType_items = [(x, x, x) for x in ['Box', 'Plane', 'Quadric']]
    
    m_Bounds = bpy.props.FloatVectorProperty(name='Bounds', description='Set/get bounds of clipping box', default=[-0.5, 0.5, -0.5, 0.5, -0.5, 0.5], size=6)
    e_ClipType = bpy.props.EnumProperty(name='ClipType', description='Set/get type of clip. Default value is 0 (plane clip)', default='Plane', items=e_ClipType_items)
    m_InsideOut = bpy.props.BoolProperty(name='InsideOut', description='Set/Get the InsideOut flag, in the case of clip by hyperplane. When off, a cell is clipped out when its origin is above said plane intercept along the considered direction, inside otherwise. When on, a cell is clipped out when its origin + size is below said said plane intercept along the considered direction', default=True)
    m_PlaneNormalAxis = bpy.props.IntProperty(name='PlaneNormalAxis', description='Set/get normal axis of clipping plane: 0=X, 1=Y, 2=Z. Default value is 0 (X-axis normal)', default=0)
    m_PlanePosition = bpy.props.FloatProperty(name='PlanePosition', description='Set/get position of clipping plane: intercept along normal axis. Default value is 0.0', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Bounds', 'e_ClipType', 'm_InsideOut', 'm_PlaneNormalAxis', 'm_PlanePosition', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Quadric'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperTreeGridAxisClip)
TYPENAMES.append('BVTK_NT_HyperTreeGridAxisClip' )


# --------------------------------------------------------------


class BVTK_NT_ImageLuminance(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageLuminance'
    bl_label = 'vtkImageLuminance'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageLuminance)
TYPENAMES.append('BVTK_NT_ImageLuminance' )


# --------------------------------------------------------------


class BVTK_NT_ClipConvexPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ClipConvexPolyData'
    bl_label = 'vtkClipConvexPolyData'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Planes'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ClipConvexPolyData)
TYPENAMES.append('BVTK_NT_ClipConvexPolyData' )


# --------------------------------------------------------------


class BVTK_NT_QuadRotationalExtrusionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_QuadRotationalExtrusionFilter'
    bl_label = 'vtkQuadRotationalExtrusionFilter'
    e_Axis_items = [(x, x, x) for x in ['X', 'Y', 'Z']]
    
    e_Axis = bpy.props.EnumProperty(name='Axis', description='Set the axis of rotation to use. It is set by default to Z', default='Z', items=e_Axis_items)
    m_Capping = bpy.props.BoolProperty(name='Capping', description='Turn on/off the capping of the skirt', default=True)
    m_DefaultAngle = bpy.props.FloatProperty(name='DefaultAngle', description='Set/Get angle of rotation', default=360.0)
    m_DeltaRadius = bpy.props.FloatProperty(name='DeltaRadius', description='Set/Get change in radius during sweep process', default=0.0)
    m_Resolution = bpy.props.IntProperty(name='Resolution', description='Set/Get resolution of sweep operation. Resolution controls the number of intermediate node points', default=12)
    m_Translation = bpy.props.FloatProperty(name='Translation', description='Set/Get total amount of translation along the z-axis', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_Axis', 'm_Capping', 'm_DefaultAngle', 'm_DeltaRadius', 'm_Resolution', 'm_Translation', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_QuadRotationalExtrusionFilter)
TYPENAMES.append('BVTK_NT_QuadRotationalExtrusionFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageButterworthHighPass(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageButterworthHighPass'
    bl_label = 'vtkImageButterworthHighPass'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_CutOff = bpy.props.FloatVectorProperty(name='CutOff', description='', default=[1e+30, 1e+30, 1e+30], size=3)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_Order = bpy.props.IntProperty(name='Order', description='The order determines sharpness of the cutoff curve', default=1)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_XCutOff = bpy.props.FloatProperty(name='XCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    m_YCutOff = bpy.props.FloatProperty(name='YCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    m_ZCutOff = bpy.props.FloatProperty(name='ZCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CutOff', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_Order', 'e_SplitMode', 'm_XCutOff', 'm_YCutOff', 'm_ZCutOff', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageButterworthHighPass)
TYPENAMES.append('BVTK_NT_ImageButterworthHighPass' )


# --------------------------------------------------------------


class BVTK_NT_ArcPlotter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ArcPlotter'
    bl_label = 'vtkArcPlotter'
    e_PlotMode_items = [(x, x, x) for x in ['PlotFieldData', 'PlotNormals', 'PlotScalars', 'PlotTCoords', 'PlotTensors', 'PlotVectors']]
    
    m_DefaultNormal = bpy.props.FloatVectorProperty(name='DefaultNormal', description='Set the default normal to use if you do not wish automatic normal calculation. The arc plot will be generated using this normal', default=[0.0, 0.0, 1.0], size=3)
    m_FieldDataArray = bpy.props.IntProperty(name='FieldDataArray', description='Set/Get the field data array to plot. This instance variable is only applicable if field data is plotted', default=0)
    m_Height = bpy.props.FloatProperty(name='Height', description='Set the height of the plot. (The radius combined with the height define the location of the plot relative to the generating polyline.', default=0.5)
    m_Offset = bpy.props.FloatProperty(name='Offset', description='Specify an offset that translates each subsequent plot (if there is more than one component plotted) from the defining arc (i.e., polyline)', default=0.0)
    m_PlotComponent = bpy.props.IntProperty(name='PlotComponent', description='Set/Get the component number to plot if the data has more than one component. If the value of the plot component is == (-1), then all the components will be plotted', default=-1)
    e_PlotMode = bpy.props.EnumProperty(name='PlotMode', description='Specify which data to plot: scalars, vectors, normals, texture coords, tensors, or field data. If the data has more than one component, use the method SetPlotComponent to control which component to plot', default='PlotScalars', items=e_PlotMode_items)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set the radius of the "median" value of the first plotted component', default=0.5)
    m_UseDefaultNormal = bpy.props.BoolProperty(name='UseDefaultNormal', description='Set a boolean to control whether to use default normals. By default, normals are automatically computed from the generating polyline and camera', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DefaultNormal', 'm_FieldDataArray', 'm_Height', 'm_Offset', 'm_PlotComponent', 'e_PlotMode', 'm_Radius', 'm_UseDefaultNormal', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ArcPlotter)
TYPENAMES.append('BVTK_NT_ArcPlotter' )


# --------------------------------------------------------------


class BVTK_NT_VectorDot(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VectorDot'
    bl_label = 'vtkVectorDot'
    
    m_MapScalars = bpy.props.BoolProperty(name='MapScalars', description='Enable/disable the mapping of scalars into a specified range. This will significantly improve the performance of the algorithm but the resulting scalar values will strictly be a function of the vector and normal data. By default, MapScalars is enabled, and the output scalar values will fall into the range ScalarRange', default=True)
    m_ScalarRange = bpy.props.FloatVectorProperty(name='ScalarRange', description='Specify the range into which to map the scalars. This mapping only occurs if MapScalars is enabled', default=[-1.0, 1.0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MapScalars', 'm_ScalarRange', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VectorDot)
TYPENAMES.append('BVTK_NT_VectorDot' )


# --------------------------------------------------------------


class BVTK_NT_ImageRange3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageRange3D'
    bl_label = 'vtkImageRange3D'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageRange3D)
TYPENAMES.append('BVTK_NT_ImageRange3D' )


# --------------------------------------------------------------


class BVTK_NT_HierarchicalDataExtractDataSets(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HierarchicalDataExtractDataSets'
    bl_label = 'vtkHierarchicalDataExtractDataSets'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HierarchicalDataExtractDataSets)
TYPENAMES.append('BVTK_NT_HierarchicalDataExtractDataSets' )


# --------------------------------------------------------------


class BVTK_NT_ImageHybridMedian2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageHybridMedian2D'
    bl_label = 'vtkImageHybridMedian2D'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageHybridMedian2D)
TYPENAMES.append('BVTK_NT_ImageHybridMedian2D' )


# --------------------------------------------------------------


class BVTK_NT_LevelIdScalars(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LevelIdScalars'
    bl_label = 'vtkLevelIdScalars'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LevelIdScalars)
TYPENAMES.append('BVTK_NT_LevelIdScalars' )


# --------------------------------------------------------------


class BVTK_NT_TransmitPolyDataPiece(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransmitPolyDataPiece'
    bl_label = 'vtkTransmitPolyDataPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty(name='CreateGhostCells', description='Turn on/off creating ghost cells (on by default)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CreateGhostCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransmitPolyDataPiece)
TYPENAMES.append('BVTK_NT_TransmitPolyDataPiece' )


# --------------------------------------------------------------


class BVTK_NT_SynchronizedTemplatesCutter3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SynchronizedTemplatesCutter3D'
    bl_label = 'vtkSynchronizedTemplatesCutter3D'
    
    m_ArrayComponent = bpy.props.IntProperty(name='ArrayComponent', description='Set/get which component of the scalar array to contour on; defaults to 0', default=0)
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_GenerateTriangles = bpy.props.BoolProperty(name='GenerateTriangles', description='If this is enabled (by default), the output will be triangles otherwise, the output will be the intersection polygon', default=True)
    m_InputMemoryLimit = bpy.props.IntProperty(name='InputMemoryLimit', description='Determines the chunk size fro streaming. This filter will act like a collector: ask for many input pieces, but generate one output. Limit is in KByte', default=0)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Set the number of contours to place into the list. You only really need to use this method to reduce list size. The method SetValue() will automatically increase list size as needed', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayComponent', 'm_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_GenerateTriangles', 'm_InputMemoryLimit', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['CutFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SynchronizedTemplatesCutter3D)
TYPENAMES.append('BVTK_NT_SynchronizedTemplatesCutter3D' )


# --------------------------------------------------------------


class BVTK_NT_DataObjectToDataSetFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataObjectToDataSetFilter'
    bl_label = 'vtkDataObjectToDataSetFilter'
    e_DataSetType_items = [(x, x, x) for x in ['PolyData', 'RectilinearGrid', 'StructuredGrid', 'StructuredPoints', 'UnstructuredGrid']]
    
    e_DataSetType = bpy.props.EnumProperty(name='DataSetType', description='Control what type of data is generated for output', default='PolyData', items=e_DataSetType_items)
    m_DefaultNormalize = bpy.props.BoolProperty(name='DefaultNormalize', description='Set the default Normalize() flag for those methods setting a default Normalize value (e.g., SetPointComponent)', default=True)
    m_Dimensions = bpy.props.IntVectorProperty(name='Dimensions', description='Specify the dimensions to use if generating a dataset that requires dimensions specification (vtkStructuredPoints, vtkStructuredGrid, vtkRectilinearGrid)', default=[0, 0, 0], size=3)
    m_Origin = bpy.props.FloatVectorProperty(name='Origin', description='Specify the origin to use if generating a dataset whose origin can be set (i.e., a vtkStructuredPoints dataset)', default=[0.0, 0.0, 0.0], size=3)
    m_Spacing = bpy.props.FloatVectorProperty(name='Spacing', description='Specify the spacing to use if generating a dataset whose spacing can be set (i.e., a vtkStructuredPoints dataset)', default=[0.0, 0.0, 0.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataSetType', 'm_DefaultNormalize', 'm_Dimensions', 'm_Origin', 'm_Spacing', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataObjectToDataSetFilter)
TYPENAMES.append('BVTK_NT_DataObjectToDataSetFilter' )


# --------------------------------------------------------------


class BVTK_NT_HyperTreeGridContour(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperTreeGridContour'
    bl_label = 'vtkHyperTreeGridContour'
    
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Methods (inlined) to set / get contour values', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperTreeGridContour)
TYPENAMES.append('BVTK_NT_HyperTreeGridContour' )


# --------------------------------------------------------------


class BVTK_NT_SampleImplicitFunctionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SampleImplicitFunctionFilter'
    bl_label = 'vtkSampleImplicitFunctionFilter'
    
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Turn on/off the computation of gradients', default=True)
    m_GradientArrayName = bpy.props.StringProperty(name='GradientArrayName', description='Set/get the gradient array name for this data set. The initial value is "Implicit gradients"', default='Implicit gradients')
    m_ScalarArrayName = bpy.props.StringProperty(name='ScalarArrayName', description='Set/get the scalar array name for this data set. The initial value is "Implicit scalars"', default='Implicit scalars')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_GradientArrayName', 'm_ScalarArrayName', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['ImplicitFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SampleImplicitFunctionFilter)
TYPENAMES.append('BVTK_NT_SampleImplicitFunctionFilter' )


# --------------------------------------------------------------


class BVTK_NT_HierarchicalBoxDataSetAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HierarchicalBoxDataSetAlgorithm'
    bl_label = 'vtkHierarchicalBoxDataSetAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HierarchicalBoxDataSetAlgorithm)
TYPENAMES.append('BVTK_NT_HierarchicalBoxDataSetAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_TableFFT(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TableFFT'
    bl_label = 'vtkTableFFT'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TableFFT)
TYPENAMES.append('BVTK_NT_TableFFT' )


# --------------------------------------------------------------


class BVTK_NT_TemporalDataSetCache(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TemporalDataSetCache'
    bl_label = 'vtkTemporalDataSetCache'
    
    m_CacheSize = bpy.props.IntProperty(name='CacheSize', description='This is the maximum number of time steps that can be retained in memory. it defaults to 10', default=10)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CacheSize', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TemporalDataSetCache)
TYPENAMES.append('BVTK_NT_TemporalDataSetCache' )


# --------------------------------------------------------------


class BVTK_NT_ImageMapToRGBA(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMapToRGBA'
    bl_label = 'vtkImageMapToRGBA'
    e_OutputFormat_items = [(x, x, x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_ActiveComponent = bpy.props.IntProperty(name='ActiveComponent', description='Set the component to map for multi-component images (default: 0', default=0)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NaNColor = bpy.props.IntVectorProperty(name='NaNColor', description='', default=[0, 0, 0, 0], size=4)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_OutputFormat = bpy.props.EnumProperty(name='OutputFormat', description='Set the output format, the default is RGBA', default='RGBA', items=e_OutputFormat_items)
    m_PassAlphaToOutput = bpy.props.BoolProperty(name='PassAlphaToOutput', description='Use the alpha component of the input when computing the alpha component of the output (useful when converting monochrome+alpha data to RGBA', default=True)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ActiveComponent', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NaNColor', 'm_NumberOfThreads', 'e_OutputFormat', 'm_PassAlphaToOutput', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['LookupTable'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMapToRGBA)
TYPENAMES.append('BVTK_NT_ImageMapToRGBA' )


# --------------------------------------------------------------


class BVTK_NT_CollectPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CollectPolyData'
    bl_label = 'vtkCollectPolyData'
    
    m_PassThrough = bpy.props.BoolProperty(name='PassThrough', description='To collect or just copy input to output. Off (collect) by default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PassThrough', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CollectPolyData)
TYPENAMES.append('BVTK_NT_CollectPolyData' )


# --------------------------------------------------------------


class BVTK_NT_AggregateDataSetFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AggregateDataSetFilter'
    bl_label = 'vtkAggregateDataSetFilter'
    
    m_NumberOfTargetProcesses = bpy.props.IntProperty(name='NumberOfTargetProcesses', description='Number of target processes. Valid values are between 1 and the total number of processes. The default is 1. If a value is passed in that is less than 1 than NumberOfTargetProcesses is changed/kept at 1. If a value is passed in that is greater than the total number of processes then NumberOfTargetProcesses is changed/kept at the total number of processes. This is useful for scripting use cases where later on the script is run with more processes than the current amount', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NumberOfTargetProcesses', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AggregateDataSetFilter)
TYPENAMES.append('BVTK_NT_AggregateDataSetFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageIdealHighPass(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageIdealHighPass'
    bl_label = 'vtkImageIdealHighPass'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_CutOff = bpy.props.FloatVectorProperty(name='CutOff', description='', default=[1e+30, 1e+30, 1e+30], size=3)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_XCutOff = bpy.props.FloatProperty(name='XCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    m_YCutOff = bpy.props.FloatProperty(name='YCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    m_ZCutOff = bpy.props.FloatProperty(name='ZCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CutOff', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', 'm_XCutOff', 'm_YCutOff', 'm_ZCutOff', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageIdealHighPass)
TYPENAMES.append('BVTK_NT_ImageIdealHighPass' )


# --------------------------------------------------------------


class BVTK_NT_ImageBSplineCoefficients(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageBSplineCoefficients'
    bl_label = 'vtkImageBSplineCoefficients'
    e_BorderMode_items = [(x, x, x) for x in ['Clamp', 'Mirror', 'Repeat']]
    e_OutputScalarType_items = [(x, x, x) for x in ['Double', 'Float']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    e_BorderMode = bpy.props.EnumProperty(name='BorderMode', description='Set the border mode. The filter that is used to create the coefficients must repeat the image somehow to make a theoritically infinite input. The default is to clamp values that are off the edge of the image, to the value at the closest point on the edge. The other ways of virtually extending the image are to produce mirrored copies, which results in optimal smoothness at the boundary, or to repeat the image, which results in a cyclic or periodic spline', default='Clamp', items=e_BorderMode_items)
    m_Bypass = bpy.props.BoolProperty(name='Bypass', description='Bypass the filter, do not do any processing. If this is on, then the output data will reference the input data directly, and the output type will be the same as the input type. This is useful a downstream filter sometimes uses b-spline interpolation and sometimes uses other forms of interpolation', default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_OutputScalarType = bpy.props.EnumProperty(name='OutputScalarType', description='Set the scalar type of the output. Default is float. Floating-point output is used to avoid overflow, since the range of the output values is larger than the input values', default='Float', items=e_OutputScalarType_items)
    m_SplineDegree = bpy.props.IntProperty(name='SplineDegree', description='Set the degree of the spline polynomial. The default value is 3, and the maximum is 9', default=3)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_BorderMode', 'm_Bypass', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_OutputScalarType', 'm_SplineDegree', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageBSplineCoefficients)
TYPENAMES.append('BVTK_NT_ImageBSplineCoefficients' )


# --------------------------------------------------------------


class BVTK_NT_ImageConstantPad(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageConstantPad'
    bl_label = 'vtkImageConstantPad'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_Constant = bpy.props.FloatProperty(name='Constant', description='Set/Get the pad value', default=0.0)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_OutputNumberOfScalarComponents = bpy.props.IntProperty(name='OutputNumberOfScalarComponents', description='Set/Get the number of output scalar components', default=-1)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Constant', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_OutputNumberOfScalarComponents', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageConstantPad)
TYPENAMES.append('BVTK_NT_ImageConstantPad' )


# --------------------------------------------------------------


class BVTK_NT_TextureMapToSphere(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TextureMapToSphere'
    bl_label = 'vtkTextureMapToSphere'
    
    m_AutomaticSphereGeneration = bpy.props.BoolProperty(name='AutomaticSphereGeneration', description='Turn on/off automatic sphere generation. This means it automatically finds the sphere center', default=True)
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Specify a point defining the center of the sphere', default=[0.0, 0.0, 0.0], size=3)
    m_PreventSeam = bpy.props.BoolProperty(name='PreventSeam', description='Control how the texture coordinates are generated. If PreventSeam is set, the s-coordinate ranges from 0->1 and 1->0 corresponding to the theta angle variation between 0->180 and 180->0 degrees. Otherwise, the s-coordinate ranges from 0->1 between 0->360 degrees', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutomaticSphereGeneration', 'm_Center', 'm_PreventSeam', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TextureMapToSphere)
TYPENAMES.append('BVTK_NT_TextureMapToSphere' )


# --------------------------------------------------------------


class BVTK_NT_ContourFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ContourFilter'
    bl_label = 'vtkContourFilter'
    
    m_ArrayComponent = bpy.props.IntProperty(name='ArrayComponent', description='Set/get which component of the scalar array to contour on; defaults to 0. Currently this feature only works if the input is a vtkImageData', default=0)
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off. This setting defaults to On for vtkImageData, vtkRectilinearGrid, vtkStructuredGrid, and vtkUnstructuredGrid inputs, and Off for all others. This default behavior is to preserve the behavior of an older version of this filter, which would ignore this setting for certain inputs', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_GenerateTriangles = bpy.props.BoolProperty(name='GenerateTriangles', description='If this is enabled (by default), the output will be triangles otherwise, the output will be the intersection polygon WARNING: if the contour surface is not planar, the output polygon will not be planar, which might be nice to look at but hard to compute with downstream', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Methods to set / get contour values', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayComponent', 'm_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_GenerateTriangles', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ContourFilter)
TYPENAMES.append('BVTK_NT_ContourFilter' )


# --------------------------------------------------------------


class BVTK_NT_POutlineCornerFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_POutlineCornerFilter'
    bl_label = 'vtkPOutlineCornerFilter'
    
    m_CornerFactor = bpy.props.FloatProperty(name='CornerFactor', description='Set/Get the factor that controls the relative size of the corners to the length of the corresponding bounds Typically vtkSetClampMacro(CornerFactor, double, 0.001, 0.5) would used but since we are chaining this to an internal method we rewrite the code in the macr', default=0.2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CornerFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_POutlineCornerFilter)
TYPENAMES.append('BVTK_NT_POutlineCornerFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImplicitTextureCoords(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImplicitTextureCoords'
    bl_label = 'vtkImplicitTextureCoords'
    
    m_FlipTexture = bpy.props.BoolProperty(name='FlipTexture', description='If enabled, this will flip the sense of inside and outside the implicit function (i.e., a rotation around the r-s-t=0.5 axis)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FlipTexture', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['RFunction', 'SFunction', 'TFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImplicitTextureCoords)
TYPENAMES.append('BVTK_NT_ImplicitTextureCoords' )


# --------------------------------------------------------------


class BVTK_NT_TransformCoordinateSystems(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransformCoordinateSystems'
    bl_label = 'vtkTransformCoordinateSystems'
    e_InputCoordinateSystem_items = [(x, x, x) for x in ['Display', 'Viewport', 'World']]
    e_OutputCoordinateSystem_items = [(x, x, x) for x in ['Display', 'Viewport', 'World']]
    
    e_InputCoordinateSystem = bpy.props.EnumProperty(name='InputCoordinateSystem', description='Set/get the coordinate system in which the input is specified. The current options are World, Viewport, and Display. By default the input coordinate system is World', default='World', items=e_InputCoordinateSystem_items)
    e_OutputCoordinateSystem = bpy.props.EnumProperty(name='OutputCoordinateSystem', description='Set/get the coordinate system to which to transform the output. The current options are World, Viewport, and Display. By default the output coordinate system is Display', default='Display', items=e_OutputCoordinateSystem_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_InputCoordinateSystem', 'e_OutputCoordinateSystem', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Viewport'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransformCoordinateSystems)
TYPENAMES.append('BVTK_NT_TransformCoordinateSystems' )


# --------------------------------------------------------------


class BVTK_NT_ExtractCTHPart(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractCTHPart'
    bl_label = 'vtkExtractCTHPart'
    
    m_Capping = bpy.props.BoolProperty(name='Capping', description='On by default, enables logic to cap the material volume', default=True)
    m_GenerateTriangles = bpy.props.BoolProperty(name='GenerateTriangles', description='Triangulate results. When set to false, the internal cut and contour filters are told not to triangulate results if possible. true by default', default=True)
    m_RemoveGhostCells = bpy.props.BoolProperty(name='RemoveGhostCells', description='When set to false, the output surfaces will not hide contours extracted from ghost cells. This results in overlapping contours but overcomes holes. Default is set to true', default=True)
    m_VolumeFractionSurfaceValue = bpy.props.FloatProperty(name='VolumeFractionSurfaceValue', description='Set and get the volume fraction surface value. This value should be between 0 and ', default=0.499)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Capping', 'm_GenerateTriangles', 'm_RemoveGhostCells', 'm_VolumeFractionSurfaceValue', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['ClipPlane'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractCTHPart)
TYPENAMES.append('BVTK_NT_ExtractCTHPart' )


# --------------------------------------------------------------


class BVTK_NT_LinearSelector(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LinearSelector'
    bl_label = 'vtkLinearSelector'
    
    m_EndPoint = bpy.props.FloatVectorProperty(name='EndPoint', description='Set/Get end point of intersecting segmen', default=[1.0, 1.0, 1.0], size=3)
    m_IncludeVertices = bpy.props.BoolProperty(name='IncludeVertices', description='Set/Get whether lines vertice are included in selectio', default=True)
    m_StartPoint = bpy.props.FloatVectorProperty(name='StartPoint', description='Set/Get starting point of intersecting segmen', default=[0.0, 0.0, 0.0], size=3)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Set/Get tolerance to be used by intersection algorith', default=0.0)
    m_VertexEliminationTolerance = bpy.props.FloatProperty(name='VertexEliminationTolerance', description='Set/Get relative tolerance for vertex eliminatio', default=1e-06)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_EndPoint', 'm_IncludeVertices', 'm_StartPoint', 'm_Tolerance', 'm_VertexEliminationTolerance', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Points'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LinearSelector)
TYPENAMES.append('BVTK_NT_LinearSelector' )


# --------------------------------------------------------------


class BVTK_NT_ImageAppend(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageAppend'
    bl_label = 'vtkImageAppend'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_AppendAxis = bpy.props.IntProperty(name='AppendAxis', description='This axis is expanded to hold the multiple images. The default AppendAxis is the X axis. If you want to create a volue from a series of XY images, then you should set the AppendAxis to 2 (Z axis)', default=0)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_PreserveExtents = bpy.props.BoolProperty(name='PreserveExtents', description='By default "PreserveExtents" is off and the append axis is used. When "PreseveExtents" is on, the extent of the inputs is used to place the image in the output. The whole extent of the output is the union of the input whole extents. Any portion of the output not covered by the inputs is set to zero. The origin and spacing is taken from the first input', default=True)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AppendAxis', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_PreserveExtents', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageAppend)
TYPENAMES.append('BVTK_NT_ImageAppend' )


# --------------------------------------------------------------


class BVTK_NT_PointDataToCellData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PointDataToCellData'
    bl_label = 'vtkPointDataToCellData'
    
    m_CategoricalData = bpy.props.BoolProperty(name='CategoricalData', description='Control whether the input point data is to be treated as categorical. If the data is categorical, then the resultant cell data will be determined by a "majority rules" vote, with ties going to the smaller value', default=True)
    m_PassPointData = bpy.props.BoolProperty(name='PassPointData', description='Control whether the input point data is to be passed to the output. If on, then the input point data is passed through to the output; otherwise, only generated point data is placed into the output', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CategoricalData', 'm_PassPointData', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PointDataToCellData)
TYPENAMES.append('BVTK_NT_PointDataToCellData' )


# --------------------------------------------------------------


class BVTK_NT_ImageDataGeometryFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageDataGeometryFilter'
    bl_label = 'vtkImageDataGeometryFilter'
    
    m_OutputTriangles = bpy.props.BoolProperty(name='OutputTriangles', description='Set OutputTriangles to true if you wish to generate triangles instead of quads when extracting cells from 2D imagedata Currently this functionality is only implemented for 2D imagedat', default=True)
    m_ThresholdCells = bpy.props.BoolProperty(name='ThresholdCells', description='Set ThresholdCells to true if you wish to skip any voxel/pixels which have scalar values less than the specified threshold. Currently this functionality is only implemented for 2D imagedat', default=True)
    m_ThresholdValue = bpy.props.BoolProperty(name='ThresholdValue', description='Set ThresholdValue to the scalar value by which to threshold cells when extracting geometry when ThresholdCells is true. Cells with scalar values greater than the threshold will be output', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_OutputTriangles', 'm_ThresholdCells', 'm_ThresholdValue', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageDataGeometryFilter)
TYPENAMES.append('BVTK_NT_ImageDataGeometryFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageIslandRemoval2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageIslandRemoval2D'
    bl_label = 'vtkImageIslandRemoval2D'
    
    m_AreaThreshold = bpy.props.IntProperty(name='AreaThreshold', description='Set/Get the cutoff area for remova', default=4)
    m_IslandValue = bpy.props.FloatProperty(name='IslandValue', description='Set/Get the value to remove', default=0.0)
    m_ReplaceValue = bpy.props.FloatProperty(name='ReplaceValue', description='Set/Get the value to put in the place of removed pixels', default=255.0)
    m_SquareNeighborhood = bpy.props.BoolProperty(name='SquareNeighborhood', description='Set/Get whether to use 4 or 8 neighbor', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AreaThreshold', 'm_IslandValue', 'm_ReplaceValue', 'm_SquareNeighborhood', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageIslandRemoval2D)
TYPENAMES.append('BVTK_NT_ImageIslandRemoval2D' )


# --------------------------------------------------------------


class BVTK_NT_TableToStructuredGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TableToStructuredGrid'
    bl_label = 'vtkTableToStructuredGrid'
    
    m_XColumn = bpy.props.StringProperty(name='XColumn', description='Set the name of the column to use as the X coordinate for the points')
    m_XComponent = bpy.props.IntProperty(name='XComponent', description='Specify the component for the column specified using SetXColumn() to use as the xcoordinate in case the column is a multi-component array. Default is 0', default=0)
    m_YColumn = bpy.props.StringProperty(name='YColumn', description='Set the name of the column to use as the Y coordinate for the points. Default is 0')
    m_YComponent = bpy.props.IntProperty(name='YComponent', description='Specify the component for the column specified using SetYColumn() to use as the Ycoordinate in case the column is a multi-component array', default=0)
    m_ZColumn = bpy.props.StringProperty(name='ZColumn', description='Set the name of the column to use as the Z coordinate for the points. Default is 0')
    m_ZComponent = bpy.props.IntProperty(name='ZComponent', description='Specify the component for the column specified using SetZColumn() to use as the Zcoordinate in case the column is a multi-component array', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_XColumn', 'm_XComponent', 'm_YColumn', 'm_YComponent', 'm_ZColumn', 'm_ZComponent', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TableToStructuredGrid)
TYPENAMES.append('BVTK_NT_TableToStructuredGrid' )


# --------------------------------------------------------------


class BVTK_NT_OverlappingAMRLevelIdScalars(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_OverlappingAMRLevelIdScalars'
    bl_label = 'vtkOverlappingAMRLevelIdScalars'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_OverlappingAMRLevelIdScalars)
TYPENAMES.append('BVTK_NT_OverlappingAMRLevelIdScalars' )


# --------------------------------------------------------------


class BVTK_NT_ExtractDataOverTime(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractDataOverTime'
    bl_label = 'vtkExtractDataOverTime'
    
    m_PointIndex = bpy.props.IntProperty(name='PointIndex', description='Index of point to extract at each time ste', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PointIndex', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractDataOverTime)
TYPENAMES.append('BVTK_NT_ExtractDataOverTime' )


# --------------------------------------------------------------


class BVTK_NT_AMRResampleFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AMRResampleFilter'
    bl_label = 'vtkAMRResampleFilter'
    
    m_BiasVector = bpy.props.FloatVectorProperty(name='BiasVector', description='', default=[0.0, 0.0, 0.0], size=3)
    m_DemandDrivenMode = bpy.props.IntProperty(name='DemandDrivenMode', description='Set & Get macro to allow the filter to operate in both demand-driven and standard mode', default=0)
    m_Max = bpy.props.FloatVectorProperty(name='Max', description='', default=[1.0, 1.0, 1.0], size=3)
    m_Min = bpy.props.FloatVectorProperty(name='Min', description='', default=[0.0, 0.0, 0.0], size=3)
    m_NumberOfPartitions = bpy.props.IntProperty(name='NumberOfPartitions', description='Set & Get macro for the number of subdivision', default=1)
    m_NumberOfSamples = bpy.props.IntVectorProperty(name='NumberOfSamples', description='', default=[10, 10, 10], size=3)
    m_TransferToNodes = bpy.props.IntProperty(name='TransferToNodes', description='Set & Get macro for the TransferToNodes fla', default=1)
    m_UseBiasVector = bpy.props.BoolProperty(name='UseBiasVector', description='Set & Get macro for the number of subdivision', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BiasVector', 'm_DemandDrivenMode', 'm_Max', 'm_Min', 'm_NumberOfPartitions', 'm_NumberOfSamples', 'm_TransferToNodes', 'm_UseBiasVector', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AMRResampleFilter)
TYPENAMES.append('BVTK_NT_AMRResampleFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractTimeSteps(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractTimeSteps'
    bl_label = 'vtkExtractTimeSteps'
    e_TimeEstimationMode_items = [(x, x, x) for x in ['Nearest', 'Next', 'Previous']]
    
    m_Range = bpy.props.IntVectorProperty(name='Range', description='', default=[0, 0], size=2)
    e_TimeEstimationMode = bpy.props.EnumProperty(name='TimeEstimationMode', description='Get/Set what to do when the requested time is not one of the timesteps this filter is set to extract. Should be one of the values of the enum vtkExtractTimeSteps::EstimationMode. The default is PREVIOUS_TIMESTEP', default='Previous', items=e_TimeEstimationMode_items)
    m_TimeStepInterval = bpy.props.IntProperty(name='TimeStepInterval', description="Get/Set the time step interval to extract. This is the N in 'extract every Nth timestep in this range'. Default to 1 or 'extract all timesteps in this range", default=1)
    m_UseRange = bpy.props.BoolProperty(name='UseRange', description='Get/Set whether to extract a range of timesteps. When false, extracts the time steps explicitly set with SetTimeStepIndices. Defaults to false', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Range', 'e_TimeEstimationMode', 'm_TimeStepInterval', 'm_UseRange', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractTimeSteps)
TYPENAMES.append('BVTK_NT_ExtractTimeSteps' )


# --------------------------------------------------------------


class BVTK_NT_HyperTreeGridGeometry(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperTreeGridGeometry'
    bl_label = 'vtkHyperTreeGridGeometry'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperTreeGridGeometry)
TYPENAMES.append('BVTK_NT_HyperTreeGridGeometry' )


# --------------------------------------------------------------


class BVTK_NT_AMRToMultiBlockFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AMRToMultiBlockFilter'
    bl_label = 'vtkAMRToMultiBlockFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AMRToMultiBlockFilter)
TYPENAMES.append('BVTK_NT_AMRToMultiBlockFilter' )


# --------------------------------------------------------------


class BVTK_NT_ReverseSense(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ReverseSense'
    bl_label = 'vtkReverseSense'
    
    m_ReverseCells = bpy.props.BoolProperty(name='ReverseCells', description='Flag controls whether to reverse cell ordering', default=True)
    m_ReverseNormals = bpy.props.BoolProperty(name='ReverseNormals', description='Flag controls whether to reverse normal orientation', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ReverseCells', 'm_ReverseNormals', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ReverseSense)
TYPENAMES.append('BVTK_NT_ReverseSense' )


# --------------------------------------------------------------


class BVTK_NT_ProcessIdScalars(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProcessIdScalars'
    bl_label = 'vtkProcessIdScalars'
    
    m_RandomMode = bpy.props.BoolProperty(name='RandomMode', description='', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_RandomMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProcessIdScalars)
TYPENAMES.append('BVTK_NT_ProcessIdScalars' )


# --------------------------------------------------------------


class BVTK_NT_ImageIdealLowPass(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageIdealLowPass'
    bl_label = 'vtkImageIdealLowPass'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_CutOff = bpy.props.FloatVectorProperty(name='CutOff', description='', default=[1e+30, 1e+30, 1e+30], size=3)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_XCutOff = bpy.props.FloatProperty(name='XCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    m_YCutOff = bpy.props.FloatProperty(name='YCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    m_ZCutOff = bpy.props.FloatProperty(name='ZCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CutOff', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', 'm_XCutOff', 'm_YCutOff', 'm_ZCutOff', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageIdealLowPass)
TYPENAMES.append('BVTK_NT_ImageIdealLowPass' )


# --------------------------------------------------------------


class BVTK_NT_HyperTreeGridAxisReflection(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperTreeGridAxisReflection'
    bl_label = 'vtkHyperTreeGridAxisReflection'
    e_Plane_items = [(x, x, x) for x in ['X', 'XMax', 'XMin', 'Y', 'YMax', 'YMin', 'Z', 'ZMax', 'ZMin']]
    
    m_Center = bpy.props.FloatProperty(name='Center', description='If the reflection plane is set to X, Y or Z, this variable is use to set the position of the plane', default=0.0)
    e_Plane = bpy.props.EnumProperty(name='Plane', description='Set the normal of the plane to use as mirror', default='XMin', items=e_Plane_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'e_Plane', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperTreeGridAxisReflection)
TYPENAMES.append('BVTK_NT_HyperTreeGridAxisReflection' )


# --------------------------------------------------------------


class BVTK_NT_ImageHSIToRGB(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageHSIToRGB'
    bl_label = 'vtkImageHSIToRGB'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Maximum = bpy.props.FloatProperty(name='Maximum', description='Hue is an angle. Maximum specifies when it maps back to 0. HueMaximum defaults to 255 instead of 2PI, because unsigned char is expected as input. Maximum also specifies the maximum of the Saturation, and R, G, B', default=255.0)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Maximum', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageHSIToRGB)
TYPENAMES.append('BVTK_NT_ImageHSIToRGB' )


# --------------------------------------------------------------


class BVTK_NT_PolyDataStreamer(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PolyDataStreamer'
    bl_label = 'vtkPolyDataStreamer'
    
    m_ColorByPiece = bpy.props.BoolProperty(name='ColorByPiece', description='By default, this option is off. When it is on, cell scalars are generated based on which piece they are in', default=True)
    m_NumberOfStreamDivisions = bpy.props.IntProperty(name='NumberOfStreamDivisions', description='Set the number of pieces to divide the problem into', default=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ColorByPiece', 'm_NumberOfStreamDivisions', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PolyDataStreamer)
TYPENAMES.append('BVTK_NT_PolyDataStreamer' )


# --------------------------------------------------------------


class BVTK_NT_SMPContourGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SMPContourGrid'
    bl_label = 'vtkSMPContourGrid'
    
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description="Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off. @deprecated ComputeGradients is not used so these methods don't affect anything (VTK 6.0)", default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_GenerateTriangles = bpy.props.BoolProperty(name='GenerateTriangles', description='If this is enabled (by default), the output will be triangles otherwise, the output will be the intersection polygons WARNING: if the cutting function is not a plane, the output will be 3D poygons, which might be nice to look at but hard to compute with downstream', default=True)
    m_MergePieces = bpy.props.BoolProperty(name='MergePieces', description='If MergePieces is true (default), this filter will merge all pieces generated by processing the input with multiple threads. The output will be a vtkPolyData. Note that this has a slight overhead which becomes more significant as the number of threads used grows. If MergePieces is false, this filter will generate a vtkMultiBlock of vtkPolyData where the number of pieces will be equal to the number of threads used', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Methods to set / get contour values', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_GenerateTriangles', 'm_MergePieces', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SMPContourGrid)
TYPENAMES.append('BVTK_NT_SMPContourGrid' )


# --------------------------------------------------------------


class BVTK_NT_LabelSizeCalculator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LabelSizeCalculator'
    bl_label = 'vtkLabelSizeCalculator'
    
    m_DPI = bpy.props.IntProperty(name='DPI', description='Get/Set the DPI at which the labels are to be rendered. Defaults to 72. @sa vtkWindow::GetDPI(', default=72)
    m_LabelSizeArrayName = bpy.props.StringProperty(name='LabelSizeArrayName', description='The name of the output array containing text label sizes This defaults to "LabelSize', default='LabelSize')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DPI', 'm_LabelSizeArrayName', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LabelSizeCalculator)
TYPENAMES.append('BVTK_NT_LabelSizeCalculator' )


# --------------------------------------------------------------


class BVTK_NT_DataSetSurfaceFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataSetSurfaceFilter'
    bl_label = 'vtkDataSetSurfaceFilter'
    
    m_NonlinearSubdivisionLevel = bpy.props.IntProperty(name='NonlinearSubdivisionLevel', description='If the input is an unstructured grid with nonlinear faces, this parameter determines how many times the face is subdivided into linear faces. If 0, the output is the equivalent of its linear couterpart (and the midpoints determining the nonlinear interpolation are discarded). If 1 (the default), the nonlinear face is triangulated based on the midpoints. If greater than 1, the triangulated pieces are recursively subdivided to reach the desired subdivision. Setting the value to greater than 1 may cause some point data to not be passed even if no nonlinear faces exist. This option has no effect if the input is not an unstructured grid', default=1)
    m_OriginalCellIdsName = bpy.props.StringProperty(name='OriginalCellIdsName', description='If PassThroughCellIds or PassThroughPointIds is on, then these ivars control the name given to the field in which the ids are written into. If set to nullptr, then vtkOriginalCellIds or vtkOriginalPointIds (the default) is used, respectively', default='vtkOriginalCellIds')
    m_OriginalPointIdsName = bpy.props.StringProperty(name='OriginalPointIdsName', description='If PassThroughCellIds or PassThroughPointIds is on, then these ivars control the name given to the field in which the ids are written into. If set to nullptr, then vtkOriginalCellIds or vtkOriginalPointIds (the default) is used, respectively', default='vtkOriginalPointIds')
    m_PassThroughCellIds = bpy.props.BoolProperty(name='PassThroughCellIds', description='If on, the output polygonal dataset will have a celldata array that holds the cell index of the original 3D cell that produced each output cell. This is useful for cell picking. The default is off to conserve memory. Note that PassThroughCellIds will be ignored if UseStrips is on, since in that case each tringle strip can represent more than on of the input cells', default=True)
    m_PassThroughPointIds = bpy.props.BoolProperty(name='PassThroughPointIds', description='If on, the output polygonal dataset will have a celldata array that holds the cell index of the original 3D cell that produced each output cell. This is useful for cell picking. The default is off to conserve memory. Note that PassThroughCellIds will be ignored if UseStrips is on, since in that case each tringle strip can represent more than on of the input cells', default=True)
    m_PieceInvariant = bpy.props.IntProperty(name='PieceInvariant', description='If PieceInvariant is true, vtkDataSetSurfaceFilter requests 1 ghost level from input in order to remove internal surface that are between processes. False by default', default=0)
    m_UseStrips = bpy.props.BoolProperty(name='UseStrips', description='When input is structured data, this flag will generate faces with triangle strips. This should render faster and use less memory, but no cell data is copied. By default, UseStrips is Off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NonlinearSubdivisionLevel', 'm_OriginalCellIdsName', 'm_OriginalPointIdsName', 'm_PassThroughCellIds', 'm_PassThroughPointIds', 'm_PieceInvariant', 'm_UseStrips', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataSetSurfaceFilter)
TYPENAMES.append('BVTK_NT_DataSetSurfaceFilter' )


# --------------------------------------------------------------


class BVTK_NT_GenericGeometryFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GenericGeometryFilter'
    bl_label = 'vtkGenericGeometryFilter'
    
    m_CellClipping = bpy.props.BoolProperty(name='CellClipping', description='Turn on/off selection of geometry by cell id', default=True)
    m_CellMaximum = bpy.props.IntProperty(name='CellMaximum', description='Specify the maximum cell id for point id selection', default=1000000000)
    m_CellMinimum = bpy.props.IntProperty(name='CellMinimum', description='Specify the minimum cell id for point id selection', default=0)
    m_ExtentClipping = bpy.props.BoolProperty(name='ExtentClipping', description='Turn on/off selection of geometry via bounding box', default=True)
    m_Merging = bpy.props.BoolProperty(name='Merging', description='Turn on/off merging of coincident points. Note that is merging is on, points with different point attributes (e.g., normals) are merged, which may cause rendering artifacts', default=True)
    m_PassThroughCellIds = bpy.props.BoolProperty(name='PassThroughCellIds', description='If on, the output polygonal dataset will have a celldata array that holds the cell index of the original 3D cell that produced each output cell. This is useful for cell picking. The default is off to conserve memory', default=True)
    m_PointClipping = bpy.props.BoolProperty(name='PointClipping', description='Turn on/off selection of geometry by point id', default=True)
    m_PointMaximum = bpy.props.IntProperty(name='PointMaximum', description='Specify the maximum point id for point id selection', default=1000000000)
    m_PointMinimum = bpy.props.IntProperty(name='PointMinimum', description='Specify the minimum point id for point id selection', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CellClipping', 'm_CellMaximum', 'm_CellMinimum', 'm_ExtentClipping', 'm_Merging', 'm_PassThroughCellIds', 'm_PointClipping', 'm_PointMaximum', 'm_PointMinimum', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GenericGeometryFilter)
TYPENAMES.append('BVTK_NT_GenericGeometryFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageSobel3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageSobel3D'
    bl_label = 'vtkImageSobel3D'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageSobel3D)
TYPENAMES.append('BVTK_NT_ImageSobel3D' )


# --------------------------------------------------------------


class BVTK_NT_ImageMirrorPad(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMirrorPad'
    bl_label = 'vtkImageMirrorPad'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_OutputNumberOfScalarComponents = bpy.props.IntProperty(name='OutputNumberOfScalarComponents', description='Set/Get the number of output scalar components', default=-1)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_OutputNumberOfScalarComponents', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMirrorPad)
TYPENAMES.append('BVTK_NT_ImageMirrorPad' )


# --------------------------------------------------------------


class BVTK_NT_HierarchicalBinningFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HierarchicalBinningFilter'
    bl_label = 'vtkHierarchicalBinningFilter'
    
    m_Automatic = bpy.props.BoolProperty(name='Automatic', description='Specify whether to determine the determine the level divisions, and the bounding box automatically (by default this is on). If off, then the user must specify both the bounding box and bin divisions. (Computing the bounding box can be slow for large point clouds, manual specification can save time.', default=True)
    m_Bounds = bpy.props.FloatVectorProperty(name='Bounds', description='Set the bounding box of the point cloud. If Automatic is enabled, then this is computed during filter execution. If manually specified (Automatic is off) then make sure the bounds is represented as (xmin,xmax, ymin,ymax, zmin,zmax). If the bounds specified is does not enclose the points, then points are clamped to lie in the bounding box', default=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0], size=6)
    m_Divisions = bpy.props.IntVectorProperty(name='Divisions', description='Set the number of branching divisions in each binning direction. Each level of the tree is subdivided by this factor. The Divisions[i] must be >= 1. Note: if Automatic subdivision is specified, the the Divisions are set by the filter', default=[2, 2, 2], size=3)
    m_NumberOfLevels = bpy.props.IntProperty(name='NumberOfLevels', description='Specify the number of levels in the spatial hierarchy. By default, the number of levels is three', default=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Automatic', 'm_Bounds', 'm_Divisions', 'm_NumberOfLevels', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HierarchicalBinningFilter)
TYPENAMES.append('BVTK_NT_HierarchicalBinningFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageAnisotropicDiffusion2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageAnisotropicDiffusion2D'
    bl_label = 'vtkImageAnisotropicDiffusion2D'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_Corners = bpy.props.BoolProperty(name='Corners', description='Choose neighbors to diffuse (6 faces, 12 edges, 8 corners)', default=True)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_DiffusionFactor = bpy.props.FloatProperty(name='DiffusionFactor', description='The diffusion factor specifies how much neighboring pixels effect each other. No diffusion occurs with a factor of 0, and a diffusion factor of 1 causes the pixel to become the average of all its neighbors', default=1.0)
    m_DiffusionThreshold = bpy.props.FloatProperty(name='DiffusionThreshold', description='Set/Get the difference threshold that stops diffusion. when the difference between two pixel is greater than this threshold, the pixels are not diffused. This causes diffusion to avoid sharp edges. If the GradientMagnitudeThreshold is set, then gradient magnitude is used for comparison instead of pixel differences', default=5.0)
    m_Edges = bpy.props.BoolProperty(name='Edges', description='Choose neighbors to diffuse (6 faces, 12 edges, 8 corners)', default=True)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_Faces = bpy.props.BoolProperty(name='Faces', description='Choose neighbors to diffuse (6 faces, 12 edges, 8 corners)', default=True)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_GradientMagnitudeThreshold = bpy.props.BoolProperty(name='GradientMagnitudeThreshold', description='Switch between gradient magnitude threshold and pixel gradient threshold', default=True)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfIterations = bpy.props.IntProperty(name='NumberOfIterations', description='This method sets the number of interations which also affects the input neighborhood needed to compute one output pixel. Each iterations requires an extra pixel layer on the neighborhood. This is only relavent when you are trying to stream or are requesting a sub extent of the "wholeExtent"', default=4)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Corners', 'm_DesiredBytesPerPiece', 'm_DiffusionFactor', 'm_DiffusionThreshold', 'm_Edges', 'm_EnableSMP', 'm_Faces', 'm_GlobalDefaultEnableSMP', 'm_GradientMagnitudeThreshold', 'm_MinimumPieceSize', 'm_NumberOfIterations', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageAnisotropicDiffusion2D)
TYPENAMES.append('BVTK_NT_ImageAnisotropicDiffusion2D' )


# --------------------------------------------------------------


class BVTK_NT_TemporalStatistics(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TemporalStatistics'
    bl_label = 'vtkTemporalStatistics'
    
    m_ComputeAverage = bpy.props.BoolProperty(name='ComputeAverage', description='Turn on/off the computation of the average values over time. On by default. The resulting array names have "_average" appended to them', default=True)
    m_ComputeMaximum = bpy.props.BoolProperty(name='ComputeMaximum', description='Turn on/off the computation of the maximum values over time. On by default. The resulting array names have "_maximum" appended to them', default=True)
    m_ComputeMinimum = bpy.props.BoolProperty(name='ComputeMinimum', description='Turn on/off the computation of the minimum values over time. On by default. The resulting array names have "_minimum" appended to them', default=True)
    m_ComputeStandardDeviation = bpy.props.BoolProperty(name='ComputeStandardDeviation', description='', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeAverage', 'm_ComputeMaximum', 'm_ComputeMinimum', 'm_ComputeStandardDeviation', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TemporalStatistics)
TYPENAMES.append('BVTK_NT_TemporalStatistics' )


# --------------------------------------------------------------


class BVTK_NT_MultiBlockFromTimeSeriesFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MultiBlockFromTimeSeriesFilter'
    bl_label = 'vtkMultiBlockFromTimeSeriesFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MultiBlockFromTimeSeriesFilter)
TYPENAMES.append('BVTK_NT_MultiBlockFromTimeSeriesFilter' )


# --------------------------------------------------------------


class BVTK_NT_MaskPoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MaskPoints'
    bl_label = 'vtkMaskPoints'
    
    m_GenerateVertices = bpy.props.BoolProperty(name='GenerateVertices', description='Generate output polydata vertices as well as points. A useful convenience method because vertices are drawn (they are topology) while points are not (they are geometry). By default this method is off', default=True)
    m_MaximumNumberOfPoints = bpy.props.IntProperty(name='MaximumNumberOfPoints', description='Limit the number of points that can be passed through (i.e., sets the output sample size)', default=1000000000)
    m_Offset = bpy.props.IntProperty(name='Offset', description='Start sampling with this point. Ignored by certain random modes', default=0)
    m_OnRatio = bpy.props.IntProperty(name='OnRatio', description='Turn on every nth point (strided sampling), ignored by random modes', default=2)
    m_ProportionalMaximumNumberOfPoints = bpy.props.BoolProperty(name='ProportionalMaximumNumberOfPoints', description='THIS ONLY WORKS WITH THE PARALLEL IMPLEMENTATION vtkPMaskPoints RUNNING IN PARALLEL. NOTHING WILL CHANGE IF THIS IS NOT THE PARALLEL vtkPMaskPoints. Determines whether maximum number of points is taken per processor (default) or if the maximum number of points is proportionally taken across processors (i.e., number of points per processor = points on a processor * maximum number of points / total points across all processors). In the first case, the total number of points = maximum number of points * number of processors. In the second case, the total number of points = maximum number of points', default=True)
    m_RandomMode = bpy.props.BoolProperty(name='RandomMode', description='Special flag causes randomization of point selection', default=True)
    m_RandomModeType = bpy.props.IntProperty(name='RandomModeType', description='Special mode selector that switches between random mode types. 0 - randomized strides: randomly strides through the data (default); fairly certain that this is not a statistically random sample because the output depends on the order of the input and the input points do not have an equal chance to appear in the output (plus Vitter\'s incremental random algorithms are more complex than this, while not a proof it is good indication this isn\'t a statistically random sample - the closest would be algorithm S) 1 - random sample: create a statistically random sample using Vitter\'s incremental algorithm D without A described in Vitter "Faster Mthods for Random Sampling", Communications of the ACM Volume 27, Issue 7, 1984 (OnRatio and Offset are ignored) O(sample size) 2 - spatially stratified random sample: create a spatially stratified random sample using the first method described in Woodring et al. "In-situ Sampling of a Large-Scale Particle Simulation for Interactive Visualization and Analysis", Computer Graphics Forum, 2011 (EuroVis 2011). (OnRatio and Offset are ignored) O(N log N', default=0)
    m_SingleVertexPerCell = bpy.props.BoolProperty(name='SingleVertexPerCell', description='When vertex generation is enabled, by default vertices are produced as multi-vertex cells (more than one per cell), if you wish to have a single vertex per cell, enable this flag', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateVertices', 'm_MaximumNumberOfPoints', 'm_Offset', 'm_OnRatio', 'm_ProportionalMaximumNumberOfPoints', 'm_RandomMode', 'm_RandomModeType', 'm_SingleVertexPerCell', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MaskPoints)
TYPENAMES.append('BVTK_NT_MaskPoints' )


# --------------------------------------------------------------


class BVTK_NT_OutlineCornerFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_OutlineCornerFilter'
    bl_label = 'vtkOutlineCornerFilter'
    
    m_CornerFactor = bpy.props.FloatProperty(name='CornerFactor', description='Set/Get the factor that controls the relative size of the corners to the length of the corresponding bound', default=0.2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CornerFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_OutlineCornerFilter)
TYPENAMES.append('BVTK_NT_OutlineCornerFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractBlock(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractBlock'
    bl_label = 'vtkExtractBlock'
    
    m_MaintainStructure = bpy.props.BoolProperty(name='MaintainStructure', description='This is used only when PruneOutput is ON. By default, when pruning the output i.e. remove empty blocks, if node has only 1 non-null child block, then that node is removed. To preserve these parent nodes, set this flag to true. Off by default', default=True)
    m_PruneOutput = bpy.props.BoolProperty(name='PruneOutput', description='When set, the output mutliblock dataset will be pruned to remove empty nodes. On by default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MaintainStructure', 'm_PruneOutput', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractBlock)
TYPENAMES.append('BVTK_NT_ExtractBlock' )


# --------------------------------------------------------------


class BVTK_NT_ContourLoopExtraction(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ContourLoopExtraction'
    bl_label = 'vtkContourLoopExtraction'
    e_LoopClosure_items = [(x, x, x) for x in ['All', 'Boundary', 'Off']]
    
    e_LoopClosure = bpy.props.EnumProperty(name='LoopClosure', description='Specify whether to close loops or not. All loops can be closed; boundary loops (x or y vertical or horizontal lines) can be closed (default); or all loops can be closed', default='Boundary', items=e_LoopClosure_items)
    m_Normal = bpy.props.FloatVectorProperty(name='Normal', description='', default=[0.0, 0.0, 1.0], size=3)
    m_ScalarRange = bpy.props.FloatVectorProperty(name='ScalarRange', description='', default=[0.0, 1.0], size=2)
    m_ScalarThresholding = bpy.props.BoolProperty(name='ScalarThresholding', description='Turn on/off the extraction of loops based on scalar thresholding. Loops with scalar values in a specified range can be extracted. If no scalars are available from the input than this data member is ignored', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_LoopClosure', 'm_Normal', 'm_ScalarRange', 'm_ScalarThresholding', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ContourLoopExtraction)
TYPENAMES.append('BVTK_NT_ContourLoopExtraction' )


# --------------------------------------------------------------


class BVTK_NT_OutlineFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_OutlineFilter'
    bl_label = 'vtkOutlineFilter'
    
    m_GenerateFaces = bpy.props.BoolProperty(name='GenerateFaces', description='Generate solid faces for the box. This is off by default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateFaces', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_OutlineFilter)
TYPENAMES.append('BVTK_NT_OutlineFilter' )


# --------------------------------------------------------------


class BVTK_NT_CollectGraph(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CollectGraph'
    bl_label = 'vtkCollectGraph'
    
    m_OutputType = bpy.props.IntProperty(name='OutputType', description='Directedness flag, used to signal whether the output graph is directed or undirected. DIRECTED_OUTPUT expects that this filter is generating a directed graph. UNDIRECTED_OUTPUT expects that this filter is generating an undirected graph. DIRECTED_OUTPUT and UNDIRECTED_OUTPUT flags should only be set on the client filter. Server filters should be set to USE_INPUT_TYPE since they have valid input and the directedness is determined from the input type', default=2)
    m_PassThrough = bpy.props.BoolProperty(name='PassThrough', description='To collect or just copy input to output. Off (collect) by default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_OutputType', 'm_PassThrough', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CollectGraph)
TYPENAMES.append('BVTK_NT_CollectGraph' )


# --------------------------------------------------------------


class BVTK_NT_StructuredGridGeometryFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StructuredGridGeometryFilter'
    bl_label = 'vtkStructuredGridGeometryFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StructuredGridGeometryFilter)
TYPENAMES.append('BVTK_NT_StructuredGridGeometryFilter' )


# --------------------------------------------------------------


class BVTK_NT_HyperTreeGridThreshold(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperTreeGridThreshold'
    bl_label = 'vtkHyperTreeGridThreshold'
    
    m_LowerThreshold = bpy.props.FloatProperty(name='LowerThreshold', description='Set/Get minimum scalar value of threshol', default=2.2250738585072014e-308)
    m_UpperThreshold = bpy.props.FloatProperty(name='UpperThreshold', description='Set/Get maximum scalar value of threshol', default=1e+30)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_LowerThreshold', 'm_UpperThreshold', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperTreeGridThreshold)
TYPENAMES.append('BVTK_NT_HyperTreeGridThreshold' )


# --------------------------------------------------------------


class BVTK_NT_GaussianSplatter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GaussianSplatter'
    bl_label = 'vtkGaussianSplatter'
    e_AccumulationMode_items = [(x, x, x) for x in ['Max', 'Min', 'Sum']]
    
    e_AccumulationMode = bpy.props.EnumProperty(name='AccumulationMode', description='Specify the scalar accumulation mode. This mode expresses how scalar values are combined when splats are overlapped. The Max mode acts like a set union operation and is the most commonly used; the Min mode acts like a set intersection, and the sum is just weird', default='Max', items=e_AccumulationMode_items)
    m_CapValue = bpy.props.FloatProperty(name='CapValue', description='Specify the cap value to use. (This instance variable only has effect if the ivar Capping is on.', default=0.0)
    m_Capping = bpy.props.BoolProperty(name='Capping', description='Turn on/off the capping of the outer boundary of the volume to a specified cap value. This can be used to close surfaces (after iso-surfacing) and create other effects', default=True)
    m_Eccentricity = bpy.props.FloatProperty(name='Eccentricity', description='Control the shape of elliptical splatting. Eccentricity is the ratio of the major axis (aligned along normal) to the minor (axes) aligned along other two axes. So Eccentricity > 1 creates needles with the long axis in the direction of the normal; Eccentricity<1 creates pancakes perpendicular to the normal vector', default=2.5)
    m_ExponentFactor = bpy.props.FloatProperty(name='ExponentFactor', description='Set / get the sharpness of decay of the splats. This is the exponent constant in the Gaussian equation. Normally this is a negative value', default=-5.0)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Set / get the (xmin,xmax, ymin,ymax, zmin,zmax) bounding box in which the sampling is performed. If any of the (min,max) bounds values are min >= max, then the bounds will be computed automatically from the input data. Otherwise, the user-specified bounds will be used', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6)
    m_NormalWarping = bpy.props.BoolProperty(name='NormalWarping', description='Turn on/off the generation of elliptical splats. If normal warping is on, then the input normals affect the distribution of the splat. This boolean is used in combination with the Eccentricity ivar', default=True)
    m_NullValue = bpy.props.FloatProperty(name='NullValue', description='Set the Null value for output points not receiving a contribution from the input points. (This is the initial value of the voxel samples.', default=0.0)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set / get the radius of propagation of the splat. This value is expressed as a percentage of the length of the longest side of the sampling volume. Smaller numbers greatly reduce execution time', default=0.1)
    m_ScalarWarping = bpy.props.BoolProperty(name='ScalarWarping', description='Turn on/off the scaling of splats by scalar value', default=True)
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Multiply Gaussian splat distribution by this value. If ScalarWarping is on, then the Scalar value will be multiplied by the ScaleFactor times the Gaussian function', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_AccumulationMode', 'm_CapValue', 'm_Capping', 'm_Eccentricity', 'm_ExponentFactor', 'm_ModelBounds', 'm_NormalWarping', 'm_NullValue', 'm_Radius', 'm_ScalarWarping', 'm_ScaleFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GaussianSplatter)
TYPENAMES.append('BVTK_NT_GaussianSplatter' )


# --------------------------------------------------------------


class BVTK_NT_SplitColumnComponents(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SplitColumnComponents'
    bl_label = 'vtkSplitColumnComponents'
    e_NamingMode_items = [(x, x, x) for x in ['NamesWithParens', 'NamesWithUnderscores', 'NumberWithParens', 'NumberWithUnderscores']]
    
    m_CalculateMagnitudes = bpy.props.BoolProperty(name='CalculateMagnitudes', description='If on this filter will calculate an additional magnitude column for all columns it splits with two or more components. Default is on', default=True)
    e_NamingMode = bpy.props.EnumProperty(name='NamingMode', description='Get/Set the array naming mode. Description is NUMBERS_WITH_PARENS', default='NumberWithParens', items=e_NamingMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CalculateMagnitudes', 'e_NamingMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SplitColumnComponents)
TYPENAMES.append('BVTK_NT_SplitColumnComponents' )


# --------------------------------------------------------------


class BVTK_NT_PassArrays(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PassArrays'
    bl_label = 'vtkPassArrays'
    
    m_RemoveArrays = bpy.props.BoolProperty(name='RemoveArrays', description='Instead of passing only the specified arrays, remove the specified arrays and keep all other arrays. Default is off', default=False)
    m_UseFieldTypes = bpy.props.BoolProperty(name='UseFieldTypes', description='Process only those field types explicitly specified with AddFieldType. Otherwise, processes field types associated with at least one specified array. Default is off', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_RemoveArrays', 'm_UseFieldTypes', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PassArrays)
TYPENAMES.append('BVTK_NT_PassArrays' )


# --------------------------------------------------------------


class BVTK_NT_ImageDataToPointSet(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageDataToPointSet'
    bl_label = 'vtkImageDataToPointSet'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageDataToPointSet)
TYPENAMES.append('BVTK_NT_ImageDataToPointSet' )


# --------------------------------------------------------------


class BVTK_NT_ExtractUserDefinedPiece(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractUserDefinedPiece'
    bl_label = 'vtkExtractUserDefinedPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty(name='CreateGhostCells', description='Turn on/off creating ghost cells (on by default)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CreateGhostCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractUserDefinedPiece)
TYPENAMES.append('BVTK_NT_ExtractUserDefinedPiece' )


# --------------------------------------------------------------


class BVTK_NT_ImageResize(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageResize'
    bl_label = 'vtkImageResize'
    e_ResizeMethod_items = [(x, x, x) for x in ['MagnificationFactors', 'OutputDimensions', 'OutputSpacing']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_Border = bpy.props.BoolProperty(name='Border', description='If Border is Off (the default), then the centers of each of the corner voxels will be considered to form the rectangular bounds of the image. This is the way that VTK normally computes image bounds. If Border is On, then the image bounds will be defined by the outer corners of the voxels. This setting impacts how the resizing is done. For example, if a MagnificationFactor of two is applied to a 256x256 image, the output image will be 512x512 if Border is On, or 511x511 if Border is Off', default=True)
    m_Cropping = bpy.props.BoolProperty(name='Cropping', description='Whether to crop the input image before resizing (Off by default). If this is On, then the CroppingRegion must be set', default=True)
    m_CroppingRegion = bpy.props.FloatVectorProperty(name='CroppingRegion', description='', default=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0], size=6)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=0)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Interpolate = bpy.props.BoolProperty(name='Interpolate', description='Turn interpolation on or off (by default, interpolation is on)', default=True)
    m_MagnificationFactors = bpy.props.FloatVectorProperty(name='MagnificationFactors', description='', default=[1.0, 1.0, 1.0], size=3)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_OutputDimensions = bpy.props.IntVectorProperty(name='OutputDimensions', description='', default=[-1, -1, -1], size=3)
    m_OutputSpacing = bpy.props.FloatVectorProperty(name='OutputSpacing', description='', default=[0.0, 0.0, 0.0], size=3)
    e_ResizeMethod = bpy.props.EnumProperty(name='ResizeMethod', description='The resizing method to use. The default is to set the output image dimensions, and allow the filter to resize the image to these new dimensions. It is also possible to resize the image by setting the output image spacing or by setting a magnification factor', default='OutputDimensions', items=e_ResizeMethod_items)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Border', 'm_Cropping', 'm_CroppingRegion', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Interpolate', 'm_MagnificationFactors', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_OutputDimensions', 'm_OutputSpacing', 'e_ResizeMethod', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Interpolator'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageResize)
TYPENAMES.append('BVTK_NT_ImageResize' )


# --------------------------------------------------------------


class BVTK_NT_ProgrammableAttributeDataFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProgrammableAttributeDataFilter'
    bl_label = 'vtkProgrammableAttributeDataFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProgrammableAttributeDataFilter)
TYPENAMES.append('BVTK_NT_ProgrammableAttributeDataFilter' )


# --------------------------------------------------------------


class BVTK_NT_AdaptiveDataSetSurfaceFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AdaptiveDataSetSurfaceFilter'
    bl_label = 'vtkAdaptiveDataSetSurfaceFilter'
    
    m_NonlinearSubdivisionLevel = bpy.props.IntProperty(name='NonlinearSubdivisionLevel', description='If the input is an unstructured grid with nonlinear faces, this parameter determines how many times the face is subdivided into linear faces. If 0, the output is the equivalent of its linear couterpart (and the midpoints determining the nonlinear interpolation are discarded). If 1 (the default), the nonlinear face is triangulated based on the midpoints. If greater than 1, the triangulated pieces are recursively subdivided to reach the desired subdivision. Setting the value to greater than 1 may cause some point data to not be passed even if no nonlinear faces exist. This option has no effect if the input is not an unstructured grid', default=1)
    m_OriginalCellIdsName = bpy.props.StringProperty(name='OriginalCellIdsName', description='If PassThroughCellIds or PassThroughPointIds is on, then these ivars control the name given to the field in which the ids are written into. If set to nullptr, then vtkOriginalCellIds or vtkOriginalPointIds (the default) is used, respectively', default='vtkOriginalCellIds')
    m_OriginalPointIdsName = bpy.props.StringProperty(name='OriginalPointIdsName', description='If PassThroughCellIds or PassThroughPointIds is on, then these ivars control the name given to the field in which the ids are written into. If set to nullptr, then vtkOriginalCellIds or vtkOriginalPointIds (the default) is used, respectively', default='vtkOriginalPointIds')
    m_PassThroughCellIds = bpy.props.BoolProperty(name='PassThroughCellIds', description='If on, the output polygonal dataset will have a celldata array that holds the cell index of the original 3D cell that produced each output cell. This is useful for cell picking. The default is off to conserve memory. Note that PassThroughCellIds will be ignored if UseStrips is on, since in that case each tringle strip can represent more than on of the input cells', default=True)
    m_PassThroughPointIds = bpy.props.BoolProperty(name='PassThroughPointIds', description='If on, the output polygonal dataset will have a celldata array that holds the cell index of the original 3D cell that produced each output cell. This is useful for cell picking. The default is off to conserve memory. Note that PassThroughCellIds will be ignored if UseStrips is on, since in that case each tringle strip can represent more than on of the input cells', default=True)
    m_PieceInvariant = bpy.props.IntProperty(name='PieceInvariant', description='If PieceInvariant is true, vtkDataSetSurfaceFilter requests 1 ghost level from input in order to remove internal surface that are between processes. False by default', default=0)
    m_UseStrips = bpy.props.BoolProperty(name='UseStrips', description='When input is structured data, this flag will generate faces with triangle strips. This should render faster and use less memory, but no cell data is copied. By default, UseStrips is Off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NonlinearSubdivisionLevel', 'm_OriginalCellIdsName', 'm_OriginalPointIdsName', 'm_PassThroughCellIds', 'm_PassThroughPointIds', 'm_PieceInvariant', 'm_UseStrips', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Renderer'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AdaptiveDataSetSurfaceFilter)
TYPENAMES.append('BVTK_NT_AdaptiveDataSetSurfaceFilter' )


# --------------------------------------------------------------


class BVTK_NT_CompositeCutter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CompositeCutter'
    bl_label = 'vtkCompositeCutter'
    e_SortBy_items = [(x, x, x) for x in ['SortByCell', 'SortByValue']]
    
    m_GenerateCutScalars = bpy.props.BoolProperty(name='GenerateCutScalars', description='If this flag is enabled, then the output scalar values will be interpolated from the implicit function values, and not the input scalar data', default=True)
    m_GenerateTriangles = bpy.props.BoolProperty(name='GenerateTriangles', description='If this is enabled (by default), the output will be triangles otherwise, the output will be the intersection polygons WARNING: if the cutting function is not a plane, the output will be 3D poygons, which might be nice to look at but hard to compute with downstream', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Set the number of contours to place into the list. You only really need to use this method to reduce list size. The method SetValue() will automatically increase list size as needed', default=1)
    e_SortBy = bpy.props.EnumProperty(name='SortBy', description='Set the sorting order for the generated polydata. There are two possibilities: Sort by value = 0 - This is the most efficient sort. For each cell, all contour values are processed. This is the default. Sort by cell = 1 - For each contour value, all cells are processed. This order should be used if the extracted polygons must be rendered in a back-to-front or front-to-back order. This is very problem dependent. For most applications, the default order is fine (and faster)', default='SortByValue', items=e_SortBy_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateCutScalars', 'm_GenerateTriangles', 'm_NumberOfContours', 'e_SortBy', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['CutFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CompositeCutter)
TYPENAMES.append('BVTK_NT_CompositeCutter' )


# --------------------------------------------------------------


class BVTK_NT_TriangularTCoords(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TriangularTCoords'
    bl_label = 'vtkTriangularTCoords'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TriangularTCoords)
TYPENAMES.append('BVTK_NT_TriangularTCoords' )


# --------------------------------------------------------------


class BVTK_NT_GradientFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GradientFilter'
    bl_label = 'vtkGradientFilter'
    
    m_ComputeDivergence = bpy.props.BoolProperty(name='ComputeDivergence', description='Add divergence to the output field data. The name of the array will be DivergenceArrayName and will be the same type as the input array. The input array must have 3 components in order to compute this. The default is off', default=True)
    m_ComputeGradient = bpy.props.BoolProperty(name='ComputeGradient', description='Add the gradient to the output field data. The name of the array will be ResultArrayName and will be the same type as the input array. The default is on', default=True)
    m_ComputeQCriterion = bpy.props.BoolProperty(name='ComputeQCriterion', description='Add Q-criterion to the output field data. The name of the array will be QCriterionArrayName and will be the same type as the input array. The input array must have 3 components in order to compute this. Note that Q-citerion is a balance of the rate of vorticity and the rate of strain. The default is off', default=True)
    m_ComputeVorticity = bpy.props.BoolProperty(name='ComputeVorticity', description='Add voriticity/curl to the output field data. The name of the array will be VorticityArrayName and will be the same type as the input array. The input array must have 3 components in order to compute this. The default is off', default=True)
    m_ContributingCellOption = bpy.props.IntProperty(name='ContributingCellOption', description='Option to specify what cells to include in the gradient computation. Options are all cells (All, Patch and DataSetMax). The default is All', default=0)
    m_DivergenceArrayName = bpy.props.StringProperty(name='DivergenceArrayName', description='Get/Set the name of the divergence array to create. This is only used if ComputeDivergence is non-zero. If nullptr (the default) then the output array will be named "Divergence"')
    m_FasterApproximation = bpy.props.BoolProperty(name='FasterApproximation', description='When this flag is on (default is off), the gradient filter will provide a less accurate (but close) algorithm that performs fewer derivative calculations (and is therefore faster). The error contains some smoothing of the output data and some possible errors on the boundary. This parameter has no effect when performing the gradient of cell data. This only applies if the input grid is a vtkUnstructuredGrid or a vtkPolyData', default=True)
    m_QCriterionArrayName = bpy.props.StringProperty(name='QCriterionArrayName', description='Get/Set the name of the Q criterion array to create. This is only used if ComputeQCriterion is non-zero. If nullptr (the default) then the output array will be named "Q-criterion"')
    m_ReplacementValueOption = bpy.props.IntProperty(name='ReplacementValueOption', description="Option to specify what replacement value or entities that don't have any gradient computed over them based on the ContributingCellOption. Options are (Zero, NaN, DataTypeMin, DataTypeMax). The default is Zero", default=0)
    m_ResultArrayName = bpy.props.StringProperty(name='ResultArrayName', description='Get/Set the name of the gradient array to create. This is only used if ComputeGradient is non-zero. If nullptr (the default) then the output array will be named "Gradients"')
    m_VorticityArrayName = bpy.props.StringProperty(name='VorticityArrayName', description='Get/Set the name of the vorticity array to create. This is only used if ComputeVorticity is non-zero. If nullptr (the default) then the output array will be named "Vorticity"')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeDivergence', 'm_ComputeGradient', 'm_ComputeQCriterion', 'm_ComputeVorticity', 'm_ContributingCellOption', 'm_DivergenceArrayName', 'm_FasterApproximation', 'm_QCriterionArrayName', 'm_ReplacementValueOption', 'm_ResultArrayName', 'm_VorticityArrayName', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GradientFilter)
TYPENAMES.append('BVTK_NT_GradientFilter' )


# --------------------------------------------------------------


class BVTK_NT_AMRSliceFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AMRSliceFilter'
    bl_label = 'vtkAMRSliceFilter'
    
    m_EnablePrefetching = bpy.props.BoolProperty(name='EnablePrefetching', description='Set/Get EnablePrefetching propert', default=True)
    m_ForwardUpstream = bpy.props.BoolProperty(name='ForwardUpstream', description='Set/Get ForwardUpstream propert', default=True)
    m_MaxResolution = bpy.props.IntProperty(name='MaxResolution', description='Set/Get the maximum resolution used in this instance', default=1)
    m_Normal = bpy.props.IntProperty(name='Normal', description='Set/Get the Axis normal. There are only 3 acceptable values 1-(X-Normal); 2-(Y-Normal); 3-(Z-Normal', default=1)
    m_OffSetFromOrigin = bpy.props.FloatProperty(name='OffSetFromOrigin', description='', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_EnablePrefetching', 'm_ForwardUpstream', 'm_MaxResolution', 'm_Normal', 'm_OffSetFromOrigin', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AMRSliceFilter)
TYPENAMES.append('BVTK_NT_AMRSliceFilter' )


# --------------------------------------------------------------


class BVTK_NT_DiscreteMarchingCubes(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DiscreteMarchingCubes'
    bl_label = 'vtkDiscreteMarchingCubes'
    
    m_ComputeAdjacentScalars = bpy.props.BoolProperty(name='ComputeAdjacentScalars', description='Set/Get the computation of neighbouring voxel values', default=True)
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeAdjacentScalars', 'm_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DiscreteMarchingCubes)
TYPENAMES.append('BVTK_NT_DiscreteMarchingCubes' )


# --------------------------------------------------------------


class BVTK_NT_StructuredGridPartitioner(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StructuredGridPartitioner'
    bl_label = 'vtkStructuredGridPartitioner'
    
    m_DuplicateNodes = bpy.props.BoolProperty(name='DuplicateNodes', description='Set/Get & boolean macro for the DuplicateNodes property', default=True)
    m_NumberOfGhostLayers = bpy.props.IntProperty(name='NumberOfGhostLayers', description='Set/Get macro for the number of ghost layers', default=0)
    m_NumberOfPartitions = bpy.props.IntProperty(name='NumberOfPartitions', description='Set/Get macro for the number of subdivisions', default=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DuplicateNodes', 'm_NumberOfGhostLayers', 'm_NumberOfPartitions', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StructuredGridPartitioner)
TYPENAMES.append('BVTK_NT_StructuredGridPartitioner' )


# --------------------------------------------------------------


class BVTK_NT_LinearToQuadraticCellsFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LinearToQuadraticCellsFilter'
    bl_label = 'vtkLinearToQuadraticCellsFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LinearToQuadraticCellsFilter)
TYPENAMES.append('BVTK_NT_LinearToQuadraticCellsFilter' )


# --------------------------------------------------------------


class BVTK_NT_SimpleBondPerceiver(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SimpleBondPerceiver'
    bl_label = 'vtkSimpleBondPerceiver'
    
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Set/Get the tolerance used in the comparisons. (Default: 0.45', default=0.44999998807907104)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Tolerance', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SimpleBondPerceiver)
TYPENAMES.append('BVTK_NT_SimpleBondPerceiver' )


# --------------------------------------------------------------


class BVTK_NT_ImageMagnitude(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMagnitude'
    bl_label = 'vtkImageMagnitude'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMagnitude)
TYPENAMES.append('BVTK_NT_ImageMagnitude' )


# --------------------------------------------------------------


class BVTK_NT_ImageMarchingCubes(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMarchingCubes'
    bl_label = 'vtkImageMarchingCubes'
    
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_InputMemoryLimit = bpy.props.IntProperty(name='InputMemoryLimit', description='The InputMemoryLimit determines the chunk size (the number of slices requested at each iteration). The units of this limit is KiloBytes. For now, only the Z axis is split', default=10240)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Methods to set contour value', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_InputMemoryLimit', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMarchingCubes)
TYPENAMES.append('BVTK_NT_ImageMarchingCubes' )


# --------------------------------------------------------------


class BVTK_NT_PYoungsMaterialInterface(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PYoungsMaterialInterface'
    bl_label = 'vtkPYoungsMaterialInterface'
    
    m_AxisSymetric = bpy.props.BoolProperty(name='AxisSymetric', description='Turns on/off AxisSymetric computation of 2D interfaces. in axis symetric mode, 2D meshes are understood as volumes of revolution', default=True)
    m_FillMaterial = bpy.props.BoolProperty(name='FillMaterial', description='When FillMaterial is set to 1, the volume containing material is output and not only the interface surface', default=True)
    m_InverseNormal = bpy.props.BoolProperty(name='InverseNormal', description='Set/Get whether the normal vector has to be flipped', default=True)
    m_NumberOfMaterials = bpy.props.IntProperty(name='NumberOfMaterials', description='Sets/Gets the number of materials', default=0)
    m_OnionPeel = bpy.props.BoolProperty(name='OnionPeel', description='Set/Get OnionPeel flag. if this flag is on, the normal vector of the first material (which depends on material ordering) is used for all materials', default=True)
    m_ReverseMaterialOrder = bpy.props.BoolProperty(name='ReverseMaterialOrder', description='If this flag is on, material order in reversed. Otherwise, materials are sorted in ascending order depending on the given ordering array', default=True)
    m_UseAllBlocks = bpy.props.BoolProperty(name='UseAllBlocks', description='Set/Get whether all material blocks should be used, irrespective of the material block mapping', default=True)
    m_UseFractionAsDistance = bpy.props.BoolProperty(name='UseFractionAsDistance', description='when UseFractionAsDistance is true, the volume fraction is interpreted as the distance of the cutting plane from the origin. in axis symetric mode, 2D meshes are understood as volumes of revolution', default=True)
    m_VolumeFractionRange = bpy.props.FloatVectorProperty(name='VolumeFractionRange', description='Set/Get minimum and maximum volume fraction value. if a material fills a volume above the minimum value, the material is considered to be void. if a material fills a volume fraction beyond the maximum value it is considered as filling the whole volum', default=[0.01, 0.99], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AxisSymetric', 'm_FillMaterial', 'm_InverseNormal', 'm_NumberOfMaterials', 'm_OnionPeel', 'm_ReverseMaterialOrder', 'm_UseAllBlocks', 'm_UseFractionAsDistance', 'm_VolumeFractionRange', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PYoungsMaterialInterface)
TYPENAMES.append('BVTK_NT_PYoungsMaterialInterface' )


# --------------------------------------------------------------


class BVTK_NT_ExtractTemporalFieldData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractTemporalFieldData'
    bl_label = 'vtkExtractTemporalFieldData'
    
    m_HandleCompositeDataBlocksIndividually = bpy.props.BoolProperty(name='HandleCompositeDataBlocksIndividually', description='When set to true (default), if the input is a vtkCompositeDataSet, then each block in the input dataset in processed separately. If false, then the first non-empty FieldData is considered', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_HandleCompositeDataBlocksIndividually', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractTemporalFieldData)
TYPENAMES.append('BVTK_NT_ExtractTemporalFieldData' )


# --------------------------------------------------------------


class BVTK_NT_CountFaces(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CountFaces'
    bl_label = 'vtkCountFaces'
    
    m_OutputArrayName = bpy.props.StringProperty(name='OutputArrayName', description='The name of the new output array containing the face counts', default='Face Count')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_OutputArrayName', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CountFaces)
TYPENAMES.append('BVTK_NT_CountFaces' )


# --------------------------------------------------------------


class BVTK_NT_ImageStencilToImage(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageStencilToImage'
    bl_label = 'vtkImageStencilToImage'
    e_OutputScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Long', 'Short', 'UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    
    m_InsideValue = bpy.props.FloatProperty(name='InsideValue', description='The value to use inside the stencil. The default is 1', default=1.0)
    e_OutputScalarType = bpy.props.EnumProperty(name='OutputScalarType', description='The desired output scalar type. The default is unsigned char', default='UnsignedChar', items=e_OutputScalarType_items)
    m_OutsideValue = bpy.props.FloatProperty(name='OutsideValue', description='The value to use outside the stencil. The default is 0', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_InsideValue', 'e_OutputScalarType', 'm_OutsideValue', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageStencilToImage)
TYPENAMES.append('BVTK_NT_ImageStencilToImage' )


# --------------------------------------------------------------


class BVTK_NT_SynchronizedTemplates2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SynchronizedTemplates2D'
    bl_label = 'vtkSynchronizedTemplates2D'
    
    m_ArrayComponent = bpy.props.IntProperty(name='ArrayComponent', description='Set/get which component of the scalar array to contour on; defaults to 0', default=0)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Option to set the point scalars of the output. The scalars will be the iso value of course. By default this flag is on', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Set the number of contours to place into the list. You only really need to use this method to reduce list size. The method SetValue() will automatically increase list size as needed', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayComponent', 'm_ComputeScalars', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SynchronizedTemplates2D)
TYPENAMES.append('BVTK_NT_SynchronizedTemplates2D' )


# --------------------------------------------------------------


class BVTK_NT_RectilinearGridAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RectilinearGridAlgorithm'
    bl_label = 'vtkRectilinearGridAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RectilinearGridAlgorithm)
TYPENAMES.append('BVTK_NT_RectilinearGridAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_ImageWeightedSum(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageWeightedSum'
    bl_label = 'vtkImageWeightedSum'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NormalizeByWeight = bpy.props.BoolProperty(name='NormalizeByWeight', description='Setting NormalizeByWeight on will divide the final result by the total weight of the component functions. This process does not otherwise normalize the weighted sum By default, NormalizeByWeight is on', default=True)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NormalizeByWeight', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Weights'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageWeightedSum)
TYPENAMES.append('BVTK_NT_ImageWeightedSum' )


# --------------------------------------------------------------


class BVTK_NT_RectilinearGridToTetrahedra(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RectilinearGridToTetrahedra'
    bl_label = 'vtkRectilinearGridToTetrahedra'
    e_TetraPerCell_items = [(x, x, x) for x in ['12', '5', '5And12', '6']]
    
    m_RememberVoxelId = bpy.props.BoolProperty(name='RememberVoxelId', description='Should the tetrahedra have scalar data indicating which Voxel they came from in the vtkRectilinearGrid', default=True)
    e_TetraPerCell = bpy.props.EnumProperty(name='TetraPerCell', description='Set the method to divide each cell (voxel) in the RectilinearGrid into tetrahedra', default='5', items=e_TetraPerCell_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_RememberVoxelId', 'e_TetraPerCell', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RectilinearGridToTetrahedra)
TYPENAMES.append('BVTK_NT_RectilinearGridToTetrahedra' )


# --------------------------------------------------------------


class BVTK_NT_PointSetAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PointSetAlgorithm'
    bl_label = 'vtkPointSetAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PointSetAlgorithm)
TYPENAMES.append('BVTK_NT_PointSetAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_ThresholdPoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ThresholdPoints'
    bl_label = 'vtkThresholdPoints'
    
    m_LowerThreshold = bpy.props.FloatProperty(name='LowerThreshold', description='Set/Get the lower threshold', default=0.0)
    m_UpperThreshold = bpy.props.FloatProperty(name='UpperThreshold', description='Set/Get the upper threshold', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_LowerThreshold', 'm_UpperThreshold', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ThresholdPoints)
TYPENAMES.append('BVTK_NT_ThresholdPoints' )


# --------------------------------------------------------------


class BVTK_NT_POutlineFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_POutlineFilter'
    bl_label = 'vtkPOutlineFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_POutlineFilter)
TYPENAMES.append('BVTK_NT_POutlineFilter' )


# --------------------------------------------------------------


class BVTK_NT_Cutter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Cutter'
    bl_label = 'vtkCutter'
    e_SortBy_items = [(x, x, x) for x in ['SortByCell', 'SortByValue']]
    
    m_GenerateCutScalars = bpy.props.BoolProperty(name='GenerateCutScalars', description='If this flag is enabled, then the output scalar values will be interpolated from the implicit function values, and not the input scalar data', default=True)
    m_GenerateTriangles = bpy.props.BoolProperty(name='GenerateTriangles', description='If this is enabled (by default), the output will be triangles otherwise, the output will be the intersection polygons WARNING: if the cutting function is not a plane, the output will be 3D poygons, which might be nice to look at but hard to compute with downstream', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Set the number of contours to place into the list. You only really need to use this method to reduce list size. The method SetValue() will automatically increase list size as needed', default=1)
    e_SortBy = bpy.props.EnumProperty(name='SortBy', description='Set the sorting order for the generated polydata. There are two possibilities: Sort by value = 0 - This is the most efficient sort. For each cell, all contour values are processed. This is the default. Sort by cell = 1 - For each contour value, all cells are processed. This order should be used if the extracted polygons must be rendered in a back-to-front or front-to-back order. This is very problem dependent. For most applications, the default order is fine (and faster)', default='SortByValue', items=e_SortBy_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateCutScalars', 'm_GenerateTriangles', 'm_NumberOfContours', 'e_SortBy', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['CutFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Cutter)
TYPENAMES.append('BVTK_NT_Cutter' )


# --------------------------------------------------------------


class BVTK_NT_DataSetGradientPrecompute(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataSetGradientPrecompute'
    bl_label = 'vtkDataSetGradientPrecompute'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataSetGradientPrecompute)
TYPENAMES.append('BVTK_NT_DataSetGradientPrecompute' )


# --------------------------------------------------------------


class BVTK_NT_ImplicitModeller(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImplicitModeller'
    bl_label = 'vtkImplicitModeller'
    e_OutputScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Long', 'Short', 'UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    e_ProcessMode_items = [(x, x, x) for x in ['PerCell', 'PerVoxel']]
    
    m_AdjustBounds = bpy.props.BoolProperty(name='AdjustBounds', description='Control how the model bounds are computed. If the ivar AdjustBounds is set, then the bounds specified (or computed automatically) is modified by the fraction given by AdjustDistance. This means that the model bounds is expanded in each of the x-y-z directions', default=True)
    m_AdjustDistance = bpy.props.FloatProperty(name='AdjustDistance', description='Specify the amount to grow the model bounds (if the ivar AdjustBounds is set). The value is a fraction of the maximum length of the sides of the box specified by the model bounds', default=0.0125)
    m_CapValue = bpy.props.FloatProperty(name='CapValue', description='Specify the capping value to use. The CapValue is also used as an initial distance value at each point in the dataset', default=1e+30)
    m_Capping = bpy.props.BoolProperty(name='Capping', description='The outer boundary of the structured point set can be assigned a particular value. This can be used to close or "cap" all surfaces', default=True)
    m_LocatorMaxLevel = bpy.props.IntProperty(name='LocatorMaxLevel', description='Specify the level of the locator to use when using the per voxel process mode', default=5)
    m_MaximumDistance = bpy.props.FloatProperty(name='MaximumDistance', description='Set / get the distance away from surface of input geometry to sample. This value is specified as a percentage of the length of the diagonal of the input data bounding box. Smaller values make large increases in performance', default=0.1)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Set / get the region in space in which to perform the sampling. If not specified, it will be computed automatically', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Set / Get the number of threads used during Per-Voxel processing mod', default=4)
    e_OutputScalarType = bpy.props.EnumProperty(name='OutputScalarType', description='Set the desired output scalar type', default='Float', items=e_OutputScalarType_items)
    e_ProcessMode = bpy.props.EnumProperty(name='ProcessMode', description='Specify whether to visit each cell once per append or each voxel once per append. Some tests have shown once per voxel to be faster when there are a lot of cells (at least a thousand?); relative performance improvement increases with addition cells. Primitives should not be stripped for best performance of the voxel mode', default='PerCell', items=e_ProcessMode_items)
    m_ScaleToMaximumDistance = bpy.props.BoolProperty(name='ScaleToMaximumDistance', description='If a non-floating output type is specified, the output distances can be scaled to use the entire positive scalar range of the output type specified (up to the CapValue which is equal to the max for the type unless modified by the user). For example, if ScaleToMaximumDistance is On and the OutputScalarType is UnsignedChar the distances saved in the output would be linearly scaled between 0 (for distances "very close" to the surface) and 255 (at the specifed maximum distance)... assuming the CapValue is not changed from 255', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AdjustBounds', 'm_AdjustDistance', 'm_CapValue', 'm_Capping', 'm_LocatorMaxLevel', 'm_MaximumDistance', 'm_ModelBounds', 'm_NumberOfThreads', 'e_OutputScalarType', 'e_ProcessMode', 'm_ScaleToMaximumDistance', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImplicitModeller)
TYPENAMES.append('BVTK_NT_ImplicitModeller' )


# --------------------------------------------------------------


class BVTK_NT_UnstructuredGridBaseAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_UnstructuredGridBaseAlgorithm'
    bl_label = 'vtkUnstructuredGridBaseAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_UnstructuredGridBaseAlgorithm)
TYPENAMES.append('BVTK_NT_UnstructuredGridBaseAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_CompositeDataSetAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CompositeDataSetAlgorithm'
    bl_label = 'vtkCompositeDataSetAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CompositeDataSetAlgorithm)
TYPENAMES.append('BVTK_NT_CompositeDataSetAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_SplitField(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SplitField'
    bl_label = 'vtkSplitField'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SplitField)
TYPENAMES.append('BVTK_NT_SplitField' )


# --------------------------------------------------------------


class BVTK_NT_GenericDataSetTessellator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GenericDataSetTessellator'
    bl_label = 'vtkGenericDataSetTessellator'
    
    m_KeepCellIds = bpy.props.BoolProperty(name='KeepCellIds', description='Turn on/off generation of a cell centered attribute with ids of the original cells (as an input cell is tessellated into several linear cells). The name of the data array is "OriginalIds". It is true by default', default=True)
    m_Merging = bpy.props.BoolProperty(name='Merging', description='Turn on/off merging of coincident points. Note that is merging is on, points with different point attributes (e.g., normals) are merged, which may cause rendering artifacts', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_KeepCellIds', 'm_Merging', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GenericDataSetTessellator)
TYPENAMES.append('BVTK_NT_GenericDataSetTessellator' )


# --------------------------------------------------------------


class BVTK_NT_PointSetToLabelHierarchy(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PointSetToLabelHierarchy'
    bl_label = 'vtkPointSetToLabelHierarchy'
    
    m_BoundedSizeArrayName = bpy.props.StringProperty(name='BoundedSizeArrayName', description='Set/get the maximum text width (in world coordinates) array name', default='BoundedSize')
    m_IconIndexArrayName = bpy.props.StringProperty(name='IconIndexArrayName', description='Set/get the icon index array name', default='IconIndex')
    m_LabelArrayName = bpy.props.StringProperty(name='LabelArrayName', description='Set/get the label array name', default='LabelText')
    m_MaximumDepth = bpy.props.IntProperty(name='MaximumDepth', description='Set/get the maximum tree depth in the output hierarchy', default=5)
    m_OrientationArrayName = bpy.props.StringProperty(name='OrientationArrayName', description='Set/get the text orientation array name', default='Orientation')
    m_PriorityArrayName = bpy.props.StringProperty(name='PriorityArrayName', description='Set/get the priority array name', default='Priority')
    m_SizeArrayName = bpy.props.StringProperty(name='SizeArrayName', description='Set/get the priority array name', default='LabelSize')
    m_TargetLabelCount = bpy.props.IntProperty(name='TargetLabelCount', description='Set/get the "ideal" number of labels to associate with each node in the output hierarchy', default=32)
    m_UseUnicodeStrings = bpy.props.BoolProperty(name='UseUnicodeStrings', description='Whether to use unicode strings', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BoundedSizeArrayName', 'm_IconIndexArrayName', 'm_LabelArrayName', 'm_MaximumDepth', 'm_OrientationArrayName', 'm_PriorityArrayName', 'm_SizeArrayName', 'm_TargetLabelCount', 'm_UseUnicodeStrings', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['TextProperty'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PointSetToLabelHierarchy)
TYPENAMES.append('BVTK_NT_PointSetToLabelHierarchy' )


# --------------------------------------------------------------


class BVTK_NT_ClipClosedSurface(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ClipClosedSurface'
    bl_label = 'vtkClipClosedSurface'
    e_ScalarMode_items = [(x, x, x) for x in ['Colors', 'Labels', 'None']]
    
    m_ActivePlaneColor = bpy.props.FloatVectorProperty(name='ActivePlaneColor', description='', default=[1.0, 1.0, 0.0], size=3)
    m_ActivePlaneId = bpy.props.IntProperty(name='ActivePlaneId', description='Set the active plane, so that the clipping from that plane can be displayed in a different color. Set this to -1 if there is no active plane. The default value is -1', default=-1)
    m_BaseColor = bpy.props.FloatVectorProperty(name='BaseColor', description='', default=[1.0, 0.0, 0.0], size=3)
    m_ClipColor = bpy.props.FloatVectorProperty(name='ClipColor', description='', default=[1.0, 0.5, 0.0], size=3)
    m_GenerateFaces = bpy.props.BoolProperty(name='GenerateFaces', description='Set whether to generate polygonal faces for the output. This is on by default. If it is off, then the output will have no polys', default=True)
    m_GenerateOutline = bpy.props.BoolProperty(name='GenerateOutline', description='Set whether to generate an outline wherever an input face was cut by a plane. This is off by default', default=True)
    m_PassPointData = bpy.props.BoolProperty(name='PassPointData', description='Pass the point data to the output. Point data will be interpolated when new points are generated. This is off by default', default=True)
    e_ScalarMode = bpy.props.EnumProperty(name='ScalarMode', description='Set whether to add cell scalars, so that new faces and outlines can be distinguished from original faces and lines. The options are "None", "Colors", and "Labels". For the "Labels" option, a scalar value of "0" indicates an original cell, "1" indicates a new cell on a cut face, and "2" indicates a new cell on the ActivePlane as set by the SetActivePlane() method. The default scalar mode is "None"', default='None', items=e_ScalarMode_items)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Set the tolerance for creating new points while clipping. If the tolerance is too small, then degenerate triangles might be produced. The default tolerance is 1e-6', default=1e-06)
    m_TriangulationErrorDisplay = bpy.props.BoolProperty(name='TriangulationErrorDisplay', description='Generate errors when the triangulation fails. Usually the triangulation errors are too small to see, but they result in a surface that is not watertight. This option has no impact on performance', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ActivePlaneColor', 'm_ActivePlaneId', 'm_BaseColor', 'm_ClipColor', 'm_GenerateFaces', 'm_GenerateOutline', 'm_PassPointData', 'e_ScalarMode', 'm_Tolerance', 'm_TriangulationErrorDisplay', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['ClippingPlanes'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ClipClosedSurface)
TYPENAMES.append('BVTK_NT_ClipClosedSurface' )


# --------------------------------------------------------------


class BVTK_NT_BrownianPoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BrownianPoints'
    bl_label = 'vtkBrownianPoints'
    
    m_MaximumSpeed = bpy.props.FloatProperty(name='MaximumSpeed', description='Set the maximum speed value', default=1.0)
    m_MinimumSpeed = bpy.props.FloatProperty(name='MinimumSpeed', description='Set the minimum speed value', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MaximumSpeed', 'm_MinimumSpeed', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BrownianPoints)
TYPENAMES.append('BVTK_NT_BrownianPoints' )


# --------------------------------------------------------------


class BVTK_NT_ShepardMethod(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ShepardMethod'
    bl_label = 'vtkShepardMethod'
    
    m_MaximumDistance = bpy.props.FloatProperty(name='MaximumDistance', description='Specify the maximum influence distance of each input point. This distance is a fraction of the length of the diagonal of the sample space. Thus, values of 1.0 will cause each input point to influence all points in the volume dataset. Values less than 1.0 can improve performance significantly. By default the maximum distance is 0.25', default=0.25)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Specify the position in space to perform the sampling. The ModelBounds and SampleDimensions together define the output volume. (Note: if the ModelBounds are set to an invalid state [zero or negative volume] then the bounds are computed automatically.', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6)
    m_NullValue = bpy.props.FloatProperty(name='NullValue', description='Set the value for output points not receiving a contribution from any input point(s). Output points may not receive a contribution when the MaximumDistance < 1', default=0.0)
    m_PowerParameter = bpy.props.FloatProperty(name='PowerParameter', description='Set / Get the power parameter p. By default p=2. Values (which must be a positive, real value) != 2 may affect performance significantly', default=2.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MaximumDistance', 'm_ModelBounds', 'm_NullValue', 'm_PowerParameter', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ShepardMethod)
TYPENAMES.append('BVTK_NT_ShepardMethod' )


# --------------------------------------------------------------


class BVTK_NT_CheckerboardSplatter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CheckerboardSplatter'
    bl_label = 'vtkCheckerboardSplatter'
    e_AccumulationMode_items = [(x, x, x) for x in ['Max', 'Min', 'Sum']]
    e_OutputScalarType_items = [(x, x, x) for x in ['Double', 'Float']]
    
    e_AccumulationMode = bpy.props.EnumProperty(name='AccumulationMode', description='Specify the scalar accumulation mode. This mode expresses how scalar values are combined when splats overlap one another. The Max mode acts like a set union operation and is the most commonly used; the Min mode acts like a set intersection, and the sum is just weird (and can potentially cause accumulation overflow in extreme cases). Note that the NullValue must be set consistent with the accumulation operation', default='Max', items=e_AccumulationMode_items)
    m_CapValue = bpy.props.FloatProperty(name='CapValue', description='Specify the cap value to use. (This instance variable only has effect if the ivar Capping is on.', default=0.0)
    m_Capping = bpy.props.BoolProperty(name='Capping', description='Turn on/off the capping of the outer boundary of the volume to a specified cap value. This can be used to close surfaces (after iso-surfacing) and create other effects', default=True)
    m_Eccentricity = bpy.props.FloatProperty(name='Eccentricity', description='Control the shape of elliptical splatting. Eccentricity is the ratio of the major axis (aligned along normal) to the minor (axes) aligned along other two axes. So Eccentricity > 1 creates needles with the long axis in the direction of the normal; Eccentricity<1 creates pancakes perpendicular to the normal vector', default=2.5)
    m_ExponentFactor = bpy.props.FloatProperty(name='ExponentFactor', description='Set / get the sharpness of decay of the splats. This is the exponent constant in the Gaussian equation described above. Normally this is a negative value', default=-5.0)
    m_Footprint = bpy.props.IntProperty(name='Footprint', description='Control the footprint size of the splat in terms of propagation across a voxel neighborhood. The Footprint value simply indicates the number of neigboring voxels in the i-j-k directions to extend the splat. A value of zero means that only the voxel containing the splat point is affected. A value of one means the immediate neighbors touching the affected voxel are affected as well. Larger numbers increase the splat footprint and significantly increase processing time. Note that the footprint is always 3D rectangular', default=2)
    m_MaximumDimension = bpy.props.IntProperty(name='MaximumDimension', description='Set/Get the maximum dimension of the checkerboard (i.e., the number of squares in any of the i, j, or k directions). This number also impacts the granularity of the parallel threading (since each checker square is processed separaely). Because of the internal addressing, the maximum dimension is limited to 255 (maximum value of an unsigned char)', default=50)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Set / get the (xmin,xmax, ymin,ymax, zmin,zmax) bounding box in which the sampling is performed. If any of the (min,max) bounds values are min >= max, then the bounds will be computed automatically from the input data. Otherwise, the user-specified bounds will be used', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6)
    m_NormalWarping = bpy.props.BoolProperty(name='NormalWarping', description='Turn on/off the generation of elliptical splats. If normal warping is on, then the input normals affect the distribution of the splat. This boolean is used in combination with the Eccentricity ivar', default=True)
    m_NullValue = bpy.props.FloatProperty(name='NullValue', description='Set the Null value for output points not receiving a contribution from the input points. (This is the initial value of the voxel samples, by default it is set to zero.) Note that the value should be consistent with the output dataset type. The NullValue also provides the initial value on which the accumulations process operates', default=0.0)
    e_OutputScalarType = bpy.props.EnumProperty(name='OutputScalarType', description='Set what type of scalar data this source should generate. Only double and float types are supported currently due to precision requirements during accumulation. By default, float scalars are produced', default='Float', items=e_OutputScalarType_items)
    m_ParallelSplatCrossover = bpy.props.IntProperty(name='ParallelSplatCrossover', description='Set/get the crossover point expressed in footprint size where the splatting operation is parallelized (through vtkSMPTools). By default the parallel crossover point is for splat footprints of size two or greater (i.e., at footprint=2 then splat is 5x5x5 and parallel splatting occurs). This is really meant for experimental purposes', default=2)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set / get the radius variable that controls the Gaussian exponential function (see equation above). If set to zero, it is automatically set to the radius of the circumsphere bounding a single voxel. (By default, the Radius is set to zero and is automatically computed.', default=0.0)
    m_ScalarWarping = bpy.props.BoolProperty(name='ScalarWarping', description='Turn on/off the scaling of splats by scalar value', default=True)
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Multiply Gaussian splat distribution by this value. If ScalarWarping is on, then the Scalar value will be multiplied by the ScaleFactor times the Gaussian function', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_AccumulationMode', 'm_CapValue', 'm_Capping', 'm_Eccentricity', 'm_ExponentFactor', 'm_Footprint', 'm_MaximumDimension', 'm_ModelBounds', 'm_NormalWarping', 'm_NullValue', 'e_OutputScalarType', 'm_ParallelSplatCrossover', 'm_Radius', 'm_ScalarWarping', 'm_ScaleFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CheckerboardSplatter)
TYPENAMES.append('BVTK_NT_CheckerboardSplatter' )


# --------------------------------------------------------------


class BVTK_NT_CutMaterial(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CutMaterial'
    bl_label = 'vtkCutMaterial'
    
    m_ArrayName = bpy.props.StringProperty(name='ArrayName', description='For now, we just use the cell values. The array name to cut')
    m_Material = bpy.props.IntProperty(name='Material', description='Material to probe', default=0)
    m_MaterialArrayName = bpy.props.StringProperty(name='MaterialArrayName', description='Cell array that contains the material values', default='material')
    m_UpVector = bpy.props.FloatVectorProperty(name='UpVector', description='', default=[0.0, 0.0, 1.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayName', 'm_Material', 'm_MaterialArrayName', 'm_UpVector', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CutMaterial)
TYPENAMES.append('BVTK_NT_CutMaterial' )


# --------------------------------------------------------------


class BVTK_NT_MoleculeToBondStickFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MoleculeToBondStickFilter'
    bl_label = 'vtkMoleculeToBondStickFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MoleculeToBondStickFilter)
TYPENAMES.append('BVTK_NT_MoleculeToBondStickFilter' )


# --------------------------------------------------------------


class BVTK_NT_IconGlyphFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_IconGlyphFilter'
    bl_label = 'vtkIconGlyphFilter'
    e_Gravity_items = [(x, x, x) for x in ['BottomCenter', 'BottomLeft', 'BottomRight', 'CenterCenter', 'CenterLeft', 'CenterRight', 'TopCenter', 'TopLeft', 'TopRight']]
    e_IconScaling_items = [(x, x, x) for x in ['ScalingArray', 'ScalingOff']]
    
    m_DisplaySize = bpy.props.IntVectorProperty(name='DisplaySize', description='Specify the Width and Height, in pixels, of the size of the icon when it is rendered. By default, the IconSize is used to set the display size (i.e., UseIconSize is true by default). Note that assumes that IconScaling is disabled, or if enabled, the scale of a particular icon is 1', default=[25, 25], size=2)
    e_Gravity = bpy.props.EnumProperty(name='Gravity', description='Specify if the input points define the center of the icon quad or one of top right corner, top center, top left corner, center right, center, center center left, bottom right corner, bottom center or bottom left corner', default='CenterCenter', items=e_Gravity_items)
    e_IconScaling = bpy.props.EnumProperty(name='IconScaling', description='Specify how to specify individual icons. By default, icon scaling is off, but if it is on, then the filter looks for an array named "IconScale" to control individual icon size', default='ScalingOff', items=e_IconScaling_items)
    m_IconSheetSize = bpy.props.IntVectorProperty(name='IconSheetSize', description='Specify the Width and Height, in pixels, of an icon in the icon sheet', default=[1, 1], size=2)
    m_IconSize = bpy.props.IntVectorProperty(name='IconSize', description='Specify the Width and Height, in pixels, of an icon in the icon sheet', default=[1, 1], size=2)
    m_Offset = bpy.props.IntVectorProperty(name='Offset', description='Specify an offset (in pixels or display coordinates) that offsets the icons from their generating points', default=[0, 0], size=2)
    m_PassScalars = bpy.props.BoolProperty(name='PassScalars', description='Specify whether to pass the scalar icon index to the output. By default this is not passed since it can affect color during the rendering process. Note that all other point data is passed to the output regardless of the value of this flag', default=False)
    m_UseIconSize = bpy.props.BoolProperty(name='UseIconSize', description='Specify whether the Quad generated to place the icon on will be either the dimensions specified by IconSize or the DisplaySize', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DisplaySize', 'e_Gravity', 'e_IconScaling', 'm_IconSheetSize', 'm_IconSize', 'm_Offset', 'm_PassScalars', 'm_UseIconSize', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_IconGlyphFilter)
TYPENAMES.append('BVTK_NT_IconGlyphFilter' )


# --------------------------------------------------------------


class BVTK_NT_DijkstraGraphGeodesicPath(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DijkstraGraphGeodesicPath'
    bl_label = 'vtkDijkstraGraphGeodesicPath'
    
    m_EndVertex = bpy.props.IntProperty(name='EndVertex', description='The vertex at the end of the shortest pat', default=0)
    m_RepelPathFromVertices = bpy.props.BoolProperty(name='RepelPathFromVertices', description='Use the input point to repel the path by assigning high costs', default=True)
    m_StartVertex = bpy.props.IntProperty(name='StartVertex', description='The vertex at the start of the shortest pat', default=0)
    m_StopWhenEndReached = bpy.props.BoolProperty(name='StopWhenEndReached', description='Stop when the end vertex is reached or calculate shortest path to all vertice', default=True)
    m_UseScalarWeights = bpy.props.BoolProperty(name='UseScalarWeights', description='Use scalar values in the edge weight (experimental', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_EndVertex', 'm_RepelPathFromVertices', 'm_StartVertex', 'm_StopWhenEndReached', 'm_UseScalarWeights', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['RepelVertices'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DijkstraGraphGeodesicPath)
TYPENAMES.append('BVTK_NT_DijkstraGraphGeodesicPath' )


# --------------------------------------------------------------


class BVTK_NT_GeometryFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GeometryFilter'
    bl_label = 'vtkGeometryFilter'
    
    m_CellClipping = bpy.props.BoolProperty(name='CellClipping', description='Turn on/off selection of geometry by cell id', default=True)
    m_CellMaximum = bpy.props.IntProperty(name='CellMaximum', description='Specify the maximum cell id for point id selection', default=1000000000)
    m_CellMinimum = bpy.props.IntProperty(name='CellMinimum', description='Specify the minimum cell id for point id selection', default=0)
    m_ExtentClipping = bpy.props.BoolProperty(name='ExtentClipping', description='Turn on/off selection of geometry via bounding box', default=True)
    m_Merging = bpy.props.BoolProperty(name='Merging', description='Turn on/off merging of coincident points. Note that is merging is on, points with different point attributes (e.g., normals) are merged, which may cause rendering artifacts', default=True)
    m_PointClipping = bpy.props.BoolProperty(name='PointClipping', description='Turn on/off selection of geometry by point id', default=True)
    m_PointMaximum = bpy.props.IntProperty(name='PointMaximum', description='Specify the maximum point id for point id selection', default=1000000000)
    m_PointMinimum = bpy.props.IntProperty(name='PointMinimum', description='Specify the minimum point id for point id selection', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CellClipping', 'm_CellMaximum', 'm_CellMinimum', 'm_ExtentClipping', 'm_Merging', 'm_PointClipping', 'm_PointMaximum', 'm_PointMinimum', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GeometryFilter)
TYPENAMES.append('BVTK_NT_GeometryFilter' )


# --------------------------------------------------------------


class BVTK_NT_EuclideanClusterExtraction(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EuclideanClusterExtraction'
    bl_label = 'vtkEuclideanClusterExtraction'
    e_ExtractionMode_items = [(x, x, x) for x in ['AllClusters', 'ClosestPointCluster', 'LargestCluster', 'PointSeededClusters', 'SpecifiedClusters']]
    
    m_ClosestPoint = bpy.props.FloatVectorProperty(name='ClosestPoint', description='Used to specify the x-y-z point coordinates when extracting the cluster closest to a specified point', default=[0.0, 0.0, 0.0], size=3)
    m_ColorClusters = bpy.props.BoolProperty(name='ColorClusters', description='Turn on/off the coloring of connected clusters', default=False)
    e_ExtractionMode = bpy.props.EnumProperty(name='ExtractionMode', description='Control the extraction of connected surfaces', default='LargestCluster', items=e_ExtractionMode_items)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Specify the local search radius', default=2.1375398946e-314)
    m_ScalarConnectivity = bpy.props.BoolProperty(name='ScalarConnectivity', description='Turn on/off connectivity based on scalar value. If on, points are connected only if the are proximal AND the scalar value of a candidate point falls in the scalar range specified. Of course input point scalar data must be provided', default=False)
    m_ScalarRange = bpy.props.FloatVectorProperty(name='ScalarRange', description='', default=[0.0, 1.0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClosestPoint', 'm_ColorClusters', 'e_ExtractionMode', 'm_Radius', 'm_ScalarConnectivity', 'm_ScalarRange', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EuclideanClusterExtraction)
TYPENAMES.append('BVTK_NT_EuclideanClusterExtraction' )


# --------------------------------------------------------------


class BVTK_NT_TransformFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransformFilter'
    bl_label = 'vtkTransformFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Transform'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransformFilter)
TYPENAMES.append('BVTK_NT_TransformFilter' )


# --------------------------------------------------------------


class BVTK_NT_PLinearExtrusionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PLinearExtrusionFilter'
    bl_label = 'vtkPLinearExtrusionFilter'
    e_ExtrusionType_items = [(x, x, x) for x in ['NormalExtrusion', 'PointExtrusion', 'VectorExtrusion']]
    
    m_Capping = bpy.props.BoolProperty(name='Capping', description='Turn on/off the capping of the skirt', default=True)
    m_ExtrusionPoint = bpy.props.FloatVectorProperty(name='ExtrusionPoint', description='Set/Get extrusion point. Only needs to be set if PointExtrusion is turned on. This is the point towards which extrusion occurs', default=[0.0, 0.0, 0.0], size=3)
    e_ExtrusionType = bpy.props.EnumProperty(name='ExtrusionType', description='Set/Get the type of extrusion', default='NormalExtrusion', items=e_ExtrusionType_items)
    m_PieceInvariant = bpy.props.BoolProperty(name='PieceInvariant', description='', default=True)
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Set/Get extrusion scale factor', default=1.0)
    m_Vector = bpy.props.FloatVectorProperty(name='Vector', description='Set/Get extrusion vector. Only needs to be set if VectorExtrusion is turned on', default=[0.0, 0.0, 1.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Capping', 'm_ExtrusionPoint', 'e_ExtrusionType', 'm_PieceInvariant', 'm_ScaleFactor', 'm_Vector', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PLinearExtrusionFilter)
TYPENAMES.append('BVTK_NT_PLinearExtrusionFilter' )


# --------------------------------------------------------------


class BVTK_NT_PointOccupancyFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PointOccupancyFilter'
    bl_label = 'vtkPointOccupancyFilter'
    
    m_EmptyValue = bpy.props.IntProperty(name='EmptyValue', description='Set / get the values indicating whether a voxel is empty (i.e., does not contain any points) or occupied. By default, an empty voxel has a zero value; an occupied voxel has a value of one', default=0)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Set / get the (xmin,xmax, ymin,ymax, zmin,zmax) bounding box in which the sampling is performed. If any of the (min,max) bounds values are min >= max, then the bounds will be computed automatically from the input data. Otherwise, the user-specified bounds will be used', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6)
    m_OccupiedValue = bpy.props.IntProperty(name='OccupiedValue', description='Set / get the values indicating whether a voxel is empty (i.e., does not contain any points) or occupied. By default, an empty voxel has a zero value; an occupied voxel has a value of one', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_EmptyValue', 'm_ModelBounds', 'm_OccupiedValue', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PointOccupancyFilter)
TYPENAMES.append('BVTK_NT_PointOccupancyFilter' )


# --------------------------------------------------------------


class BVTK_NT_PCACurvatureEstimation(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PCACurvatureEstimation'
    bl_label = 'vtkPCACurvatureEstimation'
    
    m_SampleSize = bpy.props.IntProperty(name='SampleSize', description='For each sampled point, specify the number of the closest, surrounding points used to estimate the normal (the so called k-neighborhood). By default 25 points are used. Smaller numbers may speed performance at the cost of accuracy', default=25)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_SampleSize', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PCACurvatureEstimation)
TYPENAMES.append('BVTK_NT_PCACurvatureEstimation' )


# --------------------------------------------------------------


class BVTK_NT_VectorNorm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VectorNorm'
    bl_label = 'vtkVectorNorm'
    e_AttributeMode_items = [(x, x, x) for x in ['Default', 'UseCellData', 'UsePointData']]
    
    e_AttributeMode = bpy.props.EnumProperty(name='AttributeMode', description='Control how the filter works to generate scalar data from the input vector data. By default, (AttributeModeToDefault) the filter will generate the scalar norm for point and cell data (if vector data present in the input). Alternatively, you can explicitly set the filter to generate point data (AttributeModeToUsePointData) or cell data (AttributeModeToUseCellData)', default='Default', items=e_AttributeMode_items)
    m_Normalize = bpy.props.BoolProperty(name='Normalize', description='', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_AttributeMode', 'm_Normalize', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VectorNorm)
TYPENAMES.append('BVTK_NT_VectorNorm' )


# --------------------------------------------------------------


class BVTK_NT_DepthSortPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DepthSortPolyData'
    bl_label = 'vtkDepthSortPolyData'
    e_DepthSortMode_items = [(x, x, x) for x in ['BoundsCenter', 'FirstPoint', 'ParametricCenter']]
    e_Direction_items = [(x, x, x) for x in ['BackToFront', 'FrontToBack', 'SpecifiedVector']]
    
    e_DepthSortMode = bpy.props.EnumProperty(name='DepthSortMode', description='Specify the point to use when sorting. The fastest is to just take the first cell point. Other options are to take the bounding box center or the parametric center of the cell. By default, the first cell point is used', default='FirstPoint', items=e_DepthSortMode_items)
    e_Direction = bpy.props.EnumProperty(name='Direction', description='Specify the sort method for the polygonal primitives. By default, the poly data is sorted from back to front', default='BackToFront', items=e_Direction_items)
    m_Origin = bpy.props.FloatVectorProperty(name='Origin', description='Set/Get the sort origin. This ivar only has effect if the sort direction is set to SetDirectionToSpecifiedVector(). The sort occurs in the direction of the vector, with this point specifying the origin', default=[0.0, 0.0, 0.0], size=3)
    m_SortScalars = bpy.props.BoolProperty(name='SortScalars', description='Set/Get a flag that controls the generation of scalar values corresponding to the sort order. If enabled, the output of this filter will include scalar values that range from 0 to (ncells-1), where 0 is closest to the sort direction', default=True)
    m_Vector = bpy.props.FloatVectorProperty(name='Vector', description='Set/Get the sort direction. This ivar only has effect if the sort direction is set to SetDirectionToSpecifiedVector(). The sort occurs in the direction of the vector', default=[0.0, 0.0, 0.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DepthSortMode', 'e_Direction', 'm_Origin', 'm_SortScalars', 'm_Vector', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Prop3D'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DepthSortPolyData)
TYPENAMES.append('BVTK_NT_DepthSortPolyData' )


# --------------------------------------------------------------


class BVTK_NT_MaskPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MaskPolyData'
    bl_label = 'vtkMaskPolyData'
    
    m_Offset = bpy.props.IntProperty(name='Offset', description='Start with this entity (cell)', default=0)
    m_OnRatio = bpy.props.IntProperty(name='OnRatio', description='Turn on every nth entity (cell)', default=11)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Offset', 'm_OnRatio', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MaskPolyData)
TYPENAMES.append('BVTK_NT_MaskPolyData' )


# --------------------------------------------------------------


class BVTK_NT_ArrayDataAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ArrayDataAlgorithm'
    bl_label = 'vtkArrayDataAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ArrayDataAlgorithm)
TYPENAMES.append('BVTK_NT_ArrayDataAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_WarpVector(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_WarpVector'
    bl_label = 'vtkWarpVector'
    
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Specify value to scale displacement', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ScaleFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_WarpVector)
TYPENAMES.append('BVTK_NT_WarpVector' )


# --------------------------------------------------------------


class BVTK_NT_ImageLogarithmicScale(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageLogarithmicScale'
    bl_label = 'vtkImageLogarithmicScale'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_Constant = bpy.props.FloatProperty(name='Constant', description='Set/Get the scale factor for the logarithmic function', default=10.0)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Constant', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageLogarithmicScale)
TYPENAMES.append('BVTK_NT_ImageLogarithmicScale' )


# --------------------------------------------------------------


class BVTK_NT_CompositeDataGeometryFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CompositeDataGeometryFilter'
    bl_label = 'vtkCompositeDataGeometryFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CompositeDataGeometryFilter)
TYPENAMES.append('BVTK_NT_CompositeDataGeometryFilter' )


# --------------------------------------------------------------


class BVTK_NT_PResampleFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PResampleFilter'
    bl_label = 'vtkPResampleFilter'
    
    m_CustomSamplingBounds = bpy.props.FloatVectorProperty(name='CustomSamplingBounds', description='', default=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0], size=6)
    m_SamplingDimension = bpy.props.IntVectorProperty(name='SamplingDimension', description='', default=[10, 10, 10], size=3)
    m_UseInputBounds = bpy.props.BoolProperty(name='UseInputBounds', description='Set/Get if the filter should use Input bounds to sub-sample the data. By default it is set to 1', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CustomSamplingBounds', 'm_SamplingDimension', 'm_UseInputBounds', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PResampleFilter)
TYPENAMES.append('BVTK_NT_PResampleFilter' )


# --------------------------------------------------------------


class BVTK_NT_PieceRequestFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PieceRequestFilter'
    bl_label = 'vtkPieceRequestFilter'
    
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='The total number of pieces', default=1)
    m_Piece = bpy.props.IntProperty(name='Piece', description='The piece to extract', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NumberOfPieces', 'm_Piece', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PieceRequestFilter)
TYPENAMES.append('BVTK_NT_PieceRequestFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractGrid'
    bl_label = 'vtkExtractGrid'
    
    m_IncludeBoundary = bpy.props.BoolProperty(name='IncludeBoundary', description='Control whether to enforce that the "boundary" of the grid is output in the subsampling process. (This ivar only has effect when the SampleRate in any direction is not equal to 1.) When this ivar IncludeBoundary is on, the subsampling will always include the boundary of the grid even though the sample rate is not an even multiple of the grid dimensions. (By default IncludeBoundary is off.', default=True)
    m_SampleRate = bpy.props.IntVectorProperty(name='SampleRate', description='Set the sampling rate in the i, j, and k directions. If the rate is > 1, then the resulting VOI will be subsampled representation of the input. For example, if the SampleRate=(2,2,2), every other point will be selected, resulting in a volume 1/8th the original size. Initial value is (1,1,1)', default=[1, 1, 1], size=3)
    m_VOI = bpy.props.IntVectorProperty(name='VOI', description='Specify i-j-k (min,max) pairs to extract. The resulting structured grid dataset can be of any topological dimension (i.e., point, line, plane, or 3D grid)', default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_IncludeBoundary', 'm_SampleRate', 'm_VOI', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractGrid)
TYPENAMES.append('BVTK_NT_ExtractGrid' )


# --------------------------------------------------------------


class BVTK_NT_PointDensityFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PointDensityFilter'
    bl_label = 'vtkPointDensityFilter'
    e_DensityEstimate_items = [(x, x, x) for x in ['FixedRadius', 'RelativeRadius']]
    e_DensityForm_items = [(x, x, x) for x in ['NumberOfPoints', 'VolumeNormalized']]
    
    m_AdjustDistance = bpy.props.FloatProperty(name='AdjustDistance', description='Set / get the relative amount to pad the model bounds if automatic computation is performed. The padding is the fraction to scale the model bounds in each of the x-y-z directions. By default the padding is 0.10 (i.e., 10% larger in each direction)', default=0.1)
    m_ComputeGradient = bpy.props.BoolProperty(name='ComputeGradient', description='Turn on/off the generation of the gradient vector, gradient magnitude scalar, and function classification scalar. By default this is off. Note that this will increase execution time and the size of the output. (The names of these point data arrays are: "Gradient", "Gradient Magnitude", and "Classification".', default=False)
    e_DensityEstimate = bpy.props.EnumProperty(name='DensityEstimate', description='Specify the method to estimate point density. The density can be calculated using a fixed sphere radius; or a sphere radius that is relative to voxel size', default='RelativeRadius', items=e_DensityEstimate_items)
    e_DensityForm = bpy.props.EnumProperty(name='DensityForm', description='Specify the form by which the density is expressed. Either the density is expressed as (number of points/local sphere volume), or as simply the (number of points) within the local sphere', default='NumberOfPoints', items=e_DensityForm_items)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Set / get the (xmin,xmax, ymin,ymax, zmin,zmax) bounding box in which the sampling is performed. If any of the (min,max) bounds values are min >= max, then the bounds will be computed automatically from the input data. Otherwise, the user-specified bounds will be used', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6)
    m_Radius = bpy.props.FloatProperty(name='Radius', description="Set / get the radius variable defining the local sphere used to estimate the density function. The Radius is used when the density estimate is ^ set to a fixed radius (i.e., the radius doesn't change)", default=1.0)
    m_RelativeRadius = bpy.props.FloatProperty(name='RelativeRadius', description='Set / get the relative radius factor defining the local sphere used to estimate the density function. The relative sphere radius is equal to the diagonal length of a voxel times the radius factor. The RelativeRadius is used when the density estimate is set to relative radius (i.e., relative to voxel size)', default=1.0)
    m_ScalarWeighting = bpy.props.BoolProperty(name='ScalarWeighting', description='Turn on/off the weighting of point density by a scalar array. By default scalar weighting is off', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AdjustDistance', 'm_ComputeGradient', 'e_DensityEstimate', 'e_DensityForm', 'm_ModelBounds', 'm_Radius', 'm_RelativeRadius', 'm_ScalarWeighting', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PointDensityFilter)
TYPENAMES.append('BVTK_NT_PointDensityFilter' )


# --------------------------------------------------------------


class BVTK_NT_TableAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TableAlgorithm'
    bl_label = 'vtkTableAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TableAlgorithm)
TYPENAMES.append('BVTK_NT_TableAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_YoungsMaterialInterface(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_YoungsMaterialInterface'
    bl_label = 'vtkYoungsMaterialInterface'
    
    m_AxisSymetric = bpy.props.BoolProperty(name='AxisSymetric', description='Turns on/off AxisSymetric computation of 2D interfaces. in axis symetric mode, 2D meshes are understood as volumes of revolution', default=True)
    m_FillMaterial = bpy.props.BoolProperty(name='FillMaterial', description='When FillMaterial is set to 1, the volume containing material is output and not only the interface surface', default=True)
    m_InverseNormal = bpy.props.BoolProperty(name='InverseNormal', description='Set/Get whether the normal vector has to be flipped', default=True)
    m_NumberOfMaterials = bpy.props.IntProperty(name='NumberOfMaterials', description='Sets/Gets the number of materials', default=0)
    m_OnionPeel = bpy.props.BoolProperty(name='OnionPeel', description='Set/Get OnionPeel flag. if this flag is on, the normal vector of the first material (which depends on material ordering) is used for all materials', default=True)
    m_ReverseMaterialOrder = bpy.props.BoolProperty(name='ReverseMaterialOrder', description='If this flag is on, material order in reversed. Otherwise, materials are sorted in ascending order depending on the given ordering array', default=True)
    m_UseAllBlocks = bpy.props.BoolProperty(name='UseAllBlocks', description='Set/Get whether all material blocks should be used, irrespective of the material block mapping', default=True)
    m_UseFractionAsDistance = bpy.props.BoolProperty(name='UseFractionAsDistance', description='when UseFractionAsDistance is true, the volume fraction is interpreted as the distance of the cutting plane from the origin. in axis symetric mode, 2D meshes are understood as volumes of revolution', default=True)
    m_VolumeFractionRange = bpy.props.FloatVectorProperty(name='VolumeFractionRange', description='Set/Get minimum and maximum volume fraction value. if a material fills a volume above the minimum value, the material is considered to be void. if a material fills a volume fraction beyond the maximum value it is considered as filling the whole volum', default=[0.01, 0.99], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AxisSymetric', 'm_FillMaterial', 'm_InverseNormal', 'm_NumberOfMaterials', 'm_OnionPeel', 'm_ReverseMaterialOrder', 'm_UseAllBlocks', 'm_UseFractionAsDistance', 'm_VolumeFractionRange', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_YoungsMaterialInterface)
TYPENAMES.append('BVTK_NT_YoungsMaterialInterface' )


# --------------------------------------------------------------


class BVTK_NT_HyperTreeGridDepthLimiter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperTreeGridDepthLimiter'
    bl_label = 'vtkHyperTreeGridDepthLimiter'
    
    m_Depth = bpy.props.IntProperty(name='Depth', description='Set/Get maximum depth to which output grid should be limite', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Depth', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperTreeGridDepthLimiter)
TYPENAMES.append('BVTK_NT_HyperTreeGridDepthLimiter' )


# --------------------------------------------------------------


class BVTK_NT_ImageTranslateExtent(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageTranslateExtent'
    bl_label = 'vtkImageTranslateExtent'
    
    m_Translation = bpy.props.IntVectorProperty(name='Translation', description='', default=[0, 0, 0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Translation', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageTranslateExtent)
TYPENAMES.append('BVTK_NT_ImageTranslateExtent' )


# --------------------------------------------------------------


class BVTK_NT_ExtractDataSets(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractDataSets'
    bl_label = 'vtkExtractDataSets'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractDataSets)
TYPENAMES.append('BVTK_NT_ExtractDataSets' )


# --------------------------------------------------------------


class BVTK_NT_HyperStreamline(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperStreamline'
    bl_label = 'vtkHyperStreamline'
    e_IntegrationDirection_items = [(x, x, x) for x in ['Backward', 'Forward', 'IntegrateBothDirections']]
    e_IntegrationEigenvector_items = [(x, x, x) for x in ['Major', 'Medium', 'Minor']]
    
    e_IntegrationDirection = bpy.props.EnumProperty(name='IntegrationDirection', description='Specify the direction in which to integrate the hyperstreamline', default='Forward', items=e_IntegrationDirection_items)
    e_IntegrationEigenvector = bpy.props.EnumProperty(name='IntegrationEigenvector', description='Set / get the eigenvector field through which to ingrate. It is possible to integrate using the major, medium or minor eigenvector field. The major eigenvector is the eigenvector whose corresponding eigenvalue is closest to positive infinity. The minor eigenvector is the eigenvector whose corresponding eigenvalue is closest to negative infinity. The medium eigenvector is the eigenvector whose corresponding eigenvalue is between the major and minor eigenvalues', default='Major', items=e_IntegrationEigenvector_items)
    m_IntegrationStepLength = bpy.props.FloatProperty(name='IntegrationStepLength', description='Set / get a nominal integration step size (expressed as a fraction of the size of each cell)', default=0.2)
    m_LogScaling = bpy.props.BoolProperty(name='LogScaling', description='Turn on/off logarithmic scaling. If scaling is on, the log base 10 of the computed eigenvalues are used to scale the cross section radii', default=True)
    m_MaximumPropagationDistance = bpy.props.FloatProperty(name='MaximumPropagationDistance', description='Set / get the maximum length of the hyperstreamline expressed as absolute distance (i.e., arc length) value', default=100.0)
    m_NumberOfSides = bpy.props.IntProperty(name='NumberOfSides', description='Set / get the number of sides for the hyperstreamlines. At a minimum, number of sides is 3', default=6)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set / get the initial tube radius. This is the maximum "elliptical" radius at the beginning of the tube. Radius varies based on ratio of eigenvalues. Note that tube section is actually elliptical and may become a point or line in cross section in some cases', default=0.5)
    m_StepLength = bpy.props.FloatProperty(name='StepLength', description='Set / get the length of a tube segment composing the hyperstreamline. The length is specified as a fraction of the diagonal length of the input bounding box', default=0.01)
    m_TerminalEigenvalue = bpy.props.FloatProperty(name='TerminalEigenvalue', description='Set/get terminal eigenvalue. If major eigenvalue falls below this value, hyperstreamline terminates propagation', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_IntegrationDirection', 'e_IntegrationEigenvector', 'm_IntegrationStepLength', 'm_LogScaling', 'm_MaximumPropagationDistance', 'm_NumberOfSides', 'm_Radius', 'm_StepLength', 'm_TerminalEigenvalue', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperStreamline)
TYPENAMES.append('BVTK_NT_HyperStreamline' )


# --------------------------------------------------------------


class BVTK_NT_LabelHierarchyAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LabelHierarchyAlgorithm'
    bl_label = 'vtkLabelHierarchyAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LabelHierarchyAlgorithm)
TYPENAMES.append('BVTK_NT_LabelHierarchyAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_AppendCompositeDataLeaves(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AppendCompositeDataLeaves'
    bl_label = 'vtkAppendCompositeDataLeaves'
    
    m_AppendFieldData = bpy.props.BoolProperty(name='AppendFieldData', description='Set/get whether the field data of each dataset in the composite dataset is copied to the output. If AppendFieldData is non-zero, then field data arrays from all the inputs are added to the output. If there are duplicates, the array on the first input encountered is taken', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AppendFieldData', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AppendCompositeDataLeaves)
TYPENAMES.append('BVTK_NT_AppendCompositeDataLeaves' )


# --------------------------------------------------------------


class BVTK_NT_ImageContinuousErode3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageContinuousErode3D'
    bl_label = 'vtkImageContinuousErode3D'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageContinuousErode3D)
TYPENAMES.append('BVTK_NT_ImageContinuousErode3D' )


# --------------------------------------------------------------


class BVTK_NT_ImageFourierCenter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageFourierCenter'
    bl_label = 'vtkImageFourierCenter'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Dimensionality is the number of axes which are considered during execution. To process images dimensionality would be set to 2', default=3)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageFourierCenter)
TYPENAMES.append('BVTK_NT_ImageFourierCenter' )


# --------------------------------------------------------------


class BVTK_NT_PMaskPoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PMaskPoints'
    bl_label = 'vtkPMaskPoints'
    
    m_GenerateVertices = bpy.props.BoolProperty(name='GenerateVertices', description='Generate output polydata vertices as well as points. A useful convenience method because vertices are drawn (they are topology) while points are not (they are geometry). By default this method is off', default=True)
    m_MaximumNumberOfPoints = bpy.props.IntProperty(name='MaximumNumberOfPoints', description='Limit the number of points that can be passed through (i.e., sets the output sample size)', default=1000000000)
    m_Offset = bpy.props.IntProperty(name='Offset', description='Start sampling with this point. Ignored by certain random modes', default=0)
    m_OnRatio = bpy.props.IntProperty(name='OnRatio', description='Turn on every nth point (strided sampling), ignored by random modes', default=2)
    m_ProportionalMaximumNumberOfPoints = bpy.props.BoolProperty(name='ProportionalMaximumNumberOfPoints', description='THIS ONLY WORKS WITH THE PARALLEL IMPLEMENTATION vtkPMaskPoints RUNNING IN PARALLEL. NOTHING WILL CHANGE IF THIS IS NOT THE PARALLEL vtkPMaskPoints. Determines whether maximum number of points is taken per processor (default) or if the maximum number of points is proportionally taken across processors (i.e., number of points per processor = points on a processor * maximum number of points / total points across all processors). In the first case, the total number of points = maximum number of points * number of processors. In the second case, the total number of points = maximum number of points', default=True)
    m_RandomMode = bpy.props.BoolProperty(name='RandomMode', description='Special flag causes randomization of point selection', default=True)
    m_RandomModeType = bpy.props.IntProperty(name='RandomModeType', description='Special mode selector that switches between random mode types. 0 - randomized strides: randomly strides through the data (default); fairly certain that this is not a statistically random sample because the output depends on the order of the input and the input points do not have an equal chance to appear in the output (plus Vitter\'s incremental random algorithms are more complex than this, while not a proof it is good indication this isn\'t a statistically random sample - the closest would be algorithm S) 1 - random sample: create a statistically random sample using Vitter\'s incremental algorithm D without A described in Vitter "Faster Mthods for Random Sampling", Communications of the ACM Volume 27, Issue 7, 1984 (OnRatio and Offset are ignored) O(sample size) 2 - spatially stratified random sample: create a spatially stratified random sample using the first method described in Woodring et al. "In-situ Sampling of a Large-Scale Particle Simulation for Interactive Visualization and Analysis", Computer Graphics Forum, 2011 (EuroVis 2011). (OnRatio and Offset are ignored) O(N log N', default=0)
    m_SingleVertexPerCell = bpy.props.BoolProperty(name='SingleVertexPerCell', description='When vertex generation is enabled, by default vertices are produced as multi-vertex cells (more than one per cell), if you wish to have a single vertex per cell, enable this flag', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateVertices', 'm_MaximumNumberOfPoints', 'm_Offset', 'm_OnRatio', 'm_ProportionalMaximumNumberOfPoints', 'm_RandomMode', 'm_RandomModeType', 'm_SingleVertexPerCell', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PMaskPoints)
TYPENAMES.append('BVTK_NT_PMaskPoints' )


# --------------------------------------------------------------


class BVTK_NT_ImageButterworthLowPass(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageButterworthLowPass'
    bl_label = 'vtkImageButterworthLowPass'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_CutOff = bpy.props.FloatVectorProperty(name='CutOff', description='', default=[1e+30, 1e+30, 1e+30], size=3)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_Order = bpy.props.IntProperty(name='Order', description='The order determines sharpness of the cutoff curve', default=1)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_XCutOff = bpy.props.FloatProperty(name='XCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    m_YCutOff = bpy.props.FloatProperty(name='YCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    m_ZCutOff = bpy.props.FloatProperty(name='ZCutOff', description='Set/Get the cutoff frequency for each axis. The values are specified in the order X, Y, Z, Time. Units: Cycles per world unit (as defined by the data spacing)', default=1e+30)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CutOff', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_Order', 'e_SplitMode', 'm_XCutOff', 'm_YCutOff', 'm_ZCutOff', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageButterworthLowPass)
TYPENAMES.append('BVTK_NT_ImageButterworthLowPass' )


# --------------------------------------------------------------


class BVTK_NT_PassInputTypeAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PassInputTypeAlgorithm'
    bl_label = 'vtkPassInputTypeAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PassInputTypeAlgorithm)
TYPENAMES.append('BVTK_NT_PassInputTypeAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_DuplicatePolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DuplicatePolyData'
    bl_label = 'vtkDuplicatePolyData'
    
    m_ClientFlag = bpy.props.IntProperty(name='ClientFlag', description='This duplicate filter works in client server mode when this controller is set. We have a client flag to differentiate the client and server because the socket controller is odd: Proth processes think their id is 0', default=0)
    m_Synchronous = bpy.props.BoolProperty(name='Synchronous', description='This flag causes sends and receives to be matched. When this flag is off, two sends occur then two receives. I want to see if it makes a difference in performance. The flag is on by default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClientFlag', 'm_Synchronous', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DuplicatePolyData)
TYPENAMES.append('BVTK_NT_DuplicatePolyData' )


# --------------------------------------------------------------


class BVTK_NT_PCAAnalysisFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PCAAnalysisFilter'
    bl_label = 'vtkPCAAnalysisFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PCAAnalysisFilter)
TYPENAMES.append('BVTK_NT_PCAAnalysisFilter' )


# --------------------------------------------------------------


class BVTK_NT_WarpTo(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_WarpTo'
    bl_label = 'vtkWarpTo'
    
    m_Absolute = bpy.props.BoolProperty(name='Absolute', description='Set/Get the Absolute ivar. Turning Absolute on causes scale factor of the new position to be one unit away from Position', default=True)
    m_Position = bpy.props.FloatVectorProperty(name='Position', description='Set/Get the position to warp towards', default=[0.0, 0.0, 0.0], size=3)
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Set/Get the value to scale displacement', default=0.5)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Absolute', 'm_Position', 'm_ScaleFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_WarpTo)
TYPENAMES.append('BVTK_NT_WarpTo' )


# --------------------------------------------------------------


class BVTK_NT_FlyingEdges2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FlyingEdges2D'
    bl_label = 'vtkFlyingEdges2D'
    
    m_ArrayComponent = bpy.props.IntProperty(name='ArrayComponent', description='Set/get which component of the scalar array to contour on; defaults to 0', default=0)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Option to set the point scalars of the output. The scalars will be the iso value of course. By default this flag is on', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Set the number of contours to place into the list. You only really need to use this method to reduce list size. The method SetValue() will automatically increase list size as needed', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayComponent', 'm_ComputeScalars', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FlyingEdges2D)
TYPENAMES.append('BVTK_NT_FlyingEdges2D' )


# --------------------------------------------------------------


class BVTK_NT_PieceScalars(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PieceScalars'
    bl_label = 'vtkPieceScalars'
    
    m_RandomMode = bpy.props.BoolProperty(name='RandomMode', description='', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_RandomMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PieceScalars)
TYPENAMES.append('BVTK_NT_PieceScalars' )


# --------------------------------------------------------------


class BVTK_NT_ImageRGBToYIQ(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageRGBToYIQ'
    bl_label = 'vtkImageRGBToYIQ'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Maximum = bpy.props.FloatProperty(name='Maximum', description='', default=255.0)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Maximum', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageRGBToYIQ)
TYPENAMES.append('BVTK_NT_ImageRGBToYIQ' )


# --------------------------------------------------------------


class BVTK_NT_UniformGridPartitioner(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_UniformGridPartitioner'
    bl_label = 'vtkUniformGridPartitioner'
    
    m_DuplicateNodes = bpy.props.BoolProperty(name='DuplicateNodes', description='', default=True)
    m_NumberOfGhostLayers = bpy.props.IntProperty(name='NumberOfGhostLayers', description='Set/Get macro for the number of ghost layers', default=0)
    m_NumberOfPartitions = bpy.props.IntProperty(name='NumberOfPartitions', description='Set/Get macro for the number of subdivisions', default=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DuplicateNodes', 'm_NumberOfGhostLayers', 'm_NumberOfPartitions', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_UniformGridPartitioner)
TYPENAMES.append('BVTK_NT_UniformGridPartitioner' )


# --------------------------------------------------------------


class BVTK_NT_UniformGridGhostDataGenerator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_UniformGridGhostDataGenerator'
    bl_label = 'vtkUniformGridGhostDataGenerator'
    
    m_NumberOfGhostLayers = bpy.props.IntProperty(name='NumberOfGhostLayers', description='Set/Get for number of ghost layers to generate', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NumberOfGhostLayers', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_UniformGridGhostDataGenerator)
TYPENAMES.append('BVTK_NT_UniformGridGhostDataGenerator' )


# --------------------------------------------------------------


class BVTK_NT_RotationalExtrusionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RotationalExtrusionFilter'
    bl_label = 'vtkRotationalExtrusionFilter'
    
    m_Angle = bpy.props.FloatProperty(name='Angle', description='Set/Get angle of rotation', default=360.0)
    m_Capping = bpy.props.BoolProperty(name='Capping', description='Turn on/off the capping of the skirt', default=True)
    m_DeltaRadius = bpy.props.FloatProperty(name='DeltaRadius', description='Set/Get change in radius during sweep process', default=0.0)
    m_Resolution = bpy.props.IntProperty(name='Resolution', description='Set/Get resolution of sweep operation. Resolution controls the number of intermediate node points', default=12)
    m_Translation = bpy.props.FloatProperty(name='Translation', description='Set/Get total amount of translation along the z-axis', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Angle', 'm_Capping', 'm_DeltaRadius', 'm_Resolution', 'm_Translation', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RotationalExtrusionFilter)
TYPENAMES.append('BVTK_NT_RotationalExtrusionFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageThreshold(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageThreshold'
    bl_label = 'vtkImageThreshold'
    e_OutputScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Long', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_InValue = bpy.props.FloatProperty(name='InValue', description='Replace the in range pixels with this value', default=0.0)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_OutValue = bpy.props.FloatProperty(name='OutValue', description='Replace the in range pixels with this value', default=0.0)
    e_OutputScalarType = bpy.props.EnumProperty(name='OutputScalarType', description='Set the desired output scalar type to cast t', items=e_OutputScalarType_items)
    m_ReplaceIn = bpy.props.BoolProperty(name='ReplaceIn', description='Determines whether to replace the pixel in range with InValu', default=True)
    m_ReplaceOut = bpy.props.BoolProperty(name='ReplaceOut', description='Determines whether to replace the pixel out of range with OutValu', default=True)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_InValue', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_OutValue', 'e_OutputScalarType', 'm_ReplaceIn', 'm_ReplaceOut', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageThreshold)
TYPENAMES.append('BVTK_NT_ImageThreshold' )


# --------------------------------------------------------------


class BVTK_NT_GraphToPoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GraphToPoints'
    bl_label = 'vtkGraphToPoints'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GraphToPoints)
TYPENAMES.append('BVTK_NT_GraphToPoints' )


# --------------------------------------------------------------


class BVTK_NT_MarchingContourFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MarchingContourFilter'
    bl_label = 'vtkMarchingContourFilter'
    
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Methods to set / get contour values', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MarchingContourFilter)
TYPENAMES.append('BVTK_NT_MarchingContourFilter' )


# --------------------------------------------------------------


class BVTK_NT_VoxelModeller(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VoxelModeller'
    bl_label = 'vtkVoxelModeller'
    e_ScalarType_items = [(x, x, x) for x in ['Bit', 'Char', 'Double', 'Float', 'Int', 'Long', 'Short', 'UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    
    m_BackgroundValue = bpy.props.FloatProperty(name='BackgroundValue', description='Set the Foreground/Background values of the output. The Foreground value is set when a voxel is occupied. The Background value is set when a voxel is not occupied. The default ForegroundValue is 1. The default BackgroundValue is 0', default=0.0)
    m_ForegroundValue = bpy.props.FloatProperty(name='ForegroundValue', description='Set the Foreground/Background values of the output. The Foreground value is set when a voxel is occupied. The Background value is set when a voxel is not occupied. The default ForegroundValue is 1. The default BackgroundValue is 0', default=1.0)
    m_MaximumDistance = bpy.props.FloatProperty(name='MaximumDistance', description='Specify distance away from surface of input geometry to sample. Smaller values make large increases in performance. Default is 1.0', default=1.0)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Specify the position in space to perform the voxelization. Default is (0, 0, 0, 0, 0, 0', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6)
    e_ScalarType = bpy.props.EnumProperty(name='ScalarType', description='Control the scalar type of the output image. The default is VTK_BIT. NOTE: Not all filters/readers/writers support the VTK_BIT scalar type. You may want to use VTK_CHAR as an alternative', default='Bit', items=e_ScalarType_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BackgroundValue', 'm_ForegroundValue', 'm_MaximumDistance', 'm_ModelBounds', 'e_ScalarType', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VoxelModeller)
TYPENAMES.append('BVTK_NT_VoxelModeller' )


# --------------------------------------------------------------


class BVTK_NT_MarchingCubes(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MarchingCubes'
    bl_label = 'vtkMarchingCubes'
    
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MarchingCubes)
TYPENAMES.append('BVTK_NT_MarchingCubes' )


# --------------------------------------------------------------


class BVTK_NT_ImageDilateErode3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageDilateErode3D'
    bl_label = 'vtkImageDilateErode3D'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_DilateValue = bpy.props.FloatProperty(name='DilateValue', description='Set/Get the Dilate and Erode values to be used by this filter', default=0.0)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_ErodeValue = bpy.props.FloatProperty(name='ErodeValue', description='Set/Get the Dilate and Erode values to be used by this filter', default=255.0)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_DilateValue', 'm_EnableSMP', 'm_ErodeValue', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageDilateErode3D)
TYPENAMES.append('BVTK_NT_ImageDilateErode3D' )


# --------------------------------------------------------------


class BVTK_NT_ImageMedian3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMedian3D'
    bl_label = 'vtkImageMedian3D'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMedian3D)
TYPENAMES.append('BVTK_NT_ImageMedian3D' )


# --------------------------------------------------------------


class BVTK_NT_TubeFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TubeFilter'
    bl_label = 'vtkTubeFilter'
    e_GenerateTCoords_items = [(x, x, x) for x in ['NormalizedLength', 'Off', 'UseLength', 'UseScalars']]
    e_VaryRadius_items = [(x, x, x) for x in ['VaryRadiusByAbsoluteScalar', 'VaryRadiusByScalar', 'VaryRadiusByVector', 'VaryRadiusOff']]
    
    m_Capping = bpy.props.BoolProperty(name='Capping', description='Turn on/off whether to cap the ends with polygons. Initial value is off', default=True)
    m_DefaultNormal = bpy.props.FloatVectorProperty(name='DefaultNormal', description='Set the default normal to use if no normals are supplied, and the DefaultNormalOn is set', default=[0.0, 0.0, 1.0], size=3)
    e_GenerateTCoords = bpy.props.EnumProperty(name='GenerateTCoords', description='Control whether and how texture coordinates are produced. This is useful for striping the tube with length textures, etc. If you use scalars to create the texture, the scalars are assumed to be monotonically increasing (or decreasing)', default='Off', items=e_GenerateTCoords_items)
    m_NumberOfSides = bpy.props.IntProperty(name='NumberOfSides', description='Set the number of sides for the tube. At a minimum, number of sides is 3', default=3)
    m_Offset = bpy.props.IntProperty(name='Offset', description='Control the striping of the tubes. The offset sets the first tube side that is visible. Offset is generally used with OnRatio to create nifty striping effects', default=0)
    m_OnRatio = bpy.props.IntProperty(name='OnRatio', description='Control the striping of the tubes. If OnRatio is greater than 1, then every nth tube side is turned on, beginning with the Offset side', default=1)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set the minimum tube radius (minimum because the tube radius may vary)', default=0.5)
    m_RadiusFactor = bpy.props.FloatProperty(name='RadiusFactor', description='Set the maximum tube radius in terms of a multiple of the minimum radius', default=10.0)
    m_SidesShareVertices = bpy.props.BoolProperty(name='SidesShareVertices', description='Set a boolean to control whether tube sides should share vertices. This creates independent strips, with constant normals so the tube is always faceted in appearance', default=True)
    m_TextureLength = bpy.props.FloatProperty(name='TextureLength', description='Control the conversion of units during the texture coordinates calculation. The TextureLength indicates what length (whether calculated from scalars or length) is mapped to the [0,1) texture space', default=1.0)
    m_UseDefaultNormal = bpy.props.BoolProperty(name='UseDefaultNormal', description='Set a boolean to control whether to use default normals. DefaultNormalOn is set', default=True)
    e_VaryRadius = bpy.props.EnumProperty(name='VaryRadius', description='Turn on/off the variation of tube radius with scalar value', default='VaryRadiusOff', items=e_VaryRadius_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Capping', 'm_DefaultNormal', 'e_GenerateTCoords', 'm_NumberOfSides', 'm_Offset', 'm_OnRatio', 'm_Radius', 'm_RadiusFactor', 'm_SidesShareVertices', 'm_TextureLength', 'm_UseDefaultNormal', 'e_VaryRadius', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TubeFilter)
TYPENAMES.append('BVTK_NT_TubeFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImagePadFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImagePadFilter'
    bl_label = 'vtkImagePadFilter'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_OutputNumberOfScalarComponents = bpy.props.IntProperty(name='OutputNumberOfScalarComponents', description='Set/Get the number of output scalar components', default=-1)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_OutputNumberOfScalarComponents', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImagePadFilter)
TYPENAMES.append('BVTK_NT_ImagePadFilter' )


# --------------------------------------------------------------


class BVTK_NT_NormalizeMatrixVectors(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_NormalizeMatrixVectors'
    bl_label = 'vtkNormalizeMatrixVectors'
    
    m_PValue = bpy.props.FloatProperty(name='PValue', description='Value of p in p-norm normalization, subject to p >= 1. Default is p=2 (Euclidean norm)', default=2.0)
    m_VectorDimension = bpy.props.IntProperty(name='VectorDimension', description='Controls whether to normalize row-vectors or column-vectors. 0 = rows, 1 = columns', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PValue', 'm_VectorDimension', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_NormalizeMatrixVectors)
TYPENAMES.append('BVTK_NT_NormalizeMatrixVectors' )


# --------------------------------------------------------------


class BVTK_NT_GenericContourFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GenericContourFilter'
    bl_label = 'vtkGenericContourFilter'
    
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Methods to set / get contour values', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GenericContourFilter)
TYPENAMES.append('BVTK_NT_GenericContourFilter' )


# --------------------------------------------------------------


class BVTK_NT_ContourTriangulator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ContourTriangulator'
    bl_label = 'vtkContourTriangulator'
    
    m_TriangulationErrorDisplay = bpy.props.BoolProperty(name='TriangulationErrorDisplay', description='Generate errors when the triangulation fails. Note that triangulation failures are often minor, because they involve tiny triangles that are too small to see', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_TriangulationErrorDisplay', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ContourTriangulator)
TYPENAMES.append('BVTK_NT_ContourTriangulator' )


# --------------------------------------------------------------


class BVTK_NT_DijkstraImageGeodesicPath(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DijkstraImageGeodesicPath'
    bl_label = 'vtkDijkstraImageGeodesicPath'
    
    m_CurvatureWeight = bpy.props.FloatProperty(name='CurvatureWeight', description='Curvature cost weight', default=0.0)
    m_EdgeLengthWeight = bpy.props.FloatProperty(name='EdgeLengthWeight', description='Edge length cost weight', default=0.0)
    m_EndVertex = bpy.props.IntProperty(name='EndVertex', description='The vertex at the end of the shortest pat', default=0)
    m_ImageWeight = bpy.props.FloatProperty(name='ImageWeight', description='Image cost weight', default=1.0)
    m_RepelPathFromVertices = bpy.props.BoolProperty(name='RepelPathFromVertices', description='Use the input point to repel the path by assigning high costs', default=True)
    m_StartVertex = bpy.props.IntProperty(name='StartVertex', description='The vertex at the start of the shortest pat', default=0)
    m_StopWhenEndReached = bpy.props.BoolProperty(name='StopWhenEndReached', description='Stop when the end vertex is reached or calculate shortest path to all vertice', default=True)
    m_UseScalarWeights = bpy.props.BoolProperty(name='UseScalarWeights', description='Use scalar values in the edge weight (experimental', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CurvatureWeight', 'm_EdgeLengthWeight', 'm_EndVertex', 'm_ImageWeight', 'm_RepelPathFromVertices', 'm_StartVertex', 'm_StopWhenEndReached', 'm_UseScalarWeights', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['RepelVertices'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DijkstraImageGeodesicPath)
TYPENAMES.append('BVTK_NT_DijkstraImageGeodesicPath' )


# --------------------------------------------------------------


class BVTK_NT_TemporalSnapToTimeStep(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TemporalSnapToTimeStep'
    bl_label = 'vtkTemporalSnapToTimeStep'
    e_SnapMode_items = [(x, x, x) for x in ['Nearest', 'NextAboveOrEqual', 'NextBelowOrEqual']]
    
    e_SnapMode = bpy.props.EnumProperty(name='SnapMode', description='', default='Nearest', items=e_SnapMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_SnapMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TemporalSnapToTimeStep)
TYPENAMES.append('BVTK_NT_TemporalSnapToTimeStep' )


# --------------------------------------------------------------


class BVTK_NT_DataSetGradient(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataSetGradient'
    bl_label = 'vtkDataSetGradient'
    
    m_ResultArrayName = bpy.props.StringProperty(name='ResultArrayName', description='Set/Get the name of computed vector array', default='gradient')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ResultArrayName', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataSetGradient)
TYPENAMES.append('BVTK_NT_DataSetGradient' )


# --------------------------------------------------------------


class BVTK_NT_HierarchicalDataSetGeometryFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HierarchicalDataSetGeometryFilter'
    bl_label = 'vtkHierarchicalDataSetGeometryFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HierarchicalDataSetGeometryFilter)
TYPENAMES.append('BVTK_NT_HierarchicalDataSetGeometryFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageGaussianSmooth(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageGaussianSmooth'
    bl_label = 'vtkImageGaussianSmooth'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Set/Get the dimensionality of this filter. This determines whether a one, two, or three dimensional gaussian is performed', default=3)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_RadiusFactors = bpy.props.FloatVectorProperty(name='RadiusFactors', description='', default=[1.5, 1.5, 1.5], size=3)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_StandardDeviations = bpy.props.FloatVectorProperty(name='StandardDeviations', description='', default=[2.0, 2.0, 2.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'm_RadiusFactors', 'e_SplitMode', 'm_StandardDeviations', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageGaussianSmooth)
TYPENAMES.append('BVTK_NT_ImageGaussianSmooth' )


# --------------------------------------------------------------


class BVTK_NT_UnstructuredGridQuadricDecimation(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_UnstructuredGridQuadricDecimation'
    bl_label = 'vtkUnstructuredGridQuadricDecimation'
    
    m_AutoAddCandidates = bpy.props.IntProperty(name='AutoAddCandidates', description="Enable(1)/Disable(0) the feature of temporarily doubling the number of candidates for each randomized set if the quadric error was significantly increased over the last edge collapse, i.e. if the ratio between the error difference and the last error is over some threshold. Basically, we are trying to make up for cases when random selection returns so many 'bad' edges. By doing this we can achieve a higher quality output with much less time than just double the NumberOfCandidates. Default is Enabled(1", default=1)
    m_AutoAddCandidatesThreshold = bpy.props.FloatProperty(name='AutoAddCandidatesThreshold', description='Set/Get the threshold that decides when to double the set size. Default is 0.4', default=0.4)
    m_BoundaryWeight = bpy.props.FloatProperty(name='BoundaryWeight', description='Set/Get the weight of the boundary on the quadric metrics. The larger the number, the better the boundary is preserved', default=100.0)
    m_NumberOfCandidates = bpy.props.IntProperty(name='NumberOfCandidates', description='Set/Get the number of candidates selected for each randomized set before performing an edge collapse. Increasing this number can help producing higher quality output but it will be slower. Default is 8', default=8)
    m_NumberOfEdgesToDecimate = bpy.props.IntProperty(name='NumberOfEdgesToDecimate', description='Set/Get the desired number of edge to collaps', default=0)
    m_NumberOfTetsOutput = bpy.props.IntProperty(name='NumberOfTetsOutput', description='Set/Get the desired number of tetrahedra to be outpute', default=0)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set/Get the scalar field name used for simplificatio')
    m_TargetReduction = bpy.props.FloatProperty(name='TargetReduction', description='Set/Get the desired reduction (expressed as a fraction of the original number of tetrehedra', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutoAddCandidates', 'm_AutoAddCandidatesThreshold', 'm_BoundaryWeight', 'm_NumberOfCandidates', 'm_NumberOfEdgesToDecimate', 'm_NumberOfTetsOutput', 'm_ScalarsName', 'm_TargetReduction', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_UnstructuredGridQuadricDecimation)
TYPENAMES.append('BVTK_NT_UnstructuredGridQuadricDecimation' )


# --------------------------------------------------------------


class BVTK_NT_GraphToGlyphs(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GraphToGlyphs'
    bl_label = 'vtkGraphToGlyphs'
    
    m_Filled = bpy.props.BoolProperty(name='Filled', description='Whether to fill the glyph, or to just render the outline', default=True)
    m_GlyphType = bpy.props.IntProperty(name='GlyphType', description='The glyph type, specified as one of the enumerated values in this class. VERTEX is a special glyph that cannot be scaled, but instead is rendered as an OpenGL vertex primitive. This may appear as a box or circle depending on the hardware', default=7)
    m_Scaling = bpy.props.BoolProperty(name='Scaling', description='Whether to use the input array to process in order to scale the vertices', default=False)
    m_ScreenSize = bpy.props.FloatProperty(name='ScreenSize', description='Set the desired screen size of each glyph. If you are using scaling, this will be the size of the glyph when rendering an object with scaling value 1.0', default=10.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Filled', 'm_GlyphType', 'm_Scaling', 'm_ScreenSize', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['Renderer'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GraphToGlyphs)
TYPENAMES.append('BVTK_NT_GraphToGlyphs' )


# --------------------------------------------------------------


class BVTK_NT_ProgrammableFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProgrammableFilter'
    bl_label = 'vtkProgrammableFilter'
    
    m_CopyArrays = bpy.props.BoolProperty(name='CopyArrays', description='When CopyArrays is true, all arrays are copied to the output iff input and output are of the same type. False by default', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CopyArrays', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProgrammableFilter)
TYPENAMES.append('BVTK_NT_ProgrammableFilter' )


# --------------------------------------------------------------


class BVTK_NT_BlockIdScalars(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BlockIdScalars'
    bl_label = 'vtkBlockIdScalars'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BlockIdScalars)
TYPENAMES.append('BVTK_NT_BlockIdScalars' )


# --------------------------------------------------------------


class BVTK_NT_CountVertices(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CountVertices'
    bl_label = 'vtkCountVertices'
    
    m_OutputArrayName = bpy.props.StringProperty(name='OutputArrayName', description='The name of the new output array containing the vertex counts', default='Vertex Count')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_OutputArrayName', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CountVertices)
TYPENAMES.append('BVTK_NT_CountVertices' )


# --------------------------------------------------------------


class BVTK_NT_CleanPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CleanPolyData'
    bl_label = 'vtkCleanPolyData'
    
    m_AbsoluteTolerance = bpy.props.FloatProperty(name='AbsoluteTolerance', description='Specify tolerance in absolute terms. Default is 1.0', default=1.0)
    m_ConvertLinesToPoints = bpy.props.BoolProperty(name='ConvertLinesToPoints', description='Turn on/off conversion of degenerate lines to points. Default is On', default=True)
    m_ConvertPolysToLines = bpy.props.BoolProperty(name='ConvertPolysToLines', description='Turn on/off conversion of degenerate polys to lines. Default is On', default=True)
    m_ConvertStripsToPolys = bpy.props.BoolProperty(name='ConvertStripsToPolys', description='Turn on/off conversion of degenerate strips to polys. Default is On', default=True)
    m_PieceInvariant = bpy.props.BoolProperty(name='PieceInvariant', description='', default=True)
    m_PointMerging = bpy.props.BoolProperty(name='PointMerging', description='Set/Get a boolean value that controls whether point merging is performed. If on, a locator will be used, and points laying within the appropriate tolerance may be merged. If off, points are never merged. By default, merging is on', default=True)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Specify tolerance in terms of fraction of bounding box length. Default is 0.0', default=0.0)
    m_ToleranceIsAbsolute = bpy.props.BoolProperty(name='ToleranceIsAbsolute', description='By default ToleranceIsAbsolute is false and Tolerance is a fraction of Bounding box diagonal, if true, AbsoluteTolerance is used when adding points to locator (merging', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AbsoluteTolerance', 'm_ConvertLinesToPoints', 'm_ConvertPolysToLines', 'm_ConvertStripsToPolys', 'm_PieceInvariant', 'm_PointMerging', 'm_Tolerance', 'm_ToleranceIsAbsolute', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CleanPolyData)
TYPENAMES.append('BVTK_NT_CleanPolyData' )


# --------------------------------------------------------------


class BVTK_NT_ImageToStructuredGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageToStructuredGrid'
    bl_label = 'vtkImageToStructuredGrid'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageToStructuredGrid)
TYPENAMES.append('BVTK_NT_ImageToStructuredGrid' )


# --------------------------------------------------------------


class BVTK_NT_CellDerivatives(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CellDerivatives'
    bl_label = 'vtkCellDerivatives'
    e_TensorMode_items = [(x, x, x) for x in ['ComputeGradient', 'ComputeGreenLagrangeStrain', 'ComputeStrain', 'PassTensors']]
    e_VectorMode_items = [(x, x, x) for x in ['ComputeGradient', 'ComputeVorticity', 'PassVectors']]
    
    e_TensorMode = bpy.props.EnumProperty(name='TensorMode', description='Control how the filter works to generate tensor cell data. You can choose to pass the input cell tensors, compute the gradient of the input vectors, or compute the strain tensor (linearized or Green-Lagrange strain)of the vector gradient tensor. By default (TensorModeToComputeGradient), the filter will take the gradient of the vector data to construct a tensor', default='ComputeGradient', items=e_TensorMode_items)
    e_VectorMode = bpy.props.EnumProperty(name='VectorMode', description='Control how the filter works to generate vector cell data. You can choose to pass the input cell vectors, compute the gradient of the input scalars, or extract the vorticity of the computed vector gradient tensor. By default (VectorModeToComputeGradient), the filter will take the gradient of the input scalar data', default='ComputeGradient', items=e_VectorMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_TensorMode', 'e_VectorMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CellDerivatives)
TYPENAMES.append('BVTK_NT_CellDerivatives' )


# --------------------------------------------------------------


class BVTK_NT_PolyDataToReebGraphFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PolyDataToReebGraphFilter'
    bl_label = 'vtkPolyDataToReebGraphFilter'
    
    m_FieldId = bpy.props.IntProperty(name='FieldId', description='Set the scalar field id (default = 0)', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldId', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PolyDataToReebGraphFilter)
TYPENAMES.append('BVTK_NT_PolyDataToReebGraphFilter' )


# --------------------------------------------------------------


class BVTK_NT_GreedyTerrainDecimation(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GreedyTerrainDecimation'
    bl_label = 'vtkGreedyTerrainDecimation'
    e_ErrorMeasure_items = [(x, x, x) for x in ['AbsoluteError', 'NumberOfTriangles', 'RelativeError', 'SpecifiedReduction']]
    
    m_AbsoluteError = bpy.props.FloatProperty(name='AbsoluteError', description='Specify the absolute error of the mesh; that is, the error in height between the decimated mesh and the original height field. You need to set this value only when the error measure is set to AbsoluteError', default=1.0)
    m_BoundaryVertexDeletion = bpy.props.BoolProperty(name='BoundaryVertexDeletion', description='Turn on/off the deletion of vertices on the boundary of a mesh. This may limit the maximum reduction that may be achieved', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Compute normals based on the input image. Off by default', default=True)
    e_ErrorMeasure = bpy.props.EnumProperty(name='ErrorMeasure', description='Specify how to terminate the algorithm: either as an absolute number of triangles, a relative number of triangles (normalized by the full resolution mesh), an absolute error (in the height field), or relative error (normalized by the length of the diagonal of the image)', default='SpecifiedReduction', items=e_ErrorMeasure_items)
    m_NumberOfTriangles = bpy.props.IntProperty(name='NumberOfTriangles', description='Specify the number of triangles to produce on output. (It is a good idea to make sure this is less than a tessellated mesh at full resolution.) You need to set this value only when the error measure is set to NumberOfTriangles', default=1000)
    m_Reduction = bpy.props.FloatProperty(name='Reduction', description='Specify the reduction of the mesh (represented as a fraction). Note that a value of 0.10 means a 10% reduction. You need to set this value only when the error measure is set to SpecifiedReduction', default=0.9)
    m_RelativeError = bpy.props.FloatProperty(name='RelativeError', description='Specify the relative error of the mesh; that is, the error in height between the decimated mesh and the original height field normalized by the diagonal of the image. You need to set this value only when the error measure is set to RelativeError', default=0.01)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AbsoluteError', 'm_BoundaryVertexDeletion', 'm_ComputeNormals', 'e_ErrorMeasure', 'm_NumberOfTriangles', 'm_Reduction', 'm_RelativeError', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GreedyTerrainDecimation)
TYPENAMES.append('BVTK_NT_GreedyTerrainDecimation' )


# --------------------------------------------------------------


class BVTK_NT_RibbonFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RibbonFilter'
    bl_label = 'vtkRibbonFilter'
    e_GenerateTCoords_items = [(x, x, x) for x in ['NormalizedLength', 'Off', 'UseLength', 'UseScalars']]
    
    m_Angle = bpy.props.FloatProperty(name='Angle', description='Set the offset angle of the ribbon from the line normal. (The angle is expressed in degrees.) The default is 0.', default=0.0)
    m_DefaultNormal = bpy.props.FloatVectorProperty(name='DefaultNormal', description='Set the default normal to use if no normals are supplied, and DefaultNormalOn is set. The default is (0,0,1', default=[0.0, 0.0, 1.0], size=3)
    e_GenerateTCoords = bpy.props.EnumProperty(name='GenerateTCoords', description='Control whether and how texture coordinates are produced. This is useful for striping the ribbon with time textures, etc', default='Off', items=e_GenerateTCoords_items)
    m_TextureLength = bpy.props.FloatProperty(name='TextureLength', description='Control the conversion of units during the texture coordinates calculation. The TextureLength indicates what length (whether calculated from scalars or length) is mapped to the [0,1) texture space. The default is 1.', default=1.0)
    m_UseDefaultNormal = bpy.props.BoolProperty(name='UseDefaultNormal', description='Set a boolean to control whether to use default normals. The default is Of', default=True)
    m_VaryWidth = bpy.props.BoolProperty(name='VaryWidth', description='Turn on/off the variation of ribbon width with scalar value. The default is Of', default=True)
    m_Width = bpy.props.FloatProperty(name='Width', description='Set the "half" width of the ribbon. If the width is allowed to vary, this is the minimum width. The default is 0.', default=0.5)
    m_WidthFactor = bpy.props.FloatProperty(name='WidthFactor', description='Set the maximum ribbon width in terms of a multiple of the minimum width. The default is 2.', default=2.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Angle', 'm_DefaultNormal', 'e_GenerateTCoords', 'm_TextureLength', 'm_UseDefaultNormal', 'm_VaryWidth', 'm_Width', 'm_WidthFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RibbonFilter)
TYPENAMES.append('BVTK_NT_RibbonFilter' )


# --------------------------------------------------------------


class BVTK_NT_AppendArcLength(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AppendArcLength'
    bl_label = 'vtkAppendArcLength'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AppendArcLength)
TYPENAMES.append('BVTK_NT_AppendArcLength' )


# --------------------------------------------------------------


class BVTK_NT_QuadratureSchemeDictionaryGenerator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_QuadratureSchemeDictionaryGenerator'
    bl_label = 'vtkQuadratureSchemeDictionaryGenerator'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_QuadratureSchemeDictionaryGenerator)
TYPENAMES.append('BVTK_NT_QuadratureSchemeDictionaryGenerator' )


# --------------------------------------------------------------


class BVTK_NT_TableToPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TableToPolyData'
    bl_label = 'vtkTableToPolyData'
    
    m_Create2DPoints = bpy.props.BoolProperty(name='Create2DPoints', description='Specify whether the points of the polydata are 3D or 2D. If this is set to true then the Z Column will be ignored and the z value of each point on the polydata will be set to 0. By default this will be off', default=False)
    m_PreserveCoordinateColumnsAsDataArrays = bpy.props.BoolProperty(name='PreserveCoordinateColumnsAsDataArrays', description='Allow user to keep columns specified as X,Y,Z as Data arrays. By default this will be off', default=False)
    m_XColumn = bpy.props.StringProperty(name='XColumn', description='Set the name of the column to use as the X coordinate for the points')
    m_XColumnIndex = bpy.props.IntProperty(name='XColumnIndex', description='Set the index of the column to use as the X coordinate for the points', default=-1)
    m_XComponent = bpy.props.IntProperty(name='XComponent', description='Specify the component for the column specified using SetXColumn() to use as the xcoordinate in case the column is a multi-component array. Default is 0', default=0)
    m_YColumn = bpy.props.StringProperty(name='YColumn', description='Set the name of the column to use as the Y coordinate for the points. Default is 0')
    m_YColumnIndex = bpy.props.IntProperty(name='YColumnIndex', description='Set the index of the column to use as the Y coordinate for the points', default=-1)
    m_YComponent = bpy.props.IntProperty(name='YComponent', description='Specify the component for the column specified using SetYColumn() to use as the Ycoordinate in case the column is a multi-component array', default=0)
    m_ZColumn = bpy.props.StringProperty(name='ZColumn', description='Set the name of the column to use as the Z coordinate for the points. Default is 0')
    m_ZColumnIndex = bpy.props.IntProperty(name='ZColumnIndex', description='Set the index of the column to use as the Z coordinate for the points', default=-1)
    m_ZComponent = bpy.props.IntProperty(name='ZComponent', description='Specify the component for the column specified using SetZColumn() to use as the Zcoordinate in case the column is a multi-component array', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Create2DPoints', 'm_PreserveCoordinateColumnsAsDataArrays', 'm_XColumn', 'm_XColumnIndex', 'm_XComponent', 'm_YColumn', 'm_YColumnIndex', 'm_YComponent', 'm_ZColumn', 'm_ZColumnIndex', 'm_ZComponent', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TableToPolyData)
TYPENAMES.append('BVTK_NT_TableToPolyData' )


# --------------------------------------------------------------


class BVTK_NT_ImageClip(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageClip'
    bl_label = 'vtkImageClip'
    
    m_ClipData = bpy.props.BoolProperty(name='ClipData', description="By default, ClipData is off, and only the WholeExtent is modified. the data's extent may actually be larger. When this flag is on, the data extent will be no more than the OutputWholeExtent", default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ClipData', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageClip)
TYPENAMES.append('BVTK_NT_ImageClip' )


# --------------------------------------------------------------


class BVTK_NT_SurfaceReconstructionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SurfaceReconstructionFilter'
    bl_label = 'vtkSurfaceReconstructionFilter'
    
    m_NeighborhoodSize = bpy.props.IntProperty(name='NeighborhoodSize', description='Specify the number of neighbors each point has, used for estimating the local surface orientation. The default value of 20 should be OK for most applications, higher values can be specified if the spread of points is uneven. Values as low as 10 may yield adequate results for some surfaces. Higher values cause the algorithm to take longer. Higher values will cause errors on sharp boundaries', default=20)
    m_SampleSpacing = bpy.props.FloatProperty(name='SampleSpacing', description='Specify the spacing of the 3D sampling grid. If not set, a reasonable guess will be made', default=-1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NeighborhoodSize', 'm_SampleSpacing', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SurfaceReconstructionFilter)
TYPENAMES.append('BVTK_NT_SurfaceReconstructionFilter' )


# --------------------------------------------------------------


class BVTK_NT_MemoryLimitImageDataStreamer(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MemoryLimitImageDataStreamer'
    bl_label = 'vtkMemoryLimitImageDataStreamer'
    
    m_MemoryLimit = bpy.props.IntProperty(name='MemoryLimit', description='Set / Get the memory limit in kibibytes (1024 bytes)', default=51200)
    m_NumberOfStreamDivisions = bpy.props.IntProperty(name='NumberOfStreamDivisions', description='Set how many pieces to divide the input into. void SetNumberOfStreamDivisions(int num); int GetNumberOfStreamDivisions()', default=10)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MemoryLimit', 'm_NumberOfStreamDivisions', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['ExtentTranslator'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MemoryLimitImageDataStreamer)
TYPENAMES.append('BVTK_NT_MemoryLimitImageDataStreamer' )


# --------------------------------------------------------------


class BVTK_NT_ReflectionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ReflectionFilter'
    bl_label = 'vtkReflectionFilter'
    e_Plane_items = [(x, x, x) for x in ['X', 'XMax', 'XMin', 'Y', 'YMax', 'YMin', 'Z', 'ZMax', 'ZMin']]
    
    m_Center = bpy.props.FloatProperty(name='Center', description='If the reflection plane is set to X, Y or Z, this variable is use to set the position of the plane', default=0.0)
    m_CopyInput = bpy.props.BoolProperty(name='CopyInput', description='If on (the default), copy the input geometry to the output. If off, the output will only contain the reflection', default=True)
    m_FlipAllInputArrays = bpy.props.BoolProperty(name='FlipAllInputArrays', description="If off (the default), only Vectors, Normals and Tensors will be flipped. If on, all 3-component data arrays ( considered as 3D vectors), 6-component data arrays (considered as symmetric tensors), 9-component data arrays (considered as tensors ) of signed type will be flipped. All other won't be flipped and will only be copied", default=False)
    e_Plane = bpy.props.EnumProperty(name='Plane', description='Set the normal of the plane to use as mirror', default='XMin', items=e_Plane_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_CopyInput', 'm_FlipAllInputArrays', 'e_Plane', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ReflectionFilter)
TYPENAMES.append('BVTK_NT_ReflectionFilter' )


# --------------------------------------------------------------


class BVTK_NT_RectilinearGridOutlineFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RectilinearGridOutlineFilter'
    bl_label = 'vtkRectilinearGridOutlineFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RectilinearGridOutlineFilter)
TYPENAMES.append('BVTK_NT_RectilinearGridOutlineFilter' )


# --------------------------------------------------------------


class BVTK_NT_BlankStructuredGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BlankStructuredGrid'
    bl_label = 'vtkBlankStructuredGrid'
    
    m_ArrayId = bpy.props.IntProperty(name='ArrayId', description='Specify the data array id to use to generate the blanking field. Alternatively, you can specify the array name. (If both are set, the array name takes precedence.', default=-1)
    m_ArrayName = bpy.props.StringProperty(name='ArrayName', description='Specify the data array name to use to generate the blanking field. Alternatively, you can specify the array id. (If both are set, the array name takes precedence.')
    m_Component = bpy.props.IntProperty(name='Component', description='Specify the component in the data array to use to generate the blanking field', default=0)
    m_MaxBlankingValue = bpy.props.FloatProperty(name='MaxBlankingValue', description='Specify the upper data value in the data array specified which will be converted into a "blank" (or off) value in the blanking array', default=1e+30)
    m_MinBlankingValue = bpy.props.FloatProperty(name='MinBlankingValue', description='Specify the lower data value in the data array specified which will be converted into a "blank" (or off) value in the blanking array', default=1e+30)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayId', 'm_ArrayName', 'm_Component', 'm_MaxBlankingValue', 'm_MinBlankingValue', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BlankStructuredGrid)
TYPENAMES.append('BVTK_NT_BlankStructuredGrid' )


# --------------------------------------------------------------


class BVTK_NT_OBBDicer(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_OBBDicer'
    bl_label = 'vtkOBBDicer'
    e_DiceMode_items = [(x, x, x) for x in ['MemoryLimitPerPiece', 'NumberOfPointsPerPiece', 'SpecifiedNumberOfPieces']]
    
    e_DiceMode = bpy.props.EnumProperty(name='DiceMode', description='Specify the method to determine how many pieces the data should be broken into. By default, the number of points per piece is used', default='NumberOfPointsPerPiece', items=e_DiceMode_items)
    m_FieldData = bpy.props.BoolProperty(name='FieldData', description='Set/Get the flag which controls whether to generate point scalar data or point field data. If this flag is off, scalar data is generated. Otherwise, field data is generated. Note that the generated the data are integer numbers indicating which piece a particular point belongs to', default=True)
    m_MemoryLimit = bpy.props.IntProperty(name='MemoryLimit', description='Control piece size based on a memory limit. (This ivar has effect only when the DiceMode is set to SetDiceModeToMemoryLimit()). The memory limit should be set in kibibytes (1024 bytes)', default=51200)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Set/Get the number of pieces the object is to be separated into. (This ivar has effect only when the DiceMode is set to SetDiceModeToSpecifiedNumber()). Note that the ivar NumberOfPieces is a target - depending on the particulars of the data, more or less number of pieces than the target value may be created', default=10)
    m_NumberOfPointsPerPiece = bpy.props.IntProperty(name='NumberOfPointsPerPiece', description='Control piece size based on the maximum number of points per piece. (This ivar has effect only when the DiceMode is set to SetDiceModeToNumberOfPoints().', default=5000)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DiceMode', 'm_FieldData', 'm_MemoryLimit', 'm_NumberOfPieces', 'm_NumberOfPointsPerPiece', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_OBBDicer)
TYPENAMES.append('BVTK_NT_OBBDicer' )


# --------------------------------------------------------------


class BVTK_NT_ImageCursor3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageCursor3D'
    bl_label = 'vtkImageCursor3D'
    
    m_CursorPosition = bpy.props.FloatVectorProperty(name='CursorPosition', description='', default=[0.0, 0.0, 0.0], size=3)
    m_CursorRadius = bpy.props.IntProperty(name='CursorRadius', description='Sets/Gets the radius of the cursor. The radius determines how far the axis lines project out from the cursors center', default=5)
    m_CursorValue = bpy.props.FloatProperty(name='CursorValue', description='Sets/Gets what pixel value to draw the cursor in', default=255.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CursorPosition', 'm_CursorRadius', 'm_CursorValue', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageCursor3D)
TYPENAMES.append('BVTK_NT_ImageCursor3D' )


# --------------------------------------------------------------


class BVTK_NT_ImageMapToColors(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMapToColors'
    bl_label = 'vtkImageMapToColors'
    e_OutputFormat_items = [(x, x, x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_ActiveComponent = bpy.props.IntProperty(name='ActiveComponent', description='Set the component to map for multi-component images (default: 0', default=0)
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NaNColor = bpy.props.IntVectorProperty(name='NaNColor', description='', default=[0, 0, 0, 0], size=4)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_OutputFormat = bpy.props.EnumProperty(name='OutputFormat', description='Set the output format, the default is RGBA', default='RGBA', items=e_OutputFormat_items)
    m_PassAlphaToOutput = bpy.props.BoolProperty(name='PassAlphaToOutput', description='Use the alpha component of the input when computing the alpha component of the output (useful when converting monochrome+alpha data to RGBA', default=True)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ActiveComponent', 'm_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NaNColor', 'm_NumberOfThreads', 'e_OutputFormat', 'm_PassAlphaToOutput', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['LookupTable'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMapToColors)
TYPENAMES.append('BVTK_NT_ImageMapToColors' )


# --------------------------------------------------------------


class BVTK_NT_MergeFields(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MergeFields'
    bl_label = 'vtkMergeFields'
    
    m_NumberOfComponents = bpy.props.IntProperty(name='NumberOfComponents', description='Set the number of the components in the output field. This has to be set before execution. Default value is 0', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NumberOfComponents', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MergeFields)
TYPENAMES.append('BVTK_NT_MergeFields' )


# --------------------------------------------------------------


class BVTK_NT_QuadricDecimation(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_QuadricDecimation'
    bl_label = 'vtkQuadricDecimation'
    
    m_AttributeErrorMetric = bpy.props.BoolProperty(name='AttributeErrorMetric', description='Decide whether to include data attributes in the error metric. If off, then only geometric error is used to control the decimation. By default the attribute errors are off', default=True)
    m_NormalsAttribute = bpy.props.BoolProperty(name='NormalsAttribute', description='If attribute errors are to be included in the metric (i.e., AttributeErrorMetric is on), then the following flags control which attributes are to be included in the error calculation. By default all of these are on', default=True)
    m_NormalsWeight = bpy.props.FloatProperty(name='NormalsWeight', description='Set/Get the scaling weight contribution of the attribute. These values are used to weight the contribution of the attributes towards the error metric', default=0.1)
    m_ScalarsAttribute = bpy.props.BoolProperty(name='ScalarsAttribute', description='If attribute errors are to be included in the metric (i.e., AttributeErrorMetric is on), then the following flags control which attributes are to be included in the error calculation. By default all of these are on', default=True)
    m_ScalarsWeight = bpy.props.FloatProperty(name='ScalarsWeight', description='Set/Get the scaling weight contribution of the attribute. These values are used to weight the contribution of the attributes towards the error metric', default=0.1)
    m_TCoordsAttribute = bpy.props.BoolProperty(name='TCoordsAttribute', description='If attribute errors are to be included in the metric (i.e., AttributeErrorMetric is on), then the following flags control which attributes are to be included in the error calculation. By default all of these are on', default=True)
    m_TCoordsWeight = bpy.props.FloatProperty(name='TCoordsWeight', description='Set/Get the scaling weight contribution of the attribute. These values are used to weight the contribution of the attributes towards the error metric', default=0.1)
    m_TargetReduction = bpy.props.FloatProperty(name='TargetReduction', description='Set/Get the desired reduction (expressed as a fraction of the original number of triangles). The actual reduction may be less depending on triangulation and topological constraints', default=0.9)
    m_TensorsAttribute = bpy.props.BoolProperty(name='TensorsAttribute', description='If attribute errors are to be included in the metric (i.e., AttributeErrorMetric is on), then the following flags control which attributes are to be included in the error calculation. By default all of these are on', default=True)
    m_TensorsWeight = bpy.props.FloatProperty(name='TensorsWeight', description='Set/Get the scaling weight contribution of the attribute. These values are used to weight the contribution of the attributes towards the error metric', default=0.1)
    m_VectorsAttribute = bpy.props.BoolProperty(name='VectorsAttribute', description='If attribute errors are to be included in the metric (i.e., AttributeErrorMetric is on), then the following flags control which attributes are to be included in the error calculation. By default all of these are on', default=True)
    m_VectorsWeight = bpy.props.FloatProperty(name='VectorsWeight', description='Set/Get the scaling weight contribution of the attribute. These values are used to weight the contribution of the attributes towards the error metric', default=0.1)
    m_VolumePreservation = bpy.props.BoolProperty(name='VolumePreservation', description='Decide whether to activate volume preservation which greatly reduces errors in triangle normal direction. If off, volume preservation is disabled and if AttributeErrorMetric is active, these errors can be large. By default VolumePreservation is off the attribute errors are off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AttributeErrorMetric', 'm_NormalsAttribute', 'm_NormalsWeight', 'm_ScalarsAttribute', 'm_ScalarsWeight', 'm_TCoordsAttribute', 'm_TCoordsWeight', 'm_TargetReduction', 'm_TensorsAttribute', 'm_TensorsWeight', 'm_VectorsAttribute', 'm_VectorsWeight', 'm_VolumePreservation', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_QuadricDecimation)
TYPENAMES.append('BVTK_NT_QuadricDecimation' )


# --------------------------------------------------------------


class BVTK_NT_ShrinkPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ShrinkPolyData'
    bl_label = 'vtkShrinkPolyData'
    
    m_ShrinkFactor = bpy.props.FloatProperty(name='ShrinkFactor', description='Set the fraction of shrink for each cell', default=0.5)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ShrinkFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ShrinkPolyData)
TYPENAMES.append('BVTK_NT_ShrinkPolyData' )


# --------------------------------------------------------------


class BVTK_NT_PReflectionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PReflectionFilter'
    bl_label = 'vtkPReflectionFilter'
    e_Plane_items = [(x, x, x) for x in ['X', 'XMax', 'XMin', 'Y', 'YMax', 'YMin', 'Z', 'ZMax', 'ZMin']]
    
    m_Center = bpy.props.FloatProperty(name='Center', description='If the reflection plane is set to X, Y or Z, this variable is use to set the position of the plane', default=0.0)
    m_CopyInput = bpy.props.BoolProperty(name='CopyInput', description='If on (the default), copy the input geometry to the output. If off, the output will only contain the reflection', default=True)
    m_FlipAllInputArrays = bpy.props.BoolProperty(name='FlipAllInputArrays', description="If off (the default), only Vectors, Normals and Tensors will be flipped. If on, all 3-component data arrays ( considered as 3D vectors), 6-component data arrays (considered as symmetric tensors), 9-component data arrays (considered as tensors ) of signed type will be flipped. All other won't be flipped and will only be copied", default=False)
    e_Plane = bpy.props.EnumProperty(name='Plane', description='Set the normal of the plane to use as mirror', default='XMin', items=e_Plane_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_CopyInput', 'm_FlipAllInputArrays', 'e_Plane', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PReflectionFilter)
TYPENAMES.append('BVTK_NT_PReflectionFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractVOI(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractVOI'
    bl_label = 'vtkExtractVOI'
    
    m_IncludeBoundary = bpy.props.BoolProperty(name='IncludeBoundary', description='Control whether to enforce that the "boundary" of the grid is output in the subsampling process. (This ivar only has effect when the SampleRate in any direction is not equal to 1.) When this ivar IncludeBoundary is on, the subsampling will always include the boundary of the grid even though the sample rate is not an even multiple of the grid dimensions. (By default IncludeBoundary is off.', default=True)
    m_SampleRate = bpy.props.IntVectorProperty(name='SampleRate', description='Set the sampling rate in the i, j, and k directions. If the rate is > 1, then the resulting VOI will be subsampled representation of the input. For example, if the SampleRate=(2,2,2), every other point will be selected, resulting in a volume 1/8th the original size', default=[1, 1, 1], size=3)
    m_VOI = bpy.props.IntVectorProperty(name='VOI', description='Specify i-j-k (min,max) pairs to extract. The resulting structured points dataset can be of any topological dimension (i.e., point, line, image, or volume)', default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_IncludeBoundary', 'm_SampleRate', 'm_VOI', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractVOI)
TYPENAMES.append('BVTK_NT_ExtractVOI' )


# --------------------------------------------------------------


class BVTK_NT_UniformGridAMRAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_UniformGridAMRAlgorithm'
    bl_label = 'vtkUniformGridAMRAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_UniformGridAMRAlgorithm)
TYPENAMES.append('BVTK_NT_UniformGridAMRAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_ImageSpatialAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageSpatialAlgorithm'
    bl_label = 'vtkImageSpatialAlgorithm'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageSpatialAlgorithm)
TYPENAMES.append('BVTK_NT_ImageSpatialAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_TextureMapToCylinder(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TextureMapToCylinder'
    bl_label = 'vtkTextureMapToCylinder'
    
    m_AutomaticCylinderGeneration = bpy.props.BoolProperty(name='AutomaticCylinderGeneration', description='Turn on/off automatic cylinder generation. This means it automatically finds the cylinder center and axis', default=True)
    m_Point1 = bpy.props.FloatVectorProperty(name='Point1', description='Specify the first point defining the cylinder axis', default=[0.0, 0.0, -0.5], size=3)
    m_Point2 = bpy.props.FloatVectorProperty(name='Point2', description='Specify the second point defining the cylinder axis', default=[0.0, 0.0, 0.5], size=3)
    m_PreventSeam = bpy.props.BoolProperty(name='PreventSeam', description='Control how the texture coordinates are generated. If PreventSeam is set, the s-coordinate ranges from 0->1 and 1->0 corresponding to the angle variation from 0->180 and 180->0. Otherwise, the s-coordinate ranges from 0->1 from 0->360 degrees', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutomaticCylinderGeneration', 'm_Point1', 'm_Point2', 'm_PreventSeam', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TextureMapToCylinder)
TYPENAMES.append('BVTK_NT_TextureMapToCylinder' )


# --------------------------------------------------------------


class BVTK_NT_DensifyPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DensifyPolyData'
    bl_label = 'vtkDensifyPolyData'
    
    m_NumberOfSubdivisions = bpy.props.IntProperty(name='NumberOfSubdivisions', description='Number of recursive subdivisions. Initial value is 1', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NumberOfSubdivisions', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DensifyPolyData)
TYPENAMES.append('BVTK_NT_DensifyPolyData' )


# --------------------------------------------------------------


class BVTK_NT_RearrangeFields(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RearrangeFields'
    bl_label = 'vtkRearrangeFields'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RearrangeFields)
TYPENAMES.append('BVTK_NT_RearrangeFields' )


# --------------------------------------------------------------


class BVTK_NT_AppendPolyData(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AppendPolyData'
    bl_label = 'vtkAppendPolyData'
    
    m_ParallelStreaming = bpy.props.BoolProperty(name='ParallelStreaming', description='ParallelStreaming is for a particular application. It causes this filter to ask for a different piece from each of its inputs. If all the inputs are the same, then the output of this append filter is the whole dataset pieced back together. Duplicate points are create along the seams. The purpose of this feature is to get data parallelism at a course scale. Each of the inputs can be generated in a different process at the same time', default=True)
    m_UserManagedInputs = bpy.props.BoolProperty(name='UserManagedInputs', description='UserManagedInputs allows the user to set inputs by number instead of using the AddInput/RemoveInput functions. Calls to SetNumberOfInputs/SetInputConnectionByNumber should not be mixed with calls to AddInput/RemoveInput. By default, UserManagedInputs is false', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ParallelStreaming', 'm_UserManagedInputs', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AppendPolyData)
TYPENAMES.append('BVTK_NT_AppendPolyData' )


# --------------------------------------------------------------


class BVTK_NT_TriangleFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TriangleFilter'
    bl_label = 'vtkTriangleFilter'
    
    m_PassLines = bpy.props.BoolProperty(name='PassLines', description='Turn on/off passing lines through filter (default: on). If this is on, then the input polylines will be broken into line segments. If it is off, then the input lines will be ignored and the output will have no lines', default=True)
    m_PassVerts = bpy.props.BoolProperty(name='PassVerts', description='Turn on/off passing vertices through filter (default: on). If this is on, then the input vertex cells will be broken into individual vertex cells (one point per cell). If it is off, the input vertex cells will be ignored', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PassLines', 'm_PassVerts', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TriangleFilter)
TYPENAMES.append('BVTK_NT_TriangleFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageCityBlockDistance(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageCityBlockDistance'
    bl_label = 'vtkImageCityBlockDistance'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Dimensionality is the number of axes which are considered during execution. To process images dimensionality would be set to 2', default=3)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageCityBlockDistance)
TYPENAMES.append('BVTK_NT_ImageCityBlockDistance' )


# --------------------------------------------------------------


class BVTK_NT_SelectionAlgorithm(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SelectionAlgorithm'
    bl_label = 'vtkSelectionAlgorithm'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SelectionAlgorithm)
TYPENAMES.append('BVTK_NT_SelectionAlgorithm' )


# --------------------------------------------------------------


class BVTK_NT_ImageSeparableConvolution(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageSeparableConvolution'
    bl_label = 'vtkImageSeparableConvolution'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Dimensionality is the number of axes which are considered during execution. To process images dimensionality would be set to 2', default=3)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['XKernel', 'YKernel', 'ZKernel'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageSeparableConvolution)
TYPENAMES.append('BVTK_NT_ImageSeparableConvolution' )


# --------------------------------------------------------------


class BVTK_NT_QuadraturePointsGenerator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_QuadraturePointsGenerator'
    bl_label = 'vtkQuadraturePointsGenerator'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_QuadraturePointsGenerator)
TYPENAMES.append('BVTK_NT_QuadraturePointsGenerator' )


# --------------------------------------------------------------


class BVTK_NT_ImageCacheFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageCacheFilter'
    bl_label = 'vtkImageCacheFilter'
    
    m_CacheSize = bpy.props.IntProperty(name='CacheSize', description='This is the maximum number of images that can be retained in memory. it defaults to 10', default=10)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CacheSize', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageCacheFilter)
TYPENAMES.append('BVTK_NT_ImageCacheFilter' )


# --------------------------------------------------------------


class BVTK_NT_RuledSurfaceFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RuledSurfaceFilter'
    bl_label = 'vtkRuledSurfaceFilter'
    e_RuledMode_items = [(x, x, x) for x in ['PointWalk', 'Resample']]
    
    m_CloseSurface = bpy.props.BoolProperty(name='CloseSurface', description='Indicate whether the surface is to be closed. If this boolean is on, then the first and last polyline are used to generate a stripe that closes the surface. (Note: to close the surface in the other direction, repeat the first point in the polyline as the last point in the polyline.', default=True)
    m_DistanceFactor = bpy.props.FloatProperty(name='DistanceFactor', description='Set/Get the factor that controls tearing of the surface', default=3.0)
    m_Offset = bpy.props.IntProperty(name='Offset', description='Control the striping of the ruled surface. The offset sets the first stripe that is visible. Offset is generally used with OnRatio to create nifty striping effects', default=0)
    m_OnRatio = bpy.props.IntProperty(name='OnRatio', description='Control the striping of the ruled surface. If OnRatio is greater than 1, then every nth strip is turned on, beginning with the Offset strip', default=1)
    m_OrientLoops = bpy.props.BoolProperty(name='OrientLoops', description='Indicate whether the starting points of the loops need to be determined. If set to 0, then its assumes that the 0th point of each loop should be always connected By default the loops are not oriented', default=True)
    m_PassLines = bpy.props.BoolProperty(name='PassLines', description='Indicate whether the generating lines are to be passed to the output. By default lines are not passed to the output', default=True)
    m_Resolution = bpy.props.IntVectorProperty(name='Resolution', description='If the ruled surface generation mode is RESAMPLE, then these parameters are used to determine the resample rate. Resolution[0] defines the resolution in the direction of the polylines; Resolution[1] defines the resolution across the polylines (i.e., direction orthogonal to Resolution[0])', default=[1, 1], size=2)
    e_RuledMode = bpy.props.EnumProperty(name='RuledMode', description='Set the mode by which to create the ruled surface. (Dramatically different results are possible depending on the chosen mode.) The resample mode evenly resamples the polylines (based on length) and generates triangle strips. The point walk mode uses the existing points and walks around the polyline using existing points', default='Resample', items=e_RuledMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CloseSurface', 'm_DistanceFactor', 'm_Offset', 'm_OnRatio', 'm_OrientLoops', 'm_PassLines', 'm_Resolution', 'e_RuledMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RuledSurfaceFilter)
TYPENAMES.append('BVTK_NT_RuledSurfaceFilter' )


# --------------------------------------------------------------


class BVTK_NT_GridSynchronizedTemplates3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GridSynchronizedTemplates3D'
    bl_label = 'vtkGridSynchronizedTemplates3D'
    
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_GenerateTriangles = bpy.props.BoolProperty(name='GenerateTriangles', description='If this is enabled (by default), the output will be triangles otherwise, the output will be the intersection polygon', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Set the number of contours to place into the list. You only really need to use this method to reduce list size. The method SetValue() will automatically increase list size as needed', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_GenerateTriangles', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GridSynchronizedTemplates3D)
TYPENAMES.append('BVTK_NT_GridSynchronizedTemplates3D' )


# --------------------------------------------------------------


class BVTK_NT_MeshQuality(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MeshQuality'
    bl_label = 'vtkMeshQuality'
    e_HexQualityMeasure_items = [(x, x, x) for x in ['Condition', 'Diagonal', 'Dimension', 'Distortion', 'EdgeRatio', 'Jacobian', 'MaxAspectFrobenius', 'MaxEdgeRatios', 'MedAspectFrobenius', 'Oddy', 'RelativeSizeSquared', 'ScaledJacobian', 'Shape', 'ShapeAndSize', 'Shear', 'ShearAndSize', 'Skew', 'Stretch', 'Taper', 'Volume']]
    e_QuadQualityMeasure_items = [(x, x, x) for x in ['Area', 'AspectRatio', 'Condition', 'Distortion', 'EdgeRatio', 'Jacobian', 'MaxAngle', 'MaxAspectFrobenius', 'MaxEdgeRatios', 'MedAspectFrobenius', 'MinAngle', 'Oddy', 'RadiusRatio', 'RelativeSizeSquared', 'ScaledJacobian', 'Shape', 'ShapeAndSize', 'Shear', 'ShearAndSize', 'Skew', 'Stretch', 'Taper', 'Warpage']]
    e_TetQualityMeasure_items = [(x, x, x) for x in ['AspectBeta', 'AspectFrobenius', 'AspectGamma', 'AspectRatio', 'CollapseRatio', 'Condition', 'Distortion', 'EdgeRatio', 'Jacobian', 'MinAngle', 'RadiusRatio', 'RelativeSizeSquared', 'ScaledJacobian', 'Shape', 'ShapeAndSize', 'Volume']]
    e_TriangleQualityMeasure_items = [(x, x, x) for x in ['Area', 'AspectFrobenius', 'AspectRatio', 'Condition', 'Distortion', 'EdgeRatio', 'MaxAngle', 'MinAngle', 'RadiusRatio', 'RelativeSizeSquared', 'ScaledJacobian', 'Shape', 'ShapeAndSize']]
    
    m_CompatibilityMode = bpy.props.BoolProperty(name='CompatibilityMode', description='CompatibilityMode governs whether, when both a quality function and cell volume are to be stored as cell data, the two values are stored in a single array. When compatibility mode is off (the default), two separate arrays are used -- one labeled "Quality" and the other labeled "Volume". When compatibility mode is on, both values are stored in a single array, with volume as the first component and quality as the second component', default=True)
    e_HexQualityMeasure = bpy.props.EnumProperty(name='HexQualityMeasure', description='Set/Get the particular estimator used to measure the quality of hexahedra. The default is VTK_QUALITY_MAX_ASPECT_FROBENIUS and valid values also include VTK_QUALITY_EDGE_RATIO, VTK_QUALITY_MAX_ASPECT_FROBENIUS, VTK_QUALITY_MAX_EDGE_RATIO, VTK_QUALITY_SKEW, VTK_QUALITY_TAPER, VTK_QUALITY_VOLUME, VTK_QUALITY_STRETCH, VTK_QUALITY_DIAGONAL, VTK_QUALITY_DIMENSION, VTK_QUALITY_ODDY, VTK_QUALITY_CONDITION, VTK_QUALITY_JACOBIAN, VTK_QUALITY_SCALED_JACOBIAN, VTK_QUALITY_SHEAR, VTK_QUALITY_SHAPE, VTK_QUALITY_RELATIVE_SIZE_SQUARED, VTK_QUALITY_SHAPE_AND_SIZE, VTK_QUALITY_SHEAR_AND_SIZE, and VTK_QUALITY_DISTORTION', default='MaxAspectFrobenius', items=e_HexQualityMeasure_items)
    e_QuadQualityMeasure = bpy.props.EnumProperty(name='QuadQualityMeasure', description='Set/Get the particular estimator used to measure the quality of quadrilaterals. The default is VTK_QUALITY_EDGE_RATIO and valid values also include VTK_QUALITY_RADIUS_RATIO, VTK_QUALITY_ASPECT_RATIO, VTK_QUALITY_MAX_EDGE_RATIO VTK_QUALITY_SKEW, VTK_QUALITY_TAPER, VTK_QUALITY_WARPAGE, VTK_QUALITY_AREA, VTK_QUALITY_STRETCH, VTK_QUALITY_MIN_ANGLE, VTK_QUALITY_MAX_ANGLE, VTK_QUALITY_ODDY, VTK_QUALITY_CONDITION, VTK_QUALITY_JACOBIAN, VTK_QUALITY_SCALED_JACOBIAN, VTK_QUALITY_SHEAR, VTK_QUALITY_SHAPE, VTK_QUALITY_RELATIVE_SIZE_SQUARED, VTK_QUALITY_SHAPE_AND_SIZE, VTK_QUALITY_SHEAR_AND_SIZE, and VTK_QUALITY_DISTORTION', default='EdgeRatio', items=e_QuadQualityMeasure_items)
    m_Ratio = bpy.props.BoolProperty(name='Ratio', description='These methods are deprecated. Use Get/SetSaveCellQuality() instead', default=True)
    m_SaveCellQuality = bpy.props.BoolProperty(name='SaveCellQuality', description='This variable controls whether or not cell quality is stored as cell data in the resulting mesh or discarded (leaving only the aggregate quality average of the entire mesh, recorded in the FieldData)', default=True)
    e_TetQualityMeasure = bpy.props.EnumProperty(name='TetQualityMeasure', description="Set/Get the particular estimator used to measure the quality of tetrahedra. The default is VTK_QUALITY_RADIUS_RATIO (identical to Verdict's aspect ratio beta) and valid values also include VTK_QUALITY_ASPECT_RATIO, VTK_QUALITY_ASPECT_FROBENIUS, VTK_QUALITY_EDGE_RATIO, VTK_QUALITY_COLLAPSE_RATIO, VTK_QUALITY_ASPECT_BETA, VTK_QUALITY_ASPECT_GAMMA, VTK_QUALITY_VOLUME, VTK_QUALITY_CONDITION, VTK_QUALITY_JACOBIAN, VTK_QUALITY_SCALED_JACOBIAN, VTK_QUALITY_SHAPE, VTK_QUALITY_RELATIVE_SIZE_SQUARED, VTK_QUALITY_SHAPE_AND_SIZE, and VTK_QUALITY_DISTORTION", default='AspectRatio', items=e_TetQualityMeasure_items)
    e_TriangleQualityMeasure = bpy.props.EnumProperty(name='TriangleQualityMeasure', description='Set/Get the particular estimator used to function the quality of triangles. The default is VTK_QUALITY_RADIUS_RATIO and valid values also include VTK_QUALITY_ASPECT_RATIO, VTK_QUALITY_ASPECT_FROBENIUS, and VTK_QUALITY_EDGE_RATIO, VTK_QUALITY_MIN_ANGLE, VTK_QUALITY_MAX_ANGLE, VTK_QUALITY_CONDITION, VTK_QUALITY_SCALED_JACOBIAN, VTK_QUALITY_RELATIVE_SIZE_SQUARED, VTK_QUALITY_SHAPE, VTK_QUALITY_SHAPE_AND_SIZE, and VTK_QUALITY_DISTORTION', default='AspectRatio', items=e_TriangleQualityMeasure_items)
    m_Volume = bpy.props.BoolProperty(name='Volume', description='These methods are deprecated. The functionality of computing cell volume is being removed until it can be computed for any 3D cell. (The previous implementation only worked for tetrahedra.', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CompatibilityMode', 'e_HexQualityMeasure', 'e_QuadQualityMeasure', 'm_Ratio', 'm_SaveCellQuality', 'e_TetQualityMeasure', 'e_TriangleQualityMeasure', 'm_Volume', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MeshQuality)
TYPENAMES.append('BVTK_NT_MeshQuality' )


# --------------------------------------------------------------


class BVTK_NT_ProteinRibbonFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProteinRibbonFilter'
    bl_label = 'vtkProteinRibbonFilter'
    
    m_CoilWidth = bpy.props.FloatProperty(name='CoilWidth', description='Width of the ribbon coil. Default is 0.3', default=0.30000001192092896)
    m_DrawSmallMoleculesAsSpheres = bpy.props.BoolProperty(name='DrawSmallMoleculesAsSpheres', description='If enabled, small molecules (HETATMs) are drawn as spheres. Default is true', default=True)
    m_HelixWidth = bpy.props.FloatProperty(name='HelixWidth', description='Width of the helix part of the ribbon. Default is 1.3', default=1.2999999523162842)
    m_SphereResolution = bpy.props.IntProperty(name='SphereResolution', description='Resolution of the spheres for small molecules. Default is 20', default=20)
    m_SubdivideFactor = bpy.props.IntProperty(name='SubdivideFactor', description='Smoothing factor of the ribbon. Default is 20', default=20)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CoilWidth', 'm_DrawSmallMoleculesAsSpheres', 'm_HelixWidth', 'm_SphereResolution', 'm_SubdivideFactor', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProteinRibbonFilter)
TYPENAMES.append('BVTK_NT_ProteinRibbonFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageSeedConnectivity(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageSeedConnectivity'
    bl_label = 'vtkImageSeedConnectivity'
    
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Set the number of axes to use in connectivity', default=3)
    m_InputConnectValue = bpy.props.IntProperty(name='InputConnectValue', description='Set/Get what value is considered as connecting pixels', default=255)
    m_OutputConnectedValue = bpy.props.IntProperty(name='OutputConnectedValue', description='Set/Get the value to set connected pixels to', default=255)
    m_OutputUnconnectedValue = bpy.props.IntProperty(name='OutputUnconnectedValue', description='Set/Get the value to set unconnected pixels to', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Dimensionality', 'm_InputConnectValue', 'm_OutputConnectedValue', 'm_OutputUnconnectedValue', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageSeedConnectivity)
TYPENAMES.append('BVTK_NT_ImageSeedConnectivity' )


# --------------------------------------------------------------


class BVTK_NT_ExtractRectilinearGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractRectilinearGrid'
    bl_label = 'vtkExtractRectilinearGrid'
    
    m_IncludeBoundary = bpy.props.BoolProperty(name='IncludeBoundary', description='Control whether to enforce that the "boundary" of the grid is output in the subsampling process. (This ivar only has effect when the SampleRate in any direction is not equal to 1.) When this ivar IncludeBoundary is on, the subsampling will always include the boundary of the grid even though the sample rate is not an even multiple of the grid dimensions. (By default IncludeBoundary is off.', default=True)
    m_SampleRate = bpy.props.IntVectorProperty(name='SampleRate', description='Set the sampling rate in the i, j, and k directions. If the rate is > 1, then the resulting VOI will be subsampled representation of the input. For example, if the SampleRate=(2,2,2), every other point will be selected, resulting in a volume 1/8th the original size. Initial value is (1,1,1)', default=[1, 1, 1], size=3)
    m_VOI = bpy.props.IntVectorProperty(name='VOI', description='Specify i-j-k (min,max) pairs to extract. The resulting structured grid dataset can be of any topological dimension (i.e., point, line, plane, or 3D grid)', default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_IncludeBoundary', 'm_SampleRate', 'm_VOI', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractRectilinearGrid)
TYPENAMES.append('BVTK_NT_ExtractRectilinearGrid' )


# --------------------------------------------------------------


class BVTK_NT_ImageMagnify(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMagnify'
    bl_label = 'vtkImageMagnify'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_Interpolate = bpy.props.BoolProperty(name='Interpolate', description='Turn interpolation on and off (pixel replication is used when off). Initially, interpolation is off', default=True)
    m_MagnificationFactors = bpy.props.IntVectorProperty(name='MagnificationFactors', description='', default=[1, 1, 1], size=3)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_Interpolate', 'm_MagnificationFactors', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMagnify)
TYPENAMES.append('BVTK_NT_ImageMagnify' )


# --------------------------------------------------------------


class BVTK_NT_ImageEuclideanToPolar(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageEuclideanToPolar'
    bl_label = 'vtkImageEuclideanToPolar'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    m_ThetaMaximum = bpy.props.FloatProperty(name='ThetaMaximum', description='Theta is an angle. Maximum specifies when it maps back to 0. ThetaMaximum defaults to 255 instead of 2PI, because unsigned char is expected as input. The output type must be the same as input type', default=255.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', 'm_ThetaMaximum', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageEuclideanToPolar)
TYPENAMES.append('BVTK_NT_ImageEuclideanToPolar' )


# --------------------------------------------------------------


class BVTK_NT_EdgePoints(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EdgePoints'
    bl_label = 'vtkEdgePoints'
    
    m_Value = bpy.props.FloatProperty(name='Value', description='Set/get the contour value', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Value', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EdgePoints)
TYPENAMES.append('BVTK_NT_EdgePoints' )


# --------------------------------------------------------------


class BVTK_NT_TransmitStructuredGridPiece(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransmitStructuredGridPiece'
    bl_label = 'vtkTransmitStructuredGridPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty(name='CreateGhostCells', description='Turn on/off creating ghost cells (on by default)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CreateGhostCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransmitStructuredGridPiece)
TYPENAMES.append('BVTK_NT_TransmitStructuredGridPiece' )


# --------------------------------------------------------------


class BVTK_NT_SphereTreeFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SphereTreeFilter'
    bl_label = 'vtkSphereTreeFilter'
    e_ExtractionMode_items = [(x, x, x) for x in ['Levels', 'Line', 'Plane', 'Point']]
    
    e_ExtractionMode = bpy.props.EnumProperty(name='ExtractionMode', description='Specify what information this filter is to extract from the sphere tree. Options include: spheres that make up one or more levels; spheres that intersect a specified plane; spheres that intersect a specified line; and spheres that intersect a specified point. What is extracted are sphere centers, a radius, and an optional level. By default the specified levels are extracted', default='Levels', items=e_ExtractionMode_items)
    m_Level = bpy.props.IntProperty(name='Level', description='Specify the level of the tree to extract (used when ExtractionMode is set to Levels). A value of (-1) means all levels. Note that level 0 is the root of the sphere tree. By default all levels are extracted. Note that if TreeHierarchy is off, then it is only possible to extract leaf spheres (i.e., spheres for each cell of the associated dataset)', default=-1)
    m_Normal = bpy.props.FloatVectorProperty(name='Normal', description='Specify a plane used to extract spheres (used when ExtractionMode is set to Plane). The plane Normal plus Point define an infinite plane', default=[0.0, 0.0, 1.0], size=3)
    m_Point = bpy.props.FloatVectorProperty(name='Point', description='Specify a point used to extract one or more leaf spheres. This method is used when extracting spheres using a point, line, or plane', default=[0.0, 0.0, 0.0], size=3)
    m_Ray = bpy.props.FloatVectorProperty(name='Ray', description='Specify a line used to extract spheres (used when ExtractionMode is set to Line). The Ray plus Point define an infinite line. The ray is a vector defining the direction of the line', default=[1.0, 0.0, 0.0], size=3)
    m_TreeHierarchy = bpy.props.BoolProperty(name='TreeHierarchy', description='Enable or disable the building and generation of the sphere tree hierarchy. The hierarchy represents different levels in the tree and enables rapid traversal of the tree', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ExtractionMode', 'm_Level', 'm_Normal', 'm_Point', 'm_Ray', 'm_TreeHierarchy', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['SphereTree'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SphereTreeFilter)
TYPENAMES.append('BVTK_NT_SphereTreeFilter' )


# --------------------------------------------------------------


class BVTK_NT_FillHolesFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FillHolesFilter'
    bl_label = 'vtkFillHolesFilter'
    
    m_HoleSize = bpy.props.FloatProperty(name='HoleSize', description='Specify the maximum hole size to fill. This is represented as a radius to the bounding circumsphere containing the hole. Note that this is an approximate area; the actual area cannot be computed without first triangulating the hole', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_HoleSize', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FillHolesFilter)
TYPENAMES.append('BVTK_NT_FillHolesFilter' )


# --------------------------------------------------------------


class BVTK_NT_StrahlerMetric(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StrahlerMetric'
    bl_label = 'vtkStrahlerMetric'
    
    m_Normalize = bpy.props.BoolProperty(name='Normalize', description='Set/get setting of normalize flag. If this is set, the Strahler values are scaled into the range [0..1]. Default is for normalization to be OFF', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Normalize', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StrahlerMetric)
TYPENAMES.append('BVTK_NT_StrahlerMetric' )


# --------------------------------------------------------------


class BVTK_NT_ArrayCalculator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ArrayCalculator'
    bl_label = 'vtkArrayCalculator'
    e_AttributeType_items = [(x, x, x) for x in ['CellData', 'Default', 'EdgeData', 'PointData', 'RowData', 'VertexData']]
    
    e_AttributeType = bpy.props.EnumProperty(name='AttributeType', description="Control which AttributeType the filter operates on (point data or cell data for vtkDataSets). By default the filter uses Point/Vertex/Row data depending on the input data type. The input value for this function should be one of the constants in vtkDataObject::AttributeTypes or DEFAULT_ATTRIBUTE_TYPE for 'default behavior'", default='Default', items=e_AttributeType_items)
    m_CoordinateResults = bpy.props.BoolProperty(name='CoordinateResults', description="Set whether to output results as coordinates. ResultArrayName will be ignored. Outputing as coordinates is only valid with vector results and if the AttributeMode is AttributeModeToUsePointData. If a valid output can't be made, an error will occur", default=True)
    m_Function = bpy.props.StringProperty(name='Function', description='Set/Get the function to be evaluated')
    m_ReplaceInvalidValues = bpy.props.BoolProperty(name='ReplaceInvalidValues', description='When ReplaceInvalidValues is on, all invalid values (such as sqrt(-2), note that function parser does not handle complex numbers) will be replaced by ReplacementValue. Otherwise an error will be reporte', default=True)
    m_ReplacementValue = bpy.props.FloatProperty(name='ReplacementValue', description='When ReplaceInvalidValues is on, all invalid values (such as sqrt(-2), note that function parser does not handle complex numbers) will be replaced by ReplacementValue. Otherwise an error will be reporte', default=0.0)
    m_ResultArrayName = bpy.props.StringProperty(name='ResultArrayName', description='Set the name of the array in which to store the result of evaluating this function. If this is the name of an existing array, that array will be overwritten. Otherwise a new array will be created with the specified name', default='resultArray')
    m_ResultArrayType = bpy.props.IntProperty(name='ResultArrayType', description='Type of the result array. It is ignored if CoordinateResults is true. Initial value is VTK_DOUBLE', default=11)
    m_ResultNormals = bpy.props.BoolProperty(name='ResultNormals', description='Set whether to output results as point/cell normals. Outputing as normals is only valid with vector results. Point or cell normals are selected using AttributeMode', default=False)
    m_ResultTCoords = bpy.props.BoolProperty(name='ResultTCoords', description='Set whether to output results as point/cell texture coordinates. Point or cell texture coordinates are selected using AttributeMode. 2-component texture coordinates cannot be generated at this time', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_AttributeType', 'm_CoordinateResults', 'm_Function', 'm_ReplaceInvalidValues', 'm_ReplacementValue', 'm_ResultArrayName', 'm_ResultArrayType', 'm_ResultNormals', 'm_ResultTCoords', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ArrayCalculator)
TYPENAMES.append('BVTK_NT_ArrayCalculator' )


# --------------------------------------------------------------


class BVTK_NT_ProcrustesAlignmentFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProcrustesAlignmentFilter'
    bl_label = 'vtkProcrustesAlignmentFilter'
    
    m_StartFromCentroid = bpy.props.BoolProperty(name='StartFromCentroid', description='When on, the initial alignment is to the centroid of the cohort curves. When off, the alignment is to the centroid of the first input. Default is off for backward compatibility', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_StartFromCentroid', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProcrustesAlignmentFilter)
TYPENAMES.append('BVTK_NT_ProcrustesAlignmentFilter' )


# --------------------------------------------------------------


class BVTK_NT_DataSetToDataObjectFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataSetToDataObjectFilter'
    bl_label = 'vtkDataSetToDataObjectFilter'
    
    m_CellData = bpy.props.BoolProperty(name='CellData', description='Turn on/off the conversion of dataset cell data to a data object', default=True)
    m_FieldData = bpy.props.BoolProperty(name='FieldData', description='Turn on/off the conversion of dataset field data to a data object', default=True)
    m_Geometry = bpy.props.BoolProperty(name='Geometry', description='Turn on/off the conversion of dataset geometry to a data object', default=True)
    m_PointData = bpy.props.BoolProperty(name='PointData', description='Turn on/off the conversion of dataset point data to a data object', default=True)
    m_Topology = bpy.props.BoolProperty(name='Topology', description='Turn on/off the conversion of dataset topology to a data object', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CellData', 'm_FieldData', 'm_Geometry', 'm_PointData', 'm_Topology', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataSetToDataObjectFilter)
TYPENAMES.append('BVTK_NT_DataSetToDataObjectFilter' )


# --------------------------------------------------------------


class BVTK_NT_ImageNormalize(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageNormalize'
    bl_label = 'vtkImageNormalize'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageNormalize)
TYPENAMES.append('BVTK_NT_ImageNormalize' )


# --------------------------------------------------------------


class BVTK_NT_PiecewiseFunctionShiftScale(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PiecewiseFunctionShiftScale'
    bl_label = 'vtkPiecewiseFunctionShiftScale'
    
    m_PositionScale = bpy.props.FloatProperty(name='PositionScale', description='', default=1.0)
    m_PositionShift = bpy.props.FloatProperty(name='PositionShift', description='', default=0.0)
    m_ValueScale = bpy.props.FloatProperty(name='ValueScale', description='', default=1.0)
    m_ValueShift = bpy.props.FloatProperty(name='ValueShift', description='', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PositionScale', 'm_PositionShift', 'm_ValueScale', 'm_ValueShift', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PiecewiseFunctionShiftScale)
TYPENAMES.append('BVTK_NT_PiecewiseFunctionShiftScale' )


# --------------------------------------------------------------


class BVTK_NT_HedgeHog(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HedgeHog'
    bl_label = 'vtkHedgeHog'
    e_VectorMode_items = [(x, x, x) for x in ['UseNormal', 'UseVector']]
    
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Set scale factor to control size of oriented lines', default=1.0)
    e_VectorMode = bpy.props.EnumProperty(name='VectorMode', description='Specify whether to use vector or normal to perform vector operations', default='UseVector', items=e_VectorMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ScaleFactor', 'e_VectorMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HedgeHog)
TYPENAMES.append('BVTK_NT_HedgeHog' )


# --------------------------------------------------------------


class BVTK_NT_ImageQuantizeRGBToIndex(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageQuantizeRGBToIndex'
    bl_label = 'vtkImageQuantizeRGBToIndex'
    
    m_BuildTreeExecuteTime = bpy.props.FloatProperty(name='BuildTreeExecuteTime', description='For internal use only - set the times for executio', default=0.0)
    m_InitializeExecuteTime = bpy.props.FloatProperty(name='InitializeExecuteTime', description='For internal use only - set the times for executio', default=0.0)
    m_LookupIndexExecuteTime = bpy.props.FloatProperty(name='LookupIndexExecuteTime', description='For internal use only - set the times for executio', default=0.0)
    m_NumberOfColors = bpy.props.IntProperty(name='NumberOfColors', description='Set / Get the number of color index values to produce - must be a number between 2 and 65536', default=256)
    m_SamplingRate = bpy.props.IntVectorProperty(name='SamplingRate', description='', default=[1, 1, 1], size=3)
    m_SortIndexByLuminance = bpy.props.BoolProperty(name='SortIndexByLuminance', description='', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BuildTreeExecuteTime', 'm_InitializeExecuteTime', 'm_LookupIndexExecuteTime', 'm_NumberOfColors', 'm_SamplingRate', 'm_SortIndexByLuminance', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageQuantizeRGBToIndex)
TYPENAMES.append('BVTK_NT_ImageQuantizeRGBToIndex' )


# --------------------------------------------------------------


class BVTK_NT_Hull(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Hull'
    bl_label = 'vtkHull'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Hull)
TYPENAMES.append('BVTK_NT_Hull' )


# --------------------------------------------------------------


class BVTK_NT_PolyDataNormals(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PolyDataNormals'
    bl_label = 'vtkPolyDataNormals'
    
    m_AutoOrientNormals = bpy.props.BoolProperty(name='AutoOrientNormals', description='Turn on/off the automatic determination of correct normal orientation. NOTE: This assumes a completely closed surface (i.e. no boundary edges) and no non-manifold edges. If these constraints do not hold, all bets are off. This option adds some computational complexity, and is useful if you don\'t want to have to inspect the rendered image to determine whether to turn on the FlipNormals flag. However, this flag can work with the FlipNormals flag, and if both are set, all the normals in the output will point "inward"', default=True)
    m_ComputeCellNormals = bpy.props.BoolProperty(name='ComputeCellNormals', description='Turn on/off the computation of cell normals', default=True)
    m_ComputePointNormals = bpy.props.BoolProperty(name='ComputePointNormals', description='Turn on/off the computation of point normals', default=True)
    m_Consistency = bpy.props.BoolProperty(name='Consistency', description='Turn on/off the enforcement of consistent polygon ordering', default=True)
    m_FeatureAngle = bpy.props.FloatProperty(name='FeatureAngle', description='Specify the angle that defines a sharp edge. If the difference in angle across neighboring polygons is greater than this value, the shared edge is considered "sharp"', default=30.0)
    m_FlipNormals = bpy.props.BoolProperty(name='FlipNormals', description="Turn on/off the global flipping of normal orientation. Flipping reverves the meaning of front and back for Frontface and Backface culling in vtkProperty. Flipping modifies both the normal direction and the order of a cell's points", default=True)
    m_NonManifoldTraversal = bpy.props.BoolProperty(name='NonManifoldTraversal', description='Turn on/off traversal across non-manifold edges. This will prevent problems where the consistency of polygonal ordering is corrupted due to topological loops', default=True)
    m_Splitting = bpy.props.BoolProperty(name='Splitting', description='Turn on/off the splitting of sharp edges', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutoOrientNormals', 'm_ComputeCellNormals', 'm_ComputePointNormals', 'm_Consistency', 'm_FeatureAngle', 'm_FlipNormals', 'm_NonManifoldTraversal', 'm_Splitting', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PolyDataNormals)
TYPENAMES.append('BVTK_NT_PolyDataNormals' )


# --------------------------------------------------------------


class BVTK_NT_VolumeOfRevolutionFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VolumeOfRevolutionFilter'
    bl_label = 'vtkVolumeOfRevolutionFilter'
    
    m_AxisDirection = bpy.props.FloatVectorProperty(name='AxisDirection', description='', default=[0.0, 0.0, 1.0], size=3)
    m_AxisPosition = bpy.props.FloatVectorProperty(name='AxisPosition', description='', default=[0.0, 0.0, 0.0], size=3)
    m_Resolution = bpy.props.IntProperty(name='Resolution', description='Set/Get resolution of sweep operation. Resolution controls the number of intermediate node points', default=12)
    m_SweepAngle = bpy.props.FloatProperty(name='SweepAngle', description='Set/Get angle of rotation in degrees', default=360.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AxisDirection', 'm_AxisPosition', 'm_Resolution', 'm_SweepAngle', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VolumeOfRevolutionFilter)
TYPENAMES.append('BVTK_NT_VolumeOfRevolutionFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractUnstructuredGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractUnstructuredGrid'
    bl_label = 'vtkExtractUnstructuredGrid'
    
    m_CellClipping = bpy.props.BoolProperty(name='CellClipping', description='Turn on/off selection of geometry by cell id', default=True)
    m_CellMaximum = bpy.props.IntProperty(name='CellMaximum', description='Specify the maximum cell id for point id selection', default=1000000000)
    m_CellMinimum = bpy.props.IntProperty(name='CellMinimum', description='Specify the minimum cell id for point id selection', default=0)
    m_ExtentClipping = bpy.props.BoolProperty(name='ExtentClipping', description='Turn on/off selection of geometry via bounding box', default=True)
    m_Merging = bpy.props.BoolProperty(name='Merging', description='Turn on/off merging of coincident points. Note that is merging is on, points with different point attributes (e.g., normals) are merged, which may cause rendering artifacts', default=True)
    m_PointClipping = bpy.props.BoolProperty(name='PointClipping', description='Turn on/off selection of geometry by point id', default=True)
    m_PointMaximum = bpy.props.IntProperty(name='PointMaximum', description='Specify the maximum point id for point id selection', default=1000000000)
    m_PointMinimum = bpy.props.IntProperty(name='PointMinimum', description='Specify the minimum point id for point id selection', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CellClipping', 'm_CellMaximum', 'm_CellMinimum', 'm_ExtentClipping', 'm_Merging', 'm_PointClipping', 'm_PointMaximum', 'm_PointMinimum', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractUnstructuredGrid)
TYPENAMES.append('BVTK_NT_ExtractUnstructuredGrid' )


# --------------------------------------------------------------


class BVTK_NT_ImageRFFT(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageRFFT'
    bl_label = 'vtkImageRFFT'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_Dimensionality = bpy.props.IntProperty(name='Dimensionality', description='Dimensionality is the number of axes which are considered during execution. To process images dimensionality would be set to 2', default=3)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_Dimensionality', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfThreads', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageRFFT)
TYPENAMES.append('BVTK_NT_ImageRFFT' )


# --------------------------------------------------------------


class BVTK_NT_TemporalShiftScale(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TemporalShiftScale'
    bl_label = 'vtkTemporalShiftScale'
    
    m_MaximumNumberOfPeriods = bpy.props.FloatProperty(name='MaximumNumberOfPeriods', description='if Periodic time is enabled, this controls how many time periods time is reported for. A filter cannot output an infinite number of time steps and therefore a finite number of periods is generated when reporting time', default=1.0)
    m_Periodic = bpy.props.BoolProperty(name='Periodic', description='If Periodic is true, requests for time will be wrapped around so that the source appears to be a periodic time source. If data exists for times {0,N-1}, setting periodic to true will cause time 0 to be produced when time N, 2N, 2N etc is requested. This effectively gives the source the ability to generate time data indefinitely in a loop. When combined with Shift/Scale, the time becomes periodic in the shifted and scaled time frame of reference. Note: Since the input time may not start at zero, the wrapping of time from the end of one period to the start of the next, will subtract the initial time - a source with T{5..6} repeated periodicaly will have output time {5..6..7..8} etc', default=True)
    m_PeriodicEndCorrection = bpy.props.BoolProperty(name='PeriodicEndCorrection', description='if Periodic time is enabled, this flag determines if the last time step is the same as the first. If PeriodicEndCorrection is true, then it is assumed that the input data goes from 0-1 (or whatever scaled/shifted actual time) and time 1 is the same as time 0 so that steps will be 0,1,2,3...N,1,2,3...N,1,2,3 where step N is the same as 0 and step 0 is not repeated. When this flag is false the data is assumed to be literal and output is of the form 0,1,2,3...N,0,1,2,3... By default this flag is O', default=True)
    m_PostShift = bpy.props.FloatProperty(name='PostShift', description='Apply a translation to the tim', default=0.0)
    m_PreShift = bpy.props.FloatProperty(name='PreShift', description='Apply a translation to the data before scaling. To convert T{5,100} to T{0,1} use Preshift=-5, Scale=1/95, PostShift=0 To convert T{5,105} to T{5,10} use Preshift=-5, Scale=5/100, PostShift=', default=0.0)
    m_Scale = bpy.props.FloatProperty(name='Scale', description='Apply a scale to the time', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MaximumNumberOfPeriods', 'm_Periodic', 'm_PeriodicEndCorrection', 'm_PostShift', 'm_PreShift', 'm_Scale', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TemporalShiftScale)
TYPENAMES.append('BVTK_NT_TemporalShiftScale' )


# --------------------------------------------------------------


class BVTK_NT_ExtractUnstructuredGridPiece(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractUnstructuredGridPiece'
    bl_label = 'vtkExtractUnstructuredGridPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty(name='CreateGhostCells', description='Turn on/off creating ghost cells (on by default)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CreateGhostCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractUnstructuredGridPiece)
TYPENAMES.append('BVTK_NT_ExtractUnstructuredGridPiece' )


# --------------------------------------------------------------


class BVTK_NT_SimpleElevationFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SimpleElevationFilter'
    bl_label = 'vtkSimpleElevationFilter'
    
    m_Vector = bpy.props.FloatVectorProperty(name='Vector', description='Define the vector with which to dot against', default=[0.0, 0.0, 1.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Vector', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SimpleElevationFilter)
TYPENAMES.append('BVTK_NT_SimpleElevationFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractGeometry(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractGeometry'
    bl_label = 'vtkExtractGeometry'
    
    m_ExtractBoundaryCells = bpy.props.BoolProperty(name='ExtractBoundaryCells', description='Boolean controls whether to extract cells that are partially inside. By default, ExtractBoundaryCells is off', default=True)
    m_ExtractInside = bpy.props.BoolProperty(name='ExtractInside', description='Boolean controls whether to extract cells that are inside of implicit function (ExtractInside == 1) or outside of implicit function (ExtractInside == 0)', default=True)
    m_ExtractOnlyBoundaryCells = bpy.props.BoolProperty(name='ExtractOnlyBoundaryCells', description='Boolean controls whether to extract cells that are partially inside. By default, ExtractBoundaryCells is off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ExtractBoundaryCells', 'm_ExtractInside', 'm_ExtractOnlyBoundaryCells', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['ImplicitFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractGeometry)
TYPENAMES.append('BVTK_NT_ExtractGeometry' )


# --------------------------------------------------------------


class BVTK_NT_ImageAppendComponents(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageAppendComponents'
    bl_label = 'vtkImageAppendComponents'
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
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageAppendComponents)
TYPENAMES.append('BVTK_NT_ImageAppendComponents' )


# --------------------------------------------------------------


class BVTK_NT_PCANormalEstimation(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PCANormalEstimation'
    bl_label = 'vtkPCANormalEstimation'
    e_NormalOrientation_items = [(x, x, x) for x in ['AsComputed', 'GraphTraversal', 'Point']]
    
    m_FlipNormals = bpy.props.BoolProperty(name='FlipNormals', description='The normal orientation can be flipped by enabling this flag', default=False)
    e_NormalOrientation = bpy.props.EnumProperty(name='NormalOrientation', description='Configure how the filter addresses consistency in normal oreientation. When initially computed using PCA, a point normal may point in the + or - direction, which may not be consistent with neighboring points. To address this, various strategies have been used to create consistent normals. The simplest approach is to do nothing (AsComputed). Another simple approach is to flip the normal based on its direction with respect to a specified point (i.e., point normals will point towrads the specified point). Finally, a full traversal of points across the graph of neighboring, connected points produces the best results but is computationally expensive', default='Point', items=e_NormalOrientation_items)
    m_OrientationPoint = bpy.props.FloatVectorProperty(name='OrientationPoint', description='If the normal orientation is to be consistent with a specified direction, then an orientation point should be set. The sign of the normals will be modified so that they point towards this point. By default, the specified orientation point is (0,0,0)', default=[0.0, 0.0, 0.0], size=3)
    m_SampleSize = bpy.props.IntProperty(name='SampleSize', description='For each sampled point, specify the number of the closest, surrounding points used to estimate the normal (the so called k-neighborhood). By default 25 points are used. Smaller numbers may speed performance at the cost of accuracy', default=25)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FlipNormals', 'e_NormalOrientation', 'm_OrientationPoint', 'm_SampleSize', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PCANormalEstimation)
TYPENAMES.append('BVTK_NT_PCANormalEstimation' )


# --------------------------------------------------------------


class BVTK_NT_MultiBlockDataGroupFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MultiBlockDataGroupFilter'
    bl_label = 'vtkMultiBlockDataGroupFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MultiBlockDataGroupFilter)
TYPENAMES.append('BVTK_NT_MultiBlockDataGroupFilter' )


# --------------------------------------------------------------


class BVTK_NT_SpatialRepresentationFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SpatialRepresentationFilter'
    bl_label = 'vtkSpatialRepresentationFilter'
    
    m_GenerateLeaves = bpy.props.BoolProperty(name='GenerateLeaves', description='Turn on/off the generation of leaf nodes. Off by default', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateLeaves', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], ['SpatialRepresentation'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SpatialRepresentationFilter)
TYPENAMES.append('BVTK_NT_SpatialRepresentationFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractEdges(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractEdges'
    bl_label = 'vtkExtractEdges'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractEdges)
TYPENAMES.append('BVTK_NT_ExtractEdges' )


# --------------------------------------------------------------


class BVTK_NT_ImageSkeleton2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageSkeleton2D'
    bl_label = 'vtkImageSkeleton2D'
    e_SplitMode_items = [(x, x, x) for x in ['Beam', 'Block', 'Slab']]
    
    m_DesiredBytesPerPiece = bpy.props.IntProperty(name='DesiredBytesPerPiece', description='The desired bytes per piece when volume is split for execution. When SMP is enabled, this is used to subdivide the volume into pieces. Smaller pieces allow for better dynamic load balancing, but increase the total overhead. The default is 65536 bytes', default=65536)
    m_EnableSMP = bpy.props.BoolProperty(name='EnableSMP', description='Enable/Disable SMP for threading', default=False)
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', description='Global Disable SMP for all derived Imaging filters', default=False)
    m_MinimumPieceSize = bpy.props.IntVectorProperty(name='MinimumPieceSize', description='', default=[16, 1, 1], size=3)
    m_NumberOfIterations = bpy.props.IntProperty(name='NumberOfIterations', description='Sets the number of cycles in the erosion', default=1)
    m_NumberOfThreads = bpy.props.IntProperty(name='NumberOfThreads', description='Get/Set the number of threads to create when rendering. This is ignored if EnableSMP is On', default=4)
    m_Prune = bpy.props.BoolProperty(name='Prune', description='When prune is on, only closed loops are left unchanged', default=True)
    e_SplitMode = bpy.props.EnumProperty(name='SplitMode', description='Set the method used to divide the volume into pieces. Slab mode splits the volume along the Z direction first, Beam mode splits evenly along the Z and Y directions, and Block mode splits evenly along all three directions. Most filters use Slab mode as the default', default='Slab', items=e_SplitMode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DesiredBytesPerPiece', 'm_EnableSMP', 'm_GlobalDefaultEnableSMP', 'm_MinimumPieceSize', 'm_NumberOfIterations', 'm_NumberOfThreads', 'm_Prune', 'e_SplitMode', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageSkeleton2D)
TYPENAMES.append('BVTK_NT_ImageSkeleton2D' )


# --------------------------------------------------------------


class BVTK_NT_RectilinearSynchronizedTemplates(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RectilinearSynchronizedTemplates'
    bl_label = 'vtkRectilinearSynchronizedTemplates'
    
    m_ArrayComponent = bpy.props.IntProperty(name='ArrayComponent', description='Set/get which component of the scalar array to contour on; defaults to 0', default=0)
    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', description='Set/Get the computation of gradients. Gradient computation is fairly expensive in both time and storage. Note that if ComputeNormals is on, gradients will have to be calculated, but will not be stored in the output dataset. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Set/Get the computation of normals. Normal computation is fairly expensive in both time and storage. If the output data will be processed by filters that modify topology or geometry, it may be wise to turn Normals and Gradients off', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', description='Set/Get the computation of scalars', default=True)
    m_GenerateTriangles = bpy.props.BoolProperty(name='GenerateTriangles', description='If this is enabled (by default), the output will be triangles otherwise, the output will be the intersection polygon', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', description='Set the number of contours to place into the list. You only really need to use this method to reduce list size. The method SetValue() will automatically increase list size as needed', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayComponent', 'm_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_GenerateTriangles', 'm_NumberOfContours', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RectilinearSynchronizedTemplates)
TYPENAMES.append('BVTK_NT_RectilinearSynchronizedTemplates' )


# --------------------------------------------------------------


class BVTK_NT_HierarchicalDataLevelFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HierarchicalDataLevelFilter'
    bl_label = 'vtkHierarchicalDataLevelFilter'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HierarchicalDataLevelFilter)
TYPENAMES.append('BVTK_NT_HierarchicalDataLevelFilter' )


# --------------------------------------------------------------


class BVTK_NT_ExtractPiece(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractPiece'
    bl_label = 'vtkExtractPiece'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractPiece)
TYPENAMES.append('BVTK_NT_ExtractPiece' )


# --------------------------------------------------------------


class BVTK_NT_HyperTreeGridPlaneCutter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperTreeGridPlaneCutter'
    bl_label = 'vtkHyperTreeGridPlaneCutter'
    
    m_Dual = bpy.props.BoolProperty(name='Dual', description='Set/Get whether output mesh should be computed on dual gri', default=True)
    m_Plane = bpy.props.FloatVectorProperty(name='Plane', description='', default=[0.0, 0.0, 0.0, 0.0], size=4)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Dual', 'm_Plane', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperTreeGridPlaneCutter)
TYPENAMES.append('BVTK_NT_HyperTreeGridPlaneCutter' )


# --------------------------------------------------------------


class BVTK_NT_MapArrayValues(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MapArrayValues'
    bl_label = 'vtkMapArrayValues'
    
    m_FieldType = bpy.props.IntProperty(name='FieldType', description='Set/Get where the data is located that is being mapped. See FieldType enumeration for possible values. Default is POINT_DATA', default=0)
    m_FillValue = bpy.props.FloatProperty(name='FillValue', description='Set/Get whether to copy the data from the input array to the output array before the mapping occurs. If turned off, FillValue is used to initialize any unmapped array indices. Default is -1', default=-1.0)
    m_InputArrayName = bpy.props.StringProperty(name='InputArrayName', description='Set/Get the name of the input array. This must be set prior to execution')
    m_OutputArrayName = bpy.props.StringProperty(name='OutputArrayName', description='Set/Get the name of the output array. Default is "ArrayMap"', default='ArrayMap')
    m_OutputArrayType = bpy.props.IntProperty(name='OutputArrayType', description='Set/Get the type of the output array. See vtkSetGet.h for possible values. Default is VTK_INT', default=6)
    m_PassArray = bpy.props.BoolProperty(name='PassArray', description='Set/Get whether to copy the data from the input array to the output array before the mapping occurs. If turned off, FillValue is used to initialize any unmapped array indices. Default is off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldType', 'm_FillValue', 'm_InputArrayName', 'm_OutputArrayName', 'm_OutputArrayType', 'm_PassArray', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MapArrayValues)
TYPENAMES.append('BVTK_NT_MapArrayValues' )


# --------------------------------------------------------------


class BVTK_NT_ExtractLevel(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExtractLevel'
    bl_label = 'vtkExtractLevel'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExtractLevel)
TYPENAMES.append('BVTK_NT_ExtractLevel' )


# --------------------------------------------------------------


class BVTK_NT_DensifyPointCloudFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DensifyPointCloudFilter'
    bl_label = 'vtkDensifyPointCloudFilter'
    e_NeighborhoodType_items = [(x, x, x) for x in ['NClosest', 'Radius']]
    
    m_InterpolateAttributeData = bpy.props.BoolProperty(name='InterpolateAttributeData', description='Turn on/off the interpolation of attribute data from the input point cloud to new, added points', default=True)
    m_MaximumNumberOfIterations = bpy.props.IntProperty(name='MaximumNumberOfIterations', description='The maximum number of iterations to run. By default the maximum is one', default=3)
    m_MaximumNumberOfPoints = bpy.props.IntProperty(name='MaximumNumberOfPoints', description='Set a limit on the maximum number of points that can be created. This data member serves as a crude barrier to explosive point creation; it does not guarantee that precisely these many points will be created. Once this limit is hit, it may result in premature termination of the algorithm. Consider it a pressure relief valve', default=1000000000)
    e_NeighborhoodType = bpy.props.EnumProperty(name='NeighborhoodType', description='Specify how the local point neighborhood is defined. By default an N closest neighborhood is used. This tends to avoid explosive point creation', default='NClosest', items=e_NeighborhoodType_items)
    m_NumberOfClosestPoints = bpy.props.IntProperty(name='NumberOfClosestPoints', description='Define a local neighborhood in terms of the N closest points. By default the number of the closest points is =6. This data member is relevant only if the neighborhood type is N_CLOSEST', default=6)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Define a local neighborhood for each point in terms of a local radius. By default, the radius is 1.0. This data member is relevant only if the neighborhood type is RADIUS', default=1.0)
    m_TargetDistance = bpy.props.FloatProperty(name='TargetDistance', description='Set / get the target point distance. Points will be created in an iterative fashion until all points in their local neighborhood are the target distance apart or less. Note that the process may terminate early due to the limit on the maximum number of iterations. By default the target distance is set to 0.5. Note that the TargetDistance should be less than the Radius or nothing will change on output', default=0.5)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_InterpolateAttributeData', 'm_MaximumNumberOfIterations', 'm_MaximumNumberOfPoints', 'e_NeighborhoodType', 'm_NumberOfClosestPoints', 'm_Radius', 'm_TargetDistance', ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DensifyPointCloudFilter)
TYPENAMES.append('BVTK_NT_DensifyPointCloudFilter' )


# --------------------------------------------------------------


menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append(BVTK_NodeCategory('VTKFilter1', 'Filter1', items=menu_items))