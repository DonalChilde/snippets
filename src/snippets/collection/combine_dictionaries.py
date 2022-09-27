####################################################
#                                                  #
#   src/snippets/collection/combine_dictionaries.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2022-09-27T15:01:01-07:00            #
# Last Modified: _iso_date_         #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
from typing import Dict, Sequence


def combine_dictionaries(dicts: Sequence[Dict], use_first_dict: bool = False) -> Dict:
    """
    Convenience function to combine a Sequence of dictionaries.

    Duplicate keys will be overwritten by later values. If use_first_dict is False,
    returns a new dict with the combined key:values. if use_first_dict is True,
    the first dict in the sequence will be used to hold the combined values.

    Args:
        dicts: A sequence of dicts to be combined
        use_first_dict: If True, the first dict is used to hold the combined key:values

    Returns:
        A dict with the combined key:values
    """

    combined_dict: Dict = {}
    if dicts is not None:
        for index, item in enumerate(dicts):
            if use_first_dict and index == 0:
                combined_dict = item
                continue
            combined_dict.update(item)
    return combined_dict
