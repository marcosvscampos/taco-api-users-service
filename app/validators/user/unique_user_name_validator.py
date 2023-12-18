from fastapi import HTTPException
from app.validators.user.user_validator import UserValidator
from app.models.user import User
from app.dto.user_dto import UserDTO

class UniqueUserNameValidator(UserValidator):

    async def execute(self, user:User, request:UserDTO):
        exists = await user.find({"name": {"$in": [request.name]}}).count() > 0
        if exists:
            message = f"Já existe um usuário com o nome [{request.name}] cadastrado"
            print(f">>> ERROR: {message}")
            raise HTTPException(status_code=412, detail=message)
        