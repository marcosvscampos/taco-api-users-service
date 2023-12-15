from beanie import Document
import uuid

class ApiKey(Document):

    id:str
    key:str
    user_id:str

    class Settings:
        name = "api_keys"

    def __init__(self, user_id:str):
        self.__id = uuid.uuid4()
        self.__key = uuid.uuid4()
        self.__user_id = user_id
        pass

    def get_id(self):
        return self.__id
    
    def get_key(self):
        return self.__key
    
    def get_user_id(self):
        return self.__user_id