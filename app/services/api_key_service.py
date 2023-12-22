from app.models.user import User
from app.models.api_key import ApiKey
from app.services.notification_service import send
from app.models.notification import Notification

async def create_api_key(user:User):
    api_key = ApiKey().build(user.id)
    
    await api_key.create()

    send(Notification("USER_CREATED", user))

    return api_key.id