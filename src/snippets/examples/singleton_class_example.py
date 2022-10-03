class SingletonClass(object):
    """
    Dont use hasattr?
    https://stackoverflow.com/a/11517201/105844
    """

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance


class Singleton(object):
    """https://www.python.org/download/releases/2.2/descrintro/#__new__"""

    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        pass
