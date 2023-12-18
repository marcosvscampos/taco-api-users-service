import uuid
from beanie import Document
from typing import Optional

class User(Document):

    id: Optional[str] = None
    name:Optional[str] = None
    email:Optional[str] =  None

    class Settings:
        name = "Users"

    def build(self, name:str, email:str, id:str=None):
        self.id = id if id is not None else str(uuid.uuid4())
        self.name = name
        self.email = email
        return self