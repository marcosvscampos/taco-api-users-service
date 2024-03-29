from app.exceptions.user_not_found_exception import UserNotFoundException
from app.dto.user_dto import UserDTO
from app.models.user import User
from app.services import api_key_service
from app.validators.business.user import user_validator_factory

async def __validate(user:User, request:UserDTO):
    user_validators = user_validator_factory.get_instance()
    for validator in user_validators:
        await validator.execute(user, request)

async def create_user(request:UserDTO) -> str:
    user = User().build(name=request.name, email=request.email)

    await __validate(user, request)

    await user.insert()

    await api_key_service.create_api_key(user)
    
    return user.id

async def get_by_id(user_id:str) -> UserDTO:
    user = User()
    user_saved = await user.get(user_id)

    if(user_saved is None):
         raise UserNotFoundException()

    return UserDTO(id=user_saved.id, name=user_saved.name, email=user_saved.email)
