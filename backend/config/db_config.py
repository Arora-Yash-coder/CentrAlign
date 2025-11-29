from pymongo import MongoClient
from .settings import settings

def get_db():
    client = MongoClient(settings.MONGODB_URI)
    db = client[settings.MONGODB_DB_NAME]
    return db
