import re
from datetime import datetime

from pydantic import EmailStr


def validate_email(value: str) -> bool:
    try:
        EmailStr._validate(value)
        return True
    except ValueError:
        return False


def validate_phone(value: str) -> bool:
    phone_pattern = re.compile(r"^\+7 [0-9]{3} [0-9]{3} [0-9]{2} [0-9]{2}$")
    return bool(phone_pattern.fullmatch(value))


def validate_date(value: str) -> bool:
    date_formats = ["%d.%m.%Y", "%Y-%m-%d"]

    for date_format in date_formats:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            pass

    return False


def validate_form(form: dict) -> bool:
    for val in form.values():
        if not isinstance(val, str):
            return False
    return True
