def fullname(o):
    """
    Get the fully qualified class name of an object.
    https://stackoverflow.com/questions/2020014/get-fully-qualified-class-name-of-an-object-in-python/70693158#70693158
    https://stackoverflow.com/a/70693158/105844
    _summary_

    _extended_summary_

    Args:
        o: _description_

    Returns:
        _description_
    """
    # TODO what if o is int?
    try:
        # if o is a class or function, get module directly
        module = o.__module__
    except AttributeError:
        # then get module from o's class
        module = o.__class__.__module__
    try:
        # if o is a class or function, get name directly
        name = o.__qualname__
    except AttributeError:
        # then get o's class name
        name = o.__class__.__qualname__
    # if o is a method of builtin class, then module will be None
    if module == "builtins" or module is None:
        return name
    return module + "." + name
