import os.path
import sqlite3
from inspector import *


# -------------------------------------
# sqlite3
# -------------------------------------
filename = "VTKClasses.sqlite"
if os.path.exists(filename):
    os.remove(filename)

conn = sqlite3.connect(filename)
cursor = conn.cursor()


def run_commit_query(query, param=()):
    for statement in query.split(";"):
        if statement.strip():
            cursor.execute(statement, param)
            conn.commit()


def run_query(query, param=()):
    for statement in query.split(";"):
        if statement.strip():
            cursor.execute(statement, param)


# -------------------------------------
# DB population
# -------------------------------------
query = """
CREATE TABLE VTKClassGroups(
    VTKClassGroupID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100)
); 
CREATE TABLE VTKClasses(
    VTKClassID INTEGER PRIMARY KEY AUTOINCREMENT,
    VTKClassGroupFK INT,
    OutPortsNumber INT,
    InPortsNumber INT,
    Doc TEXT,
    Name VARCHAR(500),
    CONSTRAINT VTKClasses_VTKClassGroups_VTKClassGroupID_fk FOREIGN KEY (VTKClassGroupFK) 
    REFERENCES VTKClassGroups (VTKClassGroupID)
);
CREATE TABLE VTKMProps(
    VTKMPropID INTEGER PRIMARY KEY AUTOINCREMENT,
    VTKClassFK INT,
    Type VARCHAR(100),
    Name VARCHAR(500),
    NiceName VARCHAR(500),
    Description TEXT,
    DefaultValue VARCHAR(500),
    Size INT,
    CONSTRAINT VTKMProps_VTKClasses_VTKClassID_fk FOREIGN KEY (VTKClassFK) 
        REFERENCES VTKClasses (VTKClassID) ON DELETE CASCADE
);
CREATE TABLE VTKMPropEnumItems(
    VTKMPropFK INT,
    EnumItem VARCHAR(500),
    CONSTRAINT VTKMPropEnumItems_VTKMPropFK_EnumItem_pk PRIMARY KEY (VTKMPropFK, EnumItem),
    CONSTRAINT VTKMPropEnumItems_VTKMProps_VTKMPropID_fk FOREIGN KEY (VTKMPropFK) REFERENCES VTKMProps (VTKMPropID)
);
CREATE TABLE VTKVariables(
    VTKVariableID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(200),
    Type VARCHAR(100),
    Size INT
);
CREATE TABLE VTKMethodGroups(
    VTKMethodGroupID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100)
); 
CREATE TABLE VTKMethods(
    VTKMethodID INTEGER PRIMARY KEY AUTOINCREMENT,
    VTKMethodGroupFK INT,
    Fullname VARCHAR(500),
    Name VARCHAR(500),
    VTKReturnFK INT,
    StrReturn VARCHAR(500),
    StrArguments VARCHAR(500),
    CONSTRAINT VTKMethods_VTKVariables_VTKVariableID_fk FOREIGN KEY (VTKReturnFK) 
        REFERENCES VTKVariables (VTKVariableID)
    CONSTRAINT VTKMethods_VTKMethodGroups_VTKMethodGroupID_fk FOREIGN KEY (VTKMethodGroupFK) 
        REFERENCES VTKMethodGroups (VTKMethodGroupID)
);
CREATE TABLE VTKMethodArguments(
    VTKMethodFK INT,
    VTKVariableFK INT,
    ArgumentIndex INT,
    CONSTRAINT VTKMethodArguments_VTKMethodFK_VTKVariableFK_ArgumentIndex_pk 
        PRIMARY KEY (VTKMethodFK, VTKVariableFK, ArgumentIndex),
    CONSTRAINT VTKMethodArguments_VTKMethods_VTKMethodID_fk FOREIGN KEY (VTKMethodFK) 
        REFERENCES VTKMethods (VTKMethodID),
    CONSTRAINT VTKMethodArguments_VTKVariables_VTKVariableID_fk FOREIGN KEY (VTKVariableFK) 
        REFERENCES VTKVariables (VTKVariableID)
);
CREATE TABLE VTKClassMethods(
    VTKClassFK INT,
    VTKMethodFK INT,
    CONSTRAINT VTKClassMethods_VTKClassFK_VTKMethodFK_pk PRIMARY KEY (VTKClassFK, VTKMethodFK),
    CONSTRAINT VTKClassMethods_VTKClasses_VTKClassID_fk FOREIGN KEY (VTKClassFK) REFERENCES VTKClasses (VTKClassID),
    CONSTRAINT VTKClassMethods_VTKMethods_VTKMethodID_fk FOREIGN KEY (VTKMethodFK) REFERENCES VTKMethods (VTKMethodID)
);
CREATE TABLE VTKMethodDocs(
    VTKClassFK INT,
    VTKMethodFK INT,
    Doc TEXT,
    CONSTRAINT VTKMethodDocs_VTKClassFK_VTKMethodFK_pk PRIMARY KEY (VTKClassFK, VTKMethodFK),
    CONSTRAINT VTKMethodDocs_VTKClasses_VTKClassID_fk FOREIGN KEY (VTKClassFK) REFERENCES VTKClasses (VTKClassID),
    CONSTRAINT VTKMethodDocs_VTKMethods_VTKMethodID_fk FOREIGN KEY (VTKMethodFK) REFERENCES VTKMethods (VTKMethodID)
);
"""
run_commit_query(query)


# -------------------------------------
# add groups
# -------------------------------------
# Class groups
class_group_ids = {
    "Source": 0,
    "Reader": 0,
    "Writer": 0,
    "Mapper": 0,
    "Sink": 0,
    "Filter1": 0,
    "Filter2": 0,
    "Filter": 0,
    "Transform": 0,
    "ImplicitFunc": 0,
    "ParametricFunc": 0,
    "Integrator": 0,
    "Unknown": 0
}
for group_name in class_group_ids:
    query = "INSERT INTO VTKClassGroups(Name) VALUES (?)"
    run_query(query, (group_name,))
    class_group_ids[group_name] = cursor.lastrowid

# Method groups
method_group_ids = {
    "Getter": 0,
    "Setter": 0
}
for group_name in method_group_ids:
    query = "INSERT INTO VTKMethodGroups(Name) VALUES (?)"
    run_query(query, (group_name,))
    method_group_ids[group_name] = cursor.lastrowid


# -------------------------------------
# add variables
# -------------------------------------
variable_ids = {}
for variable in all_variables:
    query = "INSERT INTO VTKVariables(Name, Type, Size) VALUES (?,?,?)"
    run_query(query, (variable.name, variable.type, variable.size))
    variable_ids[hash(variable)] = cursor.lastrowid


# -------------------------------------
# add methods
# -------------------------------------
method_ids = {}
for method in all_methods:
    # Define method group
    group = "Getter"
    if method.name.startswith("Set"):
        group = "Setter"

    return_var = method.returns
    return_var_id = None if not return_var else variable_ids[hash(return_var)]
    query = """INSERT INTO VTKMethods(VTKMethodGroupFK, Fullname, Name, VTKReturnFK, StrReturn, StrArguments) 
               VALUES (?, ?, ?, ?, ?, ?)"""
    run_query(query, (method_group_ids[group], method.fullname,
                      method.name, return_var_id, method.str_returns,
                      method.str_arguments))
    method_id = cursor.lastrowid
    method_ids[hash(method)] = method_id

    # Add method arguments
    for i, argument in enumerate(method.arguments):
        var_id = variable_ids[hash(argument)]
        query = """INSERT INTO VTKMethodArguments(VTKMethodFK, VTKVariableFK, ArgumentIndex) 
                       VALUES (?, ?, ?)"""
        run_query(query, (method_id, var_id, i))


# -------------------------------------
# add classes
# -------------------------------------
class_ids = {}
for vtk_class in vtk_classes:
    # Define class group
    out_ports = vtk_class.out_ports
    in_ports = vtk_class.in_ports
    name = vtk_class.name
    real_class = vtk_class.vtk_class  # The actual class, not the inspector class
    group = "Filter"
    if issubclass(real_class, vtk.vtkAbstractTransform):
        group = "Transform"
    elif issubclass(real_class, vtk.vtkImplicitFunction):
        group = "ImplicitFunc"
    elif issubclass(real_class, vtk.vtkParametricFunction):
        group = "ParametricFunc"
    elif issubclass(real_class, vtk.vtkInitialValueProblemSolver):
        group = "Integrator"
    elif "Reader" in name:
        group = "Reader"
    elif "Writer" in name:
        group = "Writer"
    elif "Mapper" in name:
        group = "Mapper"
    elif in_ports == 0 and out_ports == 0:
        group = "Unknown"
    elif in_ports == 0 and out_ports == 1:
        group = "Source"
    elif in_ports == 1 and out_ports == 0:
        group = "Sink"
    elif in_ports == 1 and out_ports == 1:
        group = "Filter1"
    elif in_ports == 2 and out_ports == 1:
        group = "Filter2"

    # Add class
    if name in class_ids:
        log.post("Duplicate classes", name)
        continue
    query = """INSERT INTO VTKClasses(VTKClassGroupFK, OutPortsNumber, InPortsNumber, Doc, Name) 
            VALUES (?, ?, ?, ?, ?)"""
    run_query(query, (class_group_ids[group], out_ports, in_ports, vtk_class.doc, name))
    class_id = cursor.lastrowid
    class_ids[name] = class_id

    # Add methods (getters and setters)
    class_methods = vtk_class.getters
    class_methods.extend(vtk_class.setters)
    for method in class_methods:
        method_id = method_ids[hash(method)]
        query = """INSERT INTO VTKClassMethods(VTKClassFK, VTKMethodFK) VALUES (?, ?)"""
        run_query(query, (class_id, method_id))

    # Add mirror properties
    for m_prop in vtk_class.m_properties:
        query = """INSERT INTO VTKMProps(VTKClassFK, Type, Name, NiceName, Description, DefaultValue, Size) 
                   VALUES (?, ?, ?, ?, ?, ?, ?)"""
        default_value = repr(m_prop.default) if m_prop.default is not None else None
        run_query(query, (class_id, m_prop.type, m_prop.name, m_prop.nice_name, m_prop.description, default_value,
                          m_prop.size))
        m_prop_id = cursor.lastrowid

        # Add enum items
        for enum_item in m_prop.enum_items:
            query = """INSERT INTO VTKMPropEnumItems(VTKMPropFK, EnumItem) VALUES (?, ?)"""
            run_query(query, (m_prop_id, enum_item))

conn.commit()

print("Database generated: '{}'.".format(filename))
