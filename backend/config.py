import os


MONGO_URI = os.getenv('MONGO_URI', f'mongodb://localhost:27017/')
