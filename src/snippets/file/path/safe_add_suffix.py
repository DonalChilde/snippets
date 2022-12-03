from pathlib import Path


def safe_add_suffix(path: Path, suffix: str) -> Path:
    """Add a suffix to a path without clobbering an existing suffix"""
    return Path(f"{path}.{suffix}")


def append_suffix(path: Path, suffix: str) -> Path:
    """Append a value to the last part of a path.

    Can be used to append a suffix to a filename, without removing the old suffix.
    """
    if not path.parts:
        raise ValueError(f"{path} has no parts. Was Path('') used to make it?")
    return path.parent / f"{path.parts[-1]}{suffix}"
