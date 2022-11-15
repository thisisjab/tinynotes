import datetime
import tzlocal


DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S %z'


def datetime_str(value: datetime.datetime = None, format_: str = None) -> str:
    """
    Return datetime as a string

    :param value: A datetime object. Defaults to `datetime.now()`
    :param format_: Datetime format string. Defaults to `DATETIME_FORMAT`
    :return: A formatted datetime string
    """
    if value is None:
        value = datetime.datetime.now(tz=tzlocal.get_localzone())
    else:
        if not isinstance(value, datetime.datetime):
            raise ValueError("`value` must be a datetime object.")

        if value.tzinfo is None or value.tzinfo.utcoffset(value) is None:
            raise ValueError("`value` must be an aware datetime object.")

    if format_ is None:
        format_ = DATETIME_FORMAT
    elif not isinstance(format_, str):
        raise ValueError("`format_` must be a string.")

    return value.strftime(format_)


def is_valid_datetime_str(value: str, format_: str = None) -> bool:
    """
    Check if a string is a valid datetime

    :param value: A datetime string
    :param format_: Datetime string format
    :return: True if value is correctly formatted using `format_`
    """
    if not isinstance(value, str):
        raise ValueError("`value` must be a string.")

    if format_ is None:
        format_ = DATETIME_FORMAT
    elif not isinstance(format_, str):
        raise ValueError("`format_` must be a string.")

    try:
        datetime.datetime.strptime(value, format_)
        return True
    except Exception:
        return False
