import logging
from dataclasses import dataclass
from typing import Dict, List, Optional

import pytest

from snippets.collection.misc import wrap_range

#### setting up logger ####
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def test_wrap_range(caplog):
    # caplog.set_level(logging.DEBUG)
    range_gen = wrap_range(0, 10, 6, 1)
    as_list = list(range_gen)
    expected = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
    assert as_list == expected

    range_gen = wrap_range(0, 10, 6, -1)
    as_list = list(range_gen)
    expected = [6, 5, 4, 3, 2, 1, 0, 9, 8, 7]
    assert as_list == expected

    range_gen = wrap_range(-2, 10, 6, -1)
    as_list = list(range_gen)
    expected = [6, 5, 4, 3, 2, 1, 0, -1, -2, 9, 8, 7]
    assert as_list == expected

    range_gen = wrap_range(1, 8, 4, -1)
    as_list = list(range_gen)
    expected = [4, 3, 2, 1, 7, 6, 5]
    assert as_list == expected

    # zero in direction
    with pytest.raises(ValueError):
        range_gen = wrap_range(1, 8, 4, 0)
    # left bound greater than right bound
    with pytest.raises(ValueError):
        range_gen = wrap_range(8, 1, 4, 1)
