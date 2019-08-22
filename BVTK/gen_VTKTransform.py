from .core import *
TYPENAMES = []


# --------------------------------------------------------------


class BVTK_NT_Transform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_Transform'
    bl_label = 'vtkTransform'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['Input', 'Inverse', 'Matrix'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_Transform)
TYPENAMES.append('BVTK_NT_Transform' )


# --------------------------------------------------------------


class BVTK_NT_MatrixToHomogeneousTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MatrixToHomogeneousTransform'
    bl_label = 'vtkMatrixToHomogeneousTransform'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['Input', 'Inverse'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_MatrixToHomogeneousTransform)
TYPENAMES.append('BVTK_NT_MatrixToHomogeneousTransform' )


# --------------------------------------------------------------


class BVTK_NT_GridTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GridTransform'
    bl_label = 'vtkGridTransform'
    e_InterpolationMode_items = [(x, x, x) for x in ['Cubic', 'Linear', 'NearestNeighbor']]
    
    m_DisplacementScale = bpy.props.FloatProperty(name='DisplacementScale', description='Set scale factor to be applied to the displacements. This is used primarily for grids which contain integer data types. Default: ', default=1.0)
    m_DisplacementShift = bpy.props.FloatProperty(name='DisplacementShift', description='Set a shift to be applied to the displacements. The shift is applied after the scale, i.e. x = scale*y + shift. Default: ', default=0.0)
    e_InterpolationMode = bpy.props.EnumProperty(name='InterpolationMode', description='Set interpolation mode for sampling the grid. Higher-order interpolation allows you to use a sparser grid. Default: Linear', default='Linear', items=e_InterpolationMode_items)
    m_InverseIterations = bpy.props.IntProperty(name='InverseIterations', description='Set the maximum number of iterations for the inverse transformation. The default is 500, but usually only 2 to 5 iterations are used. The inversion method is fairly robust, and it should converge for nearly all smooth transformations that do not fold back on themselves', default=500)
    m_InverseTolerance = bpy.props.FloatProperty(name='InverseTolerance', description='Set the tolerance for inverse transformation. The default is 0.001', default=0.01)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_DisplacementScale', 'm_DisplacementShift', 'e_InterpolationMode', 'm_InverseIterations', 'm_InverseTolerance', ]
    
    def m_connections(self):
        return [], [], ['Inverse'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_GridTransform)
TYPENAMES.append('BVTK_NT_GridTransform' )


# --------------------------------------------------------------


class BVTK_NT_SphericalTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_SphericalTransform'
    bl_label = 'vtkSphericalTransform'
    
    m_InverseIterations = bpy.props.IntProperty(name='InverseIterations', description='Set the maximum number of iterations for the inverse transformation. The default is 500, but usually only 2 to 5 iterations are used. The inversion method is fairly robust, and it should converge for nearly all smooth transformations that do not fold back on themselves', default=500)
    m_InverseTolerance = bpy.props.FloatProperty(name='InverseTolerance', description='Set the tolerance for inverse transformation. The default is 0.001', default=0.001)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_InverseIterations', 'm_InverseTolerance', ]
    
    def m_connections(self):
        return [], [], ['Inverse'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_SphericalTransform)
TYPENAMES.append('BVTK_NT_SphericalTransform' )


# --------------------------------------------------------------


class BVTK_NT_IterativeClosestPointTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_IterativeClosestPointTransform'
    bl_label = 'vtkIterativeClosestPointTransform'
    e_MeanDistanceMode_items = [(x, x, x) for x in ['AbsoluteValue', 'RMS']]
    
    m_CheckMeanDistance = bpy.props.BoolProperty(name='CheckMeanDistance', description='Force the algorithm to check the mean distance between two iterations. Default is Off', default=True)
    m_MaximumMeanDistance = bpy.props.FloatProperty(name='MaximumMeanDistance', description='Set/Get the maximum mean distance between two iteration. If the mean distance is lower than this, the convergence stops. The default is 0.01', default=0.01)
    m_MaximumNumberOfIterations = bpy.props.IntProperty(name='MaximumNumberOfIterations', description='Set/Get the maximum number of iterations. Default is 50', default=50)
    m_MaximumNumberOfLandmarks = bpy.props.IntProperty(name='MaximumNumberOfLandmarks', description='Set/Get the maximum number of landmarks sampled in your dataset. If your dataset is dense, then you will typically not need all the points to compute the ICP transform. The default is 200', default=200)
    e_MeanDistanceMode = bpy.props.EnumProperty(name='MeanDistanceMode', description='Specify the mean distance mode. This mode expresses how the mean distance is computed. The RMS mode is the square root of the average of the sum of squares of the closest point distances. The Absolute Value mode is the mean of the sum of absolute values of the closest point distances. The default is VTK_ICP_MODE_RM', default='RMS', items=e_MeanDistanceMode_items)
    m_StartByMatchingCentroids = bpy.props.BoolProperty(name='StartByMatchingCentroids', description='Starts the process by translating source centroid to target centroid. The default is Off', default=True)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_CheckMeanDistance', 'm_MaximumMeanDistance', 'm_MaximumNumberOfIterations', 'm_MaximumNumberOfLandmarks', 'e_MeanDistanceMode', 'm_StartByMatchingCentroids', ]
    
    def m_connections(self):
        return [], [], ['Inverse', 'Source', 'Target'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_IterativeClosestPointTransform)
TYPENAMES.append('BVTK_NT_IterativeClosestPointTransform' )


# --------------------------------------------------------------


class BVTK_NT_MatrixToLinearTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_MatrixToLinearTransform'
    bl_label = 'vtkMatrixToLinearTransform'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['Input', 'Inverse'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_MatrixToLinearTransform)
TYPENAMES.append('BVTK_NT_MatrixToLinearTransform' )


# --------------------------------------------------------------


class BVTK_NT_LandmarkTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_LandmarkTransform'
    bl_label = 'vtkLandmarkTransform'
    e_Mode_items = [(x, x, x) for x in ['Affine', 'RigidBody', 'Similarity']]
    
    e_Mode = bpy.props.EnumProperty(name='Mode', description='Set the number of degrees of freedom to constrain the solution to. Rigidbody (VTK_LANDMARK_RIGIDBODY): rotation and translation only. Similarity (VTK_LANDMARK_SIMILARITY): rotation, translation and isotropic scaling. Affine (VTK_LANDMARK_AFFINE): collinearity is preserved. Ratios of distances along a line are preserved. The default is similarity', default='Similarity', items=e_Mode_items)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_Mode', ]
    
    def m_connections(self):
        return [], [], ['Inverse', 'SourceLandmarks', 'TargetLandmarks'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_LandmarkTransform)
TYPENAMES.append('BVTK_NT_LandmarkTransform' )


# --------------------------------------------------------------


class BVTK_NT_PerspectiveTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_PerspectiveTransform'
    bl_label = 'vtkPerspectiveTransform'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['Input', 'Inverse', 'Matrix'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_PerspectiveTransform)
TYPENAMES.append('BVTK_NT_PerspectiveTransform' )


# --------------------------------------------------------------


class BVTK_NT_ThinPlateSplineTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_ThinPlateSplineTransform'
    bl_label = 'vtkThinPlateSplineTransform'
    e_Basis_items = [(x, x, x) for x in ['R', 'R2LogR']]
    
    e_Basis = bpy.props.EnumProperty(name='Basis', description='Specify the radial basis function to use. The default is R2LogR which is appropriate for 2D. Use |R| (SetBasisToR) if your data is 3D. Alternatively specify your own basis function, however this will mean that the transform will no longer be a true thin-plate spline', default='R2LogR', items=e_Basis_items)
    m_InverseIterations = bpy.props.IntProperty(name='InverseIterations', description='Set the maximum number of iterations for the inverse transformation. The default is 500, but usually only 2 to 5 iterations are used. The inversion method is fairly robust, and it should converge for nearly all smooth transformations that do not fold back on themselves', default=500)
    m_InverseTolerance = bpy.props.FloatProperty(name='InverseTolerance', description='Set the tolerance for inverse transformation. The default is 0.001', default=0.001)
    m_Sigma = bpy.props.FloatProperty(name='Sigma', description="Specify the 'stiffness' of the spline. The default is 1.0", default=1.0)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_Basis', 'm_InverseIterations', 'm_InverseTolerance', 'm_Sigma', ]
    
    def m_connections(self):
        return [], [], ['Inverse', 'SourceLandmarks', 'TargetLandmarks'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_ThinPlateSplineTransform)
TYPENAMES.append('BVTK_NT_ThinPlateSplineTransform' )


# --------------------------------------------------------------


class BVTK_NT_GeneralTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_GeneralTransform'
    bl_label = 'vtkGeneralTransform'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['Input', 'Inverse'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_GeneralTransform)
TYPENAMES.append('BVTK_NT_GeneralTransform' )


# --------------------------------------------------------------


class BVTK_NT_BSplineTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_BSplineTransform'
    bl_label = 'vtkBSplineTransform'
    e_BorderMode_items = [(x, x, x) for x in ['Edge', 'Zero', 'ZeroAtBorder']]
    
    e_BorderMode = bpy.props.EnumProperty(name='BorderMode', description='Set/Get the border mode, to alter behavior at the edge of the grid. The Edge mode allows the displacement to converge to the edge coefficient past the boundary, which is similar to the behavior of the vtkGridTransform. The Zero mode allows the displacement to smoothly converge to zero two node-spacings past the boundary, which is useful when you want to create a localized transform. The ZeroAtBorder mode sacrifices smoothness to further localize the transform to just one node-spacing past the boundary', default='Edge', items=e_BorderMode_items)
    m_DisplacementScale = bpy.props.FloatProperty(name='DisplacementScale', description='Set/Get a scale to apply to the transformation', default=1.0)
    m_InverseIterations = bpy.props.IntProperty(name='InverseIterations', description='Set the maximum number of iterations for the inverse transformation. The default is 500, but usually only 2 to 5 iterations are used. The inversion method is fairly robust, and it should converge for nearly all smooth transformations that do not fold back on themselves', default=500)
    m_InverseTolerance = bpy.props.FloatProperty(name='InverseTolerance', description='Set the tolerance for inverse transformation. The default is 0.001', default=1e-06)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['e_BorderMode', 'm_DisplacementScale', 'm_InverseIterations', 'm_InverseTolerance', ]
    
    def m_connections(self):
        return [], [], ['CoefficientData', 'Inverse'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_BSplineTransform)
TYPENAMES.append('BVTK_NT_BSplineTransform' )


# --------------------------------------------------------------


class BVTK_NT_CylindricalTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_CylindricalTransform'
    bl_label = 'vtkCylindricalTransform'
    
    m_InverseIterations = bpy.props.IntProperty(name='InverseIterations', description='Set the maximum number of iterations for the inverse transformation. The default is 500, but usually only 2 to 5 iterations are used. The inversion method is fairly robust, and it should converge for nearly all smooth transformations that do not fold back on themselves', default=500)
    m_InverseTolerance = bpy.props.FloatProperty(name='InverseTolerance', description='Set the tolerance for inverse transformation. The default is 0.001', default=0.001)
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['m_InverseIterations', 'm_InverseTolerance', ]
    
    def m_connections(self):
        return [], [], ['Inverse'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_CylindricalTransform)
TYPENAMES.append('BVTK_NT_CylindricalTransform' )


# --------------------------------------------------------------


class BVTK_NT_IdentityTransform(Node, BVTK_Node):

    bl_idname = 'BVTK_NT_IdentityTransform'
    bl_label = 'vtkIdentityTransform'
    
    
    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return []
    
    def m_connections(self):
        return [], [], ['Inverse'], ['Self']
    
    def methods(self):
        return []


add_class(BVTK_NT_IdentityTransform)
TYPENAMES.append('BVTK_NT_IdentityTransform' )


# --------------------------------------------------------------


menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append(BVTK_NodeCategory('VTKTransform', 'Transform', items=menu_items))