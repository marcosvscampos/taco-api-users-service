from abc import ABC, abstractmethod
from app.exceptions.request_data_validation_exception import RequestDataValidationException

class FieldValueValidator(ABC):

    _field_name:str

    def __init__(self, field_name:str) -> None:
        self._field_name = field_name

    @property
    def field_name(self):
        return self._field_name.title()

    def execute(self, val):
        message = self._validate(val)
        if(message != None):
            raise RequestDataValidationException(message)

    @abstractmethod
    def _validate(self, val):
        pass