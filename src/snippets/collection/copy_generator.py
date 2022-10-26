####################################################
#                                                  #
#   src/snippets/collection/copy_generator.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-18T09:06:49-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

from copy import deepcopy
from typing import Any, Callable, Collection, Iterator, TypeVar

T = TypeVar("T", bound=Collection[Any])


def copy_generator(
    collection: Collection[T], copy: Callable[[T], T] | None = deepcopy
) -> Iterator[T]:
    """
    Make a generator that produces copies of the items in a collection.

    This is useful in cases where a collection may need to have its members changed
    without affecting the original collection. E.g. formatting output to a csv file
    when the default __str__ of an object is not the desired output. The output of this
    generator could be altered as desired.

    Args:
        collection: A collection of objects to be copied
        copy: The function used to copy the items in the collection.
            Defaults to deepcopy. None makes a generator, but does not change the items.

    Returns:
        A generator that produces the copied items from the collection
    """
    if copy is None:
        return (x for x in collection)
    return (copy(x) for x in collection)
