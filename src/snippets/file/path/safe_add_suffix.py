from pathlib import Path


def safe_add_suffix(path: Path, suffix: str) -> Path:
    """Add a suffix to a path without clobbering an existing suffix"""
    return Path(f"{path}.{suffix}")
