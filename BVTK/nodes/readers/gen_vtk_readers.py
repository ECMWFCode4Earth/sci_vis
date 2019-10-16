from ... core import *
type_names = []


# --------------------------------------------------------------


class BVTK_NT_XMLStructuredGridReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLStructuredGridReader'
    bl_label = 'vtkXMLStructuredGridReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    m_WholeSlices = bpy.props.BoolProperty(name='WholeSlices', description='Get/Set whether the reader gets a whole slice from disk when only a rectangle inside it is needed. This mode reads more data than necessary, but prevents many short reads from interacting poorly with the compression and encoding schemes', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', 'm_WholeSlices', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLStructuredGridReader)
type_names.append('BVTK_NT_XMLStructuredGridReader')


# --------------------------------------------------------------


class BVTK_NT_DataObjectReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataObjectReader'
    bl_label = 'vtkDataObjectReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataObjectReader)
type_names.append('BVTK_NT_DataObjectReader')


# --------------------------------------------------------------


class BVTK_NT_BiomTableReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BiomTableReader'
    bl_label = 'vtkBiomTableReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BiomTableReader)
type_names.append('BVTK_NT_BiomTableReader')


# --------------------------------------------------------------


class BVTK_NT_DEMReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DEMReader'
    bl_label = 'vtkDEMReader'
    e_ElevationReference_items = [(x, x, x) for x in ['ElevationBounds', 'SeaLevel']]
    
    e_ElevationReference = bpy.props.EnumProperty(name='ElevationReference', description='Specify the elevation origin to use. By default, the elevation origin is equal to ElevationBounds[0]. A more convenient origin is to use sea level (i.e., a value of 0.0)', default='ElevationBounds', items=e_ElevationReference_items)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of Digital Elevation Model (DEM) fil', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ElevationReference', 'm_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DEMReader)
type_names.append('BVTK_NT_DEMReader')


# --------------------------------------------------------------


class BVTK_NT_MultiBlockPLOT3DReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MultiBlockPLOT3DReader'
    bl_label = 'vtkMultiBlockPLOT3DReader'
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AutoDetectFormat = bpy.props.BoolProperty(name='AutoDetectFormat', description='When this option is turned on, the reader will try to figure out the values of various options such as byte order, byte count etc. automatically. This options works only for binary files. When it is turned on, the reader should be able to read most Plot3D files automatically. The default is OFF for backwards compatibility reasons. For binary files, it is strongly recommended that you turn on AutoDetectFormat and leave the other file format related options untouched', default=True)
    m_BinaryFile = bpy.props.BoolProperty(name='BinaryFile', description='Is the file to be read written in binary format (as opposed to ascii)', default=True)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description='Set the byte order of the file (remember, more Unix workstations write big endian whereas PCs write little endian). Default is big endian (since most older PLOT3D files were written by workstations)', default='BigEndian', items=e_ByteOrder_items)
    m_DoublePrecision = bpy.props.BoolProperty(name='DoublePrecision', description='Is this file in double precision or single precision. This only matters for binary files. Default is single', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set/Get the PLOT3D geometry filename', subtype='FILE_PATH')
    m_ForceRead = bpy.props.BoolProperty(name='ForceRead', description='Try to read a binary file even if the file length seems to be inconsistent with the header information. Use this with caution, if the file length is not the same as calculated from the header. either the file is corrupt or the settings are wrong', default=True)
    m_FunctionFileName = bpy.props.StringProperty(name='FunctionFileName', description='Set/Get the PLOT3D function filename', subtype='FILE_PATH')
    m_Gamma = bpy.props.FloatProperty(name='Gamma', description='Set/Get the ratio of specific heats. Default is 1.4', default=1.4)
    m_HasByteCount = bpy.props.BoolProperty(name='HasByteCount', description="Were the arrays written with leading and trailing byte counts ? Usually, files written by a fortran program will contain these byte counts whereas the ones written by C/C++ won't", default=True)
    m_IBlanking = bpy.props.BoolProperty(name='IBlanking', description='Is there iblanking (point visibility) information in the file. If there is iblanking arrays, these will be read and assigned to the PointVisibility array of the output', default=True)
    m_MultiGrid = bpy.props.BoolProperty(name='MultiGrid', description='Does the file to be read contain information about number of grids. In some PLOT3D files, the first value contains the number of grids (even if there is only 1). If reading such a file, set this to true', default=True)
    m_PreserveIntermediateFunctions = bpy.props.BoolProperty(name='PreserveIntermediateFunctions', description='When set to true (default), the reader will preserve intermediate computed quantities that were not explicitly requested e.g. if `VelocityMagnitude` is enabled, but not `Velocity`, the reader still needs to compute `Velocity`. If `PreserveIntermediateFunctions` if false, then the output will not have `Velocity` array, only the requested `VelocityMagnitude`. This is useful to avoid using up memory for arrays that are not relevant for the analysis', default=True)
    m_QFileName = bpy.props.StringProperty(name='QFileName', description='Set/Get the PLOT3D solution filename', subtype='FILE_PATH')
    m_R = bpy.props.FloatProperty(name='R', description='Set/Get the gas constant. Default is 1.0', default=1.0)
    m_ScalarFunctionNumber = bpy.props.IntProperty(name='ScalarFunctionNumber', description='Specify the scalar function to extract. If ==(-1), then no scalar function is extracted', default=100)
    m_TwoDimensionalGeometry = bpy.props.BoolProperty(name='TwoDimensionalGeometry', description='If only two-dimensional data was written to the file, turn this on', default=True)
    m_VectorFunctionNumber = bpy.props.IntProperty(name='VectorFunctionNumber', description='Specify the vector function to extract. If ==(-1), then no vector function is extracted', default=202)
    m_XYZFileName = bpy.props.StringProperty(name='XYZFileName', description='Set/Get the PLOT3D geometry filename', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutoDetectFormat', 'm_BinaryFile', 'e_ByteOrder', 'm_DoublePrecision', 'm_FileName', 'm_ForceRead', 'm_FunctionFileName', 'm_Gamma', 'm_HasByteCount', 'm_IBlanking', 'm_MultiGrid', 'm_PreserveIntermediateFunctions', 'm_QFileName', 'm_R', 'm_ScalarFunctionNumber', 'm_TwoDimensionalGeometry', 'm_VectorFunctionNumber', 'm_XYZFileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MultiBlockPLOT3DReader)
type_names.append('BVTK_NT_MultiBlockPLOT3DReader')


# --------------------------------------------------------------


class BVTK_NT_GenericDataObjectReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GenericDataObjectReader'
    bl_label = 'vtkGenericDataObjectReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GenericDataObjectReader)
type_names.append('BVTK_NT_GenericDataObjectReader')


# --------------------------------------------------------------


class BVTK_NT_OpenFOAMReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_OpenFOAMReader'
    bl_label = 'vtkOpenFOAMReader'
    
    m_AddDimensionsToArrayNames = bpy.props.BoolProperty(name='AddDimensionsToArrayNames', description='Add dimensions to array name', default=True)
    m_CacheMesh = bpy.props.BoolProperty(name='CacheMesh', description='Set/Get whether mesh is to be cached', default=True)
    m_CreateCellToPoint = bpy.props.BoolProperty(name='CreateCellToPoint', description='Set/Get whether to create cell-to-point translated data for cell-type dat', default=True)
    m_DecomposePolyhedra = bpy.props.BoolProperty(name='DecomposePolyhedra', description='Set/Get whether polyhedra are to be decomposed', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set/Get the filename', subtype='FILE_PATH')
    m_ListTimeStepsByControlDict = bpy.props.BoolProperty(name='ListTimeStepsByControlDict', description='Determine if time directories are to be listed according to controlDic', default=True)
    m_PositionsIsIn13Format = bpy.props.BoolProperty(name='PositionsIsIn13Format', description='Set/Get whether the lagrangian/positions have additional data or not. For historical reasons, PositionsIsIn13Format is used to denote that the positions only have x,y,z value and the cell of the enclosing cell. In OpenFOAM 1.4-2.4, positions included facei and stepFraction information', default=True)
    m_ReadZones = bpy.props.BoolProperty(name='ReadZones', description='Set/Get whether zones will be read', default=True)
    m_SkipZeroTime = bpy.props.BoolProperty(name='SkipZeroTime', description='Ignore 0/ time directory, which is normally missing Lagrangian fields and may have many dictionary functionality that we cannot easily handle', default=False)
    m_Use64BitFloats = bpy.props.BoolProperty(name='Use64BitFloats', description='If true, floats are expected to be 64-bit, rather than 32. Note that vtkFloatArrays may still be used in the output if this is true. This flag is only used to ensure that binary data is correctly parsed', default=True)
    m_Use64BitLabels = bpy.props.BoolProperty(name='Use64BitLabels', description='If true, labels are expected to be 64-bit, rather than 32', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AddDimensionsToArrayNames', 'm_CacheMesh', 'm_CreateCellToPoint', 'm_DecomposePolyhedra', 'm_FileName', 'm_ListTimeStepsByControlDict', 'm_PositionsIsIn13Format', 'm_ReadZones', 'm_SkipZeroTime', 'm_Use64BitFloats', 'm_Use64BitLabels', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_OpenFOAMReader)
type_names.append('BVTK_NT_OpenFOAMReader')


# --------------------------------------------------------------


class BVTK_NT_TableReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TableReader'
    bl_label = 'vtkTableReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TableReader)
type_names.append('BVTK_NT_TableReader')


# --------------------------------------------------------------


class BVTK_NT_DataSetReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataSetReader'
    bl_label = 'vtkDataSetReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataSetReader)
type_names.append('BVTK_NT_DataSetReader')


# --------------------------------------------------------------


class BVTK_NT_ImageReader2(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageReader2'
    bl_label = 'vtkImageReader2'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageReader2)
type_names.append('BVTK_NT_ImageReader2')


# --------------------------------------------------------------


class BVTK_NT_SimplePointsReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SimplePointsReader'
    bl_label = 'vtkSimplePointsReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set/Get the name of the file from which to read points', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SimplePointsReader)
type_names.append('BVTK_NT_SimplePointsReader')


# --------------------------------------------------------------


class BVTK_NT_XMLPImageDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLPImageDataReader'
    bl_label = 'vtkXMLPImageDataReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLPImageDataReader)
type_names.append('BVTK_NT_XMLPImageDataReader')


# --------------------------------------------------------------


class BVTK_NT_ProStarReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProStarReader'
    bl_label = 'vtkProStarReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify the file name prefix of the cel/vrt files to read. The reader will try to open FileName.cel and FileName.vrt files', subtype='FILE_PATH')
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='The proSTAR files are often in millimeters. Specify an alternative scaling factor', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ScaleFactor', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProStarReader)
type_names.append('BVTK_NT_ProStarReader')


# --------------------------------------------------------------


class BVTK_NT_PSLACReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PSLACReader'
    bl_label = 'vtkPSLACReader'
    
    m_MeshFileName = bpy.props.StringProperty(name='MeshFileName', description='', subtype='FILE_PATH')
    m_ReadExternalSurface = bpy.props.BoolProperty(name='ReadExternalSurface', description='If on, reads the external surfaces of the data set. Set to on by default', default=True)
    m_ReadInternalVolume = bpy.props.BoolProperty(name='ReadInternalVolume', description='If on, reads the internal volume of the data set. Set to off by default', default=True)
    m_ReadMidpoints = bpy.props.BoolProperty(name='ReadMidpoints', description='If on, reads midpoint information for external surfaces and builds quadratic surface triangles. Set to on by default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MeshFileName', 'm_ReadExternalSurface', 'm_ReadInternalVolume', 'm_ReadMidpoints', ]
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PSLACReader)
type_names.append('BVTK_NT_PSLACReader')


# --------------------------------------------------------------


class BVTK_NT_FacetReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FacetReader'
    bl_label = 'vtkFacetReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of Facet datafile to rea', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FacetReader)
type_names.append('BVTK_NT_FacetReader')


# --------------------------------------------------------------


class BVTK_NT_GESignaReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GESignaReader'
    bl_label = 'vtkGESignaReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_Date = bpy.props.StringProperty(name='Date', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_ImageNumber = bpy.props.StringProperty(name='ImageNumber', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_Modality = bpy.props.StringProperty(name='Modality', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_PatientID = bpy.props.StringProperty(name='PatientID', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_PatientName = bpy.props.StringProperty(name='PatientName', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_Series = bpy.props.StringProperty(name='Series', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_Study = bpy.props.StringProperty(name='Study', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=22, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_Date', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_ImageNumber', 'm_MemoryBufferLength', 'm_Modality', 'm_NumberOfScalarComponents', 'm_PatientID', 'm_PatientName', 'm_Series', 'm_Study', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GESignaReader)
type_names.append('BVTK_NT_GESignaReader')


# --------------------------------------------------------------


class BVTK_NT_MCubesReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MCubesReader'
    bl_label = 'vtkMCubesReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='BigEndian', items=e_DataByteOrder_items)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of marching cubes file', subtype='FILE_PATH')
    m_FlipNormals = bpy.props.BoolProperty(name='FlipNormals', description='Specify whether to flip normals in opposite direction. Flipping ONLY changes the direction of the normal vector. Contrast this with flipping in vtkPolyDataNormals which flips both the normal and the cell point order', default=True)
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='Specify a header size if one exists. The header is skipped and not used at this time', default=0)
    m_LimitsFileName = bpy.props.StringProperty(name='LimitsFileName', description='Set / get the file name of the marching cubes limits file', subtype='FILE_PATH')
    m_Normals = bpy.props.BoolProperty(name='Normals', description='Specify whether to read normals', default=True)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Turn on/off byte swapping', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_FileName', 'm_FlipNormals', 'm_HeaderSize', 'm_LimitsFileName', 'm_Normals', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MCubesReader)
type_names.append('BVTK_NT_MCubesReader')


# --------------------------------------------------------------


class BVTK_NT_TecplotReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TecplotReader'
    bl_label = 'vtkTecplotReader'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TecplotReader)
type_names.append('BVTK_NT_TecplotReader')


# --------------------------------------------------------------


class BVTK_NT_MNITransformReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MNITransformReader'
    bl_label = 'vtkMNITransformReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set the file name', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], [], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MNITransformReader)
type_names.append('BVTK_NT_MNITransformReader')


# --------------------------------------------------------------


class BVTK_NT_RTXMLPolyDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RTXMLPolyDataReader'
    bl_label = 'vtkRTXMLPolyDataReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RTXMLPolyDataReader)
type_names.append('BVTK_NT_RTXMLPolyDataReader')


# --------------------------------------------------------------


class BVTK_NT_RISReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RISReader'
    bl_label = 'vtkRISReader'
    
    m_Delimiter = bpy.props.StringProperty(name='Delimiter', description='Set/get the delimiter to be used for concatenating field data (default: ";"', default=';')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set/get the file to loa', subtype='FILE_PATH')
    m_MaxRecords = bpy.props.IntProperty(name='MaxRecords', description='Set/get the maximum number of records to read from the file (zero = unlimited', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Delimiter', 'm_FileName', 'm_MaxRecords', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RISReader)
type_names.append('BVTK_NT_RISReader')


# --------------------------------------------------------------


class BVTK_NT_VASPTessellationReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VASPTessellationReader'
    bl_label = 'vtkVASPTessellationReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='The name of the file to read', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VASPTessellationReader)
type_names.append('BVTK_NT_VASPTessellationReader')


# --------------------------------------------------------------


class BVTK_NT_MultiNewickTreeReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MultiNewickTreeReader'
    bl_label = 'vtkMultiNewickTreeReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MultiNewickTreeReader)
type_names.append('BVTK_NT_MultiNewickTreeReader')


# --------------------------------------------------------------


class BVTK_NT_PLYReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PLYReader'
    bl_label = 'vtkPLYReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of AbstractPolyData file (obj / ply / stl)', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PLYReader)
type_names.append('BVTK_NT_PLYReader')


# --------------------------------------------------------------


class BVTK_NT_ExodusIIReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ExodusIIReader'
    bl_label = 'vtkExodusIIReader'
    
    m_AnimateModeShapes = bpy.props.BoolProperty(name='AnimateModeShapes', description='If this flag is on (the default) and HasModeShapes is also on, then this reader will report a continuous time range [0,1] and animate the displacements in a periodic sinusoid. If this flag is off and HasModeShapes is on, this reader ignores time. This flag has no effect if HasModeShapes is off', default=True)
    m_ApplyDisplacements = bpy.props.BoolProperty(name='ApplyDisplacements', description="Geometric locations can include displacements. By default, this is ON. The nodal positions are 'displaced' by the standard exodus displacment vector. If displacements are turned 'off', the user can explicitly add them by applying a warp filter", default=True)
    m_CacheSize = bpy.props.FloatProperty(name='CacheSize', description='Set the size of the cache in MiB', default=0.0)
    m_DisplacementMagnitude = bpy.props.FloatProperty(name='DisplacementMagnitude', description="Geometric locations can include displacements. By default, this is ON. The nodal positions are 'displaced' by the standard exodus displacment vector. If displacements are turned 'off', the user can explicitly add them by applying a warp filter", default=1.0)
    m_DisplayType = bpy.props.IntProperty(name='DisplayType', description='', default=0)
    m_FileId = bpy.props.IntProperty(name='FileId', description='', default=0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of the Exodus file', subtype='FILE_PATH')
    m_GenerateFileIdArray = bpy.props.BoolProperty(name='GenerateFileIdArray', description='', default=True)
    m_GenerateGlobalElementIdArray = bpy.props.BoolProperty(name='GenerateGlobalElementIdArray', description='', default=True)
    m_GenerateGlobalNodeIdArray = bpy.props.BoolProperty(name='GenerateGlobalNodeIdArray', description='', default=True)
    m_GenerateImplicitElementIdArray = bpy.props.BoolProperty(name='GenerateImplicitElementIdArray', description='', default=True)
    m_GenerateImplicitNodeIdArray = bpy.props.BoolProperty(name='GenerateImplicitNodeIdArray', description='', default=True)
    m_GenerateObjectIdCellArray = bpy.props.BoolProperty(name='GenerateObjectIdCellArray', description='Extra cell data array that can be generated. By default, this array is ON. The value of the array is the integer id found in the exodus file. The name of the array is returned by GetBlockIdArrayName(). For cells representing elements from an Exodus element block, this is set to the element block ID. For cells representing edges from an Exodus edge block, this is the edge block ID. Similarly, this is the face block ID for cells representing faces from an Exodus face block. The same holds for cells representing entries of node, edge, face, side, and element sets', default=True)
    m_HasModeShapes = bpy.props.BoolProperty(name='HasModeShapes', description='Set/Get whether the Exodus sequence number corresponds to time steps or mode shapes. By default, HasModeShapes is false unless two time values in the Exodus file are identical, in which case it is true', default=True)
    m_ModeShapeTime = bpy.props.FloatProperty(name='ModeShapeTime', description='Set/Get the time used to animate mode shapes. This is a number between 0 and 1 that is used to scale the DisplacementMagnitude in a sinusoidal pattern. Specifically, the displacement vector for each vertex is scaled by$ \\mathrm{DisplacementMagnitude} cos( 2\\pi \\mathrm{ModeShapeTime} ) $ before it is added to the vertex coordinates', default=-1.0)
    m_SqueezePoints = bpy.props.BoolProperty(name='SqueezePoints', description='Should the reader output only points used by elements in the output mesh, or all the points. Outputting all the points is much faster since the point array can be read straight from disk and the mesh connectivity need not be altered. Squeezing the points down to the minimum set needed to produce the output mesh is useful for glyphing and other point-based operations. On large parallel datasets, loading all the points implies loading all the points on all processes and performing subsequent filtering on a much larger set', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_XMLFileName = bpy.props.StringProperty(name='XMLFileName', description='Specify file name of the xml file', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AnimateModeShapes', 'm_ApplyDisplacements', 'm_CacheSize', 'm_DisplacementMagnitude', 'm_DisplayType', 'm_FileId', 'm_FileName', 'm_GenerateFileIdArray', 'm_GenerateGlobalElementIdArray', 'm_GenerateGlobalNodeIdArray', 'm_GenerateImplicitElementIdArray', 'm_GenerateImplicitNodeIdArray', 'm_GenerateObjectIdCellArray', 'm_HasModeShapes', 'm_ModeShapeTime', 'm_SqueezePoints', 'm_TimeStep', 'm_XMLFileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ExodusIIReader)
type_names.append('BVTK_NT_ExodusIIReader')


# --------------------------------------------------------------


class BVTK_NT_ParticleReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ParticleReader'
    bl_label = 'vtkParticleReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_FileType_items = [(x, x, x) for x in ['Binary', 'Text', 'Unknown']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian. Not used when reading text files", default='LittleEndian', items=e_DataByteOrder_items)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Get/Set the file type. The options are: - FILE_TYPE_IS_UNKNOWN (default) the class will attempt to determine the file type. If this fails then you should set the file type yourself. - FILE_TYPE_IS_TEXT the file type is text. - FILE_TYPE_IS_BINARY the file type is binary', default='Unknown', items=e_FileType_items)
    m_HasScalar = bpy.props.BoolProperty(name='HasScalar', description='Default: 1. If 1 then each particle has a value associated with it', default=True)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file. Not used when reading text files', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_FileName', 'e_FileType', 'm_HasScalar', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ParticleReader)
type_names.append('BVTK_NT_ParticleReader')


# --------------------------------------------------------------


class BVTK_NT_StructuredGridReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StructuredGridReader'
    bl_label = 'vtkStructuredGridReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StructuredGridReader)
type_names.append('BVTK_NT_StructuredGridReader')


# --------------------------------------------------------------


class BVTK_NT_ImageReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageReader'
    bl_label = 'vtkImageReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataMask = bpy.props.IntProperty(name='DataMask', description="Set/Get the Data mask. The data mask is a simply integer whose bits are treated as a mask to the bits read from disk. That is, the data mask is bitwise-and'ed to the numbers read from disk. This ivar is stored as 64 bits, the largest mask you will need. The mask will be truncated to the data size required to be read (using the least significant bits)", default=1000000000)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_DataVOI = bpy.props.IntVectorProperty(name='DataVOI', description='', default=[0, 0, 0, 0, 0, 0], size=6)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_ScalarArrayName = bpy.props.StringProperty(name='ScalarArrayName', description='Set/get the scalar array name for this data set', default='ImageFile')
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataMask', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_DataVOI', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_ScalarArrayName', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], ['Transform'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageReader)
type_names.append('BVTK_NT_ImageReader')


# --------------------------------------------------------------


class BVTK_NT_XMLGenericDataObjectReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLGenericDataObjectReader'
    bl_label = 'vtkXMLGenericDataObjectReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLGenericDataObjectReader)
type_names.append('BVTK_NT_XMLGenericDataObjectReader')


# --------------------------------------------------------------


class BVTK_NT_UnstructuredGridReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_UnstructuredGridReader'
    bl_label = 'vtkUnstructuredGridReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_UnstructuredGridReader)
type_names.append('BVTK_NT_UnstructuredGridReader')


# --------------------------------------------------------------


class BVTK_NT_PolyDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PolyDataReader'
    bl_label = 'vtkPolyDataReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PolyDataReader)
type_names.append('BVTK_NT_PolyDataReader')


# --------------------------------------------------------------


class BVTK_NT_DelimitedTextReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DelimitedTextReader'
    bl_label = 'vtkDelimitedTextReader'
    
    m_AddTabFieldDelimiter = bpy.props.BoolProperty(name='AddTabFieldDelimiter', description="If on, also add in the tab (i.e. '\\t') character as a field delimiter. We add this specially since applications may have a more difficult time doing this. Defaults to off", default=False)
    m_DefaultDoubleValue = bpy.props.FloatProperty(name='DefaultDoubleValue', description='When DetectNumericColumns is set to true, the reader use this value to populate the vtkDoubleArray where empty strings are found. Default is 0.', default=0.0)
    m_DefaultIntegerValue = bpy.props.IntProperty(name='DefaultIntegerValue', description='When DetectNumericColumns is set to true, the reader use this value to populate the vtkIntArray where empty strings are found. Default is 0', default=0)
    m_DetectNumericColumns = bpy.props.BoolProperty(name='DetectNumericColumns', description='When set to true, the reader will detect numeric columns and create vtkDoubleArray or vtkIntArray for those instead of vtkStringArray. Default is off', default=False)
    m_FieldDelimiterCharacters = bpy.props.StringProperty(name='FieldDelimiterCharacters', description='Specify the character(s) that will be used to separate fields. For example, set this to "," for a comma-separated value file. Set it to ".:;" for a file where columns can be separated by a period, colon or semicolon. The order of the characters in the string does not matter. Defaults to a comma', default=',')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specifies the delimited text file to be loaded', subtype='FILE_PATH')
    m_ForceDouble = bpy.props.BoolProperty(name='ForceDouble', description='When set to true and DetectNumericColumns is also true, forces all numeric columns to vtkDoubleArray even if they contain only integer values. Default is off', default=False)
    m_GeneratePedigreeIds = bpy.props.BoolProperty(name='GeneratePedigreeIds', description='If on (default), generates pedigree ids automatically. If off, assign one of the arrays to be the pedigree id', default=True)
    m_HaveHeaders = bpy.props.BoolProperty(name='HaveHeaders', description='Set/get whether to treat the first line of the file as headers. The default is false (no headers)', default=False)
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_MaxRecords = bpy.props.IntProperty(name='MaxRecords', description='Specifies the maximum number of records to read from the file. Limiting the number of records to read is useful for previewing the contents of a file', default=0)
    m_MergeConsecutiveDelimiters = bpy.props.BoolProperty(name='MergeConsecutiveDelimiters', description="Set/get whether to merge successive delimiters. Use this if (for example) your fields are separated by spaces but you don't know exactly how many", default=False)
    m_OutputPedigreeIds = bpy.props.BoolProperty(name='OutputPedigreeIds', description='If on, assigns pedigree ids to output. Defaults to off', default=False)
    m_PedigreeIdArrayName = bpy.props.StringProperty(name='PedigreeIdArrayName', description='The name of the array for generating or assigning pedigree ids (default "id")', default='id')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ReplacementCharacter = bpy.props.IntProperty(name='ReplacementCharacter', description="Fallback character for use in the US-ASCII-WITH-FALLBACK character set. Any characters that have their 8th bit set will be replaced with this code point. Defaults to 'x'", default=120)
    m_StringDelimiter = bpy.props.StringProperty(name='StringDelimiter', description='Get/set the character that will begin and end strings. Microsoft Excel, for example, will export the following format', default='"')
    m_TrimWhitespacePriorToNumericConversion = bpy.props.BoolProperty(name='TrimWhitespacePriorToNumericConversion', description='When DetectNumericColumns is set to true, whether to trim whitespace from strings prior to conversion to a numeric. Default is false to preserve backward compatibility', default=False)
    m_UTF8FieldDelimiters = bpy.props.StringProperty(name='UTF8FieldDelimiters', description='', default=',')
    m_UTF8RecordDelimiters = bpy.props.StringProperty(name='UTF8RecordDelimiters', description='Specify the character(s) that will be used to separate records. The order of characters in the string does not matter. Defaults to "\\r\\n"', default='\r\n')
    m_UTF8StringDelimiters = bpy.props.StringProperty(name='UTF8StringDelimiters', description='', default='"')
    m_UnicodeCharacterSet = bpy.props.StringProperty(name='UnicodeCharacterSet', description='Specifies the character set used in the input file. Valid character set names will be drawn from the list maintained by the Internet Assigned Name Authority a')
    m_UnicodeFieldDelimiters = bpy.props.StringProperty(name='UnicodeFieldDelimiters', description='', default=',')
    m_UnicodeRecordDelimiters = bpy.props.StringProperty(name='UnicodeRecordDelimiters', description='Specify the character(s) that will be used to separate records. The order of characters in the string does not matter. Defaults to "\\r\\n"', default='\r\n')
    m_UnicodeStringDelimiters = bpy.props.StringProperty(name='UnicodeStringDelimiters', description='', default='"')
    m_UseStringDelimiter = bpy.props.BoolProperty(name='UseStringDelimiter', description='Set/get whether to use the string delimiter. Defaults to on', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=26, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AddTabFieldDelimiter', 'm_DefaultDoubleValue', 'm_DefaultIntegerValue', 'm_DetectNumericColumns', 'm_FieldDelimiterCharacters', 'm_FileName', 'm_ForceDouble', 'm_GeneratePedigreeIds', 'm_HaveHeaders', 'm_InputString', 'm_MaxRecords', 'm_MergeConsecutiveDelimiters', 'm_OutputPedigreeIds', 'm_PedigreeIdArrayName', 'm_ReadFromInputString', 'm_ReplacementCharacter', 'm_StringDelimiter', 'm_TrimWhitespacePriorToNumericConversion', 'm_UTF8FieldDelimiters', 'm_UTF8RecordDelimiters', 'm_UTF8StringDelimiters', 'm_UnicodeCharacterSet', 'm_UnicodeFieldDelimiters', 'm_UnicodeRecordDelimiters', 'm_UnicodeStringDelimiters', 'm_UseStringDelimiter', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DelimitedTextReader)
type_names.append('BVTK_NT_DelimitedTextReader')


# --------------------------------------------------------------


class BVTK_NT_DataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataReader'
    bl_label = 'vtkDataReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataReader)
type_names.append('BVTK_NT_DataReader')


# --------------------------------------------------------------


class BVTK_NT_CompositeDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CompositeDataReader'
    bl_label = 'vtkCompositeDataReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CompositeDataReader)
type_names.append('BVTK_NT_CompositeDataReader')


# --------------------------------------------------------------


class BVTK_NT_AVSucdReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AVSucdReader'
    bl_label = 'vtkAVSucdReader'
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    
    m_BinaryFile = bpy.props.BoolProperty(name='BinaryFile', description='Is the file to be read written in binary format (as opposed to ascii)', default=True)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description='', default='BigEndian', items=e_ByteOrder_items)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of AVS UCD datafile to rea', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BinaryFile', 'e_ByteOrder', 'm_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AVSucdReader)
type_names.append('BVTK_NT_AVSucdReader')


# --------------------------------------------------------------


class BVTK_NT_GraphReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GraphReader'
    bl_label = 'vtkGraphReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GraphReader)
type_names.append('BVTK_NT_GraphReader')


# --------------------------------------------------------------


class BVTK_NT_MNIObjectReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MNIObjectReader'
    bl_label = 'vtkMNIObjectReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set the file name', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MNIObjectReader)
type_names.append('BVTK_NT_MNIObjectReader')


# --------------------------------------------------------------


class BVTK_NT_RectilinearGridReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RectilinearGridReader'
    bl_label = 'vtkRectilinearGridReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RectilinearGridReader)
type_names.append('BVTK_NT_RectilinearGridReader')


# --------------------------------------------------------------


class BVTK_NT_ArrayDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ArrayDataReader'
    bl_label = 'vtkArrayDataReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set the filesystem location from which data will be read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='The input string to parse. If you set the input string, you must also set the ReadFromInputString flag to parse the string instead of a file', default='')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Whether to read from an input string as opposed to a file, which is the default', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_InputString', 'm_ReadFromInputString', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ArrayDataReader)
type_names.append('BVTK_NT_ArrayDataReader')


# --------------------------------------------------------------


class BVTK_NT_Volume16Reader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Volume16Reader'
    bl_label = 'vtkVolume16Reader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataDimensions = bpy.props.IntVectorProperty(name='DataDimensions', description='Specify the dimensions for the data', default=[0, 0], size=2)
    m_DataMask = bpy.props.IntProperty(name='DataMask', description='Specify a mask used to eliminate data in the data file (e.g., connectivity bits)', default=0)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='Specify the origin for the data', default=[0.0, 0.0, 0.0], size=3)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='Specify the spacing for the data', default=[1.0, 1.0, 1.0], size=3)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s)')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='Specify the number of bytes to seek over at start of image', default=0)
    m_ImageRange = bpy.props.IntVectorProperty(name='ImageRange', description='Set the range of files to read', default=[1, 1], size=2)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Turn on/off byte swapping', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataDimensions', 'm_DataMask', 'm_DataOrigin', 'm_DataSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_ImageRange', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], ['Transform'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Volume16Reader)
type_names.append('BVTK_NT_Volume16Reader')


# --------------------------------------------------------------


class BVTK_NT_Plot3DMetaReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Plot3DMetaReader'
    bl_label = 'vtkPlot3DMetaReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set/Get the meta PLOT3D filename. See the class documentation for format details', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Plot3DMetaReader)
type_names.append('BVTK_NT_Plot3DMetaReader')


# --------------------------------------------------------------


class BVTK_NT_XYZMolReader2(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XYZMolReader2'
    bl_label = 'vtkXYZMolReader2'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the XYZ Molecule fil', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XYZMolReader2)
type_names.append('BVTK_NT_XYZMolReader2')


# --------------------------------------------------------------


class BVTK_NT_AMRFlashReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AMRFlashReader'
    bl_label = 'vtkAMRFlashReader'
    
    m_EnableCaching = bpy.props.BoolProperty(name='EnableCaching', description='Set/Get Reader caching propert', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='See vtkAMRBaseReader::SetFileNam', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_EnableCaching', 'm_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AMRFlashReader)
type_names.append('BVTK_NT_AMRFlashReader')


# --------------------------------------------------------------


class BVTK_NT_XMLTreeReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLTreeReader'
    bl_label = 'vtkXMLTreeReader'
    
    m_EdgePedigreeIdArrayName = bpy.props.StringProperty(name='EdgePedigreeIdArrayName', description='The name of the edge pedigree ids. Default is "edge id"', default='edge id')
    m_FileName = bpy.props.StringProperty(name='FileName', description='If set, reads in the XML file specified', subtype='FILE_PATH')
    m_GenerateEdgePedigreeIds = bpy.props.BoolProperty(name='GenerateEdgePedigreeIds', description='Set whether to use an property from the XML file as pedigree ids (off), or generate a new array with integer values starting at zero (on). Default is on', default=True)
    m_GenerateVertexPedigreeIds = bpy.props.BoolProperty(name='GenerateVertexPedigreeIds', description='Set whether to use an property from the XML file as pedigree ids (off), or generate a new array with integer values starting at zero (on). Default is on', default=True)
    m_MaskArrays = bpy.props.BoolProperty(name='MaskArrays', description='If on, makes bit arrays for each attribute with name .valid.attribute_name for each attribute. Default is off', default=False)
    m_ReadCharData = bpy.props.BoolProperty(name='ReadCharData', description='If on, stores the XML character data (i.e. textual data between tags) into an array named CharDataField, otherwise this field is skipped. Default is off', default=False)
    m_ReadTagName = bpy.props.BoolProperty(name='ReadTagName', description='If on, stores the XML tag name data in a field called .tagname otherwise this field is skipped. Default is on', default=True)
    m_VertexPedigreeIdArrayName = bpy.props.StringProperty(name='VertexPedigreeIdArrayName', description='The name of the vertex pedigree ids. Default is "vertex id"', default='vertex id')
    m_XMLString = bpy.props.StringProperty(name='XMLString', description='If set, and FileName is not set, reads in the XML string')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_EdgePedigreeIdArrayName', 'm_FileName', 'm_GenerateEdgePedigreeIds', 'm_GenerateVertexPedigreeIds', 'm_MaskArrays', 'm_ReadCharData', 'm_ReadTagName', 'm_VertexPedigreeIdArrayName', 'm_XMLString', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLTreeReader)
type_names.append('BVTK_NT_XMLTreeReader')


# --------------------------------------------------------------


class BVTK_NT_NIFTIImageReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_NIFTIImageReader'
    bl_label = 'vtkNIFTIImageReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_PlanarRGB = bpy.props.BoolProperty(name='PlanarRGB', description='Read planar RGB (separate R, G, and B planes), rather than packed RGB. The NIFTI format should always use packed RGB. The Analyze format, however, was used to store both planar RGB and packed RGB depending on the software, without any indication in the header about which convention was being used. Use this if you have a planar RGB file', default=False)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    m_TimeAsVector = bpy.props.BoolProperty(name='TimeAsVector', description='Read the time dimension as scalar components (default: Off). If this is on, then each time point will be stored as a component in the image data. If the file has both a time dimension and a vector dimension, then the number of components will be the product of these two dimensions, i.e. the components will store a sequence of vectors', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_PlanarRGB', 'm_SwapBytes', 'm_TimeAsVector', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_NIFTIImageReader)
type_names.append('BVTK_NT_NIFTIImageReader')


# --------------------------------------------------------------


class BVTK_NT_XMLUniformGridAMRReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLUniformGridAMRReader'
    bl_label = 'vtkXMLUniformGridAMRReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_MaximumLevelsToReadByDefault = bpy.props.IntProperty(name='MaximumLevelsToReadByDefault', description="This reader supports demand-driven heavy data reading i.e. downstream pipeline can request specific blocks from the AMR using vtkCompositeDataPipeline::UPDATE_COMPOSITE_INDICES() key in RequestUpdateExtent() pass. However, when down-stream doesn't provide any specific keys, the default behavior can be setup to read at-most N levels by default. The number of levels read can be set using this method. Set this to 0 to imply no limit. Default is 0", default=1)
    m_PieceDistribution = bpy.props.IntProperty(name='PieceDistribution', description='', default=0)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_MaximumLevelsToReadByDefault', 'm_PieceDistribution', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLUniformGridAMRReader)
type_names.append('BVTK_NT_XMLUniformGridAMRReader')


# --------------------------------------------------------------


class BVTK_NT_XMLMultiGroupDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLMultiGroupDataReader'
    bl_label = 'vtkXMLMultiGroupDataReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_PieceDistribution = bpy.props.IntProperty(name='PieceDistribution', description='', default=0)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_PieceDistribution', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLMultiGroupDataReader)
type_names.append('BVTK_NT_XMLMultiGroupDataReader')


# --------------------------------------------------------------


class BVTK_NT_MFIXReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MFIXReader'
    bl_label = 'vtkMFIXReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify the file name of the MFIX Restart data file to read', subtype='FILE_PATH')
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MFIXReader)
type_names.append('BVTK_NT_MFIXReader')


# --------------------------------------------------------------


class BVTK_NT_EnSightGoldBinaryReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EnSightGoldBinaryReader'
    bl_label = 'vtkEnSightGoldBinaryReader'
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description='Set the byte order of the file (remember, more Unix workstations write big endian whereas PCs write little endian). Default is big endian (since most older PLOT3D files were written by workstations)', items=e_ByteOrder_items)
    m_CaseFileName = bpy.props.StringProperty(name='CaseFileName', description='Set/Get the Case file name', subtype='FILE_PATH')
    m_FilePath = bpy.props.StringProperty(name='FilePath', description='Set/Get the file path')
    m_ParticleCoordinatesByIndex = bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', description="The MeasuredGeometryFile should list particle coordinates from 0->N-1. If a file is loaded where point Ids are listed from 1-N the Id to points reference will be wrong and the data will be generated incorrectly. Setting ParticleCoordinatesByIndex to true will force all Id's to increment from 0->N-1 (relative to their order in the file) and regardless of the actual Id of of the point. Warning, if the Points are listed in non sequential order then setting this flag will reorder them", default=True)
    m_ReadAllVariables = bpy.props.BoolProperty(name='ReadAllVariables', description='Set/get the flag for whether to read all the variable', default=True)
    m_TimeValue = bpy.props.FloatProperty(name='TimeValue', description='Set/Get the time value at which to get the value', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ByteOrder', 'm_CaseFileName', 'm_FilePath', 'm_ParticleCoordinatesByIndex', 'm_ReadAllVariables', 'm_TimeValue', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EnSightGoldBinaryReader)
type_names.append('BVTK_NT_EnSightGoldBinaryReader')


# --------------------------------------------------------------


class BVTK_NT_MedicalImageReader2(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MedicalImageReader2'
    bl_label = 'vtkMedicalImageReader2'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_Date = bpy.props.StringProperty(name='Date', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_ImageNumber = bpy.props.StringProperty(name='ImageNumber', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_Modality = bpy.props.StringProperty(name='Modality', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_PatientID = bpy.props.StringProperty(name='PatientID', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_PatientName = bpy.props.StringProperty(name='PatientName', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_Series = bpy.props.StringProperty(name='Series', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_Study = bpy.props.StringProperty(name='Study', description='For backward compatibility, propagate calls to the MedicalImageProperties object')
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=22, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_Date', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_ImageNumber', 'm_MemoryBufferLength', 'm_Modality', 'm_NumberOfScalarComponents', 'm_PatientID', 'm_PatientName', 'm_Series', 'm_Study', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MedicalImageReader2)
type_names.append('BVTK_NT_MedicalImageReader2')


# --------------------------------------------------------------


class BVTK_NT_GAMBITReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GAMBITReader'
    bl_label = 'vtkGAMBITReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify the file name of the GAMBIT data file to read', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GAMBITReader)
type_names.append('BVTK_NT_GAMBITReader')


# --------------------------------------------------------------


class BVTK_NT_XMLHierarchicalDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLHierarchicalDataReader'
    bl_label = 'vtkXMLHierarchicalDataReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_PieceDistribution = bpy.props.IntProperty(name='PieceDistribution', description='', default=0)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_PieceDistribution', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLHierarchicalDataReader)
type_names.append('BVTK_NT_XMLHierarchicalDataReader')


# --------------------------------------------------------------


class BVTK_NT_WindBladeReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_WindBladeReader'
    bl_label = 'vtkWindBladeReader'
    
    m_Filename = bpy.props.StringProperty(name='Filename', description='')
    m_SubExtent = bpy.props.IntVectorProperty(name='SubExtent', description='', default=[32513584, 1, 53909040, 1, 377672688, 1], size=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Filename', 'm_SubExtent', ]
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1', 'Output 2'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_WindBladeReader)
type_names.append('BVTK_NT_WindBladeReader')


# --------------------------------------------------------------


class BVTK_NT_BMPReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BMPReader'
    bl_label = 'vtkBMPReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    m_Allow8BitBMP = bpy.props.BoolProperty(name='Allow8BitBMP', description='If this flag is set and the BMP reader encounters an 8bit file, the data will be kept as unsigned chars and a lookuptable will be exporte', default=True)
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataMask = bpy.props.IntProperty(name='DataMask', description="Set/Get the Data mask. The data mask is a simply integer whose bits are treated as a mask to the bits read from disk. That is, the data mask is bitwise-and'ed to the numbers read from disk. This ivar is stored as 64 bits, the largest mask you will need. The mask will be truncated to the data size required to be read (using the least significant bits)", default=1000000000)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_DataVOI = bpy.props.IntVectorProperty(name='DataVOI', description='', default=[0, 0, 0, 0, 0, 0], size=6)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_ScalarArrayName = bpy.props.StringProperty(name='ScalarArrayName', description='Set/get the scalar array name for this data set', default='ImageFile')
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=19, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Allow8BitBMP', 'e_DataByteOrder', 'm_DataMask', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_DataVOI', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_ScalarArrayName', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], ['Transform'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BMPReader)
type_names.append('BVTK_NT_BMPReader')


# --------------------------------------------------------------


class BVTK_NT_ArrayReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ArrayReader'
    bl_label = 'vtkArrayReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set the filesystem location from which data will be read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='The input string to parse. If you set the input string, you must also set the ReadFromInputString flag to parse the string instead of a file', default='')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Whether to read from an input string as opposed to a file, which is the default', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_InputString', 'm_ReadFromInputString', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ArrayReader)
type_names.append('BVTK_NT_ArrayReader')


# --------------------------------------------------------------


class BVTK_NT_StructuredPointsReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_StructuredPointsReader'
    bl_label = 'vtkStructuredPointsReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_StructuredPointsReader)
type_names.append('BVTK_NT_StructuredPointsReader')


# --------------------------------------------------------------


class BVTK_NT_MetaImageReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MetaImageReader'
    bl_label = 'vtkMetaImageReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MetaImageReader)
type_names.append('BVTK_NT_MetaImageReader')


# --------------------------------------------------------------


class BVTK_NT_EnSight6Reader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EnSight6Reader'
    bl_label = 'vtkEnSight6Reader'
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description='Set the byte order of the file (remember, more Unix workstations write big endian whereas PCs write little endian). Default is big endian (since most older PLOT3D files were written by workstations)', items=e_ByteOrder_items)
    m_CaseFileName = bpy.props.StringProperty(name='CaseFileName', description='Set/Get the Case file name', subtype='FILE_PATH')
    m_FilePath = bpy.props.StringProperty(name='FilePath', description='Set/Get the file path')
    m_ParticleCoordinatesByIndex = bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', description="The MeasuredGeometryFile should list particle coordinates from 0->N-1. If a file is loaded where point Ids are listed from 1-N the Id to points reference will be wrong and the data will be generated incorrectly. Setting ParticleCoordinatesByIndex to true will force all Id's to increment from 0->N-1 (relative to their order in the file) and regardless of the actual Id of of the point. Warning, if the Points are listed in non sequential order then setting this flag will reorder them", default=True)
    m_ReadAllVariables = bpy.props.BoolProperty(name='ReadAllVariables', description='Set/get the flag for whether to read all the variable', default=True)
    m_TimeValue = bpy.props.FloatProperty(name='TimeValue', description='Set/Get the time value at which to get the value', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ByteOrder', 'm_CaseFileName', 'm_FilePath', 'm_ParticleCoordinatesByIndex', 'm_ReadAllVariables', 'm_TimeValue', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EnSight6Reader)
type_names.append('BVTK_NT_EnSight6Reader')


# --------------------------------------------------------------


class BVTK_NT_PTSReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PTSReader'
    bl_label = 'vtkPTSReader'
    
    m_CreateCells = bpy.props.BoolProperty(name='CreateCells', description='Boolean value indicates whether or not to create cells for this dataset. Otherwise only points and scalars are created. Defaults to true', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name', subtype='FILE_PATH')
    m_IncludeColorAndLuminance = bpy.props.BoolProperty(name='IncludeColorAndLuminance', description='Boolean value indicates when color values are present if luminance should be read in as well Defaults to true', default=True)
    m_LimitReadToBounds = bpy.props.BoolProperty(name='LimitReadToBounds', description='Boolean value indicates whether or not to limit points read to a specified (ReadBounds) region', default=False)
    m_LimitToMaxNumberOfPoints = bpy.props.BoolProperty(name='LimitToMaxNumberOfPoints', description='Boolean value indicates whether or not to limit number of points read based on MaxNumbeOfPoints', default=False)
    m_MaxNumberOfPoints = bpy.props.IntProperty(name='MaxNumberOfPoints', description='The maximum number of points to load if LimitToMaxNumberOfPoints is on/true. Sets a temporary onRatio', default=1000000)
    m_OutputDataTypeIsDouble = bpy.props.BoolProperty(name='OutputDataTypeIsDouble', description='The output type defaults to float, but can instead be double', default=False)
    m_ReadBounds = bpy.props.FloatVectorProperty(name='ReadBounds', description='', default=[1e+30, -1e+30, 1e+30, -1e+30, 1e+30, -1e+30], size=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CreateCells', 'm_FileName', 'm_IncludeColorAndLuminance', 'm_LimitReadToBounds', 'm_LimitToMaxNumberOfPoints', 'm_MaxNumberOfPoints', 'm_OutputDataTypeIsDouble', 'm_ReadBounds', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PTSReader)
type_names.append('BVTK_NT_PTSReader')


# --------------------------------------------------------------


class BVTK_NT_XMLPRectilinearGridReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLPRectilinearGridReader'
    bl_label = 'vtkXMLPRectilinearGridReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLPRectilinearGridReader)
type_names.append('BVTK_NT_XMLPRectilinearGridReader')


# --------------------------------------------------------------


class BVTK_NT_PDBReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PDBReader'
    bl_label = 'vtkPDBReader'
    
    m_BScale = bpy.props.FloatProperty(name='BScale', description='A scaling factor to compute bonds between non-hydrogen atom', default=1.0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='', subtype='FILE_PATH')
    m_HBScale = bpy.props.FloatProperty(name='HBScale', description='A scaling factor to compute bonds with hydrogen atoms', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BScale', 'm_FileName', 'm_HBScale', ]
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PDBReader)
type_names.append('BVTK_NT_PDBReader')


# --------------------------------------------------------------


class BVTK_NT_EnSight6BinaryReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EnSight6BinaryReader'
    bl_label = 'vtkEnSight6BinaryReader'
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description='Set the byte order of the file (remember, more Unix workstations write big endian whereas PCs write little endian). Default is big endian (since most older PLOT3D files were written by workstations)', items=e_ByteOrder_items)
    m_CaseFileName = bpy.props.StringProperty(name='CaseFileName', description='Set/Get the Case file name', subtype='FILE_PATH')
    m_FilePath = bpy.props.StringProperty(name='FilePath', description='Set/Get the file path')
    m_ParticleCoordinatesByIndex = bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', description="The MeasuredGeometryFile should list particle coordinates from 0->N-1. If a file is loaded where point Ids are listed from 1-N the Id to points reference will be wrong and the data will be generated incorrectly. Setting ParticleCoordinatesByIndex to true will force all Id's to increment from 0->N-1 (relative to their order in the file) and regardless of the actual Id of of the point. Warning, if the Points are listed in non sequential order then setting this flag will reorder them", default=True)
    m_ReadAllVariables = bpy.props.BoolProperty(name='ReadAllVariables', description='Set/get the flag for whether to read all the variable', default=True)
    m_TimeValue = bpy.props.FloatProperty(name='TimeValue', description='Set/Get the time value at which to get the value', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ByteOrder', 'm_CaseFileName', 'm_FilePath', 'm_ParticleCoordinatesByIndex', 'm_ReadAllVariables', 'm_TimeValue', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EnSight6BinaryReader)
type_names.append('BVTK_NT_EnSight6BinaryReader')


# --------------------------------------------------------------


class BVTK_NT_CPExodusIIInSituReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CPExodusIIInSituReader'
    bl_label = 'vtkCPExodusIIInSituReader'
    
    m_CurrentTimeStep = bpy.props.IntProperty(name='CurrentTimeStep', description='Get/Set the current timestep to read as a zero-based index', default=0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the Exodus file to read', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CurrentTimeStep', 'm_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CPExodusIIInSituReader)
type_names.append('BVTK_NT_CPExodusIIInSituReader')


# --------------------------------------------------------------


class BVTK_NT_TecplotTableReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TecplotTableReader'
    bl_label = 'vtkTecplotTableReader'
    
    m_ColumnNamesOnLine = bpy.props.IntProperty(name='ColumnNamesOnLine', description='Specifies the line number that holds the column names. Default is 1', default=1)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specifies the delimited text file to be loaded', subtype='FILE_PATH')
    m_GeneratePedigreeIds = bpy.props.BoolProperty(name='GeneratePedigreeIds', description='If on (default), generates pedigree ids automatically. If off, assign one of the arrays to be the pedigree id', default=False)
    m_HeaderLines = bpy.props.IntProperty(name='HeaderLines', description='Specifies the number of lines that form the header of the file. Default is 2', default=2)
    m_MaxRecords = bpy.props.IntProperty(name='MaxRecords', description='Specifies the maximum number of records to read from the file. Limiting the number of records to read is useful for previewing the contents of a file', default=0)
    m_OutputPedigreeIds = bpy.props.BoolProperty(name='OutputPedigreeIds', description='If on, assigns pedigree ids to output. Defaults to off', default=False)
    m_PedigreeIdArrayName = bpy.props.StringProperty(name='PedigreeIdArrayName', description='The name of the array for generating or assigning pedigree ids (default "id")', default='id')
    m_SkipColumnNames = bpy.props.IntProperty(name='SkipColumnNames', description='Specifies the number of fields to skip while reading the column names. Default is 1', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ColumnNamesOnLine', 'm_FileName', 'm_GeneratePedigreeIds', 'm_HeaderLines', 'm_MaxRecords', 'm_OutputPedigreeIds', 'm_PedigreeIdArrayName', 'm_SkipColumnNames', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TecplotTableReader)
type_names.append('BVTK_NT_TecplotTableReader')


# --------------------------------------------------------------


class BVTK_NT_XMLPPolyDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLPPolyDataReader'
    bl_label = 'vtkXMLPPolyDataReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLPPolyDataReader)
type_names.append('BVTK_NT_XMLPPolyDataReader')


# --------------------------------------------------------------


class BVTK_NT_OBJReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_OBJReader'
    bl_label = 'vtkOBJReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of AbstractPolyData file (obj / ply / stl)', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_OBJReader)
type_names.append('BVTK_NT_OBJReader')


# --------------------------------------------------------------


class BVTK_NT_NrrdReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_NrrdReader'
    bl_label = 'vtkNrrdReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataMask = bpy.props.IntProperty(name='DataMask', description="Set/Get the Data mask. The data mask is a simply integer whose bits are treated as a mask to the bits read from disk. That is, the data mask is bitwise-and'ed to the numbers read from disk. This ivar is stored as 64 bits, the largest mask you will need. The mask will be truncated to the data size required to be read (using the least significant bits)", default=1000000000)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_DataVOI = bpy.props.IntVectorProperty(name='DataVOI', description='', default=[0, 0, 0, 0, 0, 0], size=6)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_ScalarArrayName = bpy.props.StringProperty(name='ScalarArrayName', description='Set/get the scalar array name for this data set', default='ImageFile')
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataMask', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_DataVOI', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_ScalarArrayName', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], ['Transform'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_NrrdReader)
type_names.append('BVTK_NT_NrrdReader')


# --------------------------------------------------------------


class BVTK_NT_GaussianCubeReader2(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GaussianCubeReader2'
    bl_label = 'vtkGaussianCubeReader2'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the CML fil', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GaussianCubeReader2)
type_names.append('BVTK_NT_GaussianCubeReader2')


# --------------------------------------------------------------


class BVTK_NT_XMLHierarchicalBoxDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLHierarchicalBoxDataReader'
    bl_label = 'vtkXMLHierarchicalBoxDataReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_MaximumLevelsToReadByDefault = bpy.props.IntProperty(name='MaximumLevelsToReadByDefault', description="This reader supports demand-driven heavy data reading i.e. downstream pipeline can request specific blocks from the AMR using vtkCompositeDataPipeline::UPDATE_COMPOSITE_INDICES() key in RequestUpdateExtent() pass. However, when down-stream doesn't provide any specific keys, the default behavior can be setup to read at-most N levels by default. The number of levels read can be set using this method. Set this to 0 to imply no limit. Default is 0", default=1)
    m_PieceDistribution = bpy.props.IntProperty(name='PieceDistribution', description='', default=0)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_MaximumLevelsToReadByDefault', 'm_PieceDistribution', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLHierarchicalBoxDataReader)
type_names.append('BVTK_NT_XMLHierarchicalBoxDataReader')


# --------------------------------------------------------------


class BVTK_NT_JPEGReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_JPEGReader'
    bl_label = 'vtkJPEGReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_JPEGReader)
type_names.append('BVTK_NT_JPEGReader')


# --------------------------------------------------------------


class BVTK_NT_POpenFOAMReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_POpenFOAMReader'
    bl_label = 'vtkPOpenFOAMReader'
    
    m_AddDimensionsToArrayNames = bpy.props.BoolProperty(name='AddDimensionsToArrayNames', description='Add dimensions to array name', default=True)
    m_CacheMesh = bpy.props.BoolProperty(name='CacheMesh', description='Set/Get whether mesh is to be cached', default=True)
    m_CreateCellToPoint = bpy.props.BoolProperty(name='CreateCellToPoint', description='Set/Get whether to create cell-to-point translated data for cell-type dat', default=True)
    m_DecomposePolyhedra = bpy.props.BoolProperty(name='DecomposePolyhedra', description='Set/Get whether polyhedra are to be decomposed', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set/Get the filename', subtype='FILE_PATH')
    m_ListTimeStepsByControlDict = bpy.props.BoolProperty(name='ListTimeStepsByControlDict', description='Determine if time directories are to be listed according to controlDic', default=True)
    m_PositionsIsIn13Format = bpy.props.BoolProperty(name='PositionsIsIn13Format', description='Set/Get whether the lagrangian/positions have additional data or not. For historical reasons, PositionsIsIn13Format is used to denote that the positions only have x,y,z value and the cell of the enclosing cell. In OpenFOAM 1.4-2.4, positions included facei and stepFraction information', default=True)
    m_ReadZones = bpy.props.BoolProperty(name='ReadZones', description='Set/Get whether zones will be read', default=True)
    m_SkipZeroTime = bpy.props.BoolProperty(name='SkipZeroTime', description='Ignore 0/ time directory, which is normally missing Lagrangian fields and may have many dictionary functionality that we cannot easily handle', default=False)
    m_Use64BitFloats = bpy.props.BoolProperty(name='Use64BitFloats', description='If true, floats are expected to be 64-bit, rather than 32. Note that vtkFloatArrays may still be used in the output if this is true. This flag is only used to ensure that binary data is correctly parsed', default=True)
    m_Use64BitLabels = bpy.props.BoolProperty(name='Use64BitLabels', description='If true, labels are expected to be 64-bit, rather than 32', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AddDimensionsToArrayNames', 'm_CacheMesh', 'm_CreateCellToPoint', 'm_DecomposePolyhedra', 'm_FileName', 'm_ListTimeStepsByControlDict', 'm_PositionsIsIn13Format', 'm_ReadZones', 'm_SkipZeroTime', 'm_Use64BitFloats', 'm_Use64BitLabels', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_POpenFOAMReader)
type_names.append('BVTK_NT_POpenFOAMReader')


# --------------------------------------------------------------


class BVTK_NT_TulipReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TulipReader'
    bl_label = 'vtkTulipReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='The Tulip file name', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TulipReader)
type_names.append('BVTK_NT_TulipReader')


# --------------------------------------------------------------


class BVTK_NT_MPASReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MPASReader'
    bl_label = 'vtkMPASReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of MPAS data file to read', subtype='FILE_PATH')
    m_IsAtmosphere = bpy.props.BoolProperty(name='IsAtmosphere', description='', default=False)
    m_IsZeroCentered = bpy.props.BoolProperty(name='IsZeroCentered', description='', default=False)
    m_LayerThickness = bpy.props.IntProperty(name='LayerThickness', description='', default=10000)
    m_ProjectLatLon = bpy.props.BoolProperty(name='ProjectLatLon', description='', default=False)
    m_ShowMultilayerView = bpy.props.BoolProperty(name='ShowMultilayerView', description='', default=False)
    m_UseDimensionedArrayNames = bpy.props.BoolProperty(name='UseDimensionedArrayNames', description='If true, dimension info is included in the array name. For instance, "tracers" will become "tracers(Time, nCells, nVertLevels, nTracers)". This is useful for user-visible array selection, but is disabled by default for backwards compatibility', default=False)
    m_VerticalDimension = bpy.props.StringProperty(name='VerticalDimension', description='Get/Set the name to the dimension that identifies the vertical dimension. Defaults to "nVertLevels"', default='nVertLevels')
    m_VerticalLevel = bpy.props.IntProperty(name='VerticalLevel', description='Convenience functon for setting/querying [GS]etDimensionCurrentIndex for the dimension returned by GetVerticalDimension', default=-1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_IsAtmosphere', 'm_IsZeroCentered', 'm_LayerThickness', 'm_ProjectLatLon', 'm_ShowMultilayerView', 'm_UseDimensionedArrayNames', 'm_VerticalDimension', 'm_VerticalLevel', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MPASReader)
type_names.append('BVTK_NT_MPASReader')


# --------------------------------------------------------------


class BVTK_NT_TIFFReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TIFFReader'
    bl_label = 'vtkTIFFReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_OrientationType = bpy.props.IntProperty(name='OrientationType', description='Set orientation type ORIENTATION_TOPLEFT 1 (row 0 top, col 0 lhs) ORIENTATION_TOPRIGHT 2 (row 0 top, col 0 rhs) ORIENTATION_BOTRIGHT 3 (row 0 bottom, col 0 rhs) ORIENTATION_BOTLEFT 4 (row 0 bottom, col 0 lhs) ORIENTATION_LEFTTOP 5 (row 0 lhs, col 0 top) ORIENTATION_RIGHTTOP 6 (row 0 rhs, col 0 top) ORIENTATION_RIGHTBOT 7 (row 0 rhs, col 0 bottom) ORIENTATION_LEFTBOT 8 (row 0 lhs, col 0 bottom) User need to explicitly include vtk_tiff.h header to have access to those #defin', default=4)
    m_OriginSpecifiedFlag = bpy.props.BoolProperty(name='OriginSpecifiedFlag', description='Set/get methods to see if manual origin has been set', default=False)
    m_SpacingSpecifiedFlag = bpy.props.BoolProperty(name='SpacingSpecifiedFlag', description='Set/get if the spacing flag has been specified', default=False)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_OrientationType', 'm_OriginSpecifiedFlag', 'm_SpacingSpecifiedFlag', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TIFFReader)
type_names.append('BVTK_NT_TIFFReader')


# --------------------------------------------------------------


class BVTK_NT_MRCReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MRCReader'
    bl_label = 'vtkMRCReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MRCReader)
type_names.append('BVTK_NT_MRCReader')


# --------------------------------------------------------------


class BVTK_NT_XMLTableReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLTableReader'
    bl_label = 'vtkXMLTableReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLTableReader)
type_names.append('BVTK_NT_XMLTableReader')


# --------------------------------------------------------------


class BVTK_NT_NetCDFCFReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_NetCDFCFReader'
    bl_label = 'vtkNetCDFCFReader'
    e_OutputType_items = [(x, x, x) for x in ['Automatic', 'Image', 'Rectilinear', 'Structured', 'Unstructured']]
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='', subtype='FILE_PATH')
    e_OutputType = bpy.props.EnumProperty(name='OutputType', description='Set/get the data type of the output. The index used is taken from the list of VTK data types in vtkType.h. Valid types are VTK_IMAGE_DATA, VTK_RECTILINEAR_GRID, VTK_STRUCTURED_GRID, and VTK_UNSTRUCTURED_GRID. In addition you can set the type to -1 (the default), and this reader will pick the data type best suited for the dimensions being read', default='Automatic', items=e_OutputType_items)
    m_ReplaceFillValueWithNan = bpy.props.BoolProperty(name='ReplaceFillValueWithNan', description='If on, any float or double variable read that has a _FillValue attribute will have that fill value replaced with a not-a-number (NaN) value. The advantage of setting these to NaN values is that, if implemented properly by the system and careful math operations are used, they can implicitly be ignored by calculations like finding the range of the values. That said, this option should be used with caution as VTK does not fully support NaN values and therefore odd calculations may occur. By default this is off', default=True)
    m_SphericalCoordinates = bpy.props.BoolProperty(name='SphericalCoordinates', description='If on (the default), then 3D data with latitude/longitude dimensions will be read in as curvilinear data shaped like spherical coordinates. If false, then the data will always be read in Cartesian coordinates', default=True)
    m_VerticalBias = bpy.props.FloatProperty(name='VerticalBias', description='The scale and bias of the vertical component of spherical coordinates. It is common to write the vertical component with respect to something other than the center of the sphere (for example, the surface). In this case, it might be necessary to scale and/or bias the vertical height. The height will become height*scale + bias. Keep in mind that if the positive attribute of the vertical dimension is down, then the height is negated. By default the scale is 1 and the bias is 0 (that is, no change). The scaling will be adjusted if it results in invalid (negative) vertical values', default=0.0)
    m_VerticalScale = bpy.props.FloatProperty(name='VerticalScale', description='The scale and bias of the vertical component of spherical coordinates. It is common to write the vertical component with respect to something other than the center of the sphere (for example, the surface). In this case, it might be necessary to scale and/or bias the vertical height. The height will become height*scale + bias. Keep in mind that if the positive attribute of the vertical dimension is down, then the height is negated. By default the scale is 1 and the bias is 0 (that is, no change). The scaling will be adjusted if it results in invalid (negative) vertical values', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'e_OutputType', 'm_ReplaceFillValueWithNan', 'm_SphericalCoordinates', 'm_VerticalBias', 'm_VerticalScale', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_NetCDFCFReader)
type_names.append('BVTK_NT_NetCDFCFReader')


# --------------------------------------------------------------


class BVTK_NT_STLReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_STLReader'
    bl_label = 'vtkSTLReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of AbstractPolyData file (obj / ply / stl)', subtype='FILE_PATH')
    m_Merging = bpy.props.BoolProperty(name='Merging', description='Turn on/off merging of points/triangles', default=True)
    m_ScalarTags = bpy.props.BoolProperty(name='ScalarTags', description='Turn on/off tagging of solids with scalars', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_Merging', 'm_ScalarTags', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_STLReader)
type_names.append('BVTK_NT_STLReader')


# --------------------------------------------------------------


class BVTK_NT_XMLUnstructuredGridReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLUnstructuredGridReader'
    bl_label = 'vtkXMLUnstructuredGridReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLUnstructuredGridReader)
type_names.append('BVTK_NT_XMLUnstructuredGridReader')


# --------------------------------------------------------------


class BVTK_NT_GaussianCubeReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GaussianCubeReader'
    bl_label = 'vtkGaussianCubeReader'
    
    m_BScale = bpy.props.FloatProperty(name='BScale', description='A scaling factor to compute bonds between non-hydrogen atom', default=1.0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='', subtype='FILE_PATH')
    m_HBScale = bpy.props.FloatProperty(name='HBScale', description='A scaling factor to compute bonds with hydrogen atoms', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BScale', 'm_FileName', 'm_HBScale', ]
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GaussianCubeReader)
type_names.append('BVTK_NT_GaussianCubeReader')


# --------------------------------------------------------------


class BVTK_NT_MNITagPointReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MNITagPointReader'
    bl_label = 'vtkMNITagPointReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set the file name', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MNITagPointReader)
type_names.append('BVTK_NT_MNITagPointReader')


# --------------------------------------------------------------


class BVTK_NT_NetCDFReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_NetCDFReader'
    bl_label = 'vtkNetCDFReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='', subtype='FILE_PATH')
    m_ReplaceFillValueWithNan = bpy.props.BoolProperty(name='ReplaceFillValueWithNan', description='If on, any float or double variable read that has a _FillValue attribute will have that fill value replaced with a not-a-number (NaN) value. The advantage of setting these to NaN values is that, if implemented properly by the system and careful math operations are used, they can implicitly be ignored by calculations like finding the range of the values. That said, this option should be used with caution as VTK does not fully support NaN values and therefore odd calculations may occur. By default this is off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReplaceFillValueWithNan', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_NetCDFReader)
type_names.append('BVTK_NT_NetCDFReader')


# --------------------------------------------------------------


class BVTK_NT_AMRFlashParticlesReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AMRFlashParticlesReader'
    bl_label = 'vtkAMRFlashParticlesReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='', subtype='FILE_PATH')
    m_FilterLocation = bpy.props.BoolProperty(name='FilterLocation', description='Set & Get for filter location and boolean macr', default=True)
    m_Frequency = bpy.props.IntProperty(name='Frequency', description='Set & Get the frequency', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_FilterLocation', 'm_Frequency', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AMRFlashParticlesReader)
type_names.append('BVTK_NT_AMRFlashParticlesReader')


# --------------------------------------------------------------


class BVTK_NT_PNMReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PNMReader'
    bl_label = 'vtkPNMReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataMask = bpy.props.IntProperty(name='DataMask', description="Set/Get the Data mask. The data mask is a simply integer whose bits are treated as a mask to the bits read from disk. That is, the data mask is bitwise-and'ed to the numbers read from disk. This ivar is stored as 64 bits, the largest mask you will need. The mask will be truncated to the data size required to be read (using the least significant bits)", default=1000000000)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_DataVOI = bpy.props.IntVectorProperty(name='DataVOI', description='', default=[0, 0, 0, 0, 0, 0], size=6)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_ScalarArrayName = bpy.props.StringProperty(name='ScalarArrayName', description='Set/get the scalar array name for this data set', default='ImageFile')
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataMask', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_DataVOI', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_ScalarArrayName', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], ['Transform'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PNMReader)
type_names.append('BVTK_NT_PNMReader')


# --------------------------------------------------------------


class BVTK_NT_ChacoGraphReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ChacoGraphReader'
    bl_label = 'vtkChacoGraphReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='The Chaco file name', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ChacoGraphReader)
type_names.append('BVTK_NT_ChacoGraphReader')


# --------------------------------------------------------------


class BVTK_NT_SLACParticleReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SLACParticleReader'
    bl_label = 'vtkSLACParticleReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SLACParticleReader)
type_names.append('BVTK_NT_SLACParticleReader')


# --------------------------------------------------------------


class BVTK_NT_DIMACSGraphReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DIMACSGraphReader'
    bl_label = 'vtkDIMACSGraphReader'
    
    m_EdgeAttributeArrayName = bpy.props.StringProperty(name='EdgeAttributeArrayName', description='Edge attribute array nam')
    m_FileName = bpy.props.StringProperty(name='FileName', description='The DIMACS file name', subtype='FILE_PATH')
    m_VertexAttributeArrayName = bpy.props.StringProperty(name='VertexAttributeArrayName', description='Vertex attribute array nam')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_EdgeAttributeArrayName', 'm_FileName', 'm_VertexAttributeArrayName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DIMACSGraphReader)
type_names.append('BVTK_NT_DIMACSGraphReader')


# --------------------------------------------------------------


class BVTK_NT_XMLPStructuredGridReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLPStructuredGridReader'
    bl_label = 'vtkXMLPStructuredGridReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLPStructuredGridReader)
type_names.append('BVTK_NT_XMLPStructuredGridReader')


# --------------------------------------------------------------


class BVTK_NT_SLCReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SLCReader'
    bl_label = 'vtkSLCReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SLCReader)
type_names.append('BVTK_NT_SLCReader')


# --------------------------------------------------------------


class BVTK_NT_ISIReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ISIReader'
    bl_label = 'vtkISIReader'
    
    m_Delimiter = bpy.props.StringProperty(name='Delimiter', description='Set/get the delimiter to be used for concatenating field data (default: ";"', default=';')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set/get the file to loa', subtype='FILE_PATH')
    m_MaxRecords = bpy.props.IntProperty(name='MaxRecords', description='Set/get the maximum number of records to read from the file (zero = unlimited', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Delimiter', 'm_FileName', 'm_MaxRecords', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ISIReader)
type_names.append('BVTK_NT_ISIReader')


# --------------------------------------------------------------


class BVTK_NT_PDataSetReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PDataSetReader'
    bl_label = 'vtkPDataSetReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='This file to open and read', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PDataSetReader)
type_names.append('BVTK_NT_PDataSetReader')


# --------------------------------------------------------------


class BVTK_NT_LSDynaReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LSDynaReader'
    bl_label = 'vtkLSDynaReader'
    
    m_DatabaseDirectory = bpy.props.StringProperty(name='DatabaseDirectory', description='Get/Set the directory containing the LS-Dyna database and determine whether it is valid', default='')
    m_DeformedMesh = bpy.props.BoolProperty(name='DeformedMesh', description='Should deflected coordinates be used, or should the mesh remain undeflected? By default, this is true but its value is ignored if the nodal "Deflected Coordinates" array is not set to be loaded', default=True)
    m_DeletedCellsAsGhostArray = bpy.props.BoolProperty(name='DeletedCellsAsGhostArray', description='Instead of removing the cells that are dead, hide them by setting the array as the ghost levels array', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the filename. The Set/GetFileName() routines are actually wrappers around the Set/GetDatabaseDirectory() members; the actual filename you choose is irrelevant -- only the directory name is used. This is done in order to accommodate ParaView', default='/d3plot', subtype='FILE_PATH')
    m_InputDeck = bpy.props.StringProperty(name='InputDeck', description='The name of the input deck corresponding to the current database. This is used to determine the part names associated with each material ID. This file may be in two formats: a valid LSDyna input deck or a short XML summary. If the file begins with "<?xml" then the summary format is used. Otherwise, the keyword format is used and a summary file will be created if write permissions exist in the directory containing the keyword file. The newly created summary will have ".k" or ".key" stripped from the end of the keyword filename and ".lsdyna" appended')
    m_RemoveDeletedCells = bpy.props.BoolProperty(name='RemoveDeletedCells', description='Should dead cells be removed from the mesh? Cells are marked dead by setting the corresponding entry in the cellarray "Death" to 0. Cells that are not dead have the corresponding entry in the cell array "Death" set to their material ID. By default, this is true but its value is ignored if the cell "Death" array is not set to be loaded. It is also ignored if the database\'s element deletion option is set to denote points(not cells) as deleted; in that case, "Death" will appear to be a point array', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Retrieve information about the time extents of the LS-Dyna database. Do not call these functions before setting the database directory and calling UpdateInformation()', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DatabaseDirectory', 'm_DeformedMesh', 'm_DeletedCellsAsGhostArray', 'm_FileName', 'm_InputDeck', 'm_RemoveDeletedCells', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LSDynaReader)
type_names.append('BVTK_NT_LSDynaReader')


# --------------------------------------------------------------


class BVTK_NT_NetCDFPOPReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_NetCDFPOPReader'
    bl_label = 'vtkNetCDFPOPReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='The file to ope', subtype='FILE_PATH')
    m_Stride = bpy.props.IntVectorProperty(name='Stride', description='', default=[1, 1, 1], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_Stride', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_NetCDFPOPReader)
type_names.append('BVTK_NT_NetCDFPOPReader')


# --------------------------------------------------------------


class BVTK_NT_PhyloXMLTreeReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PhyloXMLTreeReader'
    bl_label = 'vtkPhyloXMLTreeReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PhyloXMLTreeReader)
type_names.append('BVTK_NT_PhyloXMLTreeReader')


# --------------------------------------------------------------


class BVTK_NT_ChacoReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ChacoReader'
    bl_label = 'vtkChacoReader'
    
    m_BaseName = bpy.props.StringProperty(name='BaseName', description='Specify the base name of the Chaco files. The reader will try to open BaseName.coords and BaseName.graph')
    m_GenerateEdgeWeightArrays = bpy.props.BoolProperty(name='GenerateEdgeWeightArrays', description='Each edge in the Chaco file connects two vertices. The file may specify one or more weights for each edge. (The weight for an edge from vertex A to vertex B equals the weight from B to A.) Indicate with the following parameter whether this reader should create a cell array for each weight for every edge. Default is OFF', default=True)
    m_GenerateGlobalElementIdArray = bpy.props.BoolProperty(name='GenerateGlobalElementIdArray', description='Indicate whether this reader should create a cell array containing global IDs for the cells in the output vtkUnstructuredGrid. These cells represent the edges that were in the Chaco file. Each edge is a vtkLine. Default is ON', default=True)
    m_GenerateGlobalNodeIdArray = bpy.props.BoolProperty(name='GenerateGlobalNodeIdArray', description='Indicate whether this reader should create a point array of global IDs for the points in the output vtkUnstructuredGrid. These points are the vertices that were in the Chaco file. Global point IDs start at "1" for the first vertex in BaseName.coords and go up from there. Default is ON', default=True)
    m_GenerateVertexWeightArrays = bpy.props.BoolProperty(name='GenerateVertexWeightArrays', description='Indicate whether this reader should create a point array for each vertex weight in the Chaco file. Default is OFF', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BaseName', 'm_GenerateEdgeWeightArrays', 'm_GenerateGlobalElementIdArray', 'm_GenerateGlobalNodeIdArray', 'm_GenerateVertexWeightArrays', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ChacoReader)
type_names.append('BVTK_NT_ChacoReader')


# --------------------------------------------------------------


class BVTK_NT_XMLPolyDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLPolyDataReader'
    bl_label = 'vtkXMLPolyDataReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLPolyDataReader)
type_names.append('BVTK_NT_XMLPolyDataReader')


# --------------------------------------------------------------


class BVTK_NT_AMREnzoReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AMREnzoReader'
    bl_label = 'vtkAMREnzoReader'
    
    m_ConvertToCGS = bpy.props.BoolProperty(name='ConvertToCGS', description='Set/Get whether data should be converted to CG', default=True)
    m_EnableCaching = bpy.props.BoolProperty(name='EnableCaching', description='Set/Get Reader caching propert', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='See vtkAMRBaseReader::SetFileNam', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ConvertToCGS', 'm_EnableCaching', 'm_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AMREnzoReader)
type_names.append('BVTK_NT_AMREnzoReader')


# --------------------------------------------------------------


class BVTK_NT_SQLiteToTableReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SQLiteToTableReader'
    bl_label = 'vtkSQLiteToTableReader'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], ['Output'], ['Database'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SQLiteToTableReader)
type_names.append('BVTK_NT_SQLiteToTableReader')


# --------------------------------------------------------------


class BVTK_NT_XYZMolReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XYZMolReader'
    bl_label = 'vtkXYZMolReader'
    
    m_BScale = bpy.props.FloatProperty(name='BScale', description='A scaling factor to compute bonds between non-hydrogen atom', default=1.0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='', subtype='FILE_PATH')
    m_HBScale = bpy.props.FloatProperty(name='HBScale', description='A scaling factor to compute bonds with hydrogen atoms', default=1.0)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Set the current time step. It should be greater than 0 and smaller than MaxTimeStep', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BScale', 'm_FileName', 'm_HBScale', 'm_TimeStep', ]
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XYZMolReader)
type_names.append('BVTK_NT_XYZMolReader')


# --------------------------------------------------------------


class BVTK_NT_BYUReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BYUReader'
    bl_label = 'vtkBYUReader'
    
    m_DisplacementFileName = bpy.props.StringProperty(name='DisplacementFileName', description='Specify name of displacement FileName', subtype='FILE_PATH')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify name of geometry FileName (alias)', subtype='FILE_PATH')
    m_GeometryFileName = bpy.props.StringProperty(name='GeometryFileName', description='Specify name of geometry FileName', subtype='FILE_PATH')
    m_PartNumber = bpy.props.IntProperty(name='PartNumber', description='Set/Get the part number to be read', default=0)
    m_ReadDisplacement = bpy.props.BoolProperty(name='ReadDisplacement', description='Turn on/off the reading of the displacement file', default=True)
    m_ReadScalar = bpy.props.BoolProperty(name='ReadScalar', description='Turn on/off the reading of the scalar file', default=True)
    m_ReadTexture = bpy.props.BoolProperty(name='ReadTexture', description='Turn on/off the reading of the texture coordinate file. Specify name of geometry FileName', default=True)
    m_ScalarFileName = bpy.props.StringProperty(name='ScalarFileName', description='Specify name of scalar FileName', subtype='FILE_PATH')
    m_TextureFileName = bpy.props.StringProperty(name='TextureFileName', description='Specify name of texture coordinates FileName', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DisplacementFileName', 'm_FileName', 'm_GeometryFileName', 'm_PartNumber', 'm_ReadDisplacement', 'm_ReadScalar', 'm_ReadTexture', 'm_ScalarFileName', 'm_TextureFileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BYUReader)
type_names.append('BVTK_NT_BYUReader')


# --------------------------------------------------------------


class BVTK_NT_XGMLReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XGMLReader'
    bl_label = 'vtkXGMLReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='The XGML file name', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XGMLReader)
type_names.append('BVTK_NT_XGMLReader')


# --------------------------------------------------------------


class BVTK_NT_XMLPTableReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLPTableReader'
    bl_label = 'vtkXMLPTableReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLPTableReader)
type_names.append('BVTK_NT_XMLPTableReader')


# --------------------------------------------------------------


class BVTK_NT_DICOMImageReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DICOMImageReader'
    bl_label = 'vtkDICOMImageReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_DirectoryName = bpy.props.StringProperty(name='DirectoryName', description='Set the directory name for the reader to look in for DICOM files. If this method is used, the reader will try to find all the DICOM files in a directory. It will select the subset corresponding to the first series UID it stumbles across and it will try to build an ordered volume from them based on the slice number. The volume building will be upgraded to something more sophisticated in the future')
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set the filename for the file to read. If this method is used, the reader will only read a single file', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_DirectoryName', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DICOMImageReader)
type_names.append('BVTK_NT_DICOMImageReader')


# --------------------------------------------------------------


class BVTK_NT_XMLPUnstructuredGridReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLPUnstructuredGridReader'
    bl_label = 'vtkXMLPUnstructuredGridReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLPUnstructuredGridReader)
type_names.append('BVTK_NT_XMLPUnstructuredGridReader')


# --------------------------------------------------------------


class BVTK_NT_XMLImageDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLImageDataReader'
    bl_label = 'vtkXMLImageDataReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    m_WholeSlices = bpy.props.BoolProperty(name='WholeSlices', description='Get/Set whether the reader gets a whole slice from disk when only a rectangle inside it is needed. This mode reads more data than necessary, but prevents many short reads from interacting poorly with the compression and encoding schemes', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', 'm_WholeSlices', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLImageDataReader)
type_names.append('BVTK_NT_XMLImageDataReader')


# --------------------------------------------------------------


class BVTK_NT_NewickTreeReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_NewickTreeReader'
    bl_label = 'vtkNewickTreeReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_NewickTreeReader)
type_names.append('BVTK_NT_NewickTreeReader')


# --------------------------------------------------------------


class BVTK_NT_MINCImageReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MINCImageReader'
    bl_label = 'vtkMINCImageReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set the file name', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_RescaleRealValues = bpy.props.BoolProperty(name='RescaleRealValues', description='Rescale real data values to float. If this is done, the RescaleSlope and RescaleIntercept will be set to 1 and 0 respectively. This is off by default', default=True)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Set the time step to read', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_RescaleRealValues', 'm_SwapBytes', 'm_TimeStep', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_MINCImageReader)
type_names.append('BVTK_NT_MINCImageReader')


# --------------------------------------------------------------


class BVTK_NT_AMREnzoParticlesReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AMREnzoParticlesReader'
    bl_label = 'vtkAMREnzoParticlesReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='', subtype='FILE_PATH')
    m_FilterLocation = bpy.props.BoolProperty(name='FilterLocation', description='Set & Get for filter location and boolean macr', default=True)
    m_Frequency = bpy.props.IntProperty(name='Frequency', description='Set & Get the frequency', default=1)
    m_ParticleType = bpy.props.IntProperty(name='ParticleType', description='Returns the requested particle type', default=-1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_FilterLocation', 'm_Frequency', 'm_ParticleType', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AMREnzoParticlesReader)
type_names.append('BVTK_NT_AMREnzoParticlesReader')


# --------------------------------------------------------------


class BVTK_NT_GenericEnSightReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GenericEnSightReader'
    bl_label = 'vtkGenericEnSightReader'
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description='Set the byte order of the file (remember, more Unix workstations write big endian whereas PCs write little endian). Default is big endian (since most older PLOT3D files were written by workstations)', items=e_ByteOrder_items)
    m_CaseFileName = bpy.props.StringProperty(name='CaseFileName', description='Set/Get the Case file name', subtype='FILE_PATH')
    m_FilePath = bpy.props.StringProperty(name='FilePath', description='Set/Get the file path')
    m_ParticleCoordinatesByIndex = bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', description="The MeasuredGeometryFile should list particle coordinates from 0->N-1. If a file is loaded where point Ids are listed from 1-N the Id to points reference will be wrong and the data will be generated incorrectly. Setting ParticleCoordinatesByIndex to true will force all Id's to increment from 0->N-1 (relative to their order in the file) and regardless of the actual Id of of the point. Warning, if the Points are listed in non sequential order then setting this flag will reorder them", default=True)
    m_ReadAllVariables = bpy.props.BoolProperty(name='ReadAllVariables', description='Set/get the flag for whether to read all the variable', default=True)
    m_TimeValue = bpy.props.FloatProperty(name='TimeValue', description='Set/Get the time value at which to get the value', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ByteOrder', 'm_CaseFileName', 'm_FilePath', 'm_ParticleCoordinatesByIndex', 'm_ReadAllVariables', 'm_TimeValue', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GenericEnSightReader)
type_names.append('BVTK_NT_GenericEnSightReader')


# --------------------------------------------------------------


class BVTK_NT_FLUENTReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FLUENTReader'
    bl_label = 'vtkFLUENTReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian. Not used when reading text files", default='LittleEndian', items=e_DataByteOrder_items)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify the file name of the Fluent case file to read', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FLUENTReader)
type_names.append('BVTK_NT_FLUENTReader')


# --------------------------------------------------------------


class BVTK_NT_XMLRectilinearGridReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLRectilinearGridReader'
    bl_label = 'vtkXMLRectilinearGridReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    m_WholeSlices = bpy.props.BoolProperty(name='WholeSlices', description='Get/Set whether the reader gets a whole slice from disk when only a rectangle inside it is needed. This mode reads more data than necessary, but prevents many short reads from interacting poorly with the compression and encoding schemes', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', 'm_WholeSlices', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLRectilinearGridReader)
type_names.append('BVTK_NT_XMLRectilinearGridReader')


# --------------------------------------------------------------


class BVTK_NT_XMLMultiBlockDataReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_XMLMultiBlockDataReader'
    bl_label = 'vtkXMLMultiBlockDataReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the input file', subtype='FILE_PATH')
    m_PieceDistribution = bpy.props.IntProperty(name='PieceDistribution', description='', default=0)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString instead of the default, a file', default=True)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Which TimeStep to read', default=0)
    m_TimeStepRange = bpy.props.IntVectorProperty(name='TimeStepRange', description='', default=[0, 0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', 'm_PieceDistribution', 'm_ReadFromInputString', 'm_TimeStep', 'm_TimeStepRange', ]
    
    def m_connections(self):
        return [], ['Output'], ['ReaderErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_XMLMultiBlockDataReader)
type_names.append('BVTK_NT_XMLMultiBlockDataReader')


# --------------------------------------------------------------


class BVTK_NT_PChacoReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PChacoReader'
    bl_label = 'vtkPChacoReader'
    
    m_BaseName = bpy.props.StringProperty(name='BaseName', description='Specify the base name of the Chaco files. The reader will try to open BaseName.coords and BaseName.graph')
    m_GenerateEdgeWeightArrays = bpy.props.BoolProperty(name='GenerateEdgeWeightArrays', description='Each edge in the Chaco file connects two vertices. The file may specify one or more weights for each edge. (The weight for an edge from vertex A to vertex B equals the weight from B to A.) Indicate with the following parameter whether this reader should create a cell array for each weight for every edge. Default is OFF', default=True)
    m_GenerateGlobalElementIdArray = bpy.props.BoolProperty(name='GenerateGlobalElementIdArray', description='Indicate whether this reader should create a cell array containing global IDs for the cells in the output vtkUnstructuredGrid. These cells represent the edges that were in the Chaco file. Each edge is a vtkLine. Default is ON', default=True)
    m_GenerateGlobalNodeIdArray = bpy.props.BoolProperty(name='GenerateGlobalNodeIdArray', description='Indicate whether this reader should create a point array of global IDs for the points in the output vtkUnstructuredGrid. These points are the vertices that were in the Chaco file. Global point IDs start at "1" for the first vertex in BaseName.coords and go up from there. Default is ON', default=True)
    m_GenerateVertexWeightArrays = bpy.props.BoolProperty(name='GenerateVertexWeightArrays', description='Indicate whether this reader should create a point array for each vertex weight in the Chaco file. Default is OFF', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BaseName', 'm_GenerateEdgeWeightArrays', 'm_GenerateGlobalElementIdArray', 'm_GenerateGlobalNodeIdArray', 'm_GenerateVertexWeightArrays', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PChacoReader)
type_names.append('BVTK_NT_PChacoReader')


# --------------------------------------------------------------


class BVTK_NT_FixedWidthTextReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FixedWidthTextReader'
    bl_label = 'vtkFixedWidthTextReader'
    
    m_FieldWidth = bpy.props.IntProperty(name='FieldWidth', description='Set/get the field widt', default=10)
    m_FileName = bpy.props.StringProperty(name='FileName', description='', subtype='FILE_PATH')
    m_HaveHeaders = bpy.props.BoolProperty(name='HaveHeaders', description='Set/get whether to treat the first line of the file as headers', default=False)
    m_StripWhiteSpace = bpy.props.BoolProperty(name='StripWhiteSpace', description='If set, this flag will cause the reader to strip whitespace from the beginning and ending of each field. Defaults to off', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldWidth', 'm_FileName', 'm_HaveHeaders', 'm_StripWhiteSpace', ]
    
    def m_connections(self):
        return [], ['Output'], ['TableErrorObserver'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FixedWidthTextReader)
type_names.append('BVTK_NT_FixedWidthTextReader')


# --------------------------------------------------------------


class BVTK_NT_VASPAnimationReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VASPAnimationReader'
    bl_label = 'vtkVASPAnimationReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='The name of the file to read', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VASPAnimationReader)
type_names.append('BVTK_NT_VASPAnimationReader')


# --------------------------------------------------------------


class BVTK_NT_SLACReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SLACReader'
    bl_label = 'vtkSLACReader'
    
    m_MeshFileName = bpy.props.StringProperty(name='MeshFileName', description='', subtype='FILE_PATH')
    m_ReadExternalSurface = bpy.props.BoolProperty(name='ReadExternalSurface', description='If on, reads the external surfaces of the data set. Set to on by default', default=True)
    m_ReadInternalVolume = bpy.props.BoolProperty(name='ReadInternalVolume', description='If on, reads the internal volume of the data set. Set to off by default', default=True)
    m_ReadMidpoints = bpy.props.BoolProperty(name='ReadMidpoints', description='If on, reads midpoint information for external surfaces and builds quadratic surface triangles. Set to on by default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_MeshFileName', 'm_ReadExternalSurface', 'm_ReadInternalVolume', 'm_ReadMidpoints', ]
    
    def m_connections(self):
        return [], ['Output 0', 'Output 1'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SLACReader)
type_names.append('BVTK_NT_SLACReader')


# --------------------------------------------------------------


class BVTK_NT_PNGReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PNGReader'
    bl_label = 'vtkPNGReader'
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Short', 'SignedChar', 'UnsignedChar', 'UnsignedInt', 'UnsignedShort']]
    
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description="These methods should be used instead of the SwapBytes methods. They indicate the byte ordering of the file you are trying to read in. These methods will then either swap or not swap the bytes depending on the byte ordering of the machine it is being run on. For example, reading in a BigEndian file on a BigEndian machine will result in no swapping. Trying to read the same file on a LittleEndian machine will result in swapping. As a quick note most UNIX machines are BigEndian while PC's and VAX tend to be LittleEndian. So if the file you are reading in was generated on a VAX or PC, SetDataByteOrderToLittleEndian otherwise SetDataByteOrderToBigEndian", default='LittleEndian', items=e_DataByteOrder_items)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set the data type of pixels in the file. If you want the output scalar type to have a different value, set it after this method is called', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='The number of dimensions stored in a file. This defaults to two', default=2)
    m_FileLowerLeft = bpy.props.BoolProperty(name='FileLowerLeft', description='Set/Get whether the data comes from the file starting in the lower left corner or upper left corner', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. If the data is stored in multiple files, then use SetFileNames or SetFilePrefix instead', subtype='FILE_PATH')
    m_FileNameSliceOffset = bpy.props.IntProperty(name='FileNameSliceOffset', description='When reading files which start at an unusual index, this can be added to the slice number when generating the file name (default = 0', default=0)
    m_FileNameSliceSpacing = bpy.props.IntProperty(name='FileNameSliceSpacing', description='When reading files which have regular, but non contiguous slices (eg filename.1,filename.3,filename.5) a spacing can be specified to skip missing files (default = 1', default=1)
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf-style format string used to build filename from FilePrefix and slice number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file or files. This can be used in place of SetFileName or SetFileNames if the filenames follow a specific naming pattern, but you must explicitly set the DataExtent so that the reader will know what range of slices to load')
    m_HeaderSize = bpy.props.IntProperty(name='HeaderSize', description='If there is a tail on the file, you want to explicitly set the header size', default=0)
    m_MemoryBufferLength = bpy.props.IntProperty(name='MemoryBufferLength', description='Specify the in memory image buffer length', default=0)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar component', default=1)
    m_ReadSpacingFromFile = bpy.props.BoolProperty(name='ReadSpacingFromFile', description="Set/Get if data spacing should be calculated from the PNG file. Use default spacing if the PNG file don't have valid pixel per meter parameters. Default is false", default=False)
    m_SwapBytes = bpy.props.BoolProperty(name='SwapBytes', description='Set/Get the byte swapping to explicitly swap the bytes of a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_DataByteOrder', 'm_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_FileDimensionality', 'm_FileLowerLeft', 'm_FileName', 'm_FileNameSliceOffset', 'm_FileNameSliceSpacing', 'm_FilePattern', 'm_FilePrefix', 'm_HeaderSize', 'm_MemoryBufferLength', 'm_NumberOfScalarComponents', 'm_ReadSpacingFromFile', 'm_SwapBytes', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PNGReader)
type_names.append('BVTK_NT_PNGReader')


# --------------------------------------------------------------


class BVTK_NT_EnSightGoldReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EnSightGoldReader'
    bl_label = 'vtkEnSightGoldReader'
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description='Set the byte order of the file (remember, more Unix workstations write big endian whereas PCs write little endian). Default is big endian (since most older PLOT3D files were written by workstations)', items=e_ByteOrder_items)
    m_CaseFileName = bpy.props.StringProperty(name='CaseFileName', description='Set/Get the Case file name', subtype='FILE_PATH')
    m_FilePath = bpy.props.StringProperty(name='FilePath', description='Set/Get the file path')
    m_ParticleCoordinatesByIndex = bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', description="The MeasuredGeometryFile should list particle coordinates from 0->N-1. If a file is loaded where point Ids are listed from 1-N the Id to points reference will be wrong and the data will be generated incorrectly. Setting ParticleCoordinatesByIndex to true will force all Id's to increment from 0->N-1 (relative to their order in the file) and regardless of the actual Id of of the point. Warning, if the Points are listed in non sequential order then setting this flag will reorder them", default=True)
    m_ReadAllVariables = bpy.props.BoolProperty(name='ReadAllVariables', description='Set/get the flag for whether to read all the variable', default=True)
    m_TimeValue = bpy.props.FloatProperty(name='TimeValue', description='Set/Get the time value at which to get the value', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ByteOrder', 'm_CaseFileName', 'm_FilePath', 'm_ParticleCoordinatesByIndex', 'm_ReadAllVariables', 'm_TimeValue', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EnSightGoldReader)
type_names.append('BVTK_NT_EnSightGoldReader')


# --------------------------------------------------------------


class BVTK_NT_EnSightMasterServerReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EnSightMasterServerReader'
    bl_label = 'vtkEnSightMasterServerReader'
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description='Set the byte order of the file (remember, more Unix workstations write big endian whereas PCs write little endian). Default is big endian (since most older PLOT3D files were written by workstations)', items=e_ByteOrder_items)
    m_CaseFileName = bpy.props.StringProperty(name='CaseFileName', description='Set/Get the Case file name', subtype='FILE_PATH')
    m_CurrentPiece = bpy.props.IntProperty(name='CurrentPiece', description='Set or get the current piece', default=-1)
    m_FilePath = bpy.props.StringProperty(name='FilePath', description='Set/Get the file path')
    m_ParticleCoordinatesByIndex = bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', description="The MeasuredGeometryFile should list particle coordinates from 0->N-1. If a file is loaded where point Ids are listed from 1-N the Id to points reference will be wrong and the data will be generated incorrectly. Setting ParticleCoordinatesByIndex to true will force all Id's to increment from 0->N-1 (relative to their order in the file) and regardless of the actual Id of of the point. Warning, if the Points are listed in non sequential order then setting this flag will reorder them", default=True)
    m_ReadAllVariables = bpy.props.BoolProperty(name='ReadAllVariables', description='Set/get the flag for whether to read all the variable', default=True)
    m_TimeValue = bpy.props.FloatProperty(name='TimeValue', description='Set/Get the time value at which to get the value', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_ByteOrder', 'm_CaseFileName', 'm_CurrentPiece', 'm_FilePath', 'm_ParticleCoordinatesByIndex', 'm_ReadAllVariables', 'm_TimeValue', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EnSightMasterServerReader)
type_names.append('BVTK_NT_EnSightMasterServerReader')


# --------------------------------------------------------------


class BVTK_NT_TreeReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TreeReader'
    bl_label = 'vtkTreeReader'
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Set the name of the field data to extract. If not specified, uses first field data encountered in file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk data file to read', subtype='FILE_PATH')
    m_InputString = bpy.props.StringProperty(name='InputString', description='Specify the InputString for use when reading from a character array. Optionally include the length for binary strings. Note that a copy of the string is made and stored. If this causes exceedingly large memory consumption, consider using InputArray instead')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Set the name of the lookup table data to extract. If not specified, uses lookup table named by scalar. Otherwise, this specification supersedes')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Set the name of the normal data to extract. If not specified, first normal data encountered is extracted')
    m_ReadAllColorScalars = bpy.props.BoolProperty(name='ReadAllColorScalars', description='Enable reading all color scalars', default=True)
    m_ReadAllFields = bpy.props.BoolProperty(name='ReadAllFields', description='Enable reading all fields', default=True)
    m_ReadAllNormals = bpy.props.BoolProperty(name='ReadAllNormals', description='Enable reading all normals', default=True)
    m_ReadAllScalars = bpy.props.BoolProperty(name='ReadAllScalars', description='Enable reading all scalars', default=True)
    m_ReadAllTCoords = bpy.props.BoolProperty(name='ReadAllTCoords', description='Enable reading all tcoords', default=True)
    m_ReadAllTensors = bpy.props.BoolProperty(name='ReadAllTensors', description='Enable reading all tensors', default=True)
    m_ReadAllVectors = bpy.props.BoolProperty(name='ReadAllVectors', description='Enable reading all vectors', default=True)
    m_ReadFromInputString = bpy.props.BoolProperty(name='ReadFromInputString', description='Enable reading from an InputString or InputArray instead of the default, a file', default=True)
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Set the name of the scalar data to extract. If not specified, first scalar data encountered is extracted')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Set the name of the texture coordinate data to extract. If not specified, first texture coordinate data encountered is extracted')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Set the name of the tensor data to extract. If not specified, first tensor data encountered is extracted')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Set the name of the vector data to extract. If not specified, first vector data encountered is extracted')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FieldDataName', 'm_FileName', 'm_InputString', 'm_LookupTableName', 'm_NormalsName', 'm_ReadAllColorScalars', 'm_ReadAllFields', 'm_ReadAllNormals', 'm_ReadAllScalars', 'm_ReadAllTCoords', 'm_ReadAllTensors', 'm_ReadAllVectors', 'm_ReadFromInputString', 'm_ScalarsName', 'm_TCoordsName', 'm_TensorsName', 'm_VectorsName', ]
    
    def m_connections(self):
        return [], ['Output'], ['InputArray'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TreeReader)
type_names.append('BVTK_NT_TreeReader')


# --------------------------------------------------------------


class BVTK_NT_CMLMoleculeReader(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CMLMoleculeReader'
    bl_label = 'vtkCMLMoleculeReader'
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the CML fil', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FileName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CMLMoleculeReader)
type_names.append('BVTK_NT_CMLMoleculeReader')


# --------------------------------------------------------------


menu_items = [NodeItem(x) for x in type_names]
node_categories.append(BVTK_NodeCategory('VTKReader', 'Reader', items=menu_items))
