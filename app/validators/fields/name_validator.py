from app.validators.fields.field_value_validator import FieldValueValidator
import re

class NameValidator(FieldValueValidator):

    def _validate(self, val) -> str:
        if (val is None or len(val) == 0):
            return 'Nome não pode ser vazio'

        if (len(val) > 70 or len(val) < 10):
            return 'Nome deve ter tamanho entre 10 e 70 caracteres'
        
        regex = re.compile(r"^[a-zA-ZÀ-ÿ\s]+$")
        if (not re.match(regex, val)):
            return 'Nome só aceita letras'

        return None 