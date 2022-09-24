"""
Created on Oct 30, 2017

@author: croaker
"""
import pprint


def makeRepr(classObj, instance=None, customFields=None):
    """Code writing helper function that will generate a __repr__ function that can be copy/pasted into a class definition.

    Args:
        classObj (class):
        instance (class):
        customFields (string):

    Returns:
        None:

    Always call the __repr__ function afterwards to ensure expected output.
    ie. print(foo)

    def __repr__(self):
        msg = "<Foo(var1 = {}, var2 = {})>"
        attributes = [self.var1, self.var2]
        return msg.format(*attributes)
    """
    if isinstance(instance, classObj):
        className = instance.__class__.__name__
    else:
        className = classObj.__name__

    print("Generating a __repr__ function for: ", className, "\n")
    print("\tClass Type: " + classObj.__name__, "has the following fields:")
    print("\t" + " ".join(classObj.__dict__.keys()), "\n")
    if instance:
        print(
            "\tInstance of: " + instance.__class__.__name__, "has the following fields:"
        )
        print("\t" + " ".join(instance.__dict__.keys()), "\n")
    else:
        print("\tInstance of: Instance not provided.\n")

    if customFields:
        print("\t" + "These fields were provided to makeRepr:")
        print("\t" + customFields, "\n")
    else:
        print("\t" + "These fields were provided to makeRepr: None\n")
    print(
        "Edit the list of fields, and rerun makeRepr with the new list if necessary.\n\n"
    )

    print("repr with class type:\n")
    classResult = buildRepr(classObj.__name__, " ".join(classObj.__dict__.keys()))
    print(classResult, "\n\n")

    if isinstance(instance, classObj):
        instanceResult = buildRepr(
            instance.__class__.__name__, " ".join(instance.__dict__.keys())
        )
    else:
        instanceResult = "\t-----Instance not provided."
    print("repr with instance of class:\n")
    print(instanceResult, "\n\n")

    if customFields:
        customResult = buildRepr(classObj.__name__, customFields)
    else:
        customResult = "\t-----Custom fields not provided"
    print("repr with custom fields and class name:\n")
    print(customResult, "\n\n")

    print("Current __repr__")
    print("Class Object: ", classObj)
    if instance:
        print("Instance: ", instance.__repr__())
    else:
        print("Instance: ", "None")


def buildRepr(typeName, fields):
    funcDefLine = "def __repr__(self):"
    msgLineBase = '    msg = "<{typename}({attribute})>"'
    attributeListLineBase = "    attributes = [{attributeList}]"
    returnLine = "    return msg.format(*attributes)"
    x = ["self." + x for x in fields.split()]
    xResult = ", ".join(x)
    y = [x + " = {}" for x in fields.split()]
    yResult = ", ".join(y)
    msgLine = msgLineBase.format(typename=typeName, attribute=yResult)
    attributeListLine = attributeListLineBase.format(attributeList=xResult)
    result = "{declaration}\n{message}\n{attributes}\n{returnLine}".format(
        declaration=funcDefLine,
        message=msgLine,
        attributes=attributeListLine,
        returnLine=returnLine,
    )
    return result


#     def _print_def__repr__(classObject, attributeList = None):
#         """
#         Code writing helper function that will generate a
#         __repr__ function that can be copy/pasted into a class definition.
#
#         Always call the __repr__ function afterwards to ensure expected output.
#         ie. print(foo)
#
#         Currently will generate incorrect output if var name in __init__ is different
#         from the name stored internally
#
#         def __repr__(self):
#             msg = "<Foo(var1 = {}, var2 = {})>"
#             attributes = [self.var1, self.var2]
#             return msg.format(*attributes)
#         """
#
#         className = classObject.__class__.__name__
#         if not attributeList:
#             attributeList = " ".join(classObject.__dict__.keys())
#
#         print('Generating a __repr__ function for: ', className,"\n")
#         print("\t"+className, "Has the following fields:")
#         print("\t"+" ".join(classObject.__dict__.keys()),"\n")
#         print("\t"+"These fields were provided to printRepr:")
#         print("\t"+attributeList,"\n")
#         print("\t"+"Edit the list of fields, and rerun printRepr with the new list if necessary.\n\n")
#
#         funcDefLine = "def __repr__(self):"
#         msgLineBase  = '    msg = "<{typename}({attribute})>"'
#         attributeListLineBase = '    attributes = [{attributeList}]'
#         returnLine = '    return msg.format(*attributes)'
#         x = ['self.' + x for x in attributeList.split()]
#         xResult = ", ".join(x)
#         y = [x + ' = {}' for x in attributeList.split()]
#         yResult = ', '.join(y)
#         msgLine = msgLineBase.format(typename = className, attribute = yResult)
#         attributeListLine = attributeListLineBase.format(attributeList = xResult)
#         result = "{declaration}\n{message}\n{attributes}\n{returnLine}".format(declaration = funcDefLine,
#                                                                            message = msgLine,
#                                                                            attributes = attributeListLine,
#                                                                            returnLine =returnLine )
#         print(result,"\n\n")


def prettyPrintData(data):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)
