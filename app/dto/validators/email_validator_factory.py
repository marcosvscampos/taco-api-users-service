from app.validators.fields.field_value_validator import FieldValueValidator

from app.validators.fields.value_length_validator import ValueLengthValidator
from app.validators.fields.value_not_empty_validator import ValueNotEmptyValidator
from app.validators.fields.value_pattern_validator import ValuePatternValidator

def get_instance() -> list[FieldValueValidator]:
    field_name = 'email'
    return [
        ValueNotEmptyValidator(field_name=field_name),
        ValueLengthValidator(min=10, max=120, field_name=field_name),
        ValuePatternValidator(pattern="^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$", field_name=field_name)
        ]