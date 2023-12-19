from app.exceptions.duplicated_user_value_exception import DuplicatedUserValueException
from app.validators.user.user_validator import UserValidator
from app.models.user import User
from app.dto.user_dto import UserDTO

class UniqueUserNameValidator(UserValidator):

    async def execute(self, user:User, request:UserDTO):
        exists = await user.find({"name": {"$in": [request.name]}}).count() > 0
        if exists:
            raise DuplicatedUserValueException(value=request.name)
        