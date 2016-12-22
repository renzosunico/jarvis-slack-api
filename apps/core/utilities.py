import pytz


def local_time(date, timezone='Asia/Manila'):
    """Return manila time."""
    utc_date = date.replace(tzinfo=pytz.utc)
    manila = pytz.timezone(timezone)
    manila_date = utc_date.astimezone(manila)
    return manila_date
