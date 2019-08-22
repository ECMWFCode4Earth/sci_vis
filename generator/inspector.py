import logger
from settings import *

# Create logs
log = logger.Log("logs/issues.txt")       # issues log
m_log = logger.Log("logs/methods.txt")    # methods log
v_log = logger.Log("logs/variables.txt")  # variables log

# Methods and variables are stored in the following dictionaries;
# the items are stored in a set, using hashes which are equal in
# different objects that can be considered equal.
all_methods = set()
all_variables = set()


# ----------------------------------------------------------------------------------------
# Functions
# ----------------------------------------------------------------------------------------


def clean_all(doc):
    return doc.replace('\n', '').replace(' ', '')


def clean(doc):
    doc = doc.replace('\n', ' ')
    while '  ' in doc:
        doc = doc.replace('  ', ' ')
    doc = doc.strip()
    return doc


def type_from_string(string):
    """Take a doc string and detect the variable type.
    Return one string in:
    > 'String'
    > 'Bool'
    > 'Float'
    > 'Int'
    > 'VTKObject'
    > 'StringVector'
    > 'BoolVector'
    > 'FloatVector'
    > 'IntVector'
    > 'VTKObject'
    """
    string = string.replace('(', '').replace(')', '')
    string = string.replace(']', '').replace('[', '')
    if ',' in string:
        arr = string.split(',')
        for s in arr:
            if s != arr[0]:
                return None
        return type_from_string(string.split(',')[0]) + 'Vector'
    else:
        if string == 'string' or string == 'char' or string == 'unicode':
            return 'String'
        elif string == 'bool':
            return 'Bool'
        elif string == 'float':
            return 'Float'
        elif string == 'int':
            return 'Int'
        elif string.startswith('vtk'):
            return 'VTKObject'
        log.post('Unrecognized variable types', string)
        return None


# ----------------------------------------------------------------------------------------
# Inspector classes
# ----------------------------------------------------------------------------------------


class VTKVariable:

    # c_doc looks like:
    # const int[2] name
    # p_doc is simpler:
    # (int, int)
    def __init__(self, p_doc, c_doc):
        self.fullname = p_doc   # Name of the variable as it was in the python doc
        self.name = ""          # Name of the variable
        self.type = None        # See 'type_from_string' for possible types
        self.size = 0           # Size of the array, if the property is a vector

        if c_doc:
            log.post("Variable names", p_doc + " " + c_doc)
            c_doc = c_doc.split('=')[0].split('[')[0]
            c_doc = c_doc.replace('const', '').replace('*', '').replace('&', '')
            c_doc = c_doc.strip()
            if ' ' in c_doc:
                self.name = c_doc.split(' ')[1]
        self.type = type_from_string(p_doc)

        if self.type and 'Vector' in self.type:
            self.size = self.vector_length(p_doc)

        # Adding variable to the log
        v_log.post(str(hash(self)),
                   "Name: " + str(self.name) + "\n" +
                   "Type: " + str(self.type) + "\n" +
                   "Size: " + str(self.size) + "\n"
                   )

        if self.check():
            all_variables.add(self)

    def compare_string(self):
        """Return a string representing the variable but without
        the first and the last parenthesis if it's
        a tuple or an array. Used to compare the variable with a
        setter arguments, it allows to find a match between
        '(float, float)' and 'float, float' ."""
        if (self.fullname.startswith("(") and self.fullname.endswith(")")) or\
           (self.fullname.startswith("[") and self.fullname.endswith("]")):
            return self.fullname[1:-1]
        return self.fullname

    def check(self):
        if self.type is None:
            return False
        return True

    def vector_length(self, p_doc):
        """Return the length of a vector variable, using the python documentation."""
        return len(p_doc.split(','))

    def is_obj(self):
        """Return true if the variable is a vtk object and not a basic type."""
        return self.type == 'VTKObject'

    def __str__(self):
        return "{} {} {}".format(self.type, self.name, self.size)

    def __eq__(self, other):
        return other and self.name == other.name and self.type == other.type and self.size == other.size

    def __hash__(self):
        return hash((self.name, self.type, self.size))


# ----------------------------------------------------------------------------------------


class VTKArguments:

    # We need both p_args string and c_args string
    # because c_args contains sometimes arg names.
    # If c_args are more or less than p_args then
    # c_args are ignored.
    def __init__(self, p_args, c_args, method):

        self.archive = []  # List of VTKVariable objects

        p_args = self.get_arguments(p_args)
        c_args = self.get_arguments(c_args.strip())
        c_args = self.remove_void(c_args)
        if len(c_args) != len(p_args):
            log.post('Number of arguments mismatch in c_args and p_args',
                     '{}\t{}\t{}'.format(c_args, p_args, method.fullname))
            c_args = [None for a in p_args]     # if p and c args don't correspond, c are ignored

        for i in range(len(p_args)):
            var = VTKVariable(p_args[i], c_args[i])
            self.archive.append(var)

    def get_arguments(self, string):
        """Take a string and return a list of separated
        arguments, as strings."""
        in_brackets = 0
        args = []
        i = 0
        for c in string:
            if c == "," and in_brackets == 0:
                i += 1
                continue
            elif c == "(" or c == '[':
                in_brackets += 1
            elif c == ")" or c == ']':
                in_brackets -= 1
            try:
                args[i] += c
            except:
                args.append(c)
        return args

    def remove_void(self, args):
        """Remove the single argument 'void', if present."""
        # Sometimes C arguments, instead of being empty, have a 'void' indication
        # inside the brackets. This is detected as an argument and must be deleted
        # or python arguments and C arguments won't match.
        if len(args) == 1:
            if args[0] == "void":
                return []
        return args

    def check(self):
        """Return true if all the arguments are significant, otherwise return false
        if some of them could't be recognized."""
        for v in self.archive:
            if not v.check():
                return False
        return True

    def __str__(self):
        s = ''
        for a in self.archive:
            s += str(a) + ', '
        return s

    def __iter__(self):
        return iter(self.archive)

    def __len__(self):
        return len(self.archive)


# ----------------------------------------------------------------------------------------


class VTKMethod:

    # The same method can have different documentations, depending on the
    # mother class; these descriptions are stored in this dictionary
    desc = {}

    # Method doc pattern:
    # V. (removed)
    # GetName(int) -> vtkObject
    # C++: returnedObject *GetName(int)
    def __init__(self, m_desc, m_doc, classname):

        self.fullname = None        # String        method name with brackets and arguments (ID)
        self.name = None            # String        just method name
        self.arguments = None       # VTKArguments  list of arguments
        self.returns = None         # VTKVariable   the return variable
        self.str_returns = None     # String        return variable as string
        self.str_arguments = None   # String        p_arguments (as in doc)

        c_doc = clean(m_doc.split('C++')[1])
        p_doc = clean_all(m_doc.split('C++')[0])

        self.fullname = p_doc
        self.name = p_doc.split('(', 1)[0]
        self.set_desc(classname, clean(m_desc))

        c_args = c_doc.split(self.name + '(', 1)[1].rsplit(')', 1)[0]
        self.str_arguments = p_doc.split('(', 1)[1].split('->')[0].rsplit(')', 1)[0]

        if '->' in p_doc:
            self.str_returns = p_doc.split('->')[1]
            self.returns = VTKVariable(self.str_returns, None)

        self.arguments = VTKArguments(self.str_arguments, c_args, self)

        # Adding method to the log
        m_log.post(self.fullname,
                   "Arguments: " + str(self.arguments)+"\n" +
                   "Returns: " + str(self.returns) + "\n" +
                   "Hash: " + str(hash(self)) + "\n"
                   )

        if self.check():
            all_methods.add(self)

    def check(self):
        """Return true if the method is significant, otherwise return false
        if some of the arguments or the return variable could't be recognized."""
        if self.arguments.check():
            if not self.returns:
                return True
            else:
                return self.returns.check()
        return False

    def set_desc(self, classname, desc):
        if not classname in self.desc:
            self.desc[classname] = {}
        self.desc[classname][self.fullname] = desc

    def get_desc(self, classname):
        return self.desc[classname][self.fullname]

    def __eq__(self, other):
        return other and self.fullname == other.fullname

    def __hash__(self):
        return hash(self.fullname)


# ----------------------------------------------------------------------------------------


class VTKMProperty:

    def __init__(self, setup_dict):
        self.type = ""              # String    See 'type_from_string' for possible types. May be 'Enum' too.
        self.name = ""              # String    Compact name of the property
        self.nice_name = ""         # String    Readable name for the user interface
        self.description = ""       # String    Documentation of getter or setter
        self.default = None         # ?         Default value of the property
        self.size = 0               # Int       Size of array for vector properties
        self.enum_items = []        # List      Items array for enum properties

        for key in setup_dict:
            setattr(self, key, setup_dict[key])

    def __eq__(self, other):
        return other and self.name == other.name


# ----------------------------------------------------------------------------------------


class VTKClass:

    # Init:
    # - Find all methods
    # - Find args of mirror methods (when Get[name]X returns A and Set[name]X takes A)
    #   and make them mirror properties
    def __init__(self, vtk_obj):

        self.vtk_obj = vtk_obj      # Object    inspected vtk object
        self.getters = []           # List      get methods
        self.setters = []           # List      set methods
        self.m_properties = []      # List      list of VTKMProperty
        self.out_ports = 0          # Int       number of output ports
        self.in_ports = 0           # Int       number of input ports
        self.doc = None             # String    documentation of the class
        self.vtk_class = None       # Class     inspected vtk class
        self.name = ""              # String    name of the inspected vtk class

        # -------------------------------------
        # Class attributes
        # -------------------------------------
        if hasattr(vtk_obj, "GetNumberOfInputPorts"):
            self.in_ports = vtk_obj.GetNumberOfInputPorts()
        if hasattr(vtk_obj, "GetNumberOfOutputPorts"):
            self.out_ports = vtk_obj.GetNumberOfOutputPorts()
        self.vtk_class = vtk_obj.__class__
        self.name = self.vtk_class.__name__[3:]
        self.doc = self.vtk_class.__doc__

        # -------------------------------------
        # fill getters and setters
        # -------------------------------------
        classname = self.name
        attributes = sorted([att for att in dir(vtk_obj) if att.startswith('Get') or att.startswith('Set')])
        for attribute in attributes:
            doc = getattr(vtk_obj, attribute).__doc__
            if not doc:
                log.post("No documentation", attribute)
            elif attribute not in banned_methods:
                doc = doc.split('\n\n')
                desc = doc[1]
                methods = doc[0][2:].split('V.')
                for m in methods:
                    if not m:
                        continue
                    m = VTKMethod(desc, m, classname)
                    if not m.check():  # returns false if one of the arguments hasn't been recognized
                        continue
                    elif attribute.startswith('Get'):
                        self.getters.append(m)
                    elif attribute.startswith('Set'):
                        self.setters.append(m)

        # -------------------------------------
        # find mirror blender properties
        # -------------------------------------
        for getter in self.getters:
            if len(getter.arguments) == 0:
                for setter in self.setters:
                    if getter.name[3:] == setter.name[3:]:
                        if getter.str_returns == setter.str_arguments or \
                           getter.returns.compare_string() == setter.str_arguments:

                            # here's something we can get and set
                            returns = getter.returns
                            if getter.name[3:] not in banned_props:
                                setup = dict()
                                setup['var_name'] = getter.name[3:]
                                setup['name'] = getter.name[3:]
                                setup['type'] = returns.type
                                setup['default'] = getattr(vtk_obj, getter.name)()
                                setup['size'] = returns.size

                                # search a valid method documentation
                                desc = setter.get_desc(classname)
                                if not desc:
                                    desc = getter.get_desc(classname)
                                setup['description'] = desc

                                # override automatic found characteristics of the blender property
                                # for special cases: enum and boolean
                                enum_names, d_e = self.enum_names(setter.name)
                                if enum_names:
                                    setup['type'] = 'Enum'
                                    setup['default'] = d_e
                                    setup['enum_items'] = enum_names
                                    setup['size'] = 0
                                if self.is_bool(getter.name):
                                    setup['type'] = 'Bool'

                                prop = VTKMProperty(setup)

                                if prop not in self.m_properties:
                                    self.m_properties.append(prop)

    def is_bool(self, base):
        """To call when getters and setters are initialized.
        Search setters for one that ends with [base]On and
        returns true if it exists.
        """
        for att in dir(self.vtk_obj):
            if att == base[3:]+'On':
                return True
        return False

    def enum_names(self, base):
        """To call when getters and setters are initialized.
        Search all setters that end with [base]To[...] and return
        a list of their names split after [base]To. These methods
        can be represented as enum properties.
        """
        getter = getattr(self.vtk_obj, 'Get' + base[3:])
        default = getter()
        default_string = None
        base += 'To'
        names = []
        for setter in self.setters:
            if base in setter.name and not setter.arguments:
                name = setter.name.split(base)[1]
                names.append(name)
                try:
                    getattr(self.vtk_obj, setter.name)()
                    if getter() == default:
                        default_string = name
                except:
                    log.post('Set..To.. needs arguments', setter.name)

        return names, default_string

    def __eq__(self, other):
        return other and self.name == other.name

    def __hash__(self):
        return hash(self.name)


# ----------------------------------------------------------------------------------------
# Inspect classes
# ----------------------------------------------------------------------------------------

vtk_classes = set()  # Set of VTKClass objects

for att in dir(vtk):

    if not att.startswith('vtk'):
        continue

    c = getattr(vtk, att)

    try:
        o = c()
    except:
        continue

    if c.__name__ in banned_class_names:
        continue

    flag = True
    for w_class in wanted_classes:
        if flag and issubclass(c, wanted_classes[w_class]):
            vtk_classes.add(VTKClass(o))
            flag = False

# Write logs
log.write()
m_log.write()
v_log.write()


print("Class inspection completed.")
