####################################################
#                                                  #
#   src/snippets/collection/iterable_to_dict.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T14:49:46-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Any, Callable, Dict, Iterable, List, Optional, TypeVar

T = TypeVar("T")


def iterable_to_dict(
    data: Iterable[T],
    key_getter: Callable[[T], Any],
    cast_key: Optional[Callable] = str,
) -> Dict[Any, T]:
    """
    Convert an iterable to a dict, using keys from the iterable values.

    itemgetter and attrgetter can be used for key_getter.
    dict comprehensions can also do this.

    Example:
        key_getter = itemgetter(1)
        data = [[2,3],[3,4],[5,6]]
        new_dict = iterable_to_dict(data,key_getter)
        print(new_dict)
        # new_dict = {"3":[2,3], "4":[3,4],"5":[5,6]}
        # dict comprehension method
        key_getter = itemgetter(1)
        new_dict = {str(key_getter(x)):x for x in data}

    Args:
        data: The iterable.
        key_getter: A function which, when called, returns the value
            to be used as the dict key.
        cast_key: Function called on the prospective key to ensure it can be used as
            a dict key. Defaults to str.

    Returns:
        The dict of the iterable.
    """
    result: Dict[Any, T] = {}
    for item in data:
        key_field_value = key_getter(item)
        if cast_key is not None:
            key_field_value = cast_key(key_field_value)
        result[key_field_value] = item
    return result


def iterable_to_dict_of_lists(
    data: Iterable[T],
    key_getter: Callable,
    cast_key: Optional[Callable] = str,
) -> Dict[Any, List[T]]:
    """
    Convert an iterable to a dict, using keys from the iterable values.

    Appends values to a list, key:List[T]
    itemgetter and attrgetter can be used for key_getter.
    dict comprehensions can duplicate much of this, but not
    preserving multiple values, afaik

    Example:
        key_getter = itemgetter(1)
        data = [[2,3],[3,4],[5,6],[5,6]]
        new_dict = iterable_to_dict_of_lists(data,key_getter)
        print(new_dict)
        # new_dict = {"3":[[2,3]], "4":[[3,4]],"5":[[5,6],[5,6]]}

    Args:
        data: The iterable.
        key_getter: A function which, when called, returns the value
            to be used as the dict key.
        cast_key: Function called on the prospective key to ensure it can be used as
            a dict key. Defaults to str.

    Returns:
        The dict of the iterable.
    """

    result: Dict[Any, List[T]] = {}
    for item in data:
        key_field_value = key_getter(item)
        if cast_key is not None:
            key_field_value = cast_key(key_field_value)
        # force all values to be contained in a list
        indexed_field: List = result.get(key_field_value, [])
        indexed_field.append(item)
        result[key_field_value] = indexed_field
    return result


# def index_objects(
#     data: Iterable[T],
#     key_field: Union[str, int],
#     use_itemgetter: bool = True,
#     cast_index: Callable = cast_str,
#     preserve_multiple: bool = False,
# ) -> Dict[Any, Union[T, List[T]]]:
#     """
#     Index an iterable of objects based on key_field.

#     [extended_summary]

#     :param data: [description]
#     :param key_field: [description]
#     :param use_itemgetter: [description], defaults to True
#     :param cast_index: [description], defaults to cast_str
#     :param preserve_multiple: [description], defaults to False
#     :return: [description]
#     """

#     if use_itemgetter:
#         indexer = itemgetter(key_field)
#     else:
#         indexer = attrgetter(key_field)  # type: ignore
#     result: Dict[Any, Union[T, List[T]]] = {}
#     for item in data:
#         key_field_value = indexer(item)
#         if cast_index is not None:
#             key_field_value = cast_index(key_field_value)
#         if preserve_multiple:
#             indexed_field = result.get(key_field_value, [])
#             indexed_field.append(item)  # type: ignore
#             result[key_field_value] = indexed_field
#         else:
#             result[key_field_value] = item
#     return result
