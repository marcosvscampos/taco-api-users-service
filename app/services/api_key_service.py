from app.models.user import User
from app.models.api_key import ApiKey
from app.services.notification_service import send
from app.models.notification.notification import Notification
from app.models.notification.user_created_notification_content import UserCreatedNotificationContent

async def create_api_key(user:User):
    api_key = ApiKey().build(user.id)
    
    await api_key.create()

    send(Notification(to=user.email, 
                      type="API_KEY_CREATED", 
                      content=UserCreatedNotificationContent(name=user.name, key=api_key.key)))

    return api_key.id