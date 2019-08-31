import bpy
from mathutils import *
from math import *
from . import core
from . utils import log
from bpy_extras.io_utils import ExportHelper
import json
import os

# -----------------------------------------------------------------------------
# Node tree JSON import/export, node arranging operator and node tree examples
# -----------------------------------------------------------------------------

examples_dir = os.path.realpath(__file__).replace('examples.py', 'examples/')
examples_data_dir = os.path.realpath(__file__).replace('examples.py', 'examples_data/')

# -----------------------------------------------------------------------------
# Functions to save node state into a dictionary
# -----------------------------------------------------------------------------


class BVTK_PT_TreeIE(bpy.types.Panel):
    """Import and export VTK node tree as json"""
    bl_label = 'Import/Export Tree'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = 'Examples'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.tree_type == 'BVTK_NodeTree'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.operator('bvtk.tree_export', text='Export JSON', icon='FILE_TEXT')

        row = layout.row()
        row.operator('bvtk.tree_import', text='Import JSON', icon='FILE')


core.add_ui_class(BVTK_PT_TreeIE)


class BVTK_PT_ArrangeTree(bpy.types.Panel):
    """ Arrange node tree """
    bl_label = 'Arrange Tree'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = 'Examples'
    # bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.tree_type == 'BVTK_NodeTree'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.label("Arrangement depends on the selected nodes!", icon="INFO")
        col = layout.column(align=True)
        col.operator('bvtk.arrange_tree', text='arrange', icon='NODETREE')
        col.prop(scene, 'bvtk_arrange_x_spacing', text='x spacing')
        col.prop(scene, 'bvtk_arrange_y_spacing', text='y spacing')
        layout.prop(scene, 'bvtk_arrange_collapse_x', text='collapse x')


def arrange(scene, context):
    bpy.ops.bvtk.arrange_tree()


bpy.types.Scene.bvtk_arrange_x_spacing = bpy.props.IntProperty(default=10, update=arrange)
bpy.types.Scene.bvtk_arrange_y_spacing = bpy.props.IntProperty(default=10, update=arrange)
bpy.types.Scene.bvtk_arrange_collapse_x = bpy.props.BoolProperty(default=False, update=arrange)

core.add_ui_class(BVTK_PT_ArrangeTree)


class BVTK_PT_Examples(bpy.types.Panel):
    """Examples Panel"""
    bl_label = 'Examples'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = 'Examples'

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.tree_type == 'BVTK_NodeTree'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        layout.menu('BVTK_MT_Examples')


core.add_ui_class(BVTK_PT_Examples)


class BVTK_MT_Examples(bpy.types.Menu):
    """Examples Menu"""
    bl_label = "Examples"

    def draw(self, context):
        layout = self.layout
        for i in os.listdir(examples_dir):
            if i.endswith('.json'):
                layout.operator('bvtk.tree_import',
                                text = i.replace('.json', '')
                                ).filepath = examples_dir + i

        for em in ExamplesMenus:
            layout.menu(em.bl_idname)


core.add_ui_class(BVTK_MT_Examples)


# Populate examples from example directory to Examples menu
ExamplesMenus = []
for name in [name for name in os.listdir(examples_dir)
             if os.path.isdir(os.path.join(examples_dir, name))]:
    def menu_draw(self, context):
        layout = self.layout
        for i in os.listdir(self.filepath):
            if i.endswith('.json'):
                layout.operator('bvtk.tree_import',
                                text=i.replace('.json', '')).filepath = \
                                os.path.join(self.filepath, i)

    menu_type = type("BVTK_MT_" + name, (bpy.types.Menu,), {
        "bl_idname": "BVTK_MT_" + name,
        "bl_label": name,
        "draw": menu_draw,
        "filepath": os.path.join(examples_dir, name)
    })

    ExamplesMenus.append(menu_type)
    core.add_ui_class(menu_type)


# -----------------------------------------------------------------------------
# Import export functions
# -----------------------------------------------------------------------------

def gisbi(node, identifier):
    """Get input socket by identifier"""
    inputs = node.inputs
    for input in inputs:
        if input.identifier == identifier:
            return input
    return None


def gosbi(node, identifier):
    """Get output socket by identifier"""
    outputs = node.outputs
    for output in outputs:
        if output.identifier == identifier:
            return output
    return None


def gnbn(nodes, name):
    """Get node by name"""
    for node in nodes:
        if node.name == name:
            return node
    return None


def node_tree_from_dict(context, node_tree_dict):
    """Create node tree from dictionary"""
    space = context.space_data
    nodes = space.node_tree.nodes
    links = space.node_tree.links
    new_nodes_dicts = node_tree_dict['nodes']
    for new_node_dict in new_nodes_dicts:
        node_from_dict(nodes, new_node_dict)
    new_links_dicts = node_tree_dict['links']
    for new_link_dict in new_links_dicts:
        link_from_dict(nodes, links, new_link_dict)


def node_from_dict(nodes, node_dict):
    """Create a node using data from node dictionary"""
    id_name = node_dict['bl_idname']
    new_node = nodes.new(type=id_name)
    for prop in node_dict:
        value = node_dict[prop]
        if prop == 'additional_properties':
            if hasattr(new_node, 'import_properties'):
                new_node.import_properties(value)
        else:
            if 'FileName' in prop and value.startswith('$/'):
                value = value.replace('$/', examples_data_dir)
            try:
                setattr(new_node, prop, value)
            except:
                log.error("setattr failed for " + str(prop) + " " + str(value))


def link_from_dict(nodes, links, new_link_dict):
    """Create link between nodes using data from node dictionary"""
    to_node = gnbn(nodes, new_link_dict['to_node_name'])
    from_node = gnbn(nodes, new_link_dict['from_node_name'])
    if from_node and to_node:
        from_socket = gosbi(from_node, new_link_dict['from_socket_identifier'])
        to_socket = gisbi(to_node, new_link_dict['to_socket_identifier'])
        if to_socket and from_socket:
            links.new(to_socket, from_socket)


def node_tree_to_dict(node_tree):
    """Create node dictionary from node tree"""
    nodes = node_tree.nodes
    links = node_tree.links
    n = []
    for node in nodes:
        n.append(node_to_dict(node))
    l = []
    for link in links:
        l.append(link_to_dict(link))
    return {"nodes": n, "links": l}


def link_to_dict(link):
    """Create a link dictionary entry from link"""
    dict = {}
    dict['from_node_name'] = link.from_node.name
    dict['to_node_name'] = link.to_node.name
    dict['from_socket_identifier'] = link.from_socket.identifier
    dict['to_socket_identifier'] = link.to_socket.identifier
    return dict


def node_to_dict(node):
    """Create a node dictionary entry from node"""
    dict = {}
    props = [k for k in node.m_properties()]
    props.extend(['bl_idname',
                  'name',
                  'color',
                  'height',
                  'hide',
                  'label',
                  'location',
                  'mute',
                  'show_options',
                  'show_preview',
                  'width'
                  ])
    for prop in props:
        attr = getattr(node, prop)
        classname = attr.__class__.__name__
        if classname in ['Vector', 'Color', 'bpy_prop_array']:
            attr = [i for i in attr]
        if 'FileName' in prop and issubclass(attr.__class__, str):
            attr = os.path.realpath(bpy.path.abspath(attr)).replace(examples_data_dir, '$/')
        log.debug(prop.ljust(20) + classname.ljust(20) + str(attr))
        dict[prop] = attr
    if hasattr(node, 'export_properties'):
        ep = node.export_properties()
        dict['additional_properties'] = ep
        for k in ep:
            if k in dict:
                dict.pop(k)
    return dict


# -----------------------------------------------------------------------------
# Import export operators
# -----------------------------------------------------------------------------


class BVTK_OT_TreeImport(bpy.types.Operator):
    """Import VTK Node Tree"""
    bl_idname = "bvtk.tree_import"
    bl_label = "choose file"

    filepath = bpy.props.StringProperty(subtype='FILE_PATH', default='')
    confirm = bpy.props.BoolProperty(default=True)

    def invoke(self, context, event):
        node_tree = context.space_data.node_tree

        if node_tree is None:
            node_tree = bpy.data.node_groups.new('NodeTree', 'BVTK_NodeTree')
            context.space_data.node_tree = node_tree

        if self.confirm and node_tree.nodes:
            def draw(self2, context):
                self2.layout.label("This will erase current node tree")
                self2.layout.operator_context = 'INVOKE_DEFAULT'
                self2.layout.operator(self.bl_idname, text='Confirm').confirm=False
            bpy.context.window_manager.popup_menu(draw, title="Are you sure?", icon='QUESTION')
            return {'FINISHED'}

        self.confirm=True

        if self.filepath == '':
            context.window_manager.fileselect_add(self)
            return {'RUNNING_MODAL'}

        return self.execute(context)

    def execute(self, context):
        f = open(self.filepath, 'r', encoding='utf-8')
        text = f.read()
        f.close()
        bpy.ops.node.select_all(action='SELECT')
        bpy.ops.node.delete()

        dic =  json.loads( text )      
        node_tree_from_dict( context, dic )
        bpy.ops.node.select_all(action='DESELECT')
        self.filepath = ''
        return {'FINISHED'}


core.add_ui_class(BVTK_OT_TreeImport)


class BVTK_OT_TreeExport(bpy.types.Operator, ExportHelper):
    """Save VTK node tree into a json file"""
    bl_idname = "bvtk.tree_export"
    bl_label = "Export Vtk Node Tree"
    filename_ext = ".json"

    def execute(self, context):
        node_tree = context.space_data.node_tree
        if node_tree is None:
            self.report({'ERROR'}, 'Select a node tree')
            return {'CANCELLED'}
        dic = node_tree_to_dict(node_tree)
        text = json.dumps( dic, indent=4, sort_keys=True) 
        f = open(self.filepath, 'w', encoding='utf-8')
        f.write( text )
        f.close()
        return {'FINISHED'}


core.add_ui_class(BVTK_OT_TreeExport)


class BVTK_OT_TreeImportFromPy(bpy.types.Operator):
    """Import VTK node tree from Python file"""
    # Note: This class and node_tree_from_py are currently not used.
    # This was an attempt to generate node tree from VTK examples.
    # TODO: Continue attempt at some point? It's a nice idea.
    bl_idname = "bvtk.tree_import_py"
    bl_label = "choose file"

    filepath = bpy.props.StringProperty(subtype='FILE_PATH', default='')
    confirm = bpy.props.BoolProperty(default=True)

    def invoke(self, context, event):
        node_tree = context.space_data.node_tree
        if node_tree is None:
            self.report({'ERROR'}, 'Select a node tree')
            return {'CANCELLED'}

        if self.confirm and node_tree.nodes:
            def draw(self2, context):
                self2.layout.label("This will erase current node tree")
                self2.layout.operator_context = 'INVOKE_DEFAULT'
                self2.layout.operator(self.bl_idname, text='Confirm').confirm=False
            bpy.context.window_manager.popup_menu(draw, title="Are you sure?", icon='QUESTION')
            return {'FINISHED'}

        self.confirm=True

        if (self.filepath == ''):
            context.window_manager.fileselect_add(self)
            return {'RUNNING_MODAL'}

        return self.execute(context)

    def execute(self, context):
        s = open(self.filepath, 'r', encoding='utf-8').read()
        bpy.ops.node.select_all(action='SELECT')
        bpy.ops.node.delete()
        node_tree_from_py(context, s)
        bpy.ops.node.select_all(action='DESELECT')
        self.filepath = ''
        return {'FINISHED'}


def node_tree_from_py(context, py):
    """Experimental idea to convert an existing vtk-python-example to a
    node-network. It is not completed, do not use it.
    """
    space = context.space_data
    nodes = space.node_tree.nodes
    links = space.node_tree.links
    lines = py.split('\n')
    vtk_objs = {}
    linked = []  # [input,output]

    for line in lines:
        line = line.replace(' ', '')
        if not line.startswith('#'):
            if '#' in line:
                line = line.split('#', 1)[0]
            if '=vtk.' in line:
                a = line.split('=vtk.')
                type = a[1].replace('()', '').replace('vtk', 'VTK') + 'Type'
                if type in core.CLASSES:
                    vtk_objs[a[0]] = nodes.new(type)
                    linked.append(vtk_objs[a[0]])
                else:
                    log.error(a[1] + " can't be converted to node")
            elif '=' not in line and '.' in line:
                if '.SetInputConnection' in line:
                    n1 = line.split('.SetInputConnection')[0]
                    n2 = line.split('(', 1)[1][:-1]
                    if '.GetOutputPort()' in n2:
                        n2 = n2.replace('.GetOutputPort()', '')
                        if n2 in vtk_objs.keys() and n1 in vtk_objs.keys():
                            links.new(vtk_objs[n1].inputs[0], vtk_objs[n2].outputs[0])
                elif '.Set' in line:
                    if line.count('(') > 1:
                        log.error(line + ": I'm too stupid to handle more than 2 brackets")
                    else:
                        n1 = line.split('.Set')[0]
                        if n1 in vtk_objs.keys():
                            toSet = line.split('.Set')[1]

                            def set(objname, attr, val):
                                if objname in vtk_objs.keys():
                                    obj = vtk_objs[objname]
                                    if attr in obj.m_properties():
                                        setattr(obj, attr, val)
                                    else:
                                        log.error(obj.bl_idname + ' got no attributes ' + attr + ' in this addon')
                                else:
                                    log.error(objname + ', missing corresponding node')

                            if 'To' in toSet:
                                if toSet.count('To') > 1:
                                    log.error('"To" is not handled yet')
                                else:
                                    set(n1, 'e_' + toSet.split('To')[0],
                                        toSet.split('To')[1].replace('(', '').replace(')', ''))
                            elif 'On()' in toSet:
                                set(n1, 'm_' + toSet.split('On()')[0], True)
                            elif 'Off' in toSet:
                                set(n1, 'm_' + toSet.split('Off()')[0], False)
                            elif toSet.count('(') == 1 and toSet.split('(')[1].replace(')', '') != '':
                                try:
                                    set(n1, 'm_' + toSet.split('(')[0], eval(toSet.split('(')[1].replace(')', '')))
                                except:
                                    log.error(toSet + ' argument not defined')
                            else:
                                log.error('This "Set" has not been interpreted: ' + line)
    for i in range(len(linked)):
        linked[i].location = (i * 300, 0)

    tb = nodes.new('BVTK_NT_ToBlender')
    tb.location = (len(linked) * 300, 0)
    links.new(tb.inputs[0], linked[len(linked) - 1].outputs[0])

# ---------------------------------------------------------------------------------
# Arrange tree operator
# ---------------------------------------------------------------------------------


def node_height(node):
    """ 'height' property of blender nodes seems not working: it's set to the same value for all nodes,
    regardless of the real height. Since 'width' and 'dimensions' properties work, this method
    uses a proportion between real width and absolute x dimension to retrieve real height.
    """
    k = node.dimensions[0] / node.width
    return node.dimensions[1] / k


def outgoing(node, seen):
    """ Return the number of nodes before the given one on an horizontal line, without considering
    nodes in the analyzed list. Remember not to pass the list of analyzed nodes as a reference
    (unless you need to do it). Outgoing and ingoing methods are used in the arranger to define
    the horizontal units occupied by a subpart of node tree.
    """
    for out in node.outputs:
        for link in out.links:
            if link.to_node not in seen:
                seen.append(node)
                return outgoing(link.to_node, seen) + 1
    return 1


def ingoing(node, seen):
    """ Return the number of nodes next to the given one on an horizontal line, without considering
    nodes in the analyzed list. Remember not to pass the list of analyzed nodes as a reference
    (unless you need to do it). Outgoing and ingoing methods are used in the arranger to define
    the horizontal units occupied by a subpart of node tree.
    """
    for socket in node.inputs:
        for link in socket.links:
            if link.from_node not in seen:
                seen.append(node)
                return ingoing(link.from_node, seen) + 1
    return 1


def linked_nodes(node, array=None):
    """ Return all nodes (recursively) linked to the one given """
    if not array: array = [node]
    for socket in node.outputs:
        for link in socket.links:
            output = link.to_node
            if output not in array:
                array.append(output)
                linked_nodes(output, array)
    for socket in node.inputs:
        for link in socket.links:
            input = link.from_node
            if input not in array:
                array.insert(0, input)
                linked_nodes(input, array)
    return array


def outputs(node):
    """ Return all nodes going out from the one given, not recursively """
    out = []
    for socket in node.outputs:
        for link in socket.links:
            out.append(link.to_node)
    return out


def inputs(node):
    """ Return all nodes going in to the one given, not recursively """
    inp = []
    for socket in node.inputs:
        for link in socket.links:
            inp.append(link.from_node)
    return inp


def collapse_tree(node, x_spacing, w=0, analyzed=None):
    """ Collapse nodes horizontally starting from the one given.
    Not always useful.
    """
    if not analyzed: analyzed = []
    node.location[0] = w
    analyzed.append(node)
    for socket in node.outputs:
        for link in socket.links:
            output = link.to_node
            if output not in analyzed:
                collapse_tree(output, x_spacing, w+node.width+x_spacing, analyzed)
    for socket in node.inputs:
        for link in socket.links:
            input = link.from_node
            if input not in analyzed:
                collapse_tree(input, x_spacing, w-input.width-x_spacing, analyzed)


class NodesColumn:
    """ Used by the node table as a node array to store
     current height and max width
     """
    def __init__(self, y_spacing, first_node=None):
        self.nodes = []
        self.y_spacing = y_spacing
        self.max_w = 0
        self.height = 0
        if first_node:
            self.nodes.append(first_node)
            self.max_w = first_node.width
            self.height = node_height(first_node) + y_spacing

    def add_node(self, node):
        self.nodes.append(node)
        self.height += node_height(node) + self.y_spacing
        if node.width > self.max_w:
            self.max_w = node.width


class NodesTable:
    """A class used to manage the arrangement of the tree."""
    def __init__(self, favorites=None, x_spacing=0, y_spacing=0, start=None,):
        self.columns = {}
        self.analyzed = []
        self.favorites = favorites if favorites else []
        self.x_spacing = x_spacing
        self.y_spacing = y_spacing
        if start:
            self.analyze(start, y_spacing)

    def analyze(self, node, column=0, x=True):
        self.analyzed.append(node)
        n_after = outgoing(node, self.analyzed[:])  # nodes after
        max_h = 0

        for j in range(n_after):
            i = column + j
            if i in self.columns:
                col = self.columns[i]
                if col.height > max_h:
                    max_h = col.height
        for j in range(n_after):
            i = column + j
            if i not in self.columns:
                self.columns[i] = NodesColumn(self.y_spacing)
            col = self.columns[i]
            col.height = max_h

        node.location[1] = -max_h

        if column not in self.columns:
            self.columns[column] = NodesColumn(self.y_spacing, node)
        else:
            self.columns[column].add_node(node)

        n_before = ingoing(node, self.analyzed[:])  # nodes before
        max_h = 0

        for j in range(n_before):
            if j != 0:
                i = column - j
                if i in self.columns:
                    col = self.columns[i]
                    if col.height > max_h:
                        max_h = col.height
        for j in range(n_before):
            if j != 0:
                i = column - j
                if i not in self.columns:
                    self.columns[i] = NodesColumn(self.y_spacing)
                col = self.columns[i]
                col.height = max_h

        out = outputs(node)
        inp = inputs(node)
        for n in self.favorites:
            if n not in self.analyzed:
                if n in out:
                    self.analyze(n, column + 1, False)
                elif n in inp:
                    self.analyze(n, column - 1, False)
        for n in out:
            if n not in self.analyzed:
                self.analyze(n, column + 1, False)
        for n in inp:
            if n not in self.analyzed:
                self.analyze(n, column - 1, False)

        if x:
            spacing = 0
            for i in sorted(self.columns):
                column = self.columns[i]
                for node in column.nodes:
                    node.location[0] = spacing + self.x_spacing
                spacing += column.max_w + self.x_spacing


class BVTK_OT_ArrangeTree(bpy.types.Operator):

    bl_idname = "bvtk.arrange_tree"
    bl_label = "Arrange Tree"

    def execute(self, context):
        tree = context.space_data.node_tree
        if tree.nodes:
            node_blocks = [linked_nodes(tree.nodes[0])]
            for node in tree.nodes:
                flag = True
                for block in node_blocks:
                    if node in block:
                        flag = False
                if flag:
                    node_blocks.append(linked_nodes(node))
            table = NodesTable(context.selected_nodes, context.scene.bvtk_arrange_x_spacing,
                               context.scene.bvtk_arrange_y_spacing)
            not_analyzed = []
            for block in node_blocks:
                start = None
                for node in context.selected_nodes:
                    if node in block:
                        start = node
                if start:
                    table.analyze(start)
                else:
                    not_analyzed.append(block)
            for block in not_analyzed:
                table.analyze(block[0])
            if context.scene.bvtk_arrange_collapse_x:
                for block in node_blocks:
                    collapse_tree(block[0], context.scene.bvtk_arrange_x_spacing)

        return {'FINISHED'}


core.add_ui_class(BVTK_OT_ArrangeTree)
