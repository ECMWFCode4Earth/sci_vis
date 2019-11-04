# <pep8 compliant>
# ---------------------------------------------------------------------------------
#   utils/register.py
#
#   Simplify the registration process for all the classes. The other modules
#   should refer to this one to register a class. The functions performing
#   the actual registration are called by BVTK/__init__.py.
# ---------------------------------------------------------------------------------


from . __init__ import log
import bpy
from nodeitems_utils import NodeItem
import bpy.utils.previews
import nodeitems_utils


# ---------------------------------------------------------------------------------
#   Regular classes
# ---------------------------------------------------------------------------------
_classes = []  # Classes to be registered
# The following dictionary is used to allow
# class overriding
_key_classes = {}
_handlers = []  # Handlers to be registered
# List of functions to perform before registering.
# Each function is stored in a tuple together with
# the corresponding args and kwargs.
_before_registering = []


def add_class(custom_class, key=""):
    """Store a class to be registered."""
    if key:
        # If a key is provided, class is stored
        # in the override dictionary.
        _key_classes[key] = custom_class
        return

    if custom_class not in _classes:
        _classes.append(custom_class)


def add_handler(handler_list, custom_handler):
    """Store a handler to be registered."""
    _handlers.append((handler_list, custom_handler))


def before_registering(callback_function, *args, **kwargs):
    """Store a function that will be called before the
    class registering starts."""
    _before_registering.append((
        callback_function,
        args,
        kwargs
    ))


# ---------------------------------------------------------------------------------
#   Preview collections
# ---------------------------------------------------------------------------------
_p_collections = {}  # preview collections for custom icons (see colormap.py)


def retrieve_collection(key):
    if key not in _p_collections:
        _p_collections[key] = bpy.utils.previews.new()
    return _p_collections[key]


def get_collection(key):
    if key not in _p_collections:
        return None
    return _p_collections[key]


# ---------------------------------------------------------------------------------
#   Custom node categories registration
# ---------------------------------------------------------------------------------
_node_categories = {}
_categories_icons = {}
_category_class = None


def set_node_category(category):
    """Define the class to use to create categories.
    This method is called by nodes/core.py where all
    the node-related classes are defined."""
    global _category_class
    _category_class = category


def set_category_icon(category, icon):
    _categories_icons[category] = icon


def node_to_category(category, node):
    """Add a node to the specified category."""
    # menu_items = [NodeItem(x) for x in TYPENAMES]
    # node_categories.append(BVTK_NodeCategory("Custom", "Custom", items=menu_items))
    # _node_categories[identifier] = icon
    cat_list = _node_categories.setdefault(category, [])
    cat_list.append(node)


def custom_register_node_categories():
    """Custom registering of node categories to prevent node categories to
    be shown on the tool-shelf and add icons in the menu.
    """

    identifier = "BVTK_NODES"

    if not _category_class:
        return

    cat_list = []
    for cat, nodes in sorted(_node_categories.items()):
        cat_list.append(_category_class(cat, cat, items=[NodeItem(x.bl_idname) for x in nodes]))

    if identifier in nodeitems_utils._node_categories:
        raise KeyError("Node categories list '%s' already registered"
                       % identifier)

    def draw_node_item(self, context):
        layout = self.layout
        col = layout.column()
        for item in self.category.items(context):
            item.draw(item, col, context)

    def layout_menu(layout, cat_identifier):
        icon = "NONE" if cat_identifier not in _categories_icons \
            else _categories_icons[cat_identifier]
        layout.menu("NODE_MT_category_%s" % cat_identifier, icon=icon)

    def draw_add_menu(self, context):
        layout = self.layout
        layout.separator()

        for cat in cat_list:
            if cat.poll(context):
                if cat.identifier in _categories_icons:
                    layout_menu(layout, cat.identifier)

        layout.separator()

        for cat in cat_list:
            if cat.poll(context):
                if cat.identifier not in _categories_icons:
                    layout_menu(layout, cat.identifier)

    menu_types = []
    for cat in cat_list:
        menu_type = type(
            "NODE_MT_category_" + cat.identifier, (bpy.types.Menu,), {
                "bl_space_type": 'NODE_EDITOR',
                "bl_label": cat.name,
                "category": cat,
                "poll": cat.poll,
                "draw": draw_node_item,
            })
        menu_types.append(menu_type)
        bpy.utils.register_class(menu_type)

    nodeitems_utils._node_categories[identifier] = \
        (cat_list, draw_add_menu, menu_types, [])


# ---------------------------------------------------------------------------------
#   Register/unregister functions
# ---------------------------------------------------------------------------------


def register():
    """Register function. node_classes and node_categories are defined in core.py and
    filled in all the gen_VTK*.py and VTK*.py files
    """

    for callback, args, kwargs in _before_registering:
        callback(*args, **kwargs)

    for handler_list, handler in _handlers:
        handler_list.append(handler)

    log.debug("Registering {} classes.".format(len(_classes)))

    for c in _classes:
        try:
            bpy.utils.register_class(c)
        except Exception as e:
            log.critical('Error registering: {} , exception: {}.'.format(c, e))

    log.debug("Registering {} key classes.".format(len(_key_classes)))

    for c in _key_classes.values():
        try:
            bpy.utils.register_class(c)
        except Exception as e:
            log.critical('Error registering: {} , exception: {}.'.format(c, e))

    custom_register_node_categories()


def unregister():
    nodeitems_utils.unregister_node_categories("BVTK_NODES")
    for c in reversed(_classes):
        bpy.utils.unregister_class(c)

    for p_c in _p_collections.values():
        bpy.utils.previews.remove(p_c)
    _p_collections.clear()

    for handler_list, handler in _handlers:
        handler_list.remove(handler)
