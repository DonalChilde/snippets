def seconds_to_nanoseconds(seconds: float) -> int:
    """Convert seconds to nanoseconds"""
    nanos = int(seconds * 1000000000)
    return nanos


def nanoseconds_to_seconds(nanos: int) -> float:
    """
    Convert nanoseconds to seconds
    Args:
        nanos: Nanoseconds to convert.
    Returns:
        Seconds as a float.
    """
    seconds = nanos / 1000000000
    return seconds
