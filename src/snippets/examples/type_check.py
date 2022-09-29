from typing import Optional


def is_string(value: str, arg_name: Optional[str] = None):
    if not isinstance(value, str):
        raise TypeError(
            f"With arg: {arg_name} expected a string, got {value} with type: {type(value)}"
        )
