from pydantic import BaseModel, field_validator
from app.dto.validators import email_validator_factory, name_validator_factory

class UserDTO(BaseModel):

    id: str = None
    name: str
    email: str

    @field_validator('name')
    def validate_name(cls, val):
        for v in name_validator_factory.get_instance():
            v.execute(val) 
        return val
    
    @field_validator('email')
    def validate_email(cls, val):
        for v in email_validator_factory.get_instance():
            v.execute(val) 
        return val