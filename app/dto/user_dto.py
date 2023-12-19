from pydantic import BaseModel, field_validator
from app.exceptions.request_data_validation_exception import RequestDataValidationException

import re

class UserDTO(BaseModel):

    id: str = None
    name: str
    email: str

    @field_validator('name')
    def validate_name(cls, val):
        if (val is None or len(val) == 0):
            raise RequestDataValidationException('Nome não pode ser vazio')

        if (len(val) > 70 or len(val) < 10):
            raise RequestDataValidationException('Nome deve ter tamanho entre 10 e 70 caracteres')
        
        regex = re.compile(r"^[a-zA-ZÀ-ÿ\s]+$")
        if (not re.match(regex, val)):
            raise RequestDataValidationException('Nome só aceita letras')

        return val
    
    @field_validator('email')
    def validate_email(cls, val):
        if (val is None or len(val) == 0):
            raise RequestDataValidationException('Email não pode ser vazio')

        if (len(val) > 120 or len(val) < 10):
            raise RequestDataValidationException('Email deve ter tamanho entre 10 e 120 caracteres')
        
        regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        if (not re.match(regex, val)):
            raise RequestDataValidationException('Email possui formato inválido')
        
        return val