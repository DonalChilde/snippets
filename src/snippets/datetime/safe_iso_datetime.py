from datetime import datetime


def safe_iso_datetime(dt: datetime) -> str:
    try:
        return dt.isoformat()
    except AttributeError:
        return ""
