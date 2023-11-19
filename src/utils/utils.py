from src.database import collection
from src.utils.validators import validate_email, validate_phone, validate_date


def get_field_type(value: str) -> str:
    """define the type of the field according to provided validators"""

    validators = {
        "email": validate_email,
        "phone": validate_phone,
        "date": validate_date,
    }

    for field_type, validator in validators.items():
        if validator(value):
            return field_type
    return "text"


async def find_matching_template(validated_data: dict) -> str | None:
    """find template from DB matching to provided validated data dict"""

    templates = await collection.find({}, {'_id': False}).to_list(length=None)
    validated_data_len = len(validated_data)
    suitable_templates = filter(lambda x: len(x) - 1 <= validated_data_len, templates)
    for template in suitable_templates:
        if all(item in validated_data.items() for item in template.items() if item[0] != "name"):
            return template["name"]
    return None
