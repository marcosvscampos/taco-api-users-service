from pydantic import BaseModel, field_validator
from app.validators.fields.field_value_validator import FieldValueValidator
from app.validators.fields.name_validator import NameValidator
from app.validators.fields.email_validator import EmailValidator

class UserDTO(BaseModel):

    id: str = None
    name: str
    email: str

    @field_validator('name')
    def validate_name(cls, val):
        value_validator:FieldValueValidator = NameValidator()
        value_validator.execute(val)
        return val
    
    @field_validator('email')
    def validate_email(cls, val):
        value_validator:FieldValueValidator = EmailValidator()
        value_validator.execute(val)
        return val