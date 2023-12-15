from fastapi import APIRouter
from app.dto.user_dto import UserDTO
from app.services import user_service

router = APIRouter()

@router.post("/users")
async def register(request: UserDTO):
    user_id: str = await user_service.create_user(request=request)
    return { "uri": f"/api/users/{user_id}"}