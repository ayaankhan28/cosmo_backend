import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()


class MongoDB:
    client: AsyncIOMotorClient = None
    database = None


db = MongoDB()


async def connect_to_mongo():
    mongo_url = os.getenv("MONGO_URL")
    if not mongo_url:
        raise ValueError("MONGO_URL environment variable is not set.")

    db.client = AsyncIOMotorClient(mongo_url)
    db.database = db.client["student_management"]


async def disconnect_from_mongo():
    if db.client:
        db.client.close()