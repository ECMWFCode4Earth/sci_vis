from ... core import *
type_names = []


# --------------------------------------------------------------


class BVTK_NT_Cone(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Cone'
    bl_label = 'vtkCone'
    
    m_Angle = bpy.props.FloatProperty(name='Angle', description='Set/Get the cone angle (expressed in degrees)', default=45.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Angle', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_Cone)
type_names.append('BVTK_NT_Cone')


# --------------------------------------------------------------


class BVTK_NT_Superquadric(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Superquadric'
    bl_label = 'vtkSuperquadric'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set the center of the superquadric. Default is 0,0,0', default=[0.0, 0.0, 0.0], size=3)
    m_PhiRoundness = bpy.props.FloatProperty(name='PhiRoundness', description='Set/Get Superquadric north/south roundness. Values range from 0 (rectangular) to 1 (circular) to higher orders', default=1.0)
    m_Scale = bpy.props.FloatVectorProperty(name='Scale', description='Set the scale factors of the superquadric. Default is 1,1,1', default=[1.0, 1.0, 1.0], size=3)
    m_Size = bpy.props.FloatProperty(name='Size', description='Set/Get Superquadric isotropic size', default=0.5)
    m_ThetaRoundness = bpy.props.FloatProperty(name='ThetaRoundness', description='Set/Get Superquadric east/west roundness. Values range from 0 (rectangular) to 1 (circular) to higher orders', default=1.0)
    m_Thickness = bpy.props.FloatProperty(name='Thickness', description='Set/Get Superquadric ring thickness (toroids only). Changing thickness maintains the outside diameter of the toroid', default=0.3333)
    m_Toroidal = bpy.props.BoolProperty(name='Toroidal', description='Set/Get whether or not the superquadric is toroidal (1) or ellipsoidal (0)', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_PhiRoundness', 'm_Scale', 'm_Size', 'm_ThetaRoundness', 'm_Thickness', 'm_Toroidal', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_Superquadric)
type_names.append('BVTK_NT_Superquadric')


# --------------------------------------------------------------


class BVTK_NT_Planes(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Planes'
    bl_label = 'vtkPlanes'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['Normals', 'Points', 'Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_Planes)
type_names.append('BVTK_NT_Planes')


# --------------------------------------------------------------


class BVTK_NT_ImplicitSum(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImplicitSum'
    bl_label = 'vtkImplicitSum'
    
    m_NormalizeByWeight = bpy.props.BoolProperty(name='NormalizeByWeight', description='When calculating the function and gradient values of the composite function, setting NormalizeByWeight on will divide the final result by the total weight of the component functions. This process does not otherwise normalize the gradient vector. By default, NormalizeByWeight is off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NormalizeByWeight', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_ImplicitSum)
type_names.append('BVTK_NT_ImplicitSum')


# --------------------------------------------------------------


class BVTK_NT_ImplicitPolyDataDistance(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImplicitPolyDataDistance'
    bl_label = 'vtkImplicitPolyDataDistance'
    
    m_NoClosestPoint = bpy.props.FloatVectorProperty(name='NoClosestPoint', description='', default=[0.0, 0.0, 0.0], size=3)
    m_NoGradient = bpy.props.FloatVectorProperty(name='NoGradient', description='', default=[0.0, 0.0, 1.0], size=3)
    m_NoValue = bpy.props.FloatProperty(name='NoValue', description='Set/get the function value to use if no input vtkPolyData specified', default=0.0)
    m_Tolerance = bpy.props.FloatProperty(name='Tolerance', description='Set/get the tolerance usued for the locator', default=1e-12)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_NoClosestPoint', 'm_NoGradient', 'm_NoValue', 'm_Tolerance', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_ImplicitPolyDataDistance)
type_names.append('BVTK_NT_ImplicitPolyDataDistance')


# --------------------------------------------------------------


class BVTK_NT_ImplicitSelectionLoop(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImplicitSelectionLoop'
    bl_label = 'vtkImplicitSelectionLoop'
    
    m_AutomaticNormalGeneration = bpy.props.BoolProperty(name='AutomaticNormalGeneration', description='Turn on/off automatic normal generation. By default, the normal is computed from the accumulated cross product of the edges. You can also specify the normal to use', default=True)
    m_Normal = bpy.props.FloatVectorProperty(name='Normal', description='Set / get the normal used to determine whether a point is inside or outside the selection loop', default=[0.0, 0.0, 1.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_AutomaticNormalGeneration', 'm_Normal', ]
    
    def m_connections(self):
        return [], [], ['Loop', 'Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_ImplicitSelectionLoop)
type_names.append('BVTK_NT_ImplicitSelectionLoop')


# --------------------------------------------------------------


class BVTK_NT_ImplicitDataSet(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImplicitDataSet'
    bl_label = 'vtkImplicitDataSet'
    
    m_OutGradient = bpy.props.FloatVectorProperty(name='OutGradient', description='', default=[0.0, 0.0, 1.0], size=3)
    m_OutValue = bpy.props.FloatProperty(name='OutValue', description='Set / get the function value to use for points outside of the dataset', default=-1e+30)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_OutGradient', 'm_OutValue', ]
    
    def m_connections(self):
        return [], [], ['DataSet', 'Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_ImplicitDataSet)
type_names.append('BVTK_NT_ImplicitDataSet')


# --------------------------------------------------------------


class BVTK_NT_ImplicitBoolean(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImplicitBoolean'
    bl_label = 'vtkImplicitBoolean'
    e_OperationType_items = [(x, x, x) for x in ['Difference', 'Intersection', 'Union', 'UnionOfMagnitudes']]
    
    e_OperationType = bpy.props.EnumProperty(name='OperationType', description='Specify the type of boolean operation', default='Union', items=e_OperationType_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_OperationType', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_ImplicitBoolean)
type_names.append('BVTK_NT_ImplicitBoolean')


# --------------------------------------------------------------


class BVTK_NT_Box(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Box'
    bl_label = 'vtkBox'
    
    m_Bounds = bpy.props.FloatVectorProperty(name='Bounds', description='', default=[1e+30, -1e+30, 1e+30, -1e+30, 1e+30, -1e+30], size=6)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Bounds', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_Box)
type_names.append('BVTK_NT_Box')


# --------------------------------------------------------------


class BVTK_NT_Plane(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Plane'
    bl_label = 'vtkPlane'
    
    m_Normal = bpy.props.FloatVectorProperty(name='Normal', description='Set/get plane normal. Plane is defined by point and normal', default=[0.0, 0.0, 1.0], size=3)
    m_Origin = bpy.props.FloatVectorProperty(name='Origin', description='Set/get point through which plane passes. Plane is defined by point and normal', default=[0.0, 0.0, 0.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Normal', 'm_Origin', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_Plane)
type_names.append('BVTK_NT_Plane')


# --------------------------------------------------------------


class BVTK_NT_Quadric(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Quadric'
    bl_label = 'vtkQuadric'
    
    m_Coefficients = bpy.props.FloatVectorProperty(name='Coefficients', description='Set / get the 10 coefficients of the quadric equation', default=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], size=10)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Coefficients', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_Quadric)
type_names.append('BVTK_NT_Quadric')


# --------------------------------------------------------------


class BVTK_NT_Sphere(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Sphere'
    bl_label = 'vtkSphere'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='Set / get the center of the sphere. The default is (0,0,0)', default=[0.0, 0.0, 0.0], size=3)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set / get the radius of the sphere. The default is 0.5', default=0.5)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_Radius', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_Sphere)
type_names.append('BVTK_NT_Sphere')


# --------------------------------------------------------------


class BVTK_NT_Cylinder(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Cylinder'
    bl_label = 'vtkCylinder'
    
    m_Axis = bpy.props.FloatVectorProperty(name='Axis', description='Set/Get the axis of the cylinder. If the axis is not specified as a unit vector, it will be normalized. If zero-length axis vector is used as input to this method, it will be ignored', default=[0.0, 1.0, 0.0], size=3)
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='', default=[0.0, 0.0, 0.0], size=3)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set/Get the cylinder radius', default=0.5)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Axis', 'm_Center', 'm_Radius', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_Cylinder)
type_names.append('BVTK_NT_Cylinder')


# --------------------------------------------------------------


class BVTK_NT_ImplicitWindowFunction(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImplicitWindowFunction'
    bl_label = 'vtkImplicitWindowFunction'
    
    m_WindowRange = bpy.props.FloatVectorProperty(name='WindowRange', description='Specify the range of function values which are considered to lie within the window. WindowRange[0] is assumed to be less than WindowRange[1]', default=[0.0, 1.0], size=2)
    m_WindowValues = bpy.props.FloatVectorProperty(name='WindowValues', description='Specify the range of output values that the window range is mapped into. This is effectively a scaling and shifting of the original function values', default=[0.0, 1.0], size=2)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_WindowRange', 'm_WindowValues', ]
    
    def m_connections(self):
        return [], [], ['ImplicitFunction', 'Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_ImplicitWindowFunction)
type_names.append('BVTK_NT_ImplicitWindowFunction')


# --------------------------------------------------------------


class BVTK_NT_ImplicitHalo(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImplicitHalo'
    bl_label = 'vtkImplicitHalo'
    
    m_Center = bpy.props.FloatVectorProperty(name='Center', description='', default=[0.0, 0.0, 0.0], size=3)
    m_FadeOut = bpy.props.FloatProperty(name='FadeOut', description='FadeOut ratio. Valid values are between 0.0 and 1.0', default=0.01)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Radius of the sphere', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Center', 'm_FadeOut', 'm_Radius', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_ImplicitHalo)
type_names.append('BVTK_NT_ImplicitHalo')


# --------------------------------------------------------------


class BVTK_NT_ImplicitVolume(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ImplicitVolume'
    bl_label = 'vtkImplicitVolume'
    
    m_OutGradient = bpy.props.FloatVectorProperty(name='OutGradient', description='', default=[0.0, 0.0, 1.0], size=3)
    m_OutValue = bpy.props.FloatProperty(name='OutValue', description='Set the function value to use for points outside of the dataset', default=-1e+30)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_OutGradient', 'm_OutValue', ]
    
    def m_connections(self):
        return [], [], ['Transform', 'Volume'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_ImplicitVolume)
type_names.append('BVTK_NT_ImplicitVolume')


# --------------------------------------------------------------


class BVTK_NT_PlanesIntersection(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PlanesIntersection'
    bl_label = 'vtkPlanesIntersection'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['Normals', 'Points', 'Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_PlanesIntersection)
type_names.append('BVTK_NT_PlanesIntersection')


# --------------------------------------------------------------


class BVTK_NT_PolyPlane(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PolyPlane'
    bl_label = 'vtkPolyPlane'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['PolyLine', 'Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_PolyPlane)
type_names.append('BVTK_NT_PolyPlane')


# --------------------------------------------------------------


class BVTK_NT_PerlinNoise(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PerlinNoise'
    bl_label = 'vtkPerlinNoise'
    
    m_Amplitude = bpy.props.FloatProperty(name='Amplitude', description='Set/get the amplitude of the noise function. Amplitude can be negative. The noise function varies randomly between -|Amplitude| and |Amplitude|. Therefore the range of values is 2*|Amplitude| large. The initial amplitude is 1', default=1.0)
    m_Frequency = bpy.props.FloatVectorProperty(name='Frequency', description='Set/get the frequency, or physical scale, of the noise function (higher is finer scale). The frequency can be adjusted per axis, or the same for all axes', default=[1.0, 1.0, 1.0], size=3)
    m_Phase = bpy.props.FloatVectorProperty(name='Phase', description='Set/get the phase of the noise function. This parameter can be used to shift the noise function within space (perhaps to avoid a beat with a noise pattern at another scale). Phase tends to repeat about every unit, so a phase of 0.5 is a half-cycle shift', default=[0.0, 0.0, 0.0], size=3)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_Amplitude', 'm_Frequency', 'm_Phase', ]
    
    def m_connections(self):
        return [], [], ['Transform'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_PerlinNoise)
type_names.append('BVTK_NT_PerlinNoise')


# --------------------------------------------------------------


menu_items = [NodeItem(x) for x in type_names]
node_categories.append(BVTK_NodeCategory('VTKImplicitFunc', 'ImplicitFunc', items=menu_items))
