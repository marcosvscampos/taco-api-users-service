from app.validators.fields.field_value_validator import FieldValueValidator

class ValueLengthValidator(FieldValueValidator):

    def __init__(self, min:int, max:int, field_name:str):
        self._min = min
        self._max = max
        super().__init__(field_name=field_name)

    def _validate(self, val):
        if (len(val) > self._max or len(val) < self._min):
            return f'{super().field_name} deve ter tamanho entre {self._min} e {self._max} caracteres' 