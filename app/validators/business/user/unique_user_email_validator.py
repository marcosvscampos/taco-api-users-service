from app.exceptions.duplicated_user_value_exception import DuplicatedUserValueException
from app.validators.business.user.user_validator import UserValidator
from app.models.user import User
from app.dto.user_dto import UserDTO

class UniqueUserEmailValidator(UserValidator):

    async def execute(self, user:User, request:UserDTO):
        exists = await user.find({"email": {"$in": [request.email]}}).count() > 0
        if exists:
            raise DuplicatedUserValueException(value=request.email)
        