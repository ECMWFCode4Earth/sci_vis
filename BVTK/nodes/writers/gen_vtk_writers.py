from .. core import *
cat = "Writers"


# --------------------------------------------------------------


class BVTK_NT_OggTheoraWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_OggTheoraWriter"
    bl_label = "vtkOggTheoraWriter"
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of avi file', subtype='FILE_PATH')
    m_Quality = bpy.props.IntProperty(name='Quality', description='Set/Get the compression quality. 0 means worst quality and smallest file size 2 means best quality and largest file siz', default=2)
    m_Rate = bpy.props.IntProperty(name='Rate', description='Set/Get the frame rate, in frame/s', default=25)
    m_Subsampling = bpy.props.BoolProperty(name='Subsampling', description='Is the video to be encoded using 4:2:0 subsampling', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileName", "m_Quality", "m_Rate", "m_Subsampling", ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_OggTheoraWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_GenericDataObjectWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_GenericDataObjectWriter"
    bl_label = "vtkGenericDataObjectWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_GenericDataObjectWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLUnstructuredGridWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLUnstructuredGridWriter"
    bl_label = "vtkXMLUnstructuredGridWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Get/Set the ghost level used to pad each piece', default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces used to stream the image through the pipeline while writing to the file', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WritePiece = bpy.props.IntProperty(name='WritePiece', description='Get/Set the piece to write to the file. If this is negative or equal to the NumberOfPieces, all pieces will be written', default=-1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_WritePiece", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLUnstructuredGridWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_StructuredGridWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_StructuredGridWriter"
    bl_label = "vtkStructuredGridWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteExtent = bpy.props.BoolProperty(name='WriteExtent', description='When WriteExtent is on, vtkStructuredPointsWriter writes data extent in the output file. Otherwise, it writes dimensions. The only time this option is useful is when the extents do not start at (0, 0, 0). This is an options to support writing of older formats while still using a newer VTK', default=False)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteExtent", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_StructuredGridWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_BMPWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_BMPWriter"
    bl_label = "vtkBMPWriter"
    
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='What dimension are the files to be written. Usually this is 2, or 3. If it is 2 and the input is a volume then the volume will be written as a series of 2d slices', default=2)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. You should specify either a FileName or a FilePrefix. Use FilePrefix if the data is stored in multiple files', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s).You should specify either a FileName or FilePrefix. Use FilePrefix if the data is stored in multiple files')
    m_WriteToMemory = bpy.props.BoolProperty(name='WriteToMemory', description='Write the image to memory (a vtkUnsignedCharArray', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileDimensionality", "m_FileName", "m_FilePattern", "m_FilePrefix", "m_WriteToMemory", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_BMPWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_UnstructuredGridWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_UnstructuredGridWriter"
    bl_label = "vtkUnstructuredGridWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_UnstructuredGridWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_NIFTIImageWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_NIFTIImageWriter"
    bl_label = "vtkNIFTIImageWriter"
    
    m_Description = bpy.props.StringProperty(name='Description', description='Set a short description (max 80 chars) of how the file was produced. The default description is "VTKX.Y" where X.Y is the VTK version', default='VTK8.1.2')
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='What dimension are the files to be written. Usually this is 2, or 3. If it is 2 and the input is a volume then the volume will be written as a series of 2d slices', default=3)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. You should specify either a FileName or a FilePrefix. Use FilePrefix if the data is stored in multiple files', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s).You should specify either a FileName or FilePrefix. Use FilePrefix if the data is stored in multiple files')
    m_NIFTIVersion = bpy.props.IntProperty(name='NIFTIVersion', description='Set the version number for the NIfTI file format to use. This can be 1, 2, or 0 (the default). If set to zero, then it will save as NIfTI version 1 unless SetNIFTIHeader() provided header information from a NIfTI version 2 file', default=0)
    m_PlanarRGB = bpy.props.BoolProperty(name='PlanarRGB', description='Write planar RGB (separate R, G, and B planes), rather than packed RGB. Use this option with extreme caution: the NIFTI standard requires RGB pixels to be packed. The Analyze format, however, was used to store both planar RGB and packed RGB depending on the software, without any indication in the header about which convention was being used', default=False)
    m_QFac = bpy.props.FloatProperty(name='QFac', description='The QFac sets the ordering of the slices in the NIFTI file. If QFac is -1, then the slice ordering in the file will be reversed as compared to VTK. Use with caution', default=0.0)
    m_RescaleIntercept = bpy.props.FloatProperty(name='RescaleIntercept', description='Set the slope and intercept for calibrating the scalar values. Other programs that read the NIFTI file can use the equation v = u*RescaleSlope + RescaleIntercept to rescale the data to real values. If both the slope and the intercept are zero, then the SclSlope and SclIntercept in the header info provided via SetNIFTIHeader() are used instead', default=0.0)
    m_RescaleSlope = bpy.props.FloatProperty(name='RescaleSlope', description='Set the slope and intercept for calibrating the scalar values. Other programs that read the NIFTI file can use the equation v = u*RescaleSlope + RescaleIntercept to rescale the data to real values. If both the slope and the intercept are zero, then the SclSlope and SclIntercept in the header info provided via SetNIFTIHeader() are used instead', default=0.0)
    m_TimeDimension = bpy.props.IntProperty(name='TimeDimension', description='Set the time dimension to use in the NIFTI file (or zero if none). The number of components of the input data must be divisible by the time dimension if the time dimension is not set to zero. The vector dimension will be set to the number of components divided by the time dimension', default=0)
    m_TimeSpacing = bpy.props.FloatProperty(name='TimeSpacing', description='Set the time dimension to use in the NIFTI file (or zero if none). The number of components of the input data must be divisible by the time dimension if the time dimension is not set to zero. The vector dimension will be set to the number of components divided by the time dimension', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_Description", "m_FileDimensionality", "m_FileName", "m_FilePattern", "m_FilePrefix", "m_NIFTIVersion", "m_PlanarRGB", "m_QFac", "m_RescaleIntercept", "m_RescaleSlope", "m_TimeDimension", "m_TimeSpacing", ]
    
    def m_connections(self):
        return ['Input'], [], ['NIFTIHeader', 'QFormMatrix', 'SFormMatrix'], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_NIFTIImageWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_MNITransformWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_MNITransformWriter"
    bl_label = "vtkMNITransformWriter"
    
    m_Comments = bpy.props.StringProperty(name='Comments', description='Set comments to be added to the file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set the file name', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_Comments", "m_FileName", ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_MNITransformWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_ArrayDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ArrayDataWriter"
    bl_label = "vtkArrayDataWriter"
    
    m_Binary = bpy.props.BoolProperty(name='Binary', description='Get / set whether data will be written in binary format (when used as a filter)', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get / set the filename where data will be stored (when used as a filter)', subtype='FILE_PATH')
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Whether to output to a string instead of to a file, which is the default', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_Binary", "m_FileName", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ArrayDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_JSONImageWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_JSONImageWriter"
    bl_label = "vtkJSONImageWriter"
    
    m_ArrayName = bpy.props.StringProperty(name='ArrayName', description='Specify ArrayName to export. By default nullptr which will dump ALL arrays')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file', subtype='FILE_PATH')
    m_Slice = bpy.props.IntProperty(name='Slice', description='Specify Slice in Z to export. By default -1 which will dump the full 3D domain', default=-1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ArrayName", "m_FileName", "m_Slice", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_JSONImageWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLDataSetWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLDataSetWriter"
    bl_label = "vtkXMLDataSetWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "e_HeaderType", "e_IdType", "m_NumberOfTimeSteps", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLDataSetWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLPRectilinearGridWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLPRectilinearGridWriter"
    bl_label = "vtkXMLPRectilinearGridWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_EndPiece = bpy.props.IntProperty(name='EndPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description="Get/Set the ghost level used for this writer's piece", default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces that are being written in parallel', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_StartPiece = bpy.props.IntProperty(name='StartPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_UseSubdirectory = bpy.props.BoolProperty(name='UseSubdirectory', description='Get/Set whether to use a subdirectory to store the piece', default=False)
    m_WriteSummaryFile = bpy.props.BoolProperty(name='WriteSummaryFile', description="Get/Set whether the writer should write the summary file that refers to all of the pieces' individual files. This is on by default. Note that only the first process writes the summary file", default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_EndPiece", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_StartPiece", "m_UseSubdirectory", "m_WriteSummaryFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLPRectilinearGridWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLMultiBlockDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLMultiBlockDataWriter"
    bl_label = "vtkXMLMultiBlockDataWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Get/Set the number of ghost levels to be written', default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WriteMetaFile = bpy.props.IntProperty(name='WriteMetaFile', description='Get/Set whether this instance will write the meta-file', default=1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfTimeSteps", "m_WriteMetaFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLMultiBlockDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLPHierarchicalBoxDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLPHierarchicalBoxDataWriter"
    bl_label = "vtkXMLPHierarchicalBoxDataWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Get/Set the number of ghost levels to be written', default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WriteMetaFile = bpy.props.IntProperty(name='WriteMetaFile', description='Set whether this instance will write the meta-file. WriteMetaFile is set to flag only on process 0 and all other processes have WriteMetaFile set to 0 by default', default=1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfTimeSteps", "m_WriteMetaFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLPHierarchicalBoxDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_JPEGWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_JPEGWriter"
    bl_label = "vtkJPEGWriter"
    
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='What dimension are the files to be written. Usually this is 2, or 3. If it is 2 and the input is a volume then the volume will be written as a series of 2d slices', default=2)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. You should specify either a FileName or a FilePrefix. Use FilePrefix if the data is stored in multiple files', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s).You should specify either a FileName or FilePrefix. Use FilePrefix if the data is stored in multiple files')
    m_Progressive = bpy.props.BoolProperty(name='Progressive', description='Progressive JPEG generation', default=True)
    m_Quality = bpy.props.IntProperty(name='Quality', description='Compression quality. 0 = Low quality, 100 = High qualit', default=95)
    m_WriteToMemory = bpy.props.BoolProperty(name='WriteToMemory', description='Write the image to memory (a vtkUnsignedCharArray', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileDimensionality", "m_FileName", "m_FilePattern", "m_FilePrefix", "m_Progressive", "m_Quality", "m_WriteToMemory", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_JPEGWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_ExodusIIWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ExodusIIWriter"
    bl_label = "vtkExodusIIWriter"
    
    m_BlockIdArrayName = bpy.props.StringProperty(name='BlockIdArrayName', description='')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Name for the output file. If writing in parallel, the number of processes and the process rank will be appended to the name, so each process is writing out a separate file. If not set, this class will make up a file name', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='We never write out ghost cells. This variable is here to satisfy the behavior of ParaView on invoking a parallel writer', default=0)
    m_IgnoreMetaDataWarning = bpy.props.BoolProperty(name='IgnoreMetaDataWarning', description="In certain cases we know that metadata doesn't exist and we want to ignore that warning", default=False)
    m_StoreDoubles = bpy.props.IntProperty(name='StoreDoubles', description='If StoreDoubles is ON, the floating point fields in the Exodus file will be double precision fields. The default is determined by the max precision of the input. If the field data appears to be doubles, then StoreDoubles will be ON, otherwise StoreDoubles will be OFF', default=-1)
    m_WriteAllTimeSteps = bpy.props.BoolProperty(name='WriteAllTimeSteps', description='When WriteAllTimeSteps is turned ON, the writer is executed once for each timestep available from the reader', default=True)
    m_WriteOutBlockIdArray = bpy.props.BoolProperty(name='WriteOutBlockIdArray', description='By default, the integer array containing the global Block Ids of the cells is not included when the new Exodus II file is written out. If you do want to include this array, set WriteOutBlockIdArray to ON', default=True)
    m_WriteOutGlobalElementIdArray = bpy.props.BoolProperty(name='WriteOutGlobalElementIdArray', description='By default, the integer array containing the global Element Ids is not included when the new Exodus II file is written out. If you do want to include this array, set WriteOutGlobalElementIdArray to ON', default=True)
    m_WriteOutGlobalNodeIdArray = bpy.props.BoolProperty(name='WriteOutGlobalNodeIdArray', description='By default, the integer array containing the global Node Ids is not included when the new Exodus II file is written out. If you do want to include this array, set WriteOutGlobalNodeIdArray to ON', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockIdArrayName", "m_FileName", "m_GhostLevel", "m_IgnoreMetaDataWarning", "m_StoreDoubles", "m_WriteAllTimeSteps", "m_WriteOutBlockIdArray", "m_WriteOutGlobalElementIdArray", "m_WriteOutGlobalNodeIdArray", ]
    
    def m_connections(self):
        return ['Input'], [], ['ModelMetadata'], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ExodusIIWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_MetaImageWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_MetaImageWriter"
    bl_label = "vtkMetaImageWriter"
    
    m_Compression = bpy.props.BoolProperty(name='Compression', description='', default=True)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='What dimension are the files to be written. Usually this is 2, or 3. If it is 2 and the input is a volume then the volume will be written as a series of 2d slices', default=2)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of meta fil', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s).You should specify either a FileName or FilePrefix. Use FilePrefix if the data is stored in multiple files')
    m_RAWFileName = bpy.props.StringProperty(name='RAWFileName', description='Specify the file name of the raw image data', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_Compression", "m_FileDimensionality", "m_FileName", "m_FilePattern", "m_FilePrefix", "m_RAWFileName", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_MetaImageWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_TableWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_TableWriter"
    bl_label = "vtkTableWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_TableWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_RectilinearGridWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_RectilinearGridWriter"
    bl_label = "vtkRectilinearGridWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteExtent = bpy.props.BoolProperty(name='WriteExtent', description='When WriteExtent is on, vtkStructuredPointsWriter writes data extent in the output file. Otherwise, it writes dimensions. The only time this option is useful is when the extents do not start at (0, 0, 0). This is an options to support writing of older formats while still using a newer VTK', default=False)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteExtent", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_RectilinearGridWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_PhyloXMLTreeWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_PhyloXMLTreeWriter"
    bl_label = "vtkPhyloXMLTreeWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EdgeWeightArrayName = bpy.props.StringProperty(name='EdgeWeightArrayName', description='Get/Set the name of the input\'s tree edge weight array. This array must be part of the input tree\'s EdgeData. The default name is "weight". If this array cannot be found, then no edge weights will be included in the output of this writer', default='weight')
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NodeNameArrayName = bpy.props.StringProperty(name='NodeNameArrayName', description='Get/Set the name of the input\'s tree node name array. This array must be part of the input tree\'s VertexData. The default name is "node name". If this array cannot be found, then no node names will be included in the output of this writer', default='node name')
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EdgeWeightArrayName", "m_EncodeAppendedData", "m_FileName", "e_HeaderType", "e_IdType", "m_NodeNameArrayName", "m_NumberOfTimeSteps", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_PhyloXMLTreeWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLUniformGridAMRWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLUniformGridAMRWriter"
    bl_label = "vtkXMLUniformGridAMRWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Get/Set the number of ghost levels to be written', default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WriteMetaFile = bpy.props.IntProperty(name='WriteMetaFile', description='Get/Set whether this instance will write the meta-file', default=1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfTimeSteps", "m_WriteMetaFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLUniformGridAMRWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_DIMACSGraphWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_DIMACSGraphWriter"
    bl_label = "vtkDIMACSGraphWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_DIMACSGraphWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLPPolyDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLPPolyDataWriter"
    bl_label = "vtkXMLPPolyDataWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_EndPiece = bpy.props.IntProperty(name='EndPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description="Get/Set the ghost level used for this writer's piece", default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces that are being written in parallel', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_StartPiece = bpy.props.IntProperty(name='StartPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_UseSubdirectory = bpy.props.BoolProperty(name='UseSubdirectory', description='Get/Set whether to use a subdirectory to store the piece', default=False)
    m_WriteSummaryFile = bpy.props.BoolProperty(name='WriteSummaryFile', description="Get/Set whether the writer should write the summary file that refers to all of the pieces' individual files. This is on by default. Note that only the first process writes the summary file", default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_EndPiece", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_StartPiece", "m_UseSubdirectory", "m_WriteSummaryFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLPPolyDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_DelimitedTextWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_DelimitedTextWriter"
    bl_label = "vtkDelimitedTextWriter"
    
    m_FieldDelimiter = bpy.props.StringProperty(name='FieldDelimiter', description='Get/Set the delimiter use to separate fields ("," by default.', default=',')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the filename for the file', subtype='FILE_PATH')
    m_StringDelimiter = bpy.props.StringProperty(name='StringDelimiter', description='Get/Set the delimiter used for string data, if any eg. double quotes(")', default='"')
    m_UseStringDelimiter = bpy.props.BoolProperty(name='UseStringDelimiter', description='Get/Set if StringDelimiter must be used for string data. True by default', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FieldDelimiter", "m_FileName", "m_StringDelimiter", "m_UseStringDelimiter", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_DelimitedTextWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_TableToSQLiteWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_TableToSQLiteWriter"
    bl_label = "vtkTableToSQLiteWriter"
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return ['Input'], [], ['Database'], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_TableToSQLiteWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLPMultiBlockDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLPMultiBlockDataWriter"
    bl_label = "vtkXMLPMultiBlockDataWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Get/Set the number of ghost levels to be written', default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces that are being written in parallel', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_StartPiece = bpy.props.IntProperty(name='StartPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_WriteMetaFile = bpy.props.IntProperty(name='WriteMetaFile', description='Set whether this instance will write the meta-file. WriteMetaFile is set to flag only on process 0 and all other processes have WriteMetaFile set to 0 by default', default=1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_StartPiece", "m_WriteMetaFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLPMultiBlockDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLPolyDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLPolyDataWriter"
    bl_label = "vtkXMLPolyDataWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Get/Set the ghost level used to pad each piece', default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces used to stream the image through the pipeline while writing to the file', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WritePiece = bpy.props.IntProperty(name='WritePiece', description='Get/Set the piece to write to the file. If this is negative or equal to the NumberOfPieces, all pieces will be written', default=-1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_WritePiece", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLPolyDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLStructuredGridWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLStructuredGridWriter"
    bl_label = "vtkXMLStructuredGridWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Get/Set the ghost level used to pad each piece', default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces used to stream the image through the pipeline while writing to the file', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WriteExtent = bpy.props.IntVectorProperty(name='WriteExtent', description='', default=[0, -1, 0, -1, 0, -1], size=6)
    m_WritePiece = bpy.props.IntProperty(name='WritePiece', description='Get/Set the piece to write to the file. If this is negative, all pieces will be written', default=-1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_WriteExtent", "m_WritePiece", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLStructuredGridWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_PDataSetWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_PDataSetWriter"
    bl_label = "vtkPDataSetWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_EndPiece = bpy.props.IntProperty(name='EndPiece', description='This is the range of pieces that that this writer is responsible for writing. All pieces must be written by some process. The process that writes piece 0 also writes the pvtk file that lists all the piece file names', default=0)
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='This file pattern uses the file name and piece number to contruct a file name for the piece file', default='%s.%d.vtk')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Extra ghost cells will be written out to each piece file if this value is larger than 0', default=0)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='This is how many pieces the whole data set will be divided into', default=1)
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_StartPiece = bpy.props.IntProperty(name='StartPiece', description='This is the range of pieces that that this writer is responsible for writing. All pieces must be written by some process. The process that writes piece 0 also writes the pvtk file that lists all the piece file names', default=0)
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_UseRelativeFileNames = bpy.props.BoolProperty(name='UseRelativeFileNames', description='This flag determines whether to use absolute paths for the piece files. By default the pieces are put in the main directory, and the piece file names in the meta data pvtk file are relative to this directory. This should make moving the whole lot to another directory, an easier task', default=True)
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=21, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_EndPiece", "m_FieldDataName", "m_FileName", "m_FilePattern", "e_FileType", "m_GhostLevel", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_NumberOfPieces", "m_PedigreeIdsName", "m_ScalarsName", "m_StartPiece", "m_TCoordsName", "m_TensorsName", "m_UseRelativeFileNames", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_PDataSetWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_JavaScriptDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_JavaScriptDataWriter"
    bl_label = "vtkJavaScriptDataWriter"
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the filename for the file', subtype='FILE_PATH')
    m_IncludeFieldNames = bpy.props.BoolProperty(name='IncludeFieldNames', description='Get/Set the whether or not to include field names When field names are on you will get data output that looks like this: var data=[ {foo:3,time:"2009-11-04 16:09:42",bar:1 }, {foo:5,time:"2009-11-04 16:11:22",bar:0 }, without field names the data will be an array of arrays like this: var data=[ [3,"2009-11-04 16:09:42",1], [5,"2009-11-04 16:11:22",0]', default=True)
    m_VariableName = bpy.props.StringProperty(name='VariableName', description='Get/set the name of the Javascript variable that the dataset will be assigned to. The default value is "data", so the javascript code generated by the filter will look like this: "var data = [ ... ];". If VariableName is set to nullptr, then no assignment statement will be generated (i.e., only "[ ... ];" will be generated)', default='data')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileName", "m_IncludeFieldNames", "m_VariableName", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_JavaScriptDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_NewickTreeWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_NewickTreeWriter"
    bl_label = "vtkNewickTreeWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_EdgeWeightArrayName = bpy.props.StringProperty(name='EdgeWeightArrayName', description='Get/Set the name of the input\'s tree edge weight array. This array must be part of the input tree\'s EdgeData. The default name is "weight". If this array cannot be found, then no edge weights will be included in the output of this writer', default='weight')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NodeNameArrayName = bpy.props.StringProperty(name='NodeNameArrayName', description='Get/Set the name of the input\'s tree node name array. This array must be part of the input tree\'s VertexData. The default name is "node name". If this array cannot be found, then no node names will be included in the output of this writer', default='node name')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_EdgeWeightArrayName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NodeNameArrayName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_NewickTreeWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLPImageDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLPImageDataWriter"
    bl_label = "vtkXMLPImageDataWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_EndPiece = bpy.props.IntProperty(name='EndPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description="Get/Set the ghost level used for this writer's piece", default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces that are being written in parallel', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_StartPiece = bpy.props.IntProperty(name='StartPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_UseSubdirectory = bpy.props.BoolProperty(name='UseSubdirectory', description='Get/Set whether to use a subdirectory to store the piece', default=False)
    m_WriteSummaryFile = bpy.props.BoolProperty(name='WriteSummaryFile', description="Get/Set whether the writer should write the summary file that refers to all of the pieces' individual files. This is on by default. Note that only the first process writes the summary file", default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_EndPiece", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_StartPiece", "m_UseSubdirectory", "m_WriteSummaryFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLPImageDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLPStructuredGridWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLPStructuredGridWriter"
    bl_label = "vtkXMLPStructuredGridWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_EndPiece = bpy.props.IntProperty(name='EndPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description="Get/Set the ghost level used for this writer's piece", default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces that are being written in parallel', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_StartPiece = bpy.props.IntProperty(name='StartPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_UseSubdirectory = bpy.props.BoolProperty(name='UseSubdirectory', description='Get/Set whether to use a subdirectory to store the piece', default=False)
    m_WriteSummaryFile = bpy.props.BoolProperty(name='WriteSummaryFile', description="Get/Set whether the writer should write the summary file that refers to all of the pieces' individual files. This is on by default. Note that only the first process writes the summary file", default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_EndPiece", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_StartPiece", "m_UseSubdirectory", "m_WriteSummaryFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLPStructuredGridWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLPDataSetWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLPDataSetWriter"
    bl_label = "vtkXMLPDataSetWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_EndPiece = bpy.props.IntProperty(name='EndPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description="Get/Set the ghost level used for this writer's piece", default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces that are being written in parallel', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_StartPiece = bpy.props.IntProperty(name='StartPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_UseSubdirectory = bpy.props.BoolProperty(name='UseSubdirectory', description='Get/Set whether to use a subdirectory to store the piece', default=False)
    m_WriteSummaryFile = bpy.props.BoolProperty(name='WriteSummaryFile', description="Get/Set whether the writer should write the summary file that refers to all of the pieces' individual files. This is on by default. Note that only the first process writes the summary file", default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_EndPiece", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_StartPiece", "m_UseSubdirectory", "m_WriteSummaryFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLPDataSetWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_PolyDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_PolyDataWriter"
    bl_label = "vtkPolyDataWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_PolyDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_GraphWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_GraphWriter"
    bl_label = "vtkGraphWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_GraphWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_PNMWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_PNMWriter"
    bl_label = "vtkPNMWriter"
    
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='What dimension are the files to be written. Usually this is 2, or 3. If it is 2 and the input is a volume then the volume will be written as a series of 2d slices', default=2)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. You should specify either a FileName or a FilePrefix. Use FilePrefix if the data is stored in multiple files', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s).You should specify either a FileName or FilePrefix. Use FilePrefix if the data is stored in multiple files')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileDimensionality", "m_FileName", "m_FilePattern", "m_FilePrefix", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_PNMWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_IVWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_IVWriter"
    bl_label = "vtkIVWriter"
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileName", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_IVWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_MINCImageWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_MINCImageWriter"
    bl_label = "vtkMINCImageWriter"
    
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='What dimension are the files to be written. Usually this is 2, or 3. If it is 2 and the input is a volume then the volume will be written as a series of 2d slices', default=2)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Set the file name', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s).You should specify either a FileName or FilePrefix. Use FilePrefix if the data is stored in multiple files')
    m_HistoryAddition = bpy.props.StringProperty(name='HistoryAddition', description='Set a string value to append to the history of the file. This string should describe, briefly, how the file was processed')
    m_RescaleIntercept = bpy.props.FloatProperty(name='RescaleIntercept', description='Set the slope and intercept for rescaling the intensities. The default values are zero, which indicates to the reader that no rescaling is to be performed', default=0.0)
    m_RescaleSlope = bpy.props.FloatProperty(name='RescaleSlope', description='Set the slope and intercept for rescaling the intensities. The default values are zero, which indicates to the reader that no rescaling is to be performed', default=0.0)
    m_StrictValidation = bpy.props.BoolProperty(name='StrictValidation', description='Set whether to validate that all variable attributes that have been set are ones that are listed in the MINC standard', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileDimensionality", "m_FileName", "m_FilePattern", "m_FilePrefix", "m_HistoryAddition", "m_RescaleIntercept", "m_RescaleSlope", "m_StrictValidation", ]
    
    def m_connections(self):
        return ['Input'], [], ['DirectionCosines', 'ImageAttributes'], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_MINCImageWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_TreeWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_TreeWriter"
    bl_label = "vtkTreeWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_TreeWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLImageDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLImageDataWriter"
    bl_label = "vtkXMLImageDataWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Get/Set the ghost level used to pad each piece', default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces used to stream the image through the pipeline while writing to the file', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WriteExtent = bpy.props.IntVectorProperty(name='WriteExtent', description='', default=[0, -1, 0, -1, 0, -1], size=6)
    m_WritePiece = bpy.props.IntProperty(name='WritePiece', description='Get/Set the piece to write to the file. If this is negative, all pieces will be written', default=-1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_WriteExtent", "m_WritePiece", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLImageDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_DataObjectWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_DataObjectWriter"
    bl_label = "vtkDataObjectWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Methods delegated to vtkDataWriter, see vtkDataWriter', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Methods delegated to vtkDataWriter, see vtkDataWriter', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Methods delegated to vtkDataWriter, see vtkDataWriter', default='ASCII', items=e_FileType_items)
    m_Header = bpy.props.StringProperty(name='Header', description='Methods delegated to vtkDataWriter, see vtkDataWriter', default='vtk output')
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Methods delegated to vtkDataWriter, see vtkDataWriter', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FieldDataName", "m_FileName", "e_FileType", "m_Header", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_DataObjectWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_PostScriptWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_PostScriptWriter"
    bl_label = "vtkPostScriptWriter"
    
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='What dimension are the files to be written. Usually this is 2, or 3. If it is 2 and the input is a volume then the volume will be written as a series of 2d slices', default=2)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. You should specify either a FileName or a FilePrefix. Use FilePrefix if the data is stored in multiple files', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s).You should specify either a FileName or FilePrefix. Use FilePrefix if the data is stored in multiple files')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileDimensionality", "m_FileName", "m_FilePattern", "m_FilePrefix", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_PostScriptWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_SimplePointsWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_SimplePointsWriter"
    bl_label = "vtkSimplePointsWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_DecimalPrecision = bpy.props.IntProperty(name='DecimalPrecision', description='', default=6)
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_DecimalPrecision", "m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_SimplePointsWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLPTableWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLPTableWriter"
    bl_label = "vtkXMLPTableWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_EndPiece = bpy.props.IntProperty(name='EndPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description="Get/Set the ghost level used for this writer's piece", default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces that are being written in parallel', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_StartPiece = bpy.props.IntProperty(name='StartPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_UseSubdirectory = bpy.props.BoolProperty(name='UseSubdirectory', description='Get/Set whether to use a subdirectory to store the piece', default=False)
    m_WriteSummaryFile = bpy.props.BoolProperty(name='WriteSummaryFile', description="Get/Set whether the writer should write the summary file that refers to all of the pieces' individual files. This is on by default. Note that only the first process writes the summary file", default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_EndPiece", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_StartPiece", "m_UseSubdirectory", "m_WriteSummaryFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLPTableWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_STLWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_STLWriter"
    bl_label = "vtkSTLWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_Header = bpy.props.StringProperty(name='Header', description='Set the header for the file', default='Visualization Toolkit generated SLA File                                        ')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileName", "e_FileType", "m_Header", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_STLWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLDataObjectWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLDataObjectWriter"
    bl_label = "vtkXMLDataObjectWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "e_HeaderType", "e_IdType", "m_NumberOfTimeSteps", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLDataObjectWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLTableWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLTableWriter"
    bl_label = "vtkXMLTableWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces used to stream the table through the pipeline while writing to the file', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WritePiece = bpy.props.IntProperty(name='WritePiece', description='Get/Set the piece to write to the file. If this is negative or equal to the NumberOfPieces, all pieces will be written', default=-1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_WritePiece", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLTableWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_ImageWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ImageWriter"
    bl_label = "vtkImageWriter"
    
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='What dimension are the files to be written. Usually this is 2, or 3. If it is 2 and the input is a volume then the volume will be written as a series of 2d slices', default=2)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. You should specify either a FileName or a FilePrefix. Use FilePrefix if the data is stored in multiple files', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s).You should specify either a FileName or FilePrefix. Use FilePrefix if the data is stored in multiple files')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileDimensionality", "m_FileName", "m_FilePattern", "m_FilePrefix", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ImageWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_DataSetWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_DataSetWriter"
    bl_label = "vtkDataSetWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_DataSetWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_PImageWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_PImageWriter"
    bl_label = "vtkPImageWriter"
    
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='What dimension are the files to be written. Usually this is 2, or 3. If it is 2 and the input is a volume then the volume will be written as a series of 2d slices', default=2)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. You should specify either a FileName or a FilePrefix. Use FilePrefix if the data is stored in multiple files', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s).You should specify either a FileName or FilePrefix. Use FilePrefix if the data is stored in multiple files')
    m_MemoryLimit = bpy.props.IntProperty(name='MemoryLimit', description='Set / Get the memory limit in kibibytes (1024 bytes). The writer will stream to attempt to keep the pipeline size within this limi', default=1048576)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileDimensionality", "m_FileName", "m_FilePattern", "m_FilePrefix", "m_MemoryLimit", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_PImageWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_MNITagPointWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_MNITagPointWriter"
    bl_label = "vtkMNITagPointWriter"
    
    m_Comments = bpy.props.StringProperty(name='Comments', description='Set comments to be added to the file')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_Comments", "m_FileName", ]
    
    def m_connections(self):
        return ['Input 0', 'Input 1'], [], ['LabelText', 'PatientIds', 'Points', 'StructureIds', 'Weights'], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_MNITagPointWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_FacetWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_FacetWriter"
    bl_label = "vtkFacetWriter"
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of Facet datafile to rea', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileName", ]
    
    def m_connections(self):
        return ['Input'], ['Output'], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_FacetWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_HoudiniPolyDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_HoudiniPolyDataWriter"
    bl_label = "vtkHoudiniPolyDataWriter"
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specifies the delimited text file to be loaded', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileName", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_HoudiniPolyDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLPUniformGridAMRWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLPUniformGridAMRWriter"
    bl_label = "vtkXMLPUniformGridAMRWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Get/Set the number of ghost levels to be written', default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WriteMetaFile = bpy.props.IntProperty(name='WriteMetaFile', description='Set whether this instance will write the meta-file. WriteMetaFile is set to flag only on process 0 and all other processes have WriteMetaFile set to 0 by default', default=1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfTimeSteps", "m_WriteMetaFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLPUniformGridAMRWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_BYUWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_BYUWriter"
    bl_label = "vtkBYUWriter"
    
    m_DisplacementFileName = bpy.props.StringProperty(name='DisplacementFileName', description='Specify the name of the displacement file to write', subtype='FILE_PATH')
    m_GeometryFileName = bpy.props.StringProperty(name='GeometryFileName', description='Specify the name of the geometry file to write', subtype='FILE_PATH')
    m_ScalarFileName = bpy.props.StringProperty(name='ScalarFileName', description='Specify the name of the scalar file to write', subtype='FILE_PATH')
    m_TextureFileName = bpy.props.StringProperty(name='TextureFileName', description='Specify the name of the texture file to write', subtype='FILE_PATH')
    m_WriteDisplacement = bpy.props.BoolProperty(name='WriteDisplacement', description='Turn on/off writing the displacement file', default=True)
    m_WriteScalar = bpy.props.BoolProperty(name='WriteScalar', description='Turn on/off writing the scalar file', default=True)
    m_WriteTexture = bpy.props.BoolProperty(name='WriteTexture', description='Turn on/off writing the texture file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_DisplacementFileName", "m_GeometryFileName", "m_ScalarFileName", "m_TextureFileName", "m_WriteDisplacement", "m_WriteScalar", "m_WriteTexture", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_BYUWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_StructuredPointsWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_StructuredPointsWriter"
    bl_label = "vtkStructuredPointsWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteExtent = bpy.props.BoolProperty(name='WriteExtent', description='When WriteExtent is on, vtkStructuredPointsWriter writes data extent in the output file. Otherwise, it writes dimensions. The only time this option is useful is when the extents do not start at (0, 0, 0). This is an options to support writing of older formats while still using a newer VTK', default=False)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteExtent", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_StructuredPointsWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_CompositeDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_CompositeDataWriter"
    bl_label = "vtkCompositeDataWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_CompositeDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLPUnstructuredGridWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLPUnstructuredGridWriter"
    bl_label = "vtkXMLPUnstructuredGridWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_EndPiece = bpy.props.IntProperty(name='EndPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description="Get/Set the ghost level used for this writer's piece", default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces that are being written in parallel', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_StartPiece = bpy.props.IntProperty(name='StartPiece', description='Get/Set the range of pieces assigned to this writer', default=0)
    m_UseSubdirectory = bpy.props.BoolProperty(name='UseSubdirectory', description='Get/Set whether to use a subdirectory to store the piece', default=False)
    m_WriteSummaryFile = bpy.props.BoolProperty(name='WriteSummaryFile', description="Get/Set whether the writer should write the summary file that refers to all of the pieces' individual files. This is on by default. Note that only the first process writes the summary file", default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_EndPiece", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_StartPiece", "m_UseSubdirectory", "m_WriteSummaryFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLPUnstructuredGridWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_MCubesWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_MCubesWriter"
    bl_label = "vtkMCubesWriter"
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    m_LimitsFileName = bpy.props.StringProperty(name='LimitsFileName', description='Set/get file name of marching cubes limits file', subtype='FILE_PATH')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileName", "m_LimitsFileName", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_MCubesWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_DataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_DataWriter"
    bl_label = "vtkDataWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_EdgeFlagsName = bpy.props.StringProperty(name='EdgeFlagsName', description='Give a name to the edge flags data. If not specified, uses default name "edge_flags"')
    m_FieldDataName = bpy.props.StringProperty(name='FieldDataName', description='Give a name to the field data. If not specified, uses default name "field"', default='FieldData')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    m_GlobalIdsName = bpy.props.StringProperty(name='GlobalIdsName', description='Give a name to the global ids data. If not specified, uses default name "global_ids"')
    m_Header = bpy.props.StringProperty(name='Header', description='Specify the header for the vtk data file', default='vtk output')
    m_LookupTableName = bpy.props.StringProperty(name='LookupTableName', description='Give a name to the lookup table. If not specified, uses default name "lookupTable"', default='lookup_table')
    m_NormalsName = bpy.props.StringProperty(name='NormalsName', description='Give a name to the normals data. If not specified, uses default name "normals"')
    m_PedigreeIdsName = bpy.props.StringProperty(name='PedigreeIdsName', description='Give a name to the pedigree ids data. If not specified, uses default name "pedigree_ids"')
    m_ScalarsName = bpy.props.StringProperty(name='ScalarsName', description='Give a name to the scalar data. If not specified, uses default name "scalars"')
    m_TCoordsName = bpy.props.StringProperty(name='TCoordsName', description='Give a name to the texture coordinates data. If not specified, uses default name "textureCoords"')
    m_TensorsName = bpy.props.StringProperty(name='TensorsName', description='Give a name to the tensors data. If not specified, uses default name "tensors"')
    m_VectorsName = bpy.props.StringProperty(name='VectorsName', description='Give a name to the vector data. If not specified, uses default name "vectors"')
    m_WriteArrayMetaData = bpy.props.BoolProperty(name='WriteArrayMetaData', description='If true, vtkInformation objects attached to arrays and array component nameswill be written to the output. Default is true', default=True)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_EdgeFlagsName", "m_FieldDataName", "m_FileName", "e_FileType", "m_GlobalIdsName", "m_Header", "m_LookupTableName", "m_NormalsName", "m_PedigreeIdsName", "m_ScalarsName", "m_TCoordsName", "m_TensorsName", "m_VectorsName", "m_WriteArrayMetaData", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_DataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_PNGWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_PNGWriter"
    bl_label = "vtkPNGWriter"
    
    m_CompressionLevel = bpy.props.IntProperty(name='CompressionLevel', description='Set/Get the zlib compression level. The range is 0-9, with 0 meaning no compression corresponding to the largest file size, and 9 meaning best compression, corresponding to the smallest file size. The default is 5', default=5)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='What dimension are the files to be written. Usually this is 2, or 3. If it is 2 and the input is a volume then the volume will be written as a series of 2d slices', default=2)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. You should specify either a FileName or a FilePrefix. Use FilePrefix if the data is stored in multiple files', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s).You should specify either a FileName or FilePrefix. Use FilePrefix if the data is stored in multiple files')
    m_WriteToMemory = bpy.props.BoolProperty(name='WriteToMemory', description='Write the image to memory (a vtkUnsignedCharArray', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_CompressionLevel", "m_FileDimensionality", "m_FileName", "m_FilePattern", "m_FilePrefix", "m_WriteToMemory", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_PNGWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_PLYWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_PLYWriter"
    bl_label = "vtkPLYWriter"
    e_ColorMode_items = [(x, x, x) for x in ['Default', 'Off', 'UniformCellColor', 'UniformColor', 'UniformPointColor']]
    e_DataByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    e_TextureCoordinatesName_items = [(x, x, x) for x in ['TextureUV', 'UV']]
    
    m_Alpha = bpy.props.IntProperty(name='Alpha', description='Set the alpha to use when using a uniform color (effect point or cells, or both) and EnableAlpha is ON', default=255)
    m_ArrayName = bpy.props.StringProperty(name='ArrayName', description='Specify the array name to use to color the data')
    m_Color = bpy.props.IntVectorProperty(name='Color', description='', default=[255, 255, 255], size=3)
    e_ColorMode = bpy.props.EnumProperty(name='ColorMode', description='These methods enable the user to control how to add color into the PLY output file. The default behavior is as follows. The user provides the name of an array and a component number. If the type of the array is three components, unsigned char, then the data is written as three separate "red", "green" and "blue" properties. If the type of the array is four components, unsigned char, then the data is written as three separate "red", "green" and "blue" properties, dropping the "alpha". If the type is not unsigned char, and a lookup table is provided, then the array/component are mapped through the table to generate three separate "red", "green" and "blue" properties in the PLY file. The user can also set the ColorMode to specify a uniform color for the whole part (on a vertex colors, face colors, or both. (Note: vertex colors or cell colors may be written, depending on where the named array is found. If points and cells have the arrays with the same name, then both colors will be written.', default='Default', items=e_ColorMode_items)
    m_Component = bpy.props.IntProperty(name='Component', description='Specify the array component to use to color the data', default=0)
    e_DataByteOrder = bpy.props.EnumProperty(name='DataByteOrder', description='If the file type is binary, then the user can specify which byte order to use (little versus big endian)', default='LittleEndian', items=e_DataByteOrder_items)
    m_EnableAlpha = bpy.props.BoolProperty(name='EnableAlpha', description='Enable alpha output. Default is off, i.e. only color values will be saved based on ColorMode', default=False)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='Binary', items=e_FileType_items)
    e_TextureCoordinatesName = bpy.props.EnumProperty(name='TextureCoordinatesName', description='Choose the name used for the texture coordinates. (u, v) or (texture_u, texture_v', default='UV', items=e_TextureCoordinatesName_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_Alpha", "m_ArrayName", "m_Color", "e_ColorMode", "m_Component", "e_DataByteOrder", "m_EnableAlpha", "m_FileName", "e_FileType", "e_TextureCoordinatesName", ]
    
    def m_connections(self):
        return ['Input'], [], ['LookupTable'], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_PLYWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_EnSightWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_EnSightWriter"
    bl_label = "vtkEnSightWriter"
    
    m_BaseName = bpy.props.StringProperty(name='BaseName', description='Specify base name of EnSight data files to write')
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify the path and base name of the output files', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Specify the number of ghost levels to include in output file', default=0)
    m_NumberOfBlocks = bpy.props.IntProperty(name='NumberOfBlocks', description="set the number of block ID'", default=0)
    m_Path = bpy.props.StringProperty(name='Path', description='Specify path of EnSight data files to write')
    m_ProcessNumber = bpy.props.IntProperty(name='ProcessNumber', description='Specify which process this writer i', default=0)
    m_TimeStep = bpy.props.IntProperty(name='TimeStep', description='Specify the Timestep that this data is fo', default=0)
    m_TransientGeometry = bpy.props.BoolProperty(name='TransientGeometry', description='Specify whether the geoemtry changes each timestep if false, geometry is only written at timestep ', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BaseName", "m_FileName", "m_GhostLevel", "m_NumberOfBlocks", "m_Path", "m_ProcessNumber", "m_TimeStep", "m_TransientGeometry", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_EnSightWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLRectilinearGridWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLRectilinearGridWriter"
    bl_label = "vtkXMLRectilinearGridWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Get/Set the ghost level used to pad each piece', default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfPieces = bpy.props.IntProperty(name='NumberOfPieces', description='Get/Set the number of pieces used to stream the image through the pipeline while writing to the file', default=1)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WriteExtent = bpy.props.IntVectorProperty(name='WriteExtent', description='', default=[0, -1, 0, -1, 0, -1], size=6)
    m_WritePiece = bpy.props.IntProperty(name='WritePiece', description='Get/Set the piece to write to the file. If this is negative, all pieces will be written', default=-1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfPieces", "m_NumberOfTimeSteps", "m_WriteExtent", "m_WritePiece", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLRectilinearGridWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_XMLHierarchicalBoxDataWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_XMLHierarchicalBoxDataWriter"
    bl_label = "vtkXMLHierarchicalBoxDataWriter"
    e_ByteOrder_items = [(x, x, x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items = [(x, x, x) for x in ['Appended', 'Ascii', 'Binary']]
    e_HeaderType_items = [(x, x, x) for x in ['UInt32', 'UInt64']]
    e_IdType_items = [(x, x, x) for x in ['Int32', 'Int64']]
    
    m_BlockSize = bpy.props.IntProperty(name='BlockSize', description='Get/Set the block size used in compression. When reading, this controls the granularity of how much extra information must be read when only part of the data are requested. The value should be a multiple of the largest scalar data type', default=32768)
    e_ByteOrder = bpy.props.EnumProperty(name='ByteOrder', description="Get/Set the byte order of data written to the file. The default is the machine's hardware byte order", default='LittleEndian', items=e_ByteOrder_items)
    e_DataMode = bpy.props.EnumProperty(name='DataMode', description="Get/Set the data mode used for the file's data. The options are vtkXMLWriter::Ascii, vtkXMLWriter::Binary, and vtkXMLWriter::Appended", default='Appended', items=e_DataMode_items)
    m_EncodeAppendedData = bpy.props.BoolProperty(name='EncodeAppendedData', description='Get/Set whether the appended data section is base64 encoded. If encoded, reading and writing will be slower, but the file will be fully valid XML and text-only. If not encoded, the XML specification will be violated, but reading and writing will be fast. The default is to do the encoding', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get/Set the name of the output file', subtype='FILE_PATH')
    m_GhostLevel = bpy.props.IntProperty(name='GhostLevel', description='Get/Set the number of ghost levels to be written', default=0)
    e_HeaderType = bpy.props.EnumProperty(name='HeaderType', description='Get/Set the binary data header word type. The default is UInt32. Set to UInt64 when storing arrays requiring 64-bit indexing', default='UInt32', items=e_HeaderType_items)
    e_IdType = bpy.props.EnumProperty(name='IdType', description='Get/Set the size of the vtkIdType values stored in the file. The default is the real size of vtkIdType', default='Int64', items=e_IdType_items)
    m_NumberOfTimeSteps = bpy.props.IntProperty(name='NumberOfTimeSteps', description='Set the number of time step', default=1)
    m_WriteMetaFile = bpy.props.IntProperty(name='WriteMetaFile', description='Get/Set whether this instance will write the meta-file', default=1)
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Enable writing to an OutputString instead of the default, a file', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_BlockSize", "e_ByteOrder", "e_DataMode", "m_EncodeAppendedData", "m_FileName", "m_GhostLevel", "e_HeaderType", "e_IdType", "m_NumberOfTimeSteps", "m_WriteMetaFile", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_XMLHierarchicalBoxDataWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_TIFFWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_TIFFWriter"
    bl_label = "vtkTIFFWriter"
    e_Compression_items = [(x, x, x) for x in ['Deflate', 'JPEG', 'LZW', 'NoCompression', 'PackBits']]
    
    e_Compression = bpy.props.EnumProperty(name='Compression', description='Set compression type. Sinze LZW compression is patented outside US, the additional work steps have to be taken in order to use that compression', default='PackBits', items=e_Compression_items)
    m_FileDimensionality = bpy.props.IntProperty(name='FileDimensionality', description='What dimension are the files to be written. Usually this is 2, or 3. If it is 2 and the input is a volume then the volume will be written as a series of 2d slices', default=2)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name for the image file. You should specify either a FileName or a FilePrefix. Use FilePrefix if the data is stored in multiple files', subtype='FILE_PATH')
    m_FilePattern = bpy.props.StringProperty(name='FilePattern', description='The snprintf format used to build filename from FilePrefix and number', default='%s.%d')
    m_FilePrefix = bpy.props.StringProperty(name='FilePrefix', description='Specify file prefix for the image file(s).You should specify either a FileName or FilePrefix. Use FilePrefix if the data is stored in multiple files')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["e_Compression", "m_FileDimensionality", "m_FileName", "m_FilePattern", "m_FilePrefix", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_TIFFWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_MNIObjectWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_MNIObjectWriter"
    bl_label = "vtkMNIObjectWriter"
    e_FileType_items = [(x, x, x) for x in ['ASCII', 'Binary']]
    
    m_FileName = bpy.props.StringProperty(name='FileName', description='Specify file name of vtk polygon data file to write', subtype='FILE_PATH')
    e_FileType = bpy.props.EnumProperty(name='FileType', description='Specify file type (ASCII or BINARY) for vtk data file', default='ASCII', items=e_FileType_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_FileName", "e_FileType", ]
    
    def m_connections(self):
        return ['Input'], [], ['LookupTable', 'Mapper', 'Property'], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_MNIObjectWriter, cat)


# --------------------------------------------------------------


class BVTK_NT_ArrayWriter(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ArrayWriter"
    bl_label = "vtkArrayWriter"
    
    m_Binary = bpy.props.BoolProperty(name='Binary', description='Get / set whether data will be written in binary format (when used as a filter)', default=True)
    m_FileName = bpy.props.StringProperty(name='FileName', description='Get / set the filename where data will be stored (when used as a filter)', subtype='FILE_PATH')
    m_WriteToOutputString = bpy.props.BoolProperty(name='WriteToOutputString', description='Whether to output to a string instead of to a file, which is the default', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_Binary", "m_FileName", "m_WriteToOutputString", ]
    
    def m_connections(self):
        return ['Input'], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ArrayWriter, cat)


# --------------------------------------------------------------
