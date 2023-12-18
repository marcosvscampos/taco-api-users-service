from typing import Annotated

from fastapi import APIRouter, Path, HTTPException
from app.dto.user_dto import UserDTO
from app.services import user_service

router = APIRouter()

@router.post("/users")
async def register(request: UserDTO):
    user_id: str = await user_service.create_user(request=request)
    return { "uri": f"/api/users/{user_id}"}

@router.get("/users/{user_id}", response_model=UserDTO)
async def get_by_id(user_id: Annotated[str, Path(title = "ID do usuário a ser pesquisado")]):
    response = await user_service.get_by_id(user_id=user_id)
    if (response is None):
        raise HTTPException(status_code=404, detail=f"Usuário de ID {user_id} não existe")

    return response