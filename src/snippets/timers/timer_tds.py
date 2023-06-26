####################################################
#                                                  #
#          src/snippets/timers/timer_tds.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-06-26T14:43:45-07:00            #
# Last Modified: 2023-06-26T21:44:09.214298+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################
import time
from typing import NoReturn, Optional


# https://towardsdatascience.com/battle-of-the-data-containers-which-python-typed-structure-is-the-best-6d28fde824e
class Timer:
    _counter_start: Optional[float] = None
    _counter_stop: Optional[float] = None

    def start(self) -> None:
        self._counter_start = time.perf_counter_ns()

    def stop(self) -> None:
        self._counter_stop = time.perf_counter_ns()

    @property
    def time(self) -> float:
        """Time in nano seconds (ns)."""
        self._valid_start_stop()
        return self._counter_stop - self._counter_start  # type: ignore

    def _valid_start_stop(self) -> Optional[NoReturn]:
        if self._counter_start is None:
            raise ValueError("Timer has not been started.")
        if self._counter_stop is None:
            raise ValueError("Timer has not been stopped.")
        return None
