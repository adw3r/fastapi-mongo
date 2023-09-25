import pymongo

from app import config

mongo_client = pymongo.MongoClient(config.MONGO_URL)
