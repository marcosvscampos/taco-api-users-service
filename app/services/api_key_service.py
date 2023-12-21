from app.models.user import User
from app.models.api_key import ApiKey

async def create_api_key(user:User):
    api_key = ApiKey().build(user.id)
    
    await api_key.create()

    return api_key.id