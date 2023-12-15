from app.dto.user_dto import UserDTO
from app.models.user import User

async def create_user(request:UserDTO) -> str:
    user = User().build(name=request.name, email=request.email)
    await user.insert()
    return user.id
