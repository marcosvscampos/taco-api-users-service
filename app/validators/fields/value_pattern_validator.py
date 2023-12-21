from app.validators.fields.field_value_validator import FieldValueValidator
import re

class ValuePatternValidator(FieldValueValidator):

    def __init__(self, pattern:str, field_name:str):
        self._regex = re.compile(r"{0}".format(pattern))
        super().__init__(field_name=field_name)

    def _validate(self, val):
        if (not re.match(self._regex, val)):
            return f'{super().field_name} tem formato inválido'