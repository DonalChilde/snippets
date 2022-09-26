import logging
from itertools import chain
from typing import Callable, Iterator, TypeVar, Union

#### setting up logger ####
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

T = TypeVar("T")  # pylint: disable=invalid-name


def optional_object(
    argument: Union[None, T], object_factory: Callable[..., T], *args, **kwargs
) -> T:
    """
    A convenience method for initializing optional arguments.

    Meant to be used when solving the problem of passing an optional object where
    the desired behavior is a new object if None is passed. The problems with this
    are better explained here:
    https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments

    The standard solution is to use Optional[List] = None, check for None in your code,
    and initialize a new mutable as needed. `optional_object` saves a few line of code.

    For example:

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


def wrap_range(
    left_bound: int, right_bound: int, start_index: int, direction: int
) -> Iterator[int]:
    """Create a range of integer values that start somewhere between the beginning and end, wrapping around back to start.

    e.g. wrap_range(0,10,6,1) = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
         wrap_range(0,10,6,-1) = [6, 5, 4, 3, 2, 1, 0, 9, 8, 7]
         wrap_range(-2, 10, 6, -1) = [6, 5, 4, 3, 2, 1, 0, -1, -2, 9, 8, 7]

    note right_bound mimics the behavior of range(),
    where range(0,10) = [0,1,2,3,4,5,6,7,8,9]

    :param left_bound: lower boundry of number line
    :param right_bound: upper boundry of number line + 1
    :param start_index: starting value, must be  left_bound >= start_index < right_bound
    :param direction: a positive or negative integer, where positive integers increment
        to the right on the number line, and negative integers increment to the left.
    :raises ValueError: direction cannot be zero
    :raises ValueError: left_bound cannot be greater than right_bound
    :returns: Two range() generators chained by itertools.chain
    """
    logger.debug(
        "wrap_range(left_bound=%s, right_bound=%s, start_index=%s, direction=%s)",
        left_bound,
        right_bound,
        start_index,
        direction,
    )
    if direction == 0:
        raise ValueError("direction cannot be zero")
    if left_bound > right_bound:
        raise ValueError(
            f"left_bound {left_bound} is greater than right_bound {right_bound}"
        )
    range_generator = None
    if direction > 0:
        left_range = range(left_bound, start_index)
        right_range = range(start_index, right_bound)
        range_generator = chain(right_range, left_range)
    else:
        left_range = range(start_index, left_bound - 1, -1)
        right_range = range(right_bound - 1, start_index, -1)
        range_generator = chain(left_range, right_range)
    return range_generator


# TODO keep these as examples, suggest use more itertools
# def chunk(it, size):
#     """
#     https://stackoverflow.com/a/22045226
#     """
#     it = iter(it)
#     return iter(lambda: tuple(islice(it, size)), ())


# def chunk_pad(it, size, padval=None):
#     """
#     https://stackoverflow.com/a/22045226
#     """
#     it = chain(iter(it), repeat(padval))
#     return iter(lambda: tuple(islice(it, size)), (padval,) * size)


# def chunks(l, n):
#     """
#     https://stackoverflow.com/a/1751478
#     """
#     n = max(1, n)
#     return (l[i : i + n] for i in range(0, len(l), n))
