from datetime import datetime


def to_str_id(obj):
    """
    Converts MongoDB ObjectId or any relevant ID-like value to string.
    """
    try:
        return str(obj)
    except:
        return obj


def now_utc():
    """
    Returns current datetime in UTC.
    """
    return datetime.utcnow()
