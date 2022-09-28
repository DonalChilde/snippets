####################################################
#                                                  #
#    src/snippets/collection/optional_object.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T10:23:47-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

"""optional_object is a convenience method for initializing mutable default arguments."""

from typing import Callable, TypeVar, Union

T = TypeVar("T")


def optional_object(
    argument: Union[None, T], object_factory: Callable[..., T], *args, **kwargs
) -> T:
    """
    A convenience method for initializing mutable default arguments.

    Meant to be used when solving the problem of passing an optional object where
    the desired behavior is a new object if None is passed. The problems with this
    are better explained here:
    https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments

    The standard solution is to use Optional[List] = None, check for None in your code,
    and initialize a new mutable as needed. `optional_object` saves a few line of code.

    Example:

    .. code:: python

        class SomeObject:
            data_1: int
            data_2: str


        class MyClass:
            def __init__(
                self,
                plain_arg: int,
                with_data: Optional[List[str]] = None,
                new_dict: Optional[Dict[str, int]] = None,
                my_class: Optional[SomeObject] = None,
            ):
                default_some_object = {"data_1": 1, "data_2": "two"}
                self.plain_arg = plain_arg
                self.with_data: List[str] = optional_object(with_data, list, ["a", "b", "c"])
                self.new_dict: Dict[str, int] = optional_object(new_dict, dict)
                self.my_class: SomeObject = optional_object(
                    my_class, SomeObject, **default_some_object
                )

    Args:
        argument: An argument that is an object that may be None.
        object_factory: Factory function used to create the object.
        `*args`: Optional arguments passed to factory function.
        `**kwargs`: Optional keyword arguments passed to factory function.

    Returns:
        The initialized object.
    """

    if argument is None:
        return object_factory(*args, **kwargs)
    return argument
