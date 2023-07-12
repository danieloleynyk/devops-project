import pymongo

import config


client = pymongo.MongoClient(config.MONGO_URI)
db = client["todolist"]
todos_collection = db["todos"]

