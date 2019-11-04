from .. core import *
cat = "Parametric Functions"


# --------------------------------------------------------------


class BVTK_NT_ParametricFigure8Klein(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricFigure8Klein"
    bl_label = "vtkParametricFigure8Klein"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=3.141592653589793)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=3.141592653589793)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=-3.141592653589793)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=-3.141592653589793)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set/Get the radius of the bottle. Default is 1', default=1.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_Radius", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricFigure8Klein, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricBohemianDome(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricBohemianDome"
    bl_label = "vtkParametricBohemianDome"
    
    m_A = bpy.props.FloatProperty(name='A', description='Construct a Bohemian dome surface with the following parameters', default=0.5)
    m_B = bpy.props.FloatProperty(name='B', description='', default=1.5)
    m_C = bpy.props.FloatProperty(name='C', description='', default=1.0)
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=3.141592653589793)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=3.141592653589793)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=-3.141592653589793)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=-3.141592653589793)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_A", "m_B", "m_C", "m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricBohemianDome, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricPluckerConoid(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricPluckerConoid"
    bl_label = "vtkParametricPluckerConoid"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=3.0)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=6.283185307179586)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_N = bpy.props.IntProperty(name='N', description='This is the number of folds in the conoid', default=2)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_N", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricPluckerConoid, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricEllipsoid(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricEllipsoid"
    bl_label = "vtkParametricEllipsoid"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=6.283185307179586)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=3.141592653589793)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_XRadius = bpy.props.FloatProperty(name='XRadius', description='Set/Get the scaling factor for the x-axis. Default is 1', default=1.0)
    m_YRadius = bpy.props.FloatProperty(name='YRadius', description='Set/Get the scaling factor for the y-axis. Default is 1', default=1.0)
    m_ZRadius = bpy.props.FloatProperty(name='ZRadius', description='Set/Get the scaling factor for the z-axis. Default is 1', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", "m_XRadius", "m_YRadius", "m_ZRadius", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricEllipsoid, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricCrossCap(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricCrossCap"
    bl_label = "vtkParametricCrossCap"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=3.141592653589793)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=3.141592653589793)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricCrossCap, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricSuperToroid(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricSuperToroid"
    bl_label = "vtkParametricSuperToroid"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_CrossSectionRadius = bpy.props.FloatProperty(name='CrossSectionRadius', description='Set/Get the radius of the cross section of ring of the supertoroid. Default = 0.5', default=0.5)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=6.283185307179586)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=6.283185307179586)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_N1 = bpy.props.FloatProperty(name='N1', description='Set/Get the shape of the torus ring. Default is 1', default=1.0)
    m_N2 = bpy.props.FloatProperty(name='N2', description='Set/Get the shape of the cross section of the ring. Default is 1', default=1.0)
    m_RingRadius = bpy.props.FloatProperty(name='RingRadius', description='Set/Get the radius from the center to the middle of the ring of the supertoroid. Default is 1', default=1.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_XRadius = bpy.props.FloatProperty(name='XRadius', description='Set/Get the scaling factor for the x-axis. Default is 1', default=1.0)
    m_YRadius = bpy.props.FloatProperty(name='YRadius', description='Set/Get the scaling factor for the y-axis. Default is 1', default=1.0)
    m_ZRadius = bpy.props.FloatProperty(name='ZRadius', description='Set/Get the scaling factor for the z-axis. Default is 1', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=21, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_CrossSectionRadius", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_N1", "m_N2", "m_RingRadius", "m_TwistU", "m_TwistV", "m_TwistW", "m_XRadius", "m_YRadius", "m_ZRadius", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricSuperToroid, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricEnneper(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricEnneper"
    bl_label = "vtkParametricEnneper"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=2.0)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=2.0)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=-2.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=-2.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricEnneper, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricHenneberg(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricHenneberg"
    bl_label = "vtkParametricHenneberg"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=1.0)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=1.5707963267948966)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=-1.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=-1.5707963267948966)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricHenneberg, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricKuen(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricKuen"
    bl_label = "vtkParametricKuen"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DeltaV0 = bpy.props.FloatProperty(name='DeltaV0', description='Set/Get the value to use when V == 0. Default is 0.05, giving the best appearance with the default settings. Setting it to a value less than 0.05 extrapolates the surface towards a pole in the -z direction. Setting it to 0 retains the pole whose z-value is -inf', default=0.05)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=4.5)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=3.141592653589793)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=-4.5)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DeltaV0", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricKuen, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricBoy(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricBoy"
    bl_label = "vtkParametricBoy"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=3.141592653589793)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=3.141592653589793)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_ZScale = bpy.props.FloatProperty(name='ZScale', description='Set/Get the scale factor for the z-coordinate. Default is 1/8, giving a nice shape', default=0.125)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", "m_ZScale", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricBoy, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricSpline(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricSpline"
    bl_label = "vtkParametricSpline"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_Closed = bpy.props.BoolProperty(name='Closed', description='Control whether the spline is open or closed. A closed spline forms a continuous loop: the first and last points are the same, and derivatives are continuous', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_LeftConstraint = bpy.props.IntProperty(name='LeftConstraint', description='Set the type of constraint of the left(right) end points. Four constraints are available', default=1)
    m_LeftValue = bpy.props.FloatProperty(name='LeftValue', description='The values of the derivative on the left and right sides. The value is used only if the left(right) constraint is type 1-3', default=0.0)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=1.0)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=1.0)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_ParameterizeByLength = bpy.props.BoolProperty(name='ParameterizeByLength', description='Control whether the spline is parameterized by length or by point index. Default is by length', default=True)
    m_RightConstraint = bpy.props.IntProperty(name='RightConstraint', description='Set the type of constraint of the left(right) end points. Four constraints are available', default=1)
    m_RightValue = bpy.props.FloatProperty(name='RightValue', description='The values of the derivative on the left and right sides. The value is used only if the left(right) constraint is type 1-3', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=20, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_Closed", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_LeftConstraint", "m_LeftValue", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_ParameterizeByLength", "m_RightConstraint", "m_RightValue", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], ['Points', 'XSpline', 'YSpline', 'ZSpline'], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricSpline, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricBour(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricBour"
    bl_label = "vtkParametricBour"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=1.0)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=12.566370614359172)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricBour, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricSuperEllipsoid(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricSuperEllipsoid"
    bl_label = "vtkParametricSuperEllipsoid"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=3.141592653589793)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=1.5707963267948966)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=-3.141592653589793)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=-1.5707963267948966)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_N1 = bpy.props.FloatProperty(name='N1', description='Set/Get the "squareness" parameter in the z axis. Default is 1', default=1.0)
    m_N2 = bpy.props.FloatProperty(name='N2', description='Set/Get the "squareness" parameter in the x-y plane. Default is 1', default=1.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_XRadius = bpy.props.FloatProperty(name='XRadius', description='Set/Get the scaling factor for the x-axis. Default is 1', default=1.0)
    m_YRadius = bpy.props.FloatProperty(name='YRadius', description='Set/Get the scaling factor for the y-axis. Default is 1', default=1.0)
    m_ZRadius = bpy.props.FloatProperty(name='ZRadius', description='Set/Get the scaling factor for the z-axis. Default is 1', default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=19, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_N1", "m_N2", "m_TwistU", "m_TwistV", "m_TwistW", "m_XRadius", "m_YRadius", "m_ZRadius", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricSuperEllipsoid, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricKlein(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricKlein"
    bl_label = "vtkParametricKlein"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=3.141592653589793)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=6.283185307179586)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricKlein, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricRoman(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricRoman"
    bl_label = "vtkParametricRoman"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=3.141592653589793)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=3.141592653589793)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set/Get the radius. Default is 1', default=1.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_Radius", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricRoman, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricPseudosphere(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricPseudosphere"
    bl_label = "vtkParametricPseudosphere"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=5.0)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=3.141592653589793)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=-5.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=-3.141592653589793)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricPseudosphere, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricRandomHills(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricRandomHills"
    bl_label = "vtkParametricRandomHills"
    
    m_AllowRandomGeneration = bpy.props.BoolProperty(name='AllowRandomGeneration', description='Set/Get the random generation flag. A value of 0 will disable the generation of random hills on the surface allowing a reproducible number of identically shaped hills to be generated. If zero, then the number of hills used will be the nearest perfect square less than or equal to the number of hills. For example, selecting 30 hills will result in a 5 X 5 array of hills being generated. Thus a square array of hills will be generated', default=True)
    m_AmplitudeScaleFactor = bpy.props.FloatProperty(name='AmplitudeScaleFactor', description='Set/Get the scaling factor for the amplitude. Default is 1/3', default=0.3333333333333333)
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_HillAmplitude = bpy.props.FloatProperty(name='HillAmplitude', description='Set/Get the hill amplitude (height). Default is 2', default=2.0)
    m_HillXVariance = bpy.props.FloatProperty(name='HillXVariance', description='Set/Get the hill variance in the x-direction. Default is 2.5', default=2.5)
    m_HillYVariance = bpy.props.FloatProperty(name='HillYVariance', description='Set/Get the hill variance in the y-direction. Default is 2.5', default=2.5)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=10.0)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=10.0)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=-10.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=-10.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_NumberOfHills = bpy.props.IntProperty(name='NumberOfHills', description='Set/Get the number of hills. Default is 30', default=30)
    m_RandomSeed = bpy.props.IntProperty(name='RandomSeed', description='Set/Get the Seed for the random number generator, a value of 1 will initialize the random number generator, a negative value will initialize it with the system time. Default is 1', default=1)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_XVarianceScaleFactor = bpy.props.FloatProperty(name='XVarianceScaleFactor', description='Set/Get the scaling factor for the variance in the x-direction. Default is 1/3', default=0.3333333333333333)
    m_YVarianceScaleFactor = bpy.props.FloatProperty(name='YVarianceScaleFactor', description='Set/Get the scaling factor for the variance in the y-direction. Default is 1/3', default=0.3333333333333333)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=23, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_AllowRandomGeneration", "m_AmplitudeScaleFactor", "m_ClockwiseOrdering", "m_DerivativesAvailable", "m_HillAmplitude", "m_HillXVariance", "m_HillYVariance", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_NumberOfHills", "m_RandomSeed", "m_TwistU", "m_TwistV", "m_TwistW", "m_XVarianceScaleFactor", "m_YVarianceScaleFactor", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricRandomHills, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricTorus(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricTorus"
    bl_label = "vtkParametricTorus"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_CrossSectionRadius = bpy.props.FloatProperty(name='CrossSectionRadius', description='Set/Get the radius of the cross section of ring of the torus. Default is 0.5', default=0.5)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=6.283185307179586)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=6.283185307179586)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_RingRadius = bpy.props.FloatProperty(name='RingRadius', description='Set/Get the radius from the center to the middle of the ring of the torus. Default is 1.0', default=1.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_CrossSectionRadius", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_RingRadius", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricTorus, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricMobius(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricMobius"
    bl_label = "vtkParametricMobius"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=6.283185307179586)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=1.0)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=-1.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_Radius = bpy.props.FloatProperty(name='Radius', description='Set/Get the radius of the Mobius strip. Default is 1', default=1.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_Radius", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricMobius, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricDini(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricDini"
    bl_label = "vtkParametricDini"
    
    m_A = bpy.props.FloatProperty(name='A', description='Set/Get the scale factor. See the definition in Parametric surfaces referred to above. Default is 1', default=1.0)
    m_B = bpy.props.FloatProperty(name='B', description='Set/Get the scale factor. See the definition in Parametric surfaces referred to above. Default is 0.', default=0.2)
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=12.566370614359172)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=2.0)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.001)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_A", "m_B", "m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricDini, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricCatalanMinimal(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricCatalanMinimal"
    bl_label = "vtkParametricCatalanMinimal"
    
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=12.566370614359172)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=1.5)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=-12.566370614359172)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=-1.5)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricCatalanMinimal, cat)


# --------------------------------------------------------------


class BVTK_NT_ParametricConicSpiral(Node, BVTK_Node):

    bl_idname = "BVTK_NT_ParametricConicSpiral"
    bl_label = "vtkParametricConicSpiral"
    
    m_A = bpy.props.FloatProperty(name='A', description='Set/Get the scale factor. Default = 0.', default=0.2)
    m_B = bpy.props.FloatProperty(name='B', description='Set/Get the A function coefficient. See the definition in Parametric surfaces referred to above. Default is 1', default=1.0)
    m_C = bpy.props.FloatProperty(name='C', description='Set/Get the B function coefficient. See the definition in Parametric surfaces referred to above. Default is 0.1', default=0.1)
    m_ClockwiseOrdering = bpy.props.BoolProperty(name='ClockwiseOrdering', description='Set/Get the flag which determines the ordering of the the vertices forming the triangle strips. The ordering of the points being inserted into the triangle strip is important because it determines the direction of the normals for the lighting. If set, the ordering is clockwise, otherwise the ordering is anti-clockwise. Default is true (i.e. clockwise ordering)', default=True)
    m_DerivativesAvailable = bpy.props.BoolProperty(name='DerivativesAvailable', description='Set/Get the flag which determines whether derivatives are available from the parametric function (i.e., whether the Evaluate() method returns valid derivatives)', default=True)
    m_JoinU = bpy.props.BoolProperty(name='JoinU', description='Set/Get the flag which joins the first triangle strip to the last one', default=True)
    m_JoinV = bpy.props.BoolProperty(name='JoinV', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_JoinW = bpy.props.BoolProperty(name='JoinW', description='Set/Get the flag which joins the the ends of the triangle strips', default=True)
    m_MaximumU = bpy.props.FloatProperty(name='MaximumU', description='Set/Get the maximum u-value', default=6.283185307179586)
    m_MaximumV = bpy.props.FloatProperty(name='MaximumV', description='Set/Get the maximum v-value', default=6.283185307179586)
    m_MaximumW = bpy.props.FloatProperty(name='MaximumW', description='Set/Get the maximum w-value', default=1.0)
    m_MinimumU = bpy.props.FloatProperty(name='MinimumU', description='Set/Get the minimum u-value', default=0.0)
    m_MinimumV = bpy.props.FloatProperty(name='MinimumV', description='Set/Get the minimum v-value', default=0.0)
    m_MinimumW = bpy.props.FloatProperty(name='MinimumW', description='Set/Get the minimum w-value', default=0.0)
    m_N = bpy.props.FloatProperty(name='N', description='Set/Get the C function coefficient. See the definition in Parametric surfaces referred to above. Default is 2', default=2.0)
    m_TwistU = bpy.props.BoolProperty(name='TwistU', description='Set/Get the flag which joins the first triangle strip to the last one with a twist. JoinU must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistV = bpy.props.BoolProperty(name='TwistV', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinV must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    m_TwistW = bpy.props.BoolProperty(name='TwistW', description='Set/Get the flag which joins the ends of the triangle strips with a twist. JoinW must also be set if this is set. Used when building some non-orientable surfaces', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ["m_A", "m_B", "m_C", "m_ClockwiseOrdering", "m_DerivativesAvailable", "m_JoinU", "m_JoinV", "m_JoinW", "m_MaximumU", "m_MaximumV", "m_MaximumW", "m_MinimumU", "m_MinimumV", "m_MinimumW", "m_N", "m_TwistU", "m_TwistV", "m_TwistW", ]
    
    def m_connections(self):
        return [], [], [], ['Self']
    
    def methods(self):
        return []


add_node(BVTK_NT_ParametricConicSpiral, cat)


# --------------------------------------------------------------
