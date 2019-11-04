import bpy
from .. utilities import register


class BVTK_PT_ShowHideProperties(bpy.types.Panel):
    """BVTK show/hide properties panel"""
    bl_label = 'Show/Hide Properties'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = 'Properties'

    @classmethod
    def poll(cls, context):
        return  context.active_node is not None and \
                context.space_data.tree_type == 'BVTK_NodeTree' and \
                hasattr(context.active_node, 'b_properties')

    def draw(self, context):
        layout = self.layout
        active_node = context.active_node
        m_properties = context.active_node.m_properties()
        for i in range(len(m_properties)):
            row = layout.row()
            row.prop(active_node, 'b_properties', index=i)
            row.label(m_properties[i][2:])


# ----------------------------------------------------------------

register.add_class(BVTK_PT_ShowHideProperties)
