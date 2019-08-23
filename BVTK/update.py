import time
from . core import *
from . utils import log, node_path

# -----------------------------------------------------------------------------
#  Functions and classes for running BVTK_Nodes internal function queue and
#  other updates
# -----------------------------------------------------------------------------


def set_color(node, color):
    """Set color of node to color"""
    node.color = color


def update_obj(node, vtkobj):
    """Update node corresponding to vtkobj by applying properties, inputs
    and call to VTK Update()
    """
    #time.sleep(1)
    node.apply_properties(vtkobj)
    node.apply_inputs(vtkobj)
    if hasattr(vtkobj, "Update"):
        vtkobj.Update()


def set_input_connection(vtkobj, i, input_obj):
    """Set input connection i of vtkobj to input object"""
    #time.sleep(1)
    vtkobj.SetInputConnection(i, input_obj)


def set_input_obj(vtkobj, name, input_obj):
    """Run a named Set function on vtkobj with argument input_obj"""
    #time.sleep(1)
    cmd = 'vtkobj.Set' + name + '( input_obj )'
    exec(cmd, globals(), locals())


def update(node, cb=None, x=True, queue=None):
    """Update the input functions of this node using the function queue.
    Sets color of node to reflect node run status. Finally updates this
    node and queues argument function cb() if argument x is True.
    """
    log.debug('on_update ' + node.name)
    if x:
        path = node_path(node)
        if path in BVTK_FunctionsQueue.queues:
            return
        queue = BVTK_FunctionsQueue(path)
        queue.add(log_check)
    ex_color = node.color.copy()  # Current color
    inputs_color = 0.84, 0.84, 0.73  # Input color
    execute_color = 0.85, 0.6, 0.2  # Execution color

    vtkobj = node.get_vtkobj()

    queue.add(set_color, node, inputs_color)
    for input_node in node.input_nodes():
        update(input_node, None, False, queue)
    queue.add(set_color, node, execute_color)
    if vtkobj:
        queue.add(update_obj, node, vtkobj)
    queue.add(set_color, node, ex_color)
    if x:
        queue.add(set_color, node, execute_color)
        queue.add(log_show)
        if cb:
            queue.add(cb)
        queue.add(set_color, node, ex_color)
        bpy.ops.bvtk.function_queue(node_path=node_path(node))


def no_queue_update(node, cb, x=True):
    """Force the update of all the input connections of this node,
    bypassing the functions queue. Does not update node colors.
    Finally updates this node by calling argument cb() if argument x
    is True, and VTK Update function otherwise.
    """
    log.debug('on_update ' + node.name)
    vtkobj = node.get_vtkobj()
    for input_node in node.input_nodes():
        no_queue_update(input_node, None, False)
    if x and cb:
        cb()
    else:
        if vtkobj:
            node.apply_properties(vtkobj)
            node.apply_inputs(vtkobj)
            if hasattr(vtkobj, "Update"):
                vtkobj.Update()


# -----------------------------------------------------------------------------
#  function queue
# -----------------------------------------------------------------------------


class BVTK_FunctionsQueue:
    """Class for Functions Queue. Used for running a queue system for
    BVTK_Nodes functions.
    """
    queues = {}  # node_path -> functions queue

    def __init__(self, node_path):
        self.queues[node_path] = self
        self.node_path = node_path
        self.functions = []
        self.executed = []
        self.i = 0

    def add(self, f, *args):
        self.functions.append((f, (a for a in args)))

    def next_function(self):
        i = self.i
        if i >= len(self.functions):
            self.queues.pop(self.node_path)
            return
        f = self.functions[i]
        if i not in self.executed:
            try:
                f[0](*f[1])
            except Exception as e:
                log.critical("function index: {}, function {}, raised exception: {}".format(i, f[0], e))
                import traceback
                log.debug(traceback.format_exc())
            self.executed.append(i)
            self.i += 1


class BVTK_OT_FunctionQueue(bpy.types.Operator):
    """Operator to call a function in functions queue.
    Calls are spaced (separated in time) by 1/100 s.
    """
    bl_idname = "bvtk.function_queue"
    bl_label = "Run a VTK function in queue"
    node_path = bpy.props.StringProperty()
    _timer = None

    def modal(self, context, event):
        if event.type == 'TIMER':
            if self.node_path in BVTK_FunctionsQueue.queues:
                queue = BVTK_FunctionsQueue.queues[self.node_path]
                queue.next_function()
            else:
                self.cancel(context)
                return {'CANCELLED'}
        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.01, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)


# -----------------------------------------------------------------------------
# Vtk logs
# -----------------------------------------------------------------------------


out = vtk.vtkFileOutputWindow()
logfile = b_path.rsplit('/', 1)[0]+'/vtklog.txt'
open(logfile, 'w').write('')
out.SetFileName(logfile)
vtk.vtkOutputWindow.SetInstance(out)

last_log = ''  # Current log file contents


def log_check():
    """Saves current log file contents. This function is to be called
    before executing more code that could generate errors, so that
    only latest error messages can be shown to user
    """
    global last_log
    last_log = open(logfile, 'r').read()


def log_show():
    """Shows log text of only latest operation"""
    logs = open(logfile, 'r').read()
    logs = logs.replace(last_log, '', 1)  # Remove old log text
    if logs:
        def draw(self, context):
            layout = self.layout
            for line in logs.split('\n'):
                if line:
                    row = layout.row()
                    row.label(text=line)

        bpy.context.window_manager.popup_menu(draw, 'vtk:', 'INFO')


add_ui_class(BVTK_OT_FunctionQueue)
