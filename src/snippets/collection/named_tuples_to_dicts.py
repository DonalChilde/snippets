####################################################
#                                                  #
#  src/snippets/collection/named_tuples_to_dicts.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-10-18T09:38:43-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

import logging
from typing import Any, Collection, Dict, List

logger = logging.getLogger(__name__)


class NamedTuplesToDicts:
    """
    Make an iterator that produces Dicts from the named tuples in a collection.

    Does not convert named tuples inside each item in the collection.

    Tracks the number of failed conversions in self.fail_count

    Args:
        data_collection: The collection of named tuples.
        stop_on_error: Raise StopIteration if there is an
            error converting to a dict.
        save_failed: Save a copy of the failed item in self.failed

    Yields:
         Dicts made from the items in the collection.

    """

    def __init__(
        self,
        data_collection: Collection,
        stop_on_error: bool = True,
        save_failed: bool = True,
    ) -> None:
        self.failed: List[Any] = []
        self.fail_count: int = 0
        self._it = iter(data_collection)
        self.stop_on_error = stop_on_error
        self.save_failed = save_failed

    def __iter__(self):
        return self

    def __next__(self) -> Dict:
        # while loop allows calling next til a successful conversion happens
        # this prevents returning None for conversion errors.
        while True:
            item = next(self._it)
            try:
                if isinstance(item, tuple):
                    if hasattr(item, "_asdict"):
                        item_dict = item._asdict()
                        return item_dict
                raise TypeError(f"item: {item} is not a named tuple.")
            except TypeError as exc:
                logger.error(
                    "Item %s from collection had an error: %s.",
                    item,
                    exc,
                    exc_info=True,
                )
                self.fail_count += 1
                if self.save_failed:
                    self.failed.append(item)
                if self.stop_on_error:
                    raise StopIteration from exc
