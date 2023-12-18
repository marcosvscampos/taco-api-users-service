from pydantic import BaseModel


class UserDTO(BaseModel):

    id: str = None
    name: str
    email: str 