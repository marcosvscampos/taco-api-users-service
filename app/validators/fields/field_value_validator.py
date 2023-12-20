from abc import ABC, abstractmethod
from app.exceptions.request_data_validation_exception import RequestDataValidationException

class FieldValueValidator(ABC):

    def execute(self, val):
        message = self._validate(val)
        if(message != None):
            raise RequestDataValidationException(message)

    @abstractmethod
    def _validate(self, val):
        pass