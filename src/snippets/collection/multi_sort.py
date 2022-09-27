####################################################
#                                                  #
#          src/snippets/collection/multi_sort.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T13:37:23-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

"""
A method for sorting collections of complex objects.
"""
from operator import attrgetter, itemgetter
from typing import Callable, Iterable, List, Sequence, TypeVar

T = TypeVar("T")


class SortInstruction:
    """Base class used to define a sort instruction.

    Subclasses should provide a sort_on() method that returns
    a function which, when called, will return the sort key to be used
    to sort an item.

    Args:
        descending: Sort descending or ascending. Defaults to False (ascending).
    """

    def __init__(self, descending: bool = False) -> None:
        self.descending = descending

    def sort_on(self) -> Callable:
        """Returns a function that when called, returns the sort key for an item."""
        raise NotImplementedError


class SortInstructionItemgetter(SortInstruction):
    """
    SortInstruction for objects that support __get_item__

    Use this for Lists, Dicts, Tuples, etc.

    Args:
        sort_key: index of the field to be used as the sort key.
        descending: Sort descending or ascending. Defaults to False (ascending).
    """

    def __init__(self, sort_key: int, descending: bool = False) -> None:
        super().__init__(descending)
        self.sort_key = sort_key

    def sort_on(self) -> Callable:
        return itemgetter(self.sort_key)


class SortInstructionAttrgetter(SortInstruction):
    """SortInstruction for objects that support __get_attribute__

    Use this for Classes.

    Args:
        sort_key: name of the attribute to be used as the sort key.
        descending: Sort descending or ascending. Defaults to False (ascending).
    """

    def __init__(self, sort_key: str, descending: bool = False) -> None:
        super().__init__(descending)
        self.sort_key = sort_key

    def sort_on(self) -> Callable:
        return attrgetter(self.sort_key)


def sort_in_place(
    sortable_collection: List[T],
    instructions: Sequence[SortInstruction],
):
    """
    Sort a list of objects in place, e.g List[List], or List[Foo].

    Following the list of instructions given, sort a List in place.
    Arbitrary List item types are supported, so long as there is a
    SortInstruction that supports them.

    Args:
        sortable_collection: A mutable collection with a sort function e.g. List.
        instructions: A list of sort instructions that define the
            sort key and sort order.

    Raises:
        AttributeError: Data must be a mutable type with a sort function, e.g. List

    reference:
    https://docs.python.org/3/howto/sorting.html#ascending-and-descending
    """
    if not hasattr(sortable_collection, "sort"):
        raise AttributeError(
            "Data must be a mutable type with a sort function, e.g. List"
        )
    for instruction in reversed(instructions):
        sortable_collection.sort(
            key=instruction.sort_on(), reverse=instruction.descending
        )


def sort_to_new_list(
    sortable_collection: Iterable[T],
    instructions: Sequence[SortInstruction],
) -> List[T]:
    """
    Sort an iterable to a new list

    Following the list of instructions given, sort an iterable.
    Arbitrary iterable item types are supported, so long as there is a
    SortInstruction that supports them.

    Args:
        sortable_collection: An iterable of objects.
        instructions: A list of sort instructions that define the
            sort key and sort order.

    Returns:
        A new list of sorted objects.

    reference:
    https://docs.python.org/3/howto/sorting.html#ascending-and-descending
    """

    for index, instruction in enumerate(reversed(instructions)):
        # Make a new list on the first sort.
        if index == 0:
            sorted_list = sorted(
                sortable_collection,
                key=instruction.sort_on(),
                reverse=instruction.descending,
            )
            continue
        # Do the rest of the sorts in place
        sorted_list.sort(key=instruction.sort_on(), reverse=instruction.descending)
    return sorted_list
