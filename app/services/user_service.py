from app.dto.user_dto import UserDTO
from app.models.user import User

async def create_user(request:UserDTO) -> str:
    user = User().build(name=request.name, email=request.email)
    await user.insert()
    return user.id

async def get_by_id(user_id:str) -> UserDTO:
    user = User()
    user_saved = await user.get(user_id)

    if(user_saved is None):
        return None

    return UserDTO(id=user_saved.id, name=user_saved.name, email=user_saved.email)
