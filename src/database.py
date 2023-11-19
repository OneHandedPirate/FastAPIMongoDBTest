from motor.motor_asyncio import AsyncIOMotorClient

from environ import DB_PORT


MONGO_URL = f"mongodb://localhost:{DB_PORT}"
client = AsyncIOMotorClient(MONGO_URL)
db = client.formsdb
collection = db.formstemplates
