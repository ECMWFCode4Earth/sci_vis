# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   inputs/__init__.py
#
#   Define nodes used by the user to input variables and objects
#   in the pipeline.
# ---------------------------------------------------------------------------------


from ... utilities import *
from .. core import *


class BVTK_NT_ImageInput(Node, BVTK_Node):
    """BVTK Info Node"""
    bl_idname = 'BVTK_NT_ImageInput'
    bl_label = 'Image'

    image = bpy.props.PointerProperty(type=bpy.types.Image)
    preview = bpy.props.BoolProperty(default=False)

    def m_properties(self):
        return []

    def m_connections(self):
        return [], [], [], ["Output"]

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.template_ID(self, "image", open="image.open")

        if self.image:
            icon = "RESTRICT_VIEW_OFF" if self.preview else "RESTRICT_VIEW_ON"
            row.prop(self, "preview", icon_only=True, icon=icon, emboss=False)

            if self.preview:
                layout.template_ID_preview(self, "image", open="image.open")

    def apply_properties(self, vtk_obj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socket):
        return self.image


cat = "Inputs"
register.set_category_icon(cat, "SETTINGS")
add_node(BVTK_NT_ImageInput, cat)
