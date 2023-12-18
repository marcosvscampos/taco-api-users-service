from abc import ABC, abstractmethod
from app.models.user import User

class UserValidator(ABC):

    @abstractmethod
    async def execute(self, user:User):
        pass