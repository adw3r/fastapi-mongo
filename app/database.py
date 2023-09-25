import pymongo

from app import config

mongo_client = pymongo.MongoClient(config.MONGO_URL)
CLIENT_LOCAL_USERS: pymongo.collection.Collection = mongo_client.local.users
CLIENT_LOCAL_USERS.create_index('email', unique=True)
