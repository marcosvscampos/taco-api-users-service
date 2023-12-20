from app.validators.fields.field_value_validator import FieldValueValidator

class ValueNotEmptyValidator(FieldValueValidator):
    
    def __init__(self, field_name:str):
        super().__init__(field_name=field_name)

    def _validate(self, val):
        if (val is None or len(val) == 0):
            return f'{super().field_name} não pode ser vazio' 