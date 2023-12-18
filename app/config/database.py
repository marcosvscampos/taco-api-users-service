from beanie import init_beanie
import motor.motor_asyncio

from app.models.api_key import ApiKey
from app.models.user import User

async def init_db():
    host = "roguesoft-cluster-dev.as6amuu.mongodb.net"
    database = "db-taco-api-users-service"

    print(">>> Starting database at Host -> @{0} - Database -> {1}".format(host, database))

    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb+srv://roguesoft:rNNFRAmcBMu2gCSz@{0}/{1}?retryWrites=true&w=majority".format(host, database)
    )

    await init_beanie(database=client.get_database(), document_models=[User, ApiKey])