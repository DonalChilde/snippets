####################################################
#                                                  #
# src/snippets/collection/mutable_collection_caster.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-18T17:26:15-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
import logging
from typing import Any, Callable, Collection, Dict, TypeVar

from snippets.inspection.full_name import fullname

logger = logging.getLogger(__name__)
T = TypeVar("T", bound=Collection[Any])


class MutableCollectionCaster:
    """
    In a collection of collections, convert specific types to another type.

    This is useful for situations like writing a list of lists to csv, where
    the lists may contain items whose stinrg output is not the desired output for
    the csv. e.g. datetime.isoformat() is the desired output.

    Warning, this class will modify the collection. If that matters, use a copy of the
    collection.

    Example:
        from copy_generator import copy_generator
        list_1=[]
        data=[list_1,[],[]]
        copied_data = copy_generator(data)
        caster = MutableCollectionCaster({},copied_data)
        value = next(caster)
        assert value is not list_1

    Args:
        type_map: A lookup table of the types to convert, with the functions to
            convert them.
        collection: The collection of collections to convert.
    """

    def __init__(
        self, type_map: Dict[str, Callable[[Any], Any]], collection: Collection[T]
    ) -> None:
        self.type_map = type_map
        self._it = iter(collection)

    def __iter__(self):
        return self

    def __next__(self) -> T:
        item = next(self._it)
        return self._dispatch_item(item)

    def _dispatch_item(self, item: Collection):
        if isinstance(item, list):
            return self._cast_list(item)
        if isinstance(item, dict):
            return self._cast_dict(item)
        raise TypeError(f"Collection type was: {type(item)}, expected List or Dict.")

    def _cast_dict(self, item) -> T:
        for key, value in item.items():
            item[key] = self._transform_type(value, key=key)
        return item

    def _cast_list(self, item):
        for index, value in enumerate(item):
            item[index] = self._transform_type(value, index=index)
        return item

    def _transform_type(self, value: Any, *args, **kwargs) -> Any:
        _ = args, kwargs
        type_sig = self.type_signature(value)
        if type_sig in self.type_map:
            return self.type_map[type_sig](value)
        return value

    @classmethod
    def type_signature(cls, obj) -> str:
        return fullname(obj)
