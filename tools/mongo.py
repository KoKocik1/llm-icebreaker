from pymongo import MongoClient
from config.config import MONGO_URI

# MongoDB Connection


def get_mongo_client():
    """Connect to MongoDB and return the client."""
    client = MongoClient(MONGO_URI)
    return client
