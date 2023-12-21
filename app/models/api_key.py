from app.utils import key_utils
from beanie import Document
from typing import Optional
import uuid

class ApiKey(Document):

    id: Optional[str] = None
    key:Optional[str] = None
    user_id:Optional[str] = None

    class Settings:
        name = "ApiKeys"

    def build(self, user_id:str):
        self.id = str(uuid.uuid4())
        self.key = key_utils.generate_key()
        self.user_id = user_id
        return self
