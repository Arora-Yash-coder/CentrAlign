from pymongo import MongoClient
from config.settings import settings

# Single global connection (recommended by pymongo)
client = MongoClient(settings.MONGODB_URI)

def get_db():
    """
    Returns the application's main database.
    """
    return client[settings.MONGODB_DB_NAME]
