from app.validators.fields.field_value_validator import FieldValueValidator
import re

class EmailValidator(FieldValueValidator):

    def _validate(self, val) -> str:
        if (val is None or len(val) == 0):
            return 'Email não pode ser vazio'

        if (len(val) > 120 or len(val) < 10):
            return 'Email deve ter tamanho entre 10 e 120 caracteres'
        
        regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        if (not re.match(regex, val)):
            return 'Email possui formato inválido'