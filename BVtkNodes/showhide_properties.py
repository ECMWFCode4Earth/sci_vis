from .utils import log
from . import core
import bpy


class BVTK_PT_ShowHideProperties(bpy.types.Panel):
    """BVTK Show/hide properties panel"""
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
            prop_dict = getattr(core.CLASSES[active_node.bl_idname], m_properties[i])[1]
            if 'name' in prop_dict:  # collection properties don't have name
                row.label(text=prop_dict['name'])
            elif 'attr' in prop_dict:
                row.label(text=prop_dict['attr'][2:])  # removing first chars 'm_'
            else:
                log.error("Broken dict " + str(prop_dict))


core.add_ui_class(BVTK_PT_ShowHideProperties)
