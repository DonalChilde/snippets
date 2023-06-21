####################################################
#                                                  #
#      src/snippets/timers/function_timer.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2023-06-19T07:38:54-07:00            #
# Last Modified: 2023-06-21T02:39:31.473449+00:00  #
# Source: https://github.com/DonalChilde/snippets  #
####################################################

import logging
from functools import wraps
from time import perf_counter_ns
from typing import Any, Callable, Tuple

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

NANOS_PER_SECOND = 1000000000


def function_timer(
    logger: logging.Logger | None = None,
    level: int = logging.DEBUG,
    repr_length: int = 100,
):
    """Log the time it takes to run a function.
    https://stackoverflow.com/a/42581103
    """
    if logger is None:
        logger = _logger

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = perf_counter_ns()
            result = func(*args, **kwargs)
            end = perf_counter_ns()
            if repr_length == -1:
                logger.log(
                    level,
                    "%s ran in %ss with args: %s",
                    func.__name__,
                    f"{(end-start)/NANOS_PER_SECOND:9f}",
                    repr((args, kwargs)),
                )
                return result
            if repr_length > 0:
                logger.log(
                    level,
                    "%s ran in %ss with args: %s",
                    func.__name__,
                    f"{(end-start)/NANOS_PER_SECOND:9f}",
                    repr((args, kwargs))[:repr_length],
                )
                return result
            logger.log(
                level,
                "%s ran in %ss",
                func.__name__,
                f"{(end-start)/NANOS_PER_SECOND:9f}",
            )
            return result

        return wrapper

    return decorator


def timer_ns(callback: Callable[[int, int, str, tuple[tuple, dict]], None]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = perf_counter_ns()
            result = func(*args, **kwargs)
            end = perf_counter_ns()
            callback(start, end, func.__qualname__, (args, kwargs))
            return result

        return wrapper

    return decorator


class TimeLogger:
    def __init__(
        self,
        logger: logging.Logger | None = None,
        level: int = logging.DEBUG,
        repr_length: int = 100,
    ) -> None:
        if logger is None:
            self.logger = _logger
        else:
            self.logger = logger
        self.level = level
        self.repr_length = repr_length

    def __call__(
        self, start: int, end: int, func_name: str, func_args: tuple[tuple, dict]
    ) -> Any:
        if self.repr_length == -1:
            self.logger.log(
                self.level,
                "%s ran in %ss with args: %s",
                func_name,
                f"{(end-start)/NANOS_PER_SECOND:9f}",
                repr(func_args),
            )

        elif self.repr_length > 0:
            self.logger.log(
                self.level,
                "%s ran in %ss with args: %s",
                func_name,
                f"{(end-start)/NANOS_PER_SECOND:9f}",
                repr(func_args)[: self.repr_length],
            )
        else:
            self.logger.log(
                self.level,
                "%s ran in %ss",
                func_name,
                f"{(end-start)/NANOS_PER_SECOND:9f}",
            )
