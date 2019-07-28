import vtk
# --------------------------------------------------------------------------
# WANTED CLASSES
# All classes derived from one of the wanted classes will be
# selected and used to populate the DB and generate the nodes
# --------------------------------------------------------------------------
wanted_classes = {
    "Algorithms":           vtk.vtkAlgorithm,
    "Transforms":           vtk.vtkAbstractTransform,
    "ImplicitFunctions":    vtk.vtkImplicitFunction,
    "RungeKutta":           vtk.vtkInitialValueProblemSolver,
    "ParametricFunctions":  vtk.vtkParametricFunction,
    "Splines":              vtk.vtkSpline
}


# --------------------------------------------------------------------------
# BANNED CLASS NAMES
# All the classes with a banned name will be ignored
# --------------------------------------------------------------------------
banned_class_names = (
    "vtk",
    "vtkAlgorithm",                         # abstract
    "vtkAbstractInteractionDevice",         # abstract
    "vtkAbstractRenderDevice",              # abstract
    "vtkInteractorStyleTrackball",          # deprecated
    "vtkStructuredPointsGeometryFilter",    # deprecated
    "vtkVolumeRayCastCompositeFunction",    # deprecated
    "vtkVolumeRayCastIsosurfaceFunction",   # deprecated
    "vtkVolumeRayCastMapper",               # deprecated
    "vtkVolumeRayCastMIPFunction",          # deprecated
    "vtkVolumeTextureMapper2D",             # deprecated
    "vtkVolumeTextureMapper3D",
    "vtkOpenGLVolumeTextureMapper2D",       # deprecated
    "vtkOpenGLVolumeTextureMapper3D",       # deprecated
    "vtkOpenGLPolyDataMapper",              # deprecated
    "vtkRenderState",
    "vtkRendererDelegate",
    "vtkRenderWidget",                      # deprecated
    "vtkThreadedSynchronizedTemplatesCutter3D",
    "vtkSynchronizedTemplates3D",
    "vtkNetCDFCAMReader",                   # obsolete methods
    "vtkQImageToImageSource",               # need qt, requires VTK built with SIP support
    "vtkRenderedRepresentation",
    "vtkRenderedGraphRepresentation",
    "vtkRenderedHierarchyRepresentation",
    "vtkRenderedSurfaceRepresentation",
    "vtkRenderedTreeAreaRepresentation",
    "vtkConvexHull2D",                      # take a Renderer as input
    "vtkDistanceToCamera",                  # take a Renderer as input
    "vtkGeoAdaptiveArcs",                   # take a Renderer as input
    "vtkGraphToGlyps",                      # take a Renderer as input
    "vtkLabelPlacer",                       # take a Renderer as input
    "vtkSelectVisiblePoints",               # take a Renderer as input
    "vtkVolumeOutlineSource",               # take a VolumeMapper as input
    "vtkRendererSource",
    "vtkRenderLargeImage",
    "vtkCompassRepresentation",
    "vtkCompassWidget",
    "vtkGeoAdaptiveArcs",
    "vtkGeoAlignedImageRepresentation",
    "vtkGeoAlignedImageSource",
    "vtkGeoArcs",
    "vtkGeoAssignCoordinates",
    "vtkGeoCamera",
    "vtkGeoFileImageSource",
    "vtkGeoFileTerrainSource",
    "vtkGeoGlobeSource",
    "vtkGeoGraticule",
    "vtkGeoImageNode",
    "vtkGeoInteractorStyle",
    "vtkGeoProjection",
    "vtkGeoProjectionSource",
    "vtkGeoRandomGraphSource",
    "vtkGeoSampleArcs",
    "vtkGeoSource",
    "vtkGeoSphereTransform",
    "vtkGeoTerrain",
    "vtkGeoTerrain2D",
    "vtkGeoTerrainNode",
    "vtkGeoTransform",
    "vtkGeoTreeNode",
    "vtkGeoTreeNodeCache",
    "vtkGlobeSource",
    "vtkAreaLayout",
    "vtkPerturbCoincidentVertices",
    "vtkGraphLayoutStrategy",
    "vtkArcParallelEdgeStrategy",
    "vtkBoxLayoutStrategy",
    "vtkPassThroughEdgeStrategy",
    "vtkConstrained2DLayoutStrategy",
    "vtkStackedTreeLayoutStrategy",
    "vtkCirclePackLayout",
    "vtkSquarifyLayoutStrategy",
    "vtkCirclePackFrontChainLayoutStrategy",
    "vtkSpanTreeLayoutStrategy",
    "vtkAttributeClustering2DLayoutStrategy",
    "vtkPassThroughLayoutStrategy",
    "vtkSplineGraphEdges",
    "vtkGraphLayout",
    "vtkTreeRingToPolyData",
    "vtkForceDirectedLayoutStrategy",
    "vtkEdgeLayout",
    "vtkFast2DLayoutStrategy",
    "vtkGeoMath",
    "vtkTreeOrbitLayoutStrategy",
    "vtkRandomLayoutStrategy",
    "vtkGeoEdgeStrategy",
    "vtkIncrementalForceLayout",
    "vtkAssignCoordinates",
    "vtkSimple2DLayoutStrategy",
    "vtkTreeLayoutStrategy",
    "vtkAreaLayoutStrategy",
    "vtkCommunity2DLayoutStrategy",
    "vtkCirclePackToPolyData",
    "vtkTreeMapLayout",
    "vtkSimple3DCirclesStrategy",
    "vtkKCoreLayout",
    "vtkSliceAndDiceLayoutStrategy",
    "vtkClustering2DLayoutStrategy",
    "vtkAssignCoordinatesLayoutStrategy",
    "vtkCosmicTreeLayoutStrategy",
    "vtkCirclePackLayoutStrategy",
    "vtkConeLayoutStrategy",
    "vtkCircularLayoutStrategy",
    "vtkEdgeLayoutStrategy",
    "vtkTreeMapLayoutStrategy",
    "vtkTreeMapToPolyData",
    "vtkCollapseGraph",
    "vtkTreeDifferenceFilter",
    "vtkRemoveIsolatedVertices",
    "vtkAdjacencyMatrixToEdgeTable",
    "vtkDotProductSimilarity",
    "vtkMutableGraphHelper",
    "vtkArrayToTable",
    "vtkTreeLevelsFilter",
    "vtkRemoveHiddenData",
    "vtkSparseArrayToTable",
    "vtkTransposeMatrix",
    "vtkEdgeCenters",
    "vtkPipelineGraphSource",
    "vtkTableToTreeFilter",
    "vtkStringToNumeric",
    "vtkMergeTables",
    "vtkReduceTable",
    "vtkTableToArray",
    "vtkCollapseVerticesByArray",
    "vtkStreamGraph",
    "vtkExtractSelectedTree",
    "vtkRandomGraphSource",
    "vtkGenerateIndexArray",
    "vtkDataObjectToTable",
    "vtkTreeFieldAggregator",
    "vtkMergeGraphs",
    "vtkTableToGraph",
    "vtkStringToCategory",
    "vtkPruneTreeFilter",
    "vtkGroupLeafVertices",
    "vtkExtractSelectedGraph",
    "vtkAddMembershipArray",
    "vtkVertexDegree",
    "vtkKCoreDecomposition",
    "vtkNetworkHierarchy",
    "vtkGraphHierarchicalBundleEdges",
    "vtkThresholdGraph",
    "vtkThresholdTable",
    "vtkTransferAttributes",
    "vtkArrayNorm",
    "vtkContinuousScatterplot",
    "vtkTableToSparseArray",
    "vtkMergeColumns",
    "vtkExpandSelectedGraph",
    "vtkBoostDividedEdgeBundling",
    "vtkBoostBiconnectedComponents",
    "vtkBoostConnectedComponents",
    "vtkBoostKruskalMinimumSpanningTree",
    "vtkBoostSplitTableField",
    "vtkBoostBetweennessClustering",
    "vtkBoostPrimMinimumSpanningTree",
    "vtkBoostBrandesCentrality",
    "vtkBoostExtractLargestComponent",
    "vtkBoostLogWeighting",
    "vtkBoostRandomSparseArraySource",
    "vtkBoostGraphAdapter",
    "vtkBoostBreadthFirstSearch",
    "vtkBoostBreadthFirstSearchTree",
    "vtkPBGLCollapseParallelEdges",
    "vtkPBGLCollectGraph",
    "vtkPBGLRMATGraphSource",
    "vtkPBGLRandomGraphSource",
    "vtkPBGLGraphSQLReader",
    "vtkPBGLVertexColoring",
    "vtkPBGLMinimumSpanningTree",
    "vtkPBGLGraphAdapter",
    "vtkPBGLCollapseGraph",
    "vtkPBGLShortestPaths",
    "vtkPBGLDistributedGraphHelper",
    "vtkPBGLConnectedComponents",
    "vtkPBGLBreadthFirstSearch",
    "vtkTryDowncast",
    "vtkVariantBoostSerialization"
)


# --------------------------------------------------------------------------
# BANNED METHODS
# All the methods with a banned name will be ignored
# --------------------------------------------------------------------------
banned_methods = (
    "AbortExecuteOff",
    "AbortExecuteOn",
    "AddObserver",
    "BreakOnError",
    "ComputeInputUpdateExtents",
    "DebugOff",
    "DebugOn",
    "Delete",
    "EnlargeOutputUpdateExtents",
    "GetAbortExecute",
    "GetAddressAsString",
    "GetDebug",
    "GetErrorCode",
    "GetGlobalWarningDisplay",
    "GetMTime",
    "GetOutputIndex",
    "GetProgress",
    "GetProgressMaxValue",
    "GetProgressText",
    "GetReferenceCount",
    "GetReleaseDataFlag",
    "GlobalWarningDisplayOn",
    "GlobalWarningDisplayOff",
    "HasObserver",
    "InRegisterLoop",
    "InvokeEvent",
    "IsA",
    "IsTypeOf",
    "New",
    "NewInstance",
    "PrintRevisions",
    "PropagateUpdateExtent",
    "Register",
    "ReleaseDataFlagOff",
    "ReleaseDataFlagOn",
    "RemoveAllInputs",
    "RemoveObserver",
    "RemoveObservers",
    "SetAbortExecute",
    "SafeDownCast",
    "SetDebug",
    "SetEndMethod",
    "SetGlobalWarningDisplay",
    "SetProgress",
    "SetProgress",
    "SetProgressMethod",
    "SetProgressText",
    "SetReleaseDataFlag",
    "SetReferenceCount",
    "SetStartMethod",
    "SqueezeInputArray",
    "TriggerAsynchronousUpdate",
    "UnRegister",
    "UnRegisterAllOutputs",
    "UpdateData",
    "UpdateInformation",
    "UpdateProgress",
    "UpdateWholeExtent",
    "GetUserTransformMatrixMTime",
    "ReleaseGraphicsResources",
    "RenderOpaqueGeometry",
    "RenderTranslucentGeometry",
    "ApplyProperties",
    "ComputeMatrix",
    "ShallowCopy",
    "WholeExtent"
)


# --------------------------------------------------------------------------
# BANNED MIRROR PROPERTIES
# All the mirror properties with a banned name will be ignored
# --------------------------------------------------------------------------
banned_props = (
    "DataExtent",
    "DataType",
    "Executive",
    "Information",
    "InputConnection",
    "InputDataObject",
    "Locator",
    "Output",
    "OutputPointsPrecision",
    "ProgressObserver",
    "ScalarTree",
    "UpdateExtent",
    "UseScalarTree",
    "WholeExtent",
    "ParserErrorObserver",
    "Kernel7x7",            # vtkImageConvolve
    "Kernel7x7x7",          # vtkImageConvolve -- Setter has no doc
    # bad getter: Set(float) Get(float):
    "ResolveCoincidentTopologyPointOffsetParameter",
    "ResolveCoincidentTopologyLineOffsetParameters",
    "RelativeCoincidentTopologyPointOffsetParameter",
    "RelativeCoincidentTopologyLineOffsetParameters",
    "Controller",           # parallel filters
    "SocketController",     # parallel filters
    "Compressor",           # xml writers
    "AssessNames",          # histogram and statistics
    "Camera",               # cant pass the camera in blender Nodes yet
    "FileNames",            # image readers for volumes on multiple slices with non generable names
    "InformationInput",     # optional in some image filters
    "LayoutStrategy",       # graph layout --- not addressed yet
    "MemoryBuffer",         # on image readers, allow reading from memory instead of file
    "ReaderErrorObserver"   # xml readers
    "Renderer",             # cant pass the renderer in blender Nodes yet
    "VolumeMapper",         # VolumeOutlineSource
    "Result",               # vtkUnsignedCharArray used in PNG and JPEG writer
    "CallbackUserData"      # in ImageImport
    "ImportVoidPointer"     # in ImageImport
)
