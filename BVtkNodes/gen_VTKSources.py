from .core import *
TYPENAMES = []


# --------------------------------------------------------------


class BVTK_NT_TrivialProducer(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TrivialProducer'
    bl_label = 'vtkTrivialProducer'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TrivialProducer)
TYPENAMES.append('BVTK_NT_TrivialProducer' )


# --------------------------------------------------------------


class BVTK_NT_ProgrammableDataObjectSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ProgrammableDataObjectSource'
    bl_label = 'vtkProgrammableDataObjectSource'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ProgrammableDataObjectSource)
TYPENAMES.append('BVTK_NT_ProgrammableDataObjectSource' )


# --------------------------------------------------------------


class BVTK_NT_SphereSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SphereSource'
    bl_label = 'vtkSphereSource'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set the center of the sphere. Default is 0,0,0', default=[0.0, 0.0, 0.0], size=3)
    m_EndPhi = bpy.props.FloatProperty(name='EndPhi', description='Set the ending latitude angle. By default EndPhi=180 degrees', default=180.0)
    m_EndTheta = bpy.props.FloatProperty(name='EndTheta', description='Set the ending longitude angle. By default EndTheta=360 degrees', default=360.0)
    m_LatLongTessellation = bpy.props.BoolProperty(name='LatLongTessellation', description='Cause the sphere to be tessellated with edges along the latitude and longitude lines. If off, triangles are generated at non-polar regions, which results in edges that are not parallel to latitude and longitude lines. If on, quadrilaterals are generated everywhere except at the poles. This can be useful for generating a wireframe sphere with natural latitude and longitude lines', default=True)
    m_PhiResolution = bpy.props.IntProperty(name='PhiResolution', description='Set the number of points in the latitude direction (ranging from StartPhi to EndPhi)', default=8)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set radius of sphere. Default is .5', default=0.5)
    m_StartPhi = bpy.props.FloatProperty(name='StartPhi', description='Set the starting latitude angle (0 is at north pole). By default StartPhi=0 degrees', default=0.0)
    m_StartTheta = bpy.props.FloatProperty(name='StartTheta', description='Set the starting longitude angle. By default StartTheta=0 degrees', default=0.0)
    m_ThetaResolution = bpy.props.IntProperty(name='ThetaResolution', description='Set the number of points in the longitude direction (ranging from StartTheta to EndTheta)', default=8)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_EndPhi', 'm_EndTheta', 'm_LatLongTessellation', 'm_PhiResolution', 'm_Radius', 'm_StartPhi', 'm_StartTheta', 'm_ThetaResolution', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SphereSource)
TYPENAMES.append('BVTK_NT_SphereSource' )


# --------------------------------------------------------------


class BVTK_NT_EnsembleSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EnsembleSource'
    bl_label = 'vtkEnsembleSource'
    
    m_CurrentMember = bpy.props.IntProperty(name='CurrentMember', description='Set/Get the current ensemble member to process. Note that this data member will not be used if the UPDATE_MEMBER key is present in the pipeline. Also, this data member may be removed in the future. Unless it is absolutely necessary to use this data member, use the UPDATE_MEMBER key instead', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CurrentMember', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EnsembleSource)
TYPENAMES.append('BVTK_NT_EnsembleSource' )


# --------------------------------------------------------------


class BVTK_NT_ParametricFunctionSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ParametricFunctionSource'
    bl_label = 'vtkParametricFunctionSource'
    e_ScalarMode_items = [(x, x, x) for x in ['Distance', 'FunctionDefined', 'Modulus', 'None', 'Phase', 'Quadrant', 'U', 'U0', 'U0V0', 'V', 'V0', 'X', 'Y', 'Z']]
    
    m_GenerateNormals = bpy.props.BoolProperty(name='GenerateNormals', description='Set/Get the generation of normals. This is on by default. Note that this is only applicable to parametric surfaces whose parametric dimension is 2', default=True)
    m_GenerateTextureCoordinates = bpy.props.BoolProperty(name='GenerateTextureCoordinates', description='Set/Get the generation of texture coordinates. This is off by default. Note that this is only applicable to parametric surfaces whose parametric dimension is 2. Note that texturing may fail in some cases', default=True)
    e_ScalarMode = bpy.props.EnumProperty(name='ScalarMode', description='Get/Set the mode used for the scalar data. See SCALAR_MODE for a description of the types of scalars generated', default='None', items=e_ScalarMode_items)
    m_UResolution = bpy.props.IntProperty(name='UResolution', description='Set/Get the number of subdivisions / tessellations in the u parametric direction. Note that the number of tessellant points in the u direction is the UResolution + 1', default=50)
    m_VResolution = bpy.props.IntProperty(name='VResolution', description='Set/Get the number of subdivisions / tessellations in the v parametric direction. Note that the number of tessellant points in the v direction is the VResolution + 1', default=50)
    m_WResolution = bpy.props.IntProperty(name='WResolution', description='Set/Get the number of subdivisions / tessellations in the w parametric direction. Note that the number of tessellant points in the w direction is the WResolution + 1', default=50)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GenerateNormals', 'm_GenerateTextureCoordinates', 'e_ScalarMode', 'm_UResolution', 'm_VResolution', 'm_WResolution', ]
    
    def m_connections(self):
        return [], ['Output'], ['ParametricFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ParametricFunctionSource)
TYPENAMES.append('BVTK_NT_ParametricFunctionSource' )


# --------------------------------------------------------------


class BVTK_NT_EllipseArcSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EllipseArcSource'
    bl_label = 'vtkEllipseArcSource'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set position of the center of the ellipse that define the arc. Default is 0, 0, 0', default=[0.0, 0.0, 0.0], size=3)
    m_MajorRadiusVector = bpy.props.FloatVectorProperty(name='MajorRadiusVector', description='Set Major Radius Vector. It defines the origin of polar angle and the major radius size. Default is 1, 0, 0', default=[1.0, 0.0, 0.0], size=3)
    m_Normal = bpy.props.FloatVectorProperty(name='Normal', description='Set normal vector. Represents the plane in which the ellipse will be drawn. Default 0, 0, 1', default=[0.0, 0.0, 1.0], size=3)
    m_Ratio = bpy.props.FloatProperty(name='Ratio', description='Set the ratio of the ellipse, i.e. the ratio b/a _ b: minor radius; a: major radius default is 1', default=1.0)
    m_Resolution = bpy.props.IntProperty(name='Resolution', description='Divide line into resolution number of pieces. Note: if Resolution is set to 1 the arc is a straight line. Default is 100', default=100)
    m_SegmentAngle = bpy.props.FloatProperty(name='SegmentAngle', description='Angular sector occupied by the arc, beginning at Start Angle Default is 90', default=90.0)
    m_StartAngle = bpy.props.FloatProperty(name='StartAngle', description='Set the start angle. The angle where the plot begins. Default is 0', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_MajorRadiusVector', 'm_Normal', 'm_Ratio', 'm_Resolution', 'm_SegmentAngle', 'm_StartAngle', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EllipseArcSource)
TYPENAMES.append('BVTK_NT_EllipseArcSource' )


# --------------------------------------------------------------


class BVTK_NT_ImageNoiseSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageNoiseSource'
    bl_label = 'vtkImageNoiseSource'
    
    m_Maximum = bpy.props.FloatProperty(name='Maximum', description='Set/Get the minimum and maximum values for the generated noise', default=10.0)
    m_Minimum = bpy.props.FloatProperty(name='Minimum', description='Set/Get the minimum and maximum values for the generated noise', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Maximum', 'm_Minimum', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageNoiseSource)
TYPENAMES.append('BVTK_NT_ImageNoiseSource' )


# --------------------------------------------------------------


class BVTK_NT_RTAnalyticSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RTAnalyticSource'
    bl_label = 'vtkRTAnalyticSource'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='', default=[0.0, 0.0, 0.0], size=3)
    m_Maximum = bpy.props.FloatProperty(name='Maximum', description='Set/Get the Maximum value of the function. Initial value is 255.0', default=255.0)
    m_StandardDeviation = bpy.props.FloatProperty(name='StandardDeviation', description='Set/Get the standard deviation of the function. Initial value is 0.5', default=0.5)
    m_SubsampleRate = bpy.props.IntProperty(name='SubsampleRate', description='Set/Get the sub-sample rate. Initial value is 1', default=1)
    m_XFreq = bpy.props.FloatProperty(name='XFreq', description='Set/Get the natural frequency in x. Initial value is 60', default=60.0)
    m_XMag = bpy.props.FloatProperty(name='XMag', description='Set/Get the magnitude in x. Initial value is 10', default=10.0)
    m_YFreq = bpy.props.FloatProperty(name='YFreq', description='Set/Get the natural frequency in y. Initial value is 30', default=30.0)
    m_YMag = bpy.props.FloatProperty(name='YMag', description='Set/Get the magnitude in y. Initial value is 18', default=18.0)
    m_ZFreq = bpy.props.FloatProperty(name='ZFreq', description='Set/Get the natural frequency in z. Initial value is 40', default=40.0)
    m_ZMag = bpy.props.FloatProperty(name='ZMag', description='Set/Get the magnitude in z. Initial value is 5', default=5.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_Maximum', 'm_StandardDeviation', 'm_SubsampleRate', 'm_XFreq', 'm_XMag', 'm_YFreq', 'm_YMag', 'm_ZFreq', 'm_ZMag', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RTAnalyticSource)
TYPENAMES.append('BVTK_NT_RTAnalyticSource' )


# --------------------------------------------------------------


class BVTK_NT_ImageMandelbrotSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageMandelbrotSource'
    bl_label = 'vtkImageMandelbrotSource'
    
    m_ConstantSize = bpy.props.BoolProperty(name='ConstantSize', description='This flag determines whether the Size or spacing of a data set remain constant (when extent is changed). By default, size remains constant', default=True)
    m_MaximumNumberOfIterations = bpy.props.IntProperty(name='MaximumNumberOfIterations', description='The maximum number of cycles run to see if the value goes over ', default=100)
    m_OriginCX = bpy.props.FloatVectorProperty(name='OriginCX', description='', default=[-1.75, -1.25, 0.0, 0.0], size=4)
    m_SampleCX = bpy.props.FloatVectorProperty(name='SampleCX', description='', default=[0.01, 0.01, 0.01, 0.01], size=4)
    m_SubsampleRate = bpy.props.IntProperty(name='SubsampleRate', description='Set/Get a subsample rate', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ConstantSize', 'm_MaximumNumberOfIterations', 'm_OriginCX', 'm_SampleCX', 'm_SubsampleRate', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageMandelbrotSource)
TYPENAMES.append('BVTK_NT_ImageMandelbrotSource' )


# --------------------------------------------------------------


class BVTK_NT_SQLDatabaseTableSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SQLDatabaseTableSource'
    bl_label = 'vtkSQLDatabaseTableSource'
    
    m_GeneratePedigreeIds = bpy.props.BoolProperty(name='GeneratePedigreeIds', description='If on (default), generates pedigree ids automatically. If off, assign one of the arrays to be the pedigree id', default=True)
    m_PedigreeIdArrayName = bpy.props.StringProperty(name='PedigreeIdArrayName', description='The name of the array for generating or assigning pedigree ids (default "id")', default='id')
    m_Query = bpy.props.StringProperty(name='Query', description='', default='')
    m_URL = bpy.props.StringProperty(name='URL', description='', default='')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GeneratePedigreeIds', 'm_PedigreeIdArrayName', 'm_Query', 'm_URL', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SQLDatabaseTableSource)
TYPENAMES.append('BVTK_NT_SQLDatabaseTableSource' )


# --------------------------------------------------------------


class BVTK_NT_SectorSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SectorSource'
    bl_label = 'vtkSectorSource'
    
    m_CircumferentialResolution = bpy.props.IntProperty(name='CircumferentialResolution', description='Set the number of points in circumferential direction', default=6)
    m_EndAngle = bpy.props.FloatProperty(name='EndAngle', description='Set the end angle of the sector', default=90.0)
    m_InnerRadius = bpy.props.FloatProperty(name='InnerRadius', description='Specify inner radius of the sector', default=1.0)
    m_OuterRadius = bpy.props.FloatProperty(name='OuterRadius', description='Specify outer radius of the sector', default=2.0)
    m_RadialResolution = bpy.props.IntProperty(name='RadialResolution', description='Set the number of points in radius direction', default=1)
    m_StartAngle = bpy.props.FloatProperty(name='StartAngle', description='Set the start angle of the sector', default=0.0)
    m_ZCoord = bpy.props.FloatProperty(name='ZCoord', description='Specify the z coordinate of the sector', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CircumferentialResolution', 'm_EndAngle', 'm_InnerRadius', 'm_OuterRadius', 'm_RadialResolution', 'm_StartAngle', 'm_ZCoord', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SectorSource)
TYPENAMES.append('BVTK_NT_SectorSource' )


# --------------------------------------------------------------


class BVTK_NT_FrustumSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_FrustumSource'
    bl_label = 'vtkFrustumSource'
    
    m_LinesLength = bpy.props.FloatProperty(name='LinesLength', description='Length of the extra lines. This a stricly positive value. Initial value is 1.0', default=1.0)
    m_ShowLines = bpy.props.BoolProperty(name='ShowLines', description='Tells if some extra lines will be generated. Initial value is true', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_LinesLength', 'm_ShowLines', ]
    
    def m_connections(self):
        return [], ['Output'], ['Planes'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_FrustumSource)
TYPENAMES.append('BVTK_NT_FrustumSource' )


# --------------------------------------------------------------


class BVTK_NT_TimeSourceExample(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TimeSourceExample'
    bl_label = 'vtkTimeSourceExample'
    
    m_Analytic = bpy.props.BoolProperty(name='Analytic', description='When off (the default) this source produces a discrete set of values. When on, this source produces a value analytically for any queried time', default=True)
    m_Growing = bpy.props.BoolProperty(name='Growing', description='When off (the default) this produces a single cell data set. When on the the number of cells (in the Y direction) grows and shrinks over time along a hat function', default=True)
    m_XAmplitude = bpy.props.FloatProperty(name='XAmplitude', description='When 0.0 (the default) this produces a data set that is stationary. When on the data set moves in the X/Y plane over a sin wave over time, amplified by the value', default=0.0)
    m_YAmplitude = bpy.props.FloatProperty(name='YAmplitude', description='When 0.0 (the default) this produces a data set that is stationary. When on the data set moves in the X/Y plane over a sin wave over time, amplified by the value', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Analytic', 'm_Growing', 'm_XAmplitude', 'm_YAmplitude', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TimeSourceExample)
TYPENAMES.append('BVTK_NT_TimeSourceExample' )


# --------------------------------------------------------------


class BVTK_NT_PSphereSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PSphereSource'
    bl_label = 'vtkPSphereSource'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set the center of the sphere. Default is 0,0,0', default=[0.0, 0.0, 0.0], size=3)
    m_EndPhi = bpy.props.FloatProperty(name='EndPhi', description='Set the ending latitude angle. By default EndPhi=180 degrees', default=180.0)
    m_EndTheta = bpy.props.FloatProperty(name='EndTheta', description='Set the ending longitude angle. By default EndTheta=360 degrees', default=360.0)
    m_LatLongTessellation = bpy.props.BoolProperty(name='LatLongTessellation', description='Cause the sphere to be tessellated with edges along the latitude and longitude lines. If off, triangles are generated at non-polar regions, which results in edges that are not parallel to latitude and longitude lines. If on, quadrilaterals are generated everywhere except at the poles. This can be useful for generating a wireframe sphere with natural latitude and longitude lines', default=True)
    m_PhiResolution = bpy.props.IntProperty(name='PhiResolution', description='Set the number of points in the latitude direction (ranging from StartPhi to EndPhi)', default=8)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set radius of sphere. Default is .5', default=0.5)
    m_StartPhi = bpy.props.FloatProperty(name='StartPhi', description='Set the starting latitude angle (0 is at north pole). By default StartPhi=0 degrees', default=0.0)
    m_StartTheta = bpy.props.FloatProperty(name='StartTheta', description='Set the starting longitude angle. By default StartTheta=0 degrees', default=0.0)
    m_ThetaResolution = bpy.props.IntProperty(name='ThetaResolution', description='Set the number of points in the longitude direction (ranging from StartTheta to EndTheta)', default=8)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_EndPhi', 'm_EndTheta', 'm_LatLongTessellation', 'm_PhiResolution', 'm_Radius', 'm_StartPhi', 'm_StartTheta', 'm_ThetaResolution', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PSphereSource)
TYPENAMES.append('BVTK_NT_PSphereSource' )


# --------------------------------------------------------------


class BVTK_NT_PointLoad(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PointLoad'
    bl_label = 'vtkPointLoad'
    
    m_ComputeEffectiveStress = bpy.props.BoolProperty(name='ComputeEffectiveStress', description='Turn on/off computation of effective stress scalar. These methods do nothing. The effective stress is always computed', default=True)
    m_LoadValue = bpy.props.FloatProperty(name='LoadValue', description='Set/Get value of applied load', default=1.0)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Specify the region in space over which the tensors are computed. The point load is assumed to be applied at top center of the volume', default=[-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], size=6)
    m_PoissonsRatio = bpy.props.FloatProperty(name='PoissonsRatio', description="Set/Get Poisson's ratio", default=0.3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeEffectiveStress', 'm_LoadValue', 'm_ModelBounds', 'm_PoissonsRatio', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PointLoad)
TYPENAMES.append('BVTK_NT_PointLoad' )


# --------------------------------------------------------------


class BVTK_NT_LassoStencilSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LassoStencilSource'
    bl_label = 'vtkLassoStencilSource'
    e_Shape_items = [(x, x, x) for x in ['Polygon', 'Spline']]
    
    m_OutputOrigin = bpy.props.FloatVectorProperty(name='OutputOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    m_OutputSpacing = bpy.props.FloatVectorProperty(name='OutputSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_OutputWholeExtent = bpy.props.IntVectorProperty(name='OutputWholeExtent', description='', default=[0, -1, 0, -1, 0, -1], size=6)
    e_Shape = bpy.props.EnumProperty(name='Shape', description='The shape to use, default is "Polygon". The spline is a cardinal spline. Bezier splines are not yet supported', default='Polygon', items=e_Shape_items)
    m_SliceOrientation = bpy.props.IntProperty(name='SliceOrientation', description='The slice orientation. The default is 2, which is XY. Other values are 0, which is YZ, and 1, which is XZ', default=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_OutputOrigin', 'm_OutputSpacing', 'm_OutputWholeExtent', 'e_Shape', 'm_SliceOrientation', ]
    
    def m_connections(self):
        return [], ['Output'], ['Points'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LassoStencilSource)
TYPENAMES.append('BVTK_NT_LassoStencilSource' )


# --------------------------------------------------------------


class BVTK_NT_ImplicitFunctionToImageStencil(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImplicitFunctionToImageStencil'
    bl_label = 'vtkImplicitFunctionToImageStencil'
    
    m_OutputOrigin = bpy.props.FloatVectorProperty(name='OutputOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    m_OutputSpacing = bpy.props.FloatVectorProperty(name='OutputSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_OutputWholeExtent = bpy.props.IntVectorProperty(name='OutputWholeExtent', description='', default=[0, -1, 0, -1, 0, -1], size=6)
    m_Threshold = bpy.props.FloatProperty(name='Threshold', description='Set the threshold value for the implicit function', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_OutputOrigin', 'm_OutputSpacing', 'm_OutputWholeExtent', 'm_Threshold', ]
    
    def m_connections(self):
        return [], ['Output'], ['Input'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImplicitFunctionToImageStencil)
TYPENAMES.append('BVTK_NT_ImplicitFunctionToImageStencil' )


# --------------------------------------------------------------


class BVTK_NT_ImageImport(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageImport'
    bl_label = 'vtkImageImport'
    e_DataScalarType_items = [(x, x, x) for x in ['Double', 'Float', 'Int', 'Short', 'UnsignedChar', 'UnsignedShort']]
    
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set/Get the data type of pixels in the imported data. This is used as the scalar type of the Output. Default: Short', default='Short', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set/Get the number of scalar components, for RGB images this must be 3. Default: 1', default=1)
    m_ScalarArrayName = bpy.props.StringProperty(name='ScalarArrayName', description='Set/get the scalar array name for this data set. Initial value is "scalars"', default='scalars')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_NumberOfScalarComponents', 'm_ScalarArrayName', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageImport)
TYPENAMES.append('BVTK_NT_ImageImport' )


# --------------------------------------------------------------


class BVTK_NT_ImageSinusoidSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageSinusoidSource'
    bl_label = 'vtkImageSinusoidSource'
    
    m_Amplitude = bpy.props.FloatProperty(name='Amplitude', description='Set/Get the magnitude of the sinusoid', default=255.0)
    m_Period = bpy.props.FloatProperty(name='Period', description='Set/Get the period of the sinusoid in pixels', default=20.0)
    m_Phase = bpy.props.FloatProperty(name='Phase', description='Set/Get the phase: 0->2Pi. 0 => Cosine, pi/2 => Sine', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Amplitude', 'm_Period', 'm_Phase', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageSinusoidSource)
TYPENAMES.append('BVTK_NT_ImageSinusoidSource' )


# --------------------------------------------------------------


class BVTK_NT_PlatonicSolidSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PlatonicSolidSource'
    bl_label = 'vtkPlatonicSolidSource'
    e_SolidType_items = [(x, x, x) for x in ['Cube', 'Dodecahedron', 'Icosahedron', 'Octahedron', 'Tetrahedron']]
    
    e_SolidType = bpy.props.EnumProperty(name='SolidType', description='Specify the type of PlatonicSolid solid to create', default='Tetrahedron', items=e_SolidType_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_SolidType', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PlatonicSolidSource)
TYPENAMES.append('BVTK_NT_PlatonicSolidSource' )


# --------------------------------------------------------------


class BVTK_NT_PolyLineSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PolyLineSource'
    bl_label = 'vtkPolyLineSource'
    
    m_Closed = bpy.props.BoolProperty(name='Closed', description='Set whether to close the poly line by connecting the last and first points', default=True)
    m_NumberOfPoints = bpy.props.IntProperty(name='NumberOfPoints', description='Set the number of points in the poly line', default=0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Closed', 'm_NumberOfPoints', ]
    
    def m_connections(self):
        return [], ['Output'], ['Points'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PolyLineSource)
TYPENAMES.append('BVTK_NT_PolyLineSource' )


# --------------------------------------------------------------


class BVTK_NT_TexturedSphereSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TexturedSphereSource'
    bl_label = 'vtkTexturedSphereSource'
    
    m_Phi = bpy.props.FloatProperty(name='Phi', description='Set the maximum latitude angle (0 is at north pole)', default=0.0)
    m_PhiResolution = bpy.props.IntProperty(name='PhiResolution', description='Set the number of points in the latitude direction', default=8)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set radius of sphere', default=0.5)
    m_Theta = bpy.props.FloatProperty(name='Theta', description='Set the maximum longitude angle', default=0.0)
    m_ThetaResolution = bpy.props.IntProperty(name='ThetaResolution', description='Set the number of points in the longitude direction', default=8)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Phi', 'm_PhiResolution', 'm_Radius', 'm_Theta', 'm_ThetaResolution', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TexturedSphereSource)
TYPENAMES.append('BVTK_NT_TexturedSphereSource' )


# --------------------------------------------------------------


class BVTK_NT_VideoSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VideoSource'
    bl_label = 'vtkVideoSource'
    e_OutputFormat_items = [(x, x, x) for x in ['Luminance', 'RGB', 'RGBA']]
    
    m_AutoAdvance = bpy.props.BoolProperty(name='AutoAdvance', description='Set whether to automatically advance the buffer before each grab. Default: o', default=True)
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_FrameBufferSize = bpy.props.IntProperty(name='FrameBufferSize', description="Set size of the frame buffer, i.e. the number of frames that the 'tape' can store", default=1)
    m_FrameCount = bpy.props.IntProperty(name='FrameCount', description='This value is incremented each time a frame is grabbed. reset it to zero (or any other value) at any time', default=0)
    m_FrameRate = bpy.props.FloatProperty(name='FrameRate', description='Request a particular frame rate (default 30 frames per second)', default=30.0)
    m_NumberOfOutputFrames = bpy.props.IntProperty(name='NumberOfOutputFrames', description='Set the number of frames to copy to the output on each execute. The frames will be concatenated along the Z dimension, with the most recent frame first. Default: ', default=1)
    m_Opacity = bpy.props.FloatProperty(name='Opacity', description='For RGBA output only (4 scalar components), set the opacity. This will not modify the existing contents of the framebuffer, only subsequently grabbed frames', default=1.0)
    e_OutputFormat = bpy.props.EnumProperty(name='OutputFormat', description='Set the output format. This must be appropriate for device, usually only VTK_LUMINANCE, VTK_RGB, and VTK_RGBA are supported', default='Luminance', items=e_OutputFormat_items)
    m_OutputWholeExtent = bpy.props.IntVectorProperty(name='OutputWholeExtent', description='', default=[0, -1, 0, -1, 0, -1], size=6)
    m_StartTimeStamp = bpy.props.FloatProperty(name='StartTimeStamp', description='And internal variable which marks the beginning of a Record session. These methods are for internal use only', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutoAdvance', 'm_DataOrigin', 'm_DataSpacing', 'm_FrameBufferSize', 'm_FrameCount', 'm_FrameRate', 'm_NumberOfOutputFrames', 'm_Opacity', 'e_OutputFormat', 'm_OutputWholeExtent', 'm_StartTimeStamp', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VideoSource)
TYPENAMES.append('BVTK_NT_VideoSource' )


# --------------------------------------------------------------


class BVTK_NT_HyperTreeGridSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_HyperTreeGridSource'
    bl_label = 'vtkHyperTreeGridSource'
    
    m_BranchFactor = bpy.props.IntProperty(name='BranchFactor', description='Set/Get the subdivision factor in the grid refinement schem', default=2)
    m_Descriptor = bpy.props.StringProperty(name='Descriptor', description='Set/Get the string used to describe the grid', default='.')
    m_Dimension = bpy.props.IntProperty(name='Dimension', description='Set/Get the dimensionality of the gri', default=3)
    m_GenerateInterfaceFields = bpy.props.BoolProperty(name='GenerateInterfaceFields', description='Set/get whether cell-centered interface fields should be generated. Default: fals', default=False)
    m_GridScale = bpy.props.FloatVectorProperty(name='GridScale', description='', default=[1.0, 1.0, 1.0], size=3)
    m_GridSize = bpy.props.IntVectorProperty(name='GridSize', description='', default=[1, 1, 1], size=3)
    m_MaterialMask = bpy.props.StringProperty(name='MaterialMask', description='Set/Get the string used to as a material mask', default='0')
    m_MaximumLevel = bpy.props.IntProperty(name='MaximumLevel', description='Set the maximum number of levels of the hypertrees. \\pre positive_levels: levels>=1 \\post is_set: this->GetLevels()==levels \\post min_is_valid: this->GetMinLevels()<this->GetLevels(', default=1)
    m_Orientation = bpy.props.IntProperty(name='Orientation', description='Set/Get the orientation of the grid (in 1D and 2D', default=0)
    m_Origin = bpy.props.FloatVectorProperty(name='Origin', description='', default=[0.0, 0.0, 0.0], size=3)
    m_TransposedRootIndexing = bpy.props.BoolProperty(name='TransposedRootIndexing', description='Specify whether indexing mode of grid root cells must be transposed to x-axis first, z-axis last, instead of the default z-axis first, k-axis las', default=False)
    m_UseDescriptor = bpy.props.BoolProperty(name='UseDescriptor', description='Set/get whether the descriptor string should be used. NB: Otherwise a quadric definition is expected. Default: tru', default=True)
    m_UseMaterialMask = bpy.props.BoolProperty(name='UseMaterialMask', description='Set/get whether the material mask should be used. NB: This is only used when UseDescriptor is ON Default: fals', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BranchFactor', 'm_Descriptor', 'm_Dimension', 'm_GenerateInterfaceFields', 'm_GridScale', 'm_GridSize', 'm_MaterialMask', 'm_MaximumLevel', 'm_Orientation', 'm_Origin', 'm_TransposedRootIndexing', 'm_UseDescriptor', 'm_UseMaterialMask', ]
    
    def m_connections(self):
        return [], ['Output'], ['DescriptorBits', 'MaterialMaskBits', 'Quadric'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_HyperTreeGridSource)
TYPENAMES.append('BVTK_NT_HyperTreeGridSource' )


# --------------------------------------------------------------


class BVTK_NT_EarthSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EarthSource'
    bl_label = 'vtkEarthSource'
    
    m_OnRatio = bpy.props.IntProperty(name='OnRatio', description='Turn on every nth entity. This controls how much detail the model will have. The maximum ratio is sixteen. (The smaller OnRatio, the more detail there is.', default=10)
    m_Outline = bpy.props.BoolProperty(name='Outline', description='Turn on/off drawing continents as filled polygons or as wireframe outlines. Warning: some graphics systems will have trouble with the very large, concave filled polygons. Recommend you use OutlienOn (i.e., disable filled polygons) for now', default=True)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set radius of earth', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_OnRatio', 'm_Outline', 'm_Radius', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EarthSource)
TYPENAMES.append('BVTK_NT_EarthSource' )


# --------------------------------------------------------------


class BVTK_NT_TessellatedBoxSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TessellatedBoxSource'
    bl_label = 'vtkTessellatedBoxSource'
    
    m_Bounds = bpy.props.FloatVectorProperty(name='Bounds', description='', default=[-0.5, 0.5, -0.5, 0.5, -0.5, 0.5], size=6)
    m_DuplicateSharedPoints = bpy.props.BoolProperty(name='DuplicateSharedPoints', description='Flag to tell the source to duplicate points shared between faces (vertices of the box and internal edge points). Initial value is false. Implementation note: duplicating points is an easier method to implement than a minimal number of points', default=True)
    m_Level = bpy.props.IntProperty(name='Level', description='Set the level of subdivision of the faces. \\pre positive_level: level>=', default=0)
    m_Quads = bpy.props.BoolProperty(name='Quads', description='Flag to tell the source to generate either a quad or two triangle for a set of four points. Initial value is false (generate triangles)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Bounds', 'm_DuplicateSharedPoints', 'm_Level', 'm_Quads', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TessellatedBoxSource)
TYPENAMES.append('BVTK_NT_TessellatedBoxSource' )


# --------------------------------------------------------------


class BVTK_NT_ImageGridSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageGridSource'
    bl_label = 'vtkImageGridSource'
    e_DataScalarType_items = [(x, x, x) for x in ['Double', 'Int', 'Short', 'UnsignedChar', 'UnsignedShort']]
    
    m_DataOrigin = bpy.props.FloatVectorProperty(name='DataOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_DataScalarType = bpy.props.EnumProperty(name='DataScalarType', description='Set/Get the data type of pixels in the imported data. As a convenience, the OutputScalarType is set to the same value', items=e_DataScalarType_items)
    m_DataSpacing = bpy.props.FloatVectorProperty(name='DataSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_FillValue = bpy.props.FloatProperty(name='FillValue', description='Set the grey level of the fill. Default 0.0', default=0.0)
    m_GridOrigin = bpy.props.IntVectorProperty(name='GridOrigin', description='', default=[0, 0, 0], size=3)
    m_GridSpacing = bpy.props.IntVectorProperty(name='GridSpacing', description='', default=[10, 10, 0], size=3)
    m_LineValue = bpy.props.FloatProperty(name='LineValue', description='Set the grey level of the lines. Default 1.0', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DataOrigin', 'e_DataScalarType', 'm_DataSpacing', 'm_FillValue', 'm_GridOrigin', 'm_GridSpacing', 'm_LineValue', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageGridSource)
TYPENAMES.append('BVTK_NT_ImageGridSource' )


# --------------------------------------------------------------


class BVTK_NT_SelectionSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SelectionSource'
    bl_label = 'vtkSelectionSource'
    
    m_ArrayComponent = bpy.props.IntProperty(name='ArrayComponent', description='Access to the component number for the array specified by ArrayName. Default is component 0. Use -1 for magnitude', default=0)
    m_ArrayName = bpy.props.StringProperty(name='ArrayName', description="Access to the name of the selection's subset description array")
    m_CompositeIndex = bpy.props.IntProperty(name='CompositeIndex', description='If CompositeIndex < 0 then COMPOSITE_INDEX() is not added to the output', default=-1)
    m_ContainingCells = bpy.props.IntProperty(name='ContainingCells', description='When extracting by points, extract the cells that contain the passing points', default=1)
    m_ContentType = bpy.props.IntProperty(name='ContentType', description='Set the content type for the generated selection. Possible values are as defined by vtkSelection::SelectionContent', default=4)
    m_FieldType = bpy.props.IntProperty(name='FieldType', description='Set the field type for the generated selection. Possible values are as defined by vtkSelection::SelectionField', default=0)
    m_HierarchicalIndex = bpy.props.IntProperty(name='HierarchicalIndex', description='If HierarchicalLevel or HierarchicalIndex < 0 , then HIERARCHICAL_LEVEL() and HIERARCHICAL_INDEX() keys are not added to the output', default=-1)
    m_HierarchicalLevel = bpy.props.IntProperty(name='HierarchicalLevel', description='If HierarchicalLevel or HierarchicalIndex < 0 , then HIERARCHICAL_LEVEL() and HIERARCHICAL_INDEX() keys are not added to the output', default=-1)
    m_Inverse = bpy.props.IntProperty(name='Inverse', description='Determines whether the selection describes what to include or exclude. Default is 0, meaning include', default=0)
    m_QueryString = bpy.props.StringProperty(name='QueryString', description='Set/Get the query expression string')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayComponent', 'm_ArrayName', 'm_CompositeIndex', 'm_ContainingCells', 'm_ContentType', 'm_FieldType', 'm_HierarchicalIndex', 'm_HierarchicalLevel', 'm_Inverse', 'm_QueryString', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SelectionSource)
TYPENAMES.append('BVTK_NT_SelectionSource' )


# --------------------------------------------------------------


class BVTK_NT_BoundedPointSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BoundedPointSource'
    bl_label = 'vtkBoundedPointSource'
    
    m_Bounds = bpy.props.FloatVectorProperty(name='Bounds', description='Set the bounding box for the point distribution. By default the bounds is (-1,1,-1,1,-1,1)', default=[-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], size=6)
    m_NumberOfPoints = bpy.props.IntProperty(name='NumberOfPoints', description='Set the number of points to generate', default=100)
    m_ProduceCellOutput = bpy.props.BoolProperty(name='ProduceCellOutput', description='Indicate whether to produce a vtkPolyVertex cell to go along with the output vtkPoints generated. By default a cell is NOT produced. Some filters do not need the vtkPolyVertex which just consumes a lot of memory', default=False)
    m_ProduceRandomScalars = bpy.props.BoolProperty(name='ProduceRandomScalars', description='Indicate whether to produce random point scalars in the output. By default this is off', default=False)
    m_ScalarRange = bpy.props.FloatVectorProperty(name='ScalarRange', description='Set the range in which the random scalars should be produced. By default the scalar range is (0,1)', default=[0.0, 1.0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Bounds', 'm_NumberOfPoints', 'm_ProduceCellOutput', 'm_ProduceRandomScalars', 'm_ScalarRange', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BoundedPointSource)
TYPENAMES.append('BVTK_NT_BoundedPointSource' )


# --------------------------------------------------------------


class BVTK_NT_SampleFunction(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SampleFunction'
    bl_label = 'vtkSampleFunction'
    e_OutputScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Long', 'Short', 'UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    
    m_CapValue = bpy.props.FloatProperty(name='CapValue', description='Set the cap value', default=1e+30)
    m_Capping = bpy.props.BoolProperty(name='Capping', description='Turn on/off capping. If capping is on, then the outer boundaries of the structured point set are set to cap value. This can be used to insure surfaces are closed', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Turn on/off the computation of normals (normals are float values)', default=True)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Specify the region in space over which the sampling occurs. The bounds is specified as (xMin,xMax, yMin,yMax, zMin,zMax)', default=[-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], size=6)
    m_NormalArrayName = bpy.props.StringProperty(name='NormalArrayName', description='Set/get the normal array name for this data set. Initial value is "normals"', default='normals')
    e_OutputScalarType = bpy.props.EnumProperty(name='OutputScalarType', description='Set what type of scalar data this source should generate', default='Double', items=e_OutputScalarType_items)
    m_ScalarArrayName = bpy.props.StringProperty(name='ScalarArrayName', description='Set/get the scalar array name for this data set. Initial value is "scalars"', default='scalars')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CapValue', 'm_Capping', 'm_ComputeNormals', 'm_ModelBounds', 'm_NormalArrayName', 'e_OutputScalarType', 'm_ScalarArrayName', ]
    
    def m_connections(self):
        return [], ['Output'], ['ImplicitFunction'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SampleFunction)
TYPENAMES.append('BVTK_NT_SampleFunction' )


# --------------------------------------------------------------


class BVTK_NT_SuperquadricSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SuperquadricSource'
    bl_label = 'vtkSuperquadricSource'
    
    m_AxisOfSymmetry = bpy.props.IntProperty(name='AxisOfSymmetry', description='Set/Get axis of symmetry for superquadric (x axis: 0, y axis: 1, z axis: 2). Initial value is 1', default=1)
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set the center of the superquadric. Default is 0,0,0', default=[0.0, 0.0, 0.0], size=3)
    m_PhiResolution = bpy.props.IntProperty(name='PhiResolution', description='Set the number of points in the latitude direction. Initial value is 16', default=16)
    m_PhiRoundness = bpy.props.FloatProperty(name='PhiRoundness', description='Set/Get Superquadric north/south roundness. Values range from 0 (rectangular) to 1 (circular) to higher orders. Initial value is 1.0', default=1.0)
    m_Scale = bpy.props.FloatVectorProperty(name='Scale', description='Set the scale factors of the superquadric. Default is 1,1,1', default=[1.0, 1.0, 1.0], size=3)
    m_Size = bpy.props.FloatProperty(name='Size', description='Set/Get Superquadric isotropic size. Initial value is 0.5', default=0.5)
    m_ThetaResolution = bpy.props.IntProperty(name='ThetaResolution', description='Set the number of points in the longitude direction. Initial value is 16', default=16)
    m_ThetaRoundness = bpy.props.FloatProperty(name='ThetaRoundness', description='Set/Get Superquadric east/west roundness. Values range from 0 (rectangular) to 1 (circular) to higher orders. Initial value is 1.0', default=1.0)
    m_Thickness = bpy.props.FloatProperty(name='Thickness', description='Set/Get Superquadric ring thickness (toroids only). Changing thickness maintains the outside diameter of the toroid. Initial value is 0.3333', default=0.3333)
    m_Toroidal = bpy.props.BoolProperty(name='Toroidal', description='Set/Get whether or not the superquadric is toroidal (1) or ellipsoidal (0). Initial value is 0', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AxisOfSymmetry', 'm_Center', 'm_PhiResolution', 'm_PhiRoundness', 'm_Scale', 'm_Size', 'm_ThetaResolution', 'm_ThetaRoundness', 'm_Thickness', 'm_Toroidal', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SuperquadricSource)
TYPENAMES.append('BVTK_NT_SuperquadricSource' )


# --------------------------------------------------------------


class BVTK_NT_GlyphSource2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GlyphSource2D'
    bl_label = 'vtkGlyphSource2D'
    e_GlyphType_items = [(x, x, x) for x in ['Arrow', 'Circle', 'Cross', 'Dash', 'Diamond', 'EdgeArrow', 'HookedArrow', 'None', 'Square', 'ThickArrow', 'ThickCross', 'Triangle', 'Vertex']]
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set the center of the glyph. By default the center is (0,0,0)', default=[0.0, 0.0, 0.0], size=3)
    m_Color = bpy.props.FloatVectorProperty(name='Color', description='Set the color of the glyph. The default color is white', default=[1.0, 1.0, 1.0], size=3)
    m_Cross = bpy.props.BoolProperty(name='Cross', description='Specify whether a cross is drawn as part of the glyph. (This is in addition to the glyph. If the glyph type is set to "Cross" there is no need to enable this flag.', default=True)
    m_Dash = bpy.props.BoolProperty(name='Dash', description='Specify whether a short line segment is drawn through the glyph. (This is in addition to the glyph. If the glyph type is set to "Dash" there is no need to enable this flag.', default=True)
    m_Filled = bpy.props.BoolProperty(name='Filled', description='Specify whether the glyph is filled (a polygon) or not (a closed polygon defined by line segments). This only applies to 2D closed glyphs', default=True)
    e_GlyphType = bpy.props.EnumProperty(name='GlyphType', description='Specify the type of glyph to generate', default='Vertex', items=e_GlyphType_items)
    m_Resolution = bpy.props.IntProperty(name='Resolution', description='Specify the number of points that form the circular glyph', default=8)
    m_RotationAngle = bpy.props.FloatProperty(name='RotationAngle', description='Specify an angle (in degrees) to rotate the glyph around the z-axis. Using this ivar, it is possible to generate rotated glyphs (e.g., crosses, arrows, etc.', default=0.0)
    m_Scale = bpy.props.FloatProperty(name='Scale', description='Set the scale of the glyph. Note that the glyphs are designed to fit in the (1,1) rectangle', default=1.0)
    m_Scale2 = bpy.props.FloatProperty(name='Scale2', description='Set the scale of optional portions of the glyph (e.g., the dash and cross is DashOn() and CrossOn())', default=1.5)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_Color', 'm_Cross', 'm_Dash', 'm_Filled', 'e_GlyphType', 'm_Resolution', 'm_RotationAngle', 'm_Scale', 'm_Scale2', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_GlyphSource2D)
TYPENAMES.append('BVTK_NT_GlyphSource2D' )


# --------------------------------------------------------------


class BVTK_NT_CylinderSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CylinderSource'
    bl_label = 'vtkCylinderSource'
    
    m_Capping = bpy.props.BoolProperty(name='Capping', description='Turn on/off whether to cap cylinder with polygons. Initial value is true', default=True)
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set/Get cylinder center. Initial value is (0.0,0.0,0.0', default=[0.0, 0.0, 0.0], size=3)
    m_Height = bpy.props.FloatProperty(name='Height', description='Set the height of the cylinder. Initial value is 1', default=1.0)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set the radius of the cylinder. Initial value is 0.', default=0.5)
    m_Resolution = bpy.props.IntProperty(name='Resolution', description='Set the number of facets used to define cylinder. Initial value is 6', default=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Capping', 'm_Center', 'm_Height', 'm_Radius', 'm_Resolution', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CylinderSource)
TYPENAMES.append('BVTK_NT_CylinderSource' )


# --------------------------------------------------------------


class BVTK_NT_PointSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PointSource'
    bl_label = 'vtkPointSource'
    e_Distribution_items = [(x, x, x) for x in ['Shell', 'Uniform']]
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set the center of the point cloud', default=[0.0, 0.0, 0.0], size=3)
    e_Distribution = bpy.props.EnumProperty(name='Distribution', description='Specify the distribution to use. The default is a uniform distribution. The shell distribution produces random points on the surface of the sphere, none in the interior', default='Uniform', items=e_Distribution_items)
    m_NumberOfPoints = bpy.props.IntProperty(name='NumberOfPoints', description='Set the number of points to generate', default=10)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set the radius of the point cloud. If you are generating a Gaussian distribution, then this is the standard deviation for each of x, y, and z', default=0.5)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'e_Distribution', 'm_NumberOfPoints', 'm_Radius', ]
    
    def m_connections(self):
        return [], ['Output'], ['RandomSequence'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PointSource)
TYPENAMES.append('BVTK_NT_PointSource' )


# --------------------------------------------------------------


class BVTK_NT_Cursor3D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Cursor3D'
    bl_label = 'vtkCursor3D'
    
    m_Axes = bpy.props.BoolProperty(name='Axes', description='Turn on/off the wireframe axes', default=True)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Set / get the boundary of the 3D cursor', default=[-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], size=6)
    m_Outline = bpy.props.BoolProperty(name='Outline', description='Turn on/off the wireframe bounding box', default=True)
    m_TranslationMode = bpy.props.BoolProperty(name='TranslationMode', description='Enable/disable the translation mode. If on, changes in cursor position cause the entire widget to translate along with the cursor. By default, translation mode is off', default=True)
    m_Wrap = bpy.props.BoolProperty(name='Wrap', description='Turn on/off cursor wrapping. If the cursor focus moves outside the specified bounds, the cursor will either be restrained against the nearest "wall" (Wrap=off), or it will wrap around (Wrap=on)', default=True)
    m_XShadows = bpy.props.BoolProperty(name='XShadows', description='Turn on/off the wireframe x-shadows', default=True)
    m_YShadows = bpy.props.BoolProperty(name='YShadows', description='Turn on/off the wireframe y-shadows', default=True)
    m_ZShadows = bpy.props.BoolProperty(name='ZShadows', description='Turn on/off the wireframe z-shadows', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Axes', 'm_ModelBounds', 'm_Outline', 'm_TranslationMode', 'm_Wrap', 'm_XShadows', 'm_YShadows', 'm_ZShadows', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Cursor3D)
TYPENAMES.append('BVTK_NT_Cursor3D' )


# --------------------------------------------------------------


class BVTK_NT_DiagonalMatrixSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DiagonalMatrixSource'
    bl_label = 'vtkDiagonalMatrixSource'
    
    m_ArrayType = bpy.props.IntProperty(name='ArrayType', description='', default=0)
    m_ColumnLabel = bpy.props.StringProperty(name='ColumnLabel', description='Controls the output matrix column dimension label. Default: "columns', default='columns')
    m_Diagonal = bpy.props.FloatProperty(name='Diagonal', description='Stores the value that will be assigned to diagonal elements (default: 1', default=1.0)
    m_Extents = bpy.props.IntProperty(name='Extents', description='Stores the extents of the output matrix (which is square', default=3)
    m_RowLabel = bpy.props.StringProperty(name='RowLabel', description='Controls the output matrix row dimension label. Default: "rows', default='rows')
    m_SubDiagonal = bpy.props.FloatProperty(name='SubDiagonal', description='Stores the value that will be assigned to subdiagonal elements (default: 0', default=0.0)
    m_SuperDiagonal = bpy.props.FloatProperty(name='SuperDiagonal', description='Stores the value that will be assigned to superdiagonal elements (default: 0', default=0.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ArrayType', 'm_ColumnLabel', 'm_Diagonal', 'm_Extents', 'm_RowLabel', 'm_SubDiagonal', 'm_SuperDiagonal', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DiagonalMatrixSource)
TYPENAMES.append('BVTK_NT_DiagonalMatrixSource' )


# --------------------------------------------------------------


class BVTK_NT_CellTypeSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CellTypeSource'
    bl_label = 'vtkCellTypeSource'
    
    m_CellOrder = bpy.props.IntProperty(name='CellOrder', description='Set/Get the order of Lagrange interpolation to be used', default=3)
    m_CellType = bpy.props.IntProperty(name='CellType', description='Set/Get the type of cells to be generated', default=12)
    m_CompleteQuadraticSimplicialElements = bpy.props.BoolProperty(name='CompleteQuadraticSimplicialElements', description='Set/Get whether quadratic cells with simplicial shapes should be "completed"', default=False)
    m_OutputPrecision = bpy.props.IntProperty(name='OutputPrecision', description='Set/get the desired precision for the output points. vtkAlgorithm::SINGLE_PRECISION (0) - Output single-precision floating point. vtkAlgorithm::DOUBLE_PRECISION (1) - Output double-precision floating point', default=0)
    m_PolynomialFieldOrder = bpy.props.IntProperty(name='PolynomialFieldOrder', description='Set/Get the polynomial order of the "Polynomial" point field. The default is 1', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CellOrder', 'm_CellType', 'm_CompleteQuadraticSimplicialElements', 'm_OutputPrecision', 'm_PolynomialFieldOrder', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CellTypeSource)
TYPENAMES.append('BVTK_NT_CellTypeSource' )


# --------------------------------------------------------------


class BVTK_NT_TextSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TextSource'
    bl_label = 'vtkTextSource'
    
    m_BackgroundColor = bpy.props.FloatVectorProperty(name='BackgroundColor', description='Set/Get the background color. Default is black (0,0,0). Alpha is always 1', default=[0.0, 0.0, 0.0], size=3)
    m_Backing = bpy.props.BoolProperty(name='Backing', description='Controls whether or not a background is drawn with the text', default=True)
    m_ForegroundColor = bpy.props.FloatVectorProperty(name='ForegroundColor', description='Set/Get the foreground color. Default is white (1,1,1). ALpha is always 1', default=[1.0, 1.0, 1.0], size=3)
    m_Text = bpy.props.StringProperty(name='Text', description='Set/Get the text to be drawn')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BackgroundColor', 'm_Backing', 'm_ForegroundColor', 'm_Text', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TextSource)
TYPENAMES.append('BVTK_NT_TextSource' )


# --------------------------------------------------------------


class BVTK_NT_ImageEllipsoidSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageEllipsoidSource'
    bl_label = 'vtkImageEllipsoidSource'
    e_OutputScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Long', 'Short', 'UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='', default=[128.0, 128.0, 0.0], size=3)
    m_InValue = bpy.props.FloatProperty(name='InValue', description='Set/Get the inside pixel values', default=255.0)
    m_OutValue = bpy.props.FloatProperty(name='OutValue', description='Set/Get the outside pixel values', default=0.0)
    e_OutputScalarType = bpy.props.EnumProperty(name='OutputScalarType', description='Set what type of scalar data this source should generate', default='UnsignedChar', items=e_OutputScalarType_items)
    m_Radius = bpy.props.FloatVectorProperty(name='Radius', description='', default=[70.0, 70.0, 70.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_InValue', 'm_OutValue', 'e_OutputScalarType', 'm_Radius', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageEllipsoidSource)
TYPENAMES.append('BVTK_NT_ImageEllipsoidSource' )


# --------------------------------------------------------------


class BVTK_NT_TemporalFractal(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TemporalFractal'
    bl_label = 'vtkTemporalFractal'
    
    m_AdaptiveSubdivision = bpy.props.BoolProperty(name='AdaptiveSubdivision', description='Make the division adaptive or not, defaults to Adaptiv', default=True)
    m_Asymetric = bpy.props.IntProperty(name='Asymetric', description='Test the case when the blocks do not have the same sizes. Adds 2 to the x extent of the far x blocks (level 1)', default=1)
    m_Dimensions = bpy.props.IntProperty(name='Dimensions', description='XYZ dimensions of cells', default=10)
    m_DiscreteTimeSteps = bpy.props.BoolProperty(name='DiscreteTimeSteps', description='Limit this source to discrete integer time steps Default is off (continuous', default=True)
    m_FractalValue = bpy.props.FloatProperty(name='FractalValue', description='Essentially the iso surface value. The fractal array is scaled to map this value to 0.5 for use as a volume fraction', default=9.5)
    m_GenerateRectilinearGrids = bpy.props.BoolProperty(name='GenerateRectilinearGrids', description='Generate either rectilinear grids either uniform grids. Default is false', default=True)
    m_GhostLevels = bpy.props.BoolProperty(name='GhostLevels', description='For testing ghost levels', default=True)
    m_MaximumLevel = bpy.props.IntProperty(name='MaximumLevel', description='Any blocks touching a predefined line will be subdivided to this level. Other blocks are subdivided so that neighboring blocks only differ by one level', default=6)
    m_TwoDimensional = bpy.props.BoolProperty(name='TwoDimensional', description='Make a 2D data set to test', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AdaptiveSubdivision', 'm_Asymetric', 'm_Dimensions', 'm_DiscreteTimeSteps', 'm_FractalValue', 'm_GenerateRectilinearGrids', 'm_GhostLevels', 'm_MaximumLevel', 'm_TwoDimensional', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TemporalFractal)
TYPENAMES.append('BVTK_NT_TemporalFractal' )


# --------------------------------------------------------------


class BVTK_NT_SpherePuzzleArrows(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SpherePuzzleArrows'
    bl_label = 'vtkSpherePuzzleArrows'
    
    m_Permutation = bpy.props.IntVectorProperty(name='Permutation', description='Permutation is an array of puzzle piece ids. Arrows will be generated for any id that does not contain itself. Permutation[3] = 3 will produce no arrow. Permutation[3] = 10 will draw an arrow from location 3 to 10', default=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], size=32)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Permutation', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SpherePuzzleArrows)
TYPENAMES.append('BVTK_NT_SpherePuzzleArrows' )


# --------------------------------------------------------------


class BVTK_NT_SpherePuzzle(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SpherePuzzle'
    bl_label = 'vtkSpherePuzzle'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_SpherePuzzle)
TYPENAMES.append('BVTK_NT_SpherePuzzle' )


# --------------------------------------------------------------


class BVTK_NT_BooleanTexture(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BooleanTexture'
    bl_label = 'vtkBooleanTexture'
    
    m_InIn = bpy.props.IntVectorProperty(name='InIn', description='Specify intensity/transparency for "in/in" region', default=[255, 255], size=2)
    m_InOn = bpy.props.IntVectorProperty(name='InOn', description='Specify intensity/transparency for "in/on" region', default=[255, 255], size=2)
    m_InOut = bpy.props.IntVectorProperty(name='InOut', description='Specify intensity/transparency for "in/out" region', default=[255, 255], size=2)
    m_OnIn = bpy.props.IntVectorProperty(name='OnIn', description='Specify intensity/transparency for "on/in" region', default=[255, 255], size=2)
    m_OnOn = bpy.props.IntVectorProperty(name='OnOn', description='Specify intensity/transparency for "on/on" region', default=[255, 255], size=2)
    m_OnOut = bpy.props.IntVectorProperty(name='OnOut', description='Specify intensity/transparency for "on/out" region', default=[255, 255], size=2)
    m_OutIn = bpy.props.IntVectorProperty(name='OutIn', description='Specify intensity/transparency for "out/in" region', default=[255, 255], size=2)
    m_OutOn = bpy.props.IntVectorProperty(name='OutOn', description='Specify intensity/transparency for "out/on" region', default=[255, 255], size=2)
    m_OutOut = bpy.props.IntVectorProperty(name='OutOut', description='Specify intensity/transparency for "out/out" region', default=[255, 255], size=2)
    m_Thickness = bpy.props.IntProperty(name='Thickness', description='Set the thickness of the "on" region', default=0)
    m_XSize = bpy.props.IntProperty(name='XSize', description='Set the X texture map dimension', default=12)
    m_YSize = bpy.props.IntProperty(name='YSize', description='Set the Y texture map dimension', default=12)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_InIn', 'm_InOn', 'm_InOut', 'm_OnIn', 'm_OnOn', 'm_OnOut', 'm_OutIn', 'm_OutOn', 'm_OutOut', 'm_Thickness', 'm_XSize', 'm_YSize', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_BooleanTexture)
TYPENAMES.append('BVTK_NT_BooleanTexture' )


# --------------------------------------------------------------


class BVTK_NT_Cursor2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Cursor2D'
    bl_label = 'vtkCursor2D'
    
    m_Axes = bpy.props.BoolProperty(name='Axes', description='Turn on/off the wireframe axes', default=True)
    m_ModelBounds = bpy.props.FloatVectorProperty(name='ModelBounds', description='Set / get the bounding box of the 2D cursor. This defines the outline of the cursor, and where the focal point should lie', default=[-10.0, 10.0, -10.0, 10.0, 0.0, 0.0], size=6)
    m_Outline = bpy.props.BoolProperty(name='Outline', description='Turn on/off the wireframe bounding box', default=True)
    m_Point = bpy.props.BoolProperty(name='Point', description='Turn on/off the point located at the cursor focus', default=True)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Specify a radius for a circle. This erases the cursor lines around the focal point', default=2.0)
    m_TranslationMode = bpy.props.BoolProperty(name='TranslationMode', description='Enable/disable the translation mode. If on, changes in cursor position cause the entire widget to translate along with the cursor. By default, translation mode is off', default=True)
    m_Wrap = bpy.props.BoolProperty(name='Wrap', description='Turn on/off cursor wrapping. If the cursor focus moves outside the specified bounds, the cursor will either be restrained against the nearest "wall" (Wrap=off), or it will wrap around (Wrap=on)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Axes', 'm_ModelBounds', 'm_Outline', 'm_Point', 'm_Radius', 'm_TranslationMode', 'm_Wrap', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Cursor2D)
TYPENAMES.append('BVTK_NT_Cursor2D' )


# --------------------------------------------------------------


class BVTK_NT_CubeSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CubeSource'
    bl_label = 'vtkCubeSource'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set the center of the cube', default=[0.0, 0.0, 0.0], size=3)
    m_XLength = bpy.props.FloatProperty(name='XLength', description='Set the length of the cube in the x-direction', default=1.0)
    m_YLength = bpy.props.FloatProperty(name='YLength', description='Set the length of the cube in the y-direction', default=1.0)
    m_ZLength = bpy.props.FloatProperty(name='ZLength', description='Set the length of the cube in the z-direction', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_XLength', 'm_YLength', 'm_ZLength', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_CubeSource)
TYPENAMES.append('BVTK_NT_CubeSource' )


# --------------------------------------------------------------


class BVTK_NT_PlaneSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PlaneSource'
    bl_label = 'vtkPlaneSource'
    
    m_Origin = bpy.props.FloatVectorProperty(name='Origin', description='Specify a point defining the origin of the plane', default=[-0.5, -0.5, 0.0], size=3)
    m_XResolution = bpy.props.IntProperty(name='XResolution', description='Specify the resolution of the plane along the first axes', default=1)
    m_YResolution = bpy.props.IntProperty(name='YResolution', description='Specify the resolution of the plane along the second axes', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Origin', 'm_XResolution', 'm_YResolution', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_PlaneSource)
TYPENAMES.append('BVTK_NT_PlaneSource' )


# --------------------------------------------------------------


class BVTK_NT_RectangularButtonSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RectangularButtonSource'
    bl_label = 'vtkRectangularButtonSource'
    e_TextureStyle_items = [(x, x, x) for x in ['FitImage', 'Proportional']]
    
    m_BoxRatio = bpy.props.FloatProperty(name='BoxRatio', description='Set/Get the ratio of the bottom of the button with the shoulder region. Numbers greater than one produce buttons with a wider bottom than shoulder; ratios less than one produce buttons that have a wider shoulder than bottom', default=1.1)
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Specify a point defining the origin (center) of the button', default=[0.0, 0.0, 0.0], size=3)
    m_Depth = bpy.props.FloatProperty(name='Depth', description='Set/Get the depth of the button (the z-eliipsoid axis length)', default=0.05)
    m_Height = bpy.props.FloatProperty(name='Height', description='Set/Get the height of the button', default=0.5)
    m_ShoulderTextureCoordinate = bpy.props.FloatVectorProperty(name='ShoulderTextureCoordinate', description='', default=[0.0, 0.0], size=2)
    m_TextureDimensions = bpy.props.IntVectorProperty(name='TextureDimensions', description='', default=[100, 100], size=2)
    m_TextureHeightRatio = bpy.props.FloatProperty(name='TextureHeightRatio', description='Set/Get the ratio of the height of the texture region to the shoulder height. Values greater than 1.0 yield convex buttons with the texture region raised above the shoulder. Values less than 1.0 yield concave buttons with the texture region below the shoulder', default=0.95)
    m_TextureRatio = bpy.props.FloatProperty(name='TextureRatio', description='Set/Get the ratio of the texture region to the shoulder region. This number must be 0<=tr<=1. If the texture style is to fit the image, then satisfying the texture ratio may only be possible in one of the two directions (length or width) depending on the dimensions of the texture', default=0.9)
    e_TextureStyle = bpy.props.EnumProperty(name='TextureStyle', description='Set/Get the style of the texture region: whether to size it according to the x-y dimensions of the texture, or whether to make the texture region proportional to the width/height of the button', default='Proportional', items=e_TextureStyle_items)
    m_TwoSided = bpy.props.BoolProperty(name='TwoSided', description='Indicate whether the button is single or double sided. A double sided button can be viewed from two sides...it looks sort of like a "pill." A single-sided button is meant to viewed from a single side; it looks like a "clam-shell.', default=True)
    m_Width = bpy.props.FloatProperty(name='Width', description='Set/Get the width of the button', default=0.5)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_BoxRatio', 'm_Center', 'm_Depth', 'm_Height', 'm_ShoulderTextureCoordinate', 'm_TextureDimensions', 'm_TextureHeightRatio', 'm_TextureRatio', 'e_TextureStyle', 'm_TwoSided', 'm_Width', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RectangularButtonSource)
TYPENAMES.append('BVTK_NT_RectangularButtonSource' )


# --------------------------------------------------------------


class BVTK_NT_DiskSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DiskSource'
    bl_label = 'vtkDiskSource'
    
    m_CircumferentialResolution = bpy.props.IntProperty(name='CircumferentialResolution', description='Set the number of points in circumferential direction', default=6)
    m_InnerRadius = bpy.props.FloatProperty(name='InnerRadius', description='Specify inner radius of hole in disc', default=0.25)
    m_OuterRadius = bpy.props.FloatProperty(name='OuterRadius', description='Specify outer radius of disc', default=0.5)
    m_RadialResolution = bpy.props.IntProperty(name='RadialResolution', description='Set the number of points in radius direction', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CircumferentialResolution', 'm_InnerRadius', 'm_OuterRadius', 'm_RadialResolution', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DiskSource)
TYPENAMES.append('BVTK_NT_DiskSource' )


# --------------------------------------------------------------


class BVTK_NT_TriangularTexture(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TriangularTexture'
    bl_label = 'vtkTriangularTexture'
    
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Set a Scale Factor', default=1.0)
    m_TexturePattern = bpy.props.IntProperty(name='TexturePattern', description='Set the texture pattern. 1 = opaque at centroid (default) 2 = opaque at vertices 3 = opaque in rings around vertice', default=1)
    m_XSize = bpy.props.IntProperty(name='XSize', description='Set the X texture map dimension. Default is 64', default=64)
    m_YSize = bpy.props.IntProperty(name='YSize', description='Set the Y texture map dimension. Default is 64', default=64)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ScaleFactor', 'm_TexturePattern', 'm_XSize', 'm_YSize', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TriangularTexture)
TYPENAMES.append('BVTK_NT_TriangularTexture' )


# --------------------------------------------------------------


class BVTK_NT_RowQueryToTable(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RowQueryToTable'
    bl_label = 'vtkRowQueryToTable'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], ['Output'], ['Query'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RowQueryToTable)
TYPENAMES.append('BVTK_NT_RowQueryToTable' )


# --------------------------------------------------------------


class BVTK_NT_ImageGaussianSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageGaussianSource'
    bl_label = 'vtkImageGaussianSource'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='', default=[0.0, 0.0, 0.0], size=3)
    m_Maximum = bpy.props.FloatProperty(name='Maximum', description='Set/Get the Maximum value of the gaussia', default=1.0)
    m_StandardDeviation = bpy.props.FloatProperty(name='StandardDeviation', description='Set/Get the standard deviation of the gaussia', default=100.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_Maximum', 'm_StandardDeviation', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageGaussianSource)
TYPENAMES.append('BVTK_NT_ImageGaussianSource' )


# --------------------------------------------------------------


class BVTK_NT_RegularPolygonSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_RegularPolygonSource'
    bl_label = 'vtkRegularPolygonSource'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set/Get the center of the polygon. By default, the center is set at the origin (0,0,0)', default=[0.0, 0.0, 0.0], size=3)
    m_GeneratePolygon = bpy.props.BoolProperty(name='GeneratePolygon', description='Control whether a polygon is produced. By default, GeneratePolygon is enabled', default=True)
    m_GeneratePolyline = bpy.props.BoolProperty(name='GeneratePolyline', description='Control whether a polyline is produced. By default, GeneratePolyline is enabled', default=True)
    m_Normal = bpy.props.FloatVectorProperty(name='Normal', description='Set/Get the normal to the polygon. The ordering of the polygon will be counter-clockwise around the normal (i.e., using the right-hand rule). By default, the normal is set to (0,0,1)', default=[0.0, 0.0, 1.0], size=3)
    m_NumberOfSides = bpy.props.IntProperty(name='NumberOfSides', description='Set/Get the number of sides of the polygon. By default, the number of sides is set to six', default=6)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set/Get the radius of the polygon. By default, the radius is set to 0.5', default=0.5)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_GeneratePolygon', 'm_GeneratePolyline', 'm_Normal', 'm_NumberOfSides', 'm_Radius', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_RegularPolygonSource)
TYPENAMES.append('BVTK_NT_RegularPolygonSource' )


# --------------------------------------------------------------


class BVTK_NT_LineSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LineSource'
    bl_label = 'vtkLineSource'
    
    m_Point1 = bpy.props.FloatVectorProperty(name='Point1', description='Set position of first end point', default=[-0.5, 0.0, 0.0], size=3)
    m_Point2 = bpy.props.FloatVectorProperty(name='Point2', description='Set position of other end point', default=[0.5, 0.0, 0.0], size=3)
    m_Resolution = bpy.props.IntProperty(name='Resolution', description='Divide line into Resolution number of pieces', default=1)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Point1', 'm_Point2', 'm_Resolution', ]
    
    def m_connections(self):
        return [], ['Output'], ['Points'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_LineSource)
TYPENAMES.append('BVTK_NT_LineSource' )


# --------------------------------------------------------------


class BVTK_NT_ConeSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ConeSource'
    bl_label = 'vtkConeSource'
    
    m_Angle = bpy.props.FloatProperty(name='Angle', description='Set the angle of the cone. This is the angle between the axis of the cone and a generatrix. Warning: this is not the aperture! The aperture is twice this angle. As a side effect, the angle plus height sets the base radius of the cone. Angle is expressed in degrees', default=26.56505117707799)
    m_Capping = bpy.props.BoolProperty(name='Capping', description='Turn on/off whether to cap the base of the cone with a polygon', default=True)
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set the center of the cone. It is located at the middle of the axis of the cone. Warning: this is not the center of the base of the cone! The default is 0,0,0', default=[0.0, 0.0, 0.0], size=3)
    m_Direction = bpy.props.FloatVectorProperty(name='Direction', description='Set the orientation vector of the cone. The vector does not have to be normalized. The direction goes from the center of the base toward the apex. The default is (1,0,0)', default=[1.0, 0.0, 0.0], size=3)
    m_Height = bpy.props.FloatProperty(name='Height', description='Set the height of the cone. This is the height along the cone in its specified direction', default=1.0)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set the base radius of the cone', default=0.5)
    m_Resolution = bpy.props.IntProperty(name='Resolution', description='Set the number of facets used to represent the cone', default=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Angle', 'm_Capping', 'm_Center', 'm_Direction', 'm_Height', 'm_Radius', 'm_Resolution', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ConeSource)
TYPENAMES.append('BVTK_NT_ConeSource' )


# --------------------------------------------------------------


class BVTK_NT_VectorText(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_VectorText'
    bl_label = 'vtkVectorText'
    
    m_Text = bpy.props.StringProperty(name='Text', description='Set/Get the text to be drawn')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Text', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_VectorText)
TYPENAMES.append('BVTK_NT_VectorText' )


# --------------------------------------------------------------


class BVTK_NT_Axes(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Axes'
    bl_label = 'vtkAxes'
    
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', description='Option for computing normals. By default they are computed', default=True)
    m_Origin = bpy.props.FloatVectorProperty(name='Origin', description='Set the origin of the axes', default=[0.0, 0.0, 0.0], size=3)
    m_ScaleFactor = bpy.props.FloatProperty(name='ScaleFactor', description='Set the scale factor of the axes. Used to control size', default=1.0)
    m_Symmetric = bpy.props.BoolProperty(name='Symmetric', description='If Symetric is on, the the axis continue to negative values', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_ComputeNormals', 'm_Origin', 'm_ScaleFactor', 'm_Symmetric', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_Axes)
TYPENAMES.append('BVTK_NT_Axes' )


# --------------------------------------------------------------


class BVTK_NT_ROIStencilSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ROIStencilSource'
    bl_label = 'vtkROIStencilSource'
    e_Shape_items = [(x, x, x) for x in ['Box', 'CylinderX', 'CylinderY', 'CylinderZ', 'Ellipsoid']]
    
    m_Bounds = bpy.props.FloatVectorProperty(name='Bounds', description='', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6)
    m_OutputOrigin = bpy.props.FloatVectorProperty(name='OutputOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    m_OutputSpacing = bpy.props.FloatVectorProperty(name='OutputSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    m_OutputWholeExtent = bpy.props.IntVectorProperty(name='OutputWholeExtent', description='', default=[0, -1, 0, -1, 0, -1], size=6)
    e_Shape = bpy.props.EnumProperty(name='Shape', description='The shape of the region of interest. Cylinders can be oriented along the X, Y, or Z axes. The default shape is "Box"', default='Box', items=e_Shape_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Bounds', 'm_OutputOrigin', 'm_OutputSpacing', 'm_OutputWholeExtent', 'e_Shape', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ROIStencilSource)
TYPENAMES.append('BVTK_NT_ROIStencilSource' )


# --------------------------------------------------------------


class BVTK_NT_TransformToGrid(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_TransformToGrid'
    bl_label = 'vtkTransformToGrid'
    e_GridScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Short', 'UnsignedChar', 'UnsignedShort']]
    
    m_GridExtent = bpy.props.IntVectorProperty(name='GridExtent', description='', default=[0, 0, 0, 0, 0, 0], size=6)
    m_GridOrigin = bpy.props.FloatVectorProperty(name='GridOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    e_GridScalarType = bpy.props.EnumProperty(name='GridScalarType', description='Get/Set the scalar type of the grid. The default is float', default='Float', items=e_GridScalarType_items)
    m_GridSpacing = bpy.props.FloatVectorProperty(name='GridSpacing', description='', default=[1.0, 1.0, 1.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_GridExtent', 'm_GridOrigin', 'e_GridScalarType', 'm_GridSpacing', ]
    
    def m_connections(self):
        return [], ['Output'], ['Input'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_TransformToGrid)
TYPENAMES.append('BVTK_NT_TransformToGrid' )


# --------------------------------------------------------------


class BVTK_NT_ImageCanvasSource2D(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImageCanvasSource2D'
    bl_label = 'vtkImageCanvasSource2D'
    e_ScalarType_items = [(x, x, x) for x in ['Char', 'Double', 'Float', 'Int', 'Long', 'Short', 'UnsignedChar', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']]
    
    m_DefaultZ = bpy.props.IntProperty(name='DefaultZ', description='The drawing operations can only draw into one 2D XY plane at a time. If the canvas is a 3D volume, then this z value is used as the default for 2D operations. The default is 0', default=0)
    m_DrawColor = bpy.props.FloatVectorProperty(name='DrawColor', description='', default=[0.0, 0.0, 0.0, 0.0], size=4)
    m_NumberOfScalarComponents = bpy.props.IntProperty(name='NumberOfScalarComponents', description='Set the number of scalar component', default=1)
    m_Ratio = bpy.props.FloatVectorProperty(name='Ratio', description='', default=[1.0, 1.0, 1.0], size=3)
    e_ScalarType = bpy.props.EnumProperty(name='ScalarType', description='Set/Get the data scalar type (i.e VTK_DOUBLE). Note that these methods are setting and getting the pipeline scalar type. i.e. they are setting the type that the image data will be once it has executed. Until the REQUEST_DATA pass the actual scalars may be of some other type. This is for backwards compatibilit', default='Double', items=e_ScalarType_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DefaultZ', 'm_DrawColor', 'm_NumberOfScalarComponents', 'm_Ratio', 'e_ScalarType', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ImageCanvasSource2D)
TYPENAMES.append('BVTK_NT_ImageCanvasSource2D' )


# --------------------------------------------------------------


class BVTK_NT_WindowToImageFilter(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_WindowToImageFilter'
    bl_label = 'vtkWindowToImageFilter'
    e_InputBufferType_items = [(x, x, x) for x in ['RGB', 'RGBA', 'ZBuffer']]
    
    m_FixBoundary = bpy.props.BoolProperty(name='FixBoundary', description='When scale factor > 1, this class render the full image in tiles. Sometimes that results in artificial artifacts at internal tile seams. To overcome this issue, set this flag to true', default=False)
    e_InputBufferType = bpy.props.EnumProperty(name='InputBufferType', description='Set/get the window buffer from which data will be read. Choices include VTK_RGB (read the color image from the window), VTK_RGBA (same, but include the alpha channel), and VTK_ZBUFFER (depth buffer, returned as a float array). Initial value is VTK_RGB', default='RGB', items=e_InputBufferType_items)
    m_ReadFrontBuffer = bpy.props.BoolProperty(name='ReadFrontBuffer', description='Set/Get the flag that determines which buffer to read from. The default is to read from the front buffer', default=True)
    m_Scale = bpy.props.IntVectorProperty(name='Scale', description='', default=[1, 1], size=2)
    m_ShouldRerender = bpy.props.BoolProperty(name='ShouldRerender', description='Set/get whether to re-render the input window. Initial value is true. (This option makes no difference if scale factor > 1.', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_FixBoundary', 'e_InputBufferType', 'm_ReadFrontBuffer', 'm_Scale', 'm_ShouldRerender', ]
    
    def m_connections(self):
        return [], ['Output'], ['Input'], []
    
    def methods(self):
        return []


add_class(BVTK_NT_WindowToImageFilter)
TYPENAMES.append('BVTK_NT_WindowToImageFilter' )


# --------------------------------------------------------------


class BVTK_NT_AMRGaussianPulseSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_AMRGaussianPulseSource'
    bl_label = 'vtkAMRGaussianPulseSource'
    
    m_PulseAmplitude = bpy.props.FloatProperty(name='PulseAmplitude', description='Set & Get macro for the pulse amplitud', default=0.0001)
    m_PulseOrigin = bpy.props.FloatVectorProperty(name='PulseOrigin', description='', default=[0.0, 0.0, 0.0], size=3)
    m_PulseWidth = bpy.props.FloatVectorProperty(name='PulseWidth', description='', default=[0.5, 0.5, 0.5], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_PulseAmplitude', 'm_PulseOrigin', 'm_PulseWidth', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_AMRGaussianPulseSource)
TYPENAMES.append('BVTK_NT_AMRGaussianPulseSource' )


# --------------------------------------------------------------


class BVTK_NT_OutlineCornerSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_OutlineCornerSource'
    bl_label = 'vtkOutlineCornerSource'
    e_BoxType_items = [(x, x, x) for x in ['AxisAligned', 'Oriented']]
    
    m_Bounds = bpy.props.FloatVectorProperty(name='Bounds', description='Specify the bounds of the box to be used in Axis Aligned mode', default=[-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], size=6)
    e_BoxType = bpy.props.EnumProperty(name='BoxType', description='Set box type to AxisAligned (default) or Oriented. Use the method SetBounds() with AxisAligned mode, and SetCorners() with Oriented mode', default='AxisAligned', items=e_BoxType_items)
    m_CornerFactor = bpy.props.FloatProperty(name='CornerFactor', description='Set/Get the factor that controls the relative size of the corners to the length of the corresponding bound', default=0.2)
    m_Corners = bpy.props.FloatVectorProperty(name='Corners', description='Specify the corners of the outline when in Oriented mode, the values are supplied as 8*3 double values The correct corner ordering is using {x,y,z} convention for the unit cube as follows: {0,0,0},{1,0,0},{0,1,0},{1,1,0},{0,0,1},{1,0,1},{0,1,1},{1,1,1}', default=[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0], size=24)
    m_GenerateFaces = bpy.props.BoolProperty(name='GenerateFaces', description='Generate solid faces for the box. This is off by default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Bounds', 'e_BoxType', 'm_CornerFactor', 'm_Corners', 'm_GenerateFaces', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_OutlineCornerSource)
TYPENAMES.append('BVTK_NT_OutlineCornerSource' )


# --------------------------------------------------------------


class BVTK_NT_EllipticalButtonSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_EllipticalButtonSource'
    bl_label = 'vtkEllipticalButtonSource'
    e_TextureStyle_items = [(x, x, x) for x in ['FitImage', 'Proportional']]
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Specify a point defining the origin (center) of the button', default=[0.0, 0.0, 0.0], size=3)
    m_CircumferentialResolution = bpy.props.IntProperty(name='CircumferentialResolution', description='Specify the resolution of the button in the circumferential direction', default=4)
    m_Depth = bpy.props.FloatProperty(name='Depth', description='Set/Get the depth of the button (the z-eliipsoid axis length)', default=0.05)
    m_Height = bpy.props.FloatProperty(name='Height', description='Set/Get the height of the button (the y-ellipsoid axis length * 2)', default=0.5)
    m_RadialRatio = bpy.props.FloatProperty(name='RadialRatio', description="Set/Get the radial ratio. This is the measure of the radius of the outer ellipsoid to the inner ellipsoid of the button. The outer ellipsoid is the boundary of the button defined by the height and width. The inner ellipsoid circumscribes the texture region. Larger RadialRatio's cause the button to be more rounded (and the texture region to be smaller); smaller ratios produce sharply curved shoulders with a larger texture region", default=1.1)
    m_ShoulderResolution = bpy.props.IntProperty(name='ShoulderResolution', description='Specify the resolution of the texture in the radial direction in the shoulder region', default=2)
    m_ShoulderTextureCoordinate = bpy.props.FloatVectorProperty(name='ShoulderTextureCoordinate', description='', default=[0.0, 0.0], size=2)
    m_TextureDimensions = bpy.props.IntVectorProperty(name='TextureDimensions', description='', default=[100, 100], size=2)
    m_TextureResolution = bpy.props.IntProperty(name='TextureResolution', description='Specify the resolution of the texture in the radial direction in the texture region', default=2)
    e_TextureStyle = bpy.props.EnumProperty(name='TextureStyle', description='Set/Get the style of the texture region: whether to size it according to the x-y dimensions of the texture, or whether to make the texture region proportional to the width/height of the button', default='Proportional', items=e_TextureStyle_items)
    m_TwoSided = bpy.props.BoolProperty(name='TwoSided', description='Indicate whether the button is single or double sided. A double sided button can be viewed from two sides...it looks sort of like a "pill." A single-sided button is meant to viewed from a single side; it looks like a "clam-shell.', default=True)
    m_Width = bpy.props.FloatProperty(name='Width', description='Set/Get the width of the button (the x-ellipsoid axis length * 2)', default=0.5)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_CircumferentialResolution', 'm_Depth', 'm_Height', 'm_RadialRatio', 'm_ShoulderResolution', 'm_ShoulderTextureCoordinate', 'm_TextureDimensions', 'm_TextureResolution', 'e_TextureStyle', 'm_TwoSided', 'm_Width', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_EllipticalButtonSource)
TYPENAMES.append('BVTK_NT_EllipticalButtonSource' )


# --------------------------------------------------------------


class BVTK_NT_ArrowSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ArrowSource'
    bl_label = 'vtkArrowSource'
    
    m_Invert = bpy.props.BoolProperty(name='Invert', description='Inverts the arrow direction. When set to true, base is at (1, 0, 0) while the tip is at (0, 0, 0). The default is false, i.e. base at (0, 0, 0) and the tip at (1, 0, 0)', default=False)
    m_ShaftRadius = bpy.props.FloatProperty(name='ShaftRadius', description='Set the radius of the shaft. Defaults to 0.03', default=0.03)
    m_ShaftResolution = bpy.props.IntProperty(name='ShaftResolution', description='Set the resolution of the shaft. 2 gives a rectangle. I would like to extend the cone to produce a line, but this is not an option now', default=6)
    m_TipLength = bpy.props.FloatProperty(name='TipLength', description='Set the length, and radius of the tip. They default to 0.35 and 0.', default=0.35)
    m_TipRadius = bpy.props.FloatProperty(name='TipRadius', description='Set the length, and radius of the tip. They default to 0.35 and 0.', default=0.1)
    m_TipResolution = bpy.props.IntProperty(name='TipResolution', description='Set the resolution of the tip. The tip behaves the same as a cone. Resoultion 1 gives a single triangle, 2 gives two crossed triangles', default=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Invert', 'm_ShaftRadius', 'm_ShaftResolution', 'm_TipLength', 'm_TipRadius', 'm_TipResolution', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ArrowSource)
TYPENAMES.append('BVTK_NT_ArrowSource' )


# --------------------------------------------------------------


class BVTK_NT_OutlineSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_OutlineSource'
    bl_label = 'vtkOutlineSource'
    e_BoxType_items = [(x, x, x) for x in ['AxisAligned', 'Oriented']]
    
    m_Bounds = bpy.props.FloatVectorProperty(name='Bounds', description='Specify the bounds of the box to be used in Axis Aligned mode', default=[-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], size=6)
    e_BoxType = bpy.props.EnumProperty(name='BoxType', description='Set box type to AxisAligned (default) or Oriented. Use the method SetBounds() with AxisAligned mode, and SetCorners() with Oriented mode', default='AxisAligned', items=e_BoxType_items)
    m_Corners = bpy.props.FloatVectorProperty(name='Corners', description='Specify the corners of the outline when in Oriented mode, the values are supplied as 8*3 double values The correct corner ordering is using {x,y,z} convention for the unit cube as follows: {0,0,0},{1,0,0},{0,1,0},{1,1,0},{0,0,1},{1,0,1},{0,1,1},{1,1,1}', default=[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0], size=24)
    m_GenerateFaces = bpy.props.BoolProperty(name='GenerateFaces', description='Generate solid faces for the box. This is off by default', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Bounds', 'e_BoxType', 'm_Corners', 'm_GenerateFaces', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_OutlineSource)
TYPENAMES.append('BVTK_NT_OutlineSource' )


# --------------------------------------------------------------


class BVTK_NT_DataObjectGenerator(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_DataObjectGenerator'
    bl_label = 'vtkDataObjectGenerator'
    
    m_Program = bpy.props.StringProperty(name='Program', description='The string that will be parsed to specify a dataobject structure', default='ID1')
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Program', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_DataObjectGenerator)
TYPENAMES.append('BVTK_NT_DataObjectGenerator' )


# --------------------------------------------------------------


class BVTK_NT_ArcSource(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ArcSource'
    bl_label = 'vtkArcSource'
    
    m_Angle = bpy.props.FloatProperty(name='Angle', description='Arc length (in degrees), beginning at the polar vector. The direction is counterclockwise by default; a negative value draws the arc in the clockwise direction. Note: This is only used when UseNormalAndAngle is ON', default=90.0)
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set position of the center of the circle that defines the arc. Note: you can use the function vtkMath::Solve3PointCircle to find the center from 3 points located on a circle', default=[0.0, 0.0, 0.0], size=3)
    m_Negative = bpy.props.BoolProperty(name='Negative', description='By default the arc spans the shortest angular sector point1 and point2. By setting this to true, the longest angular sector is used instead (i.e. the negative coterminal angle to the shortest one). Note: This is only used when UseNormalAndAngle is OFF. False by default', default=False)
    m_Normal = bpy.props.FloatVectorProperty(name='Normal', description='Set the normal vector to the plane of the arc. By default it points in the positive Z direction. Note: This is only used when UseNormalAndAngle is ON', default=[0.0, 0.0, 1.0], size=3)
    m_Point1 = bpy.props.FloatVectorProperty(name='Point1', description='Set position of the first end point', default=[0.0, 0.5, 0.0], size=3)
    m_Point2 = bpy.props.FloatVectorProperty(name='Point2', description='Set position of the other end point', default=[0.5, 0.0, 0.0], size=3)
    m_PolarVector = bpy.props.FloatVectorProperty(name='PolarVector', description='Set polar vector (starting point of the arc). By default it is the unit vector in the positive X direction. Note: This is only used when UseNormalAndAngle is ON', default=[1.0, 0.0, 0.0], size=3)
    m_Resolution = bpy.props.IntProperty(name='Resolution', description='Define the number of segments of the polyline that draws the arc. Note: if the resolution is set to 1 (the default value), the arc is drawn as a straight line', default=1)
    m_UseNormalAndAngle = bpy.props.BoolProperty(name='UseNormalAndAngle', description='Activate the API based on a normal vector, a starting point (polar vector) and an angle defining the arc length. The previous API (which remains the default) allows for inputs that are inconsistent (when Point1 and Point2 are not equidistant from Center) or ambiguous (when Point1, Point2, and Center are aligned). Note: false by default', default=False)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Angle', 'm_Center', 'm_Negative', 'm_Normal', 'm_Point1', 'm_Point2', 'm_PolarVector', 'm_Resolution', 'm_UseNormalAndAngle', ]
    
    def m_connections(self):
        return [], ['Output'], [], []
    
    def methods(self):
        return []


add_class(BVTK_NT_ArcSource)
TYPENAMES.append('BVTK_NT_ArcSource' )


# --------------------------------------------------------------


menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append(BVTK_NodeCategory('VTKSource', 'Source', items=menu_items))