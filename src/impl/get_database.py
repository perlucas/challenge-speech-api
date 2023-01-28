from pymongo import MongoClient
import os

def get_database():
   CONNECTION_STRING = "mongodb://{}:{}@{}/{}".format(
      os.environ['MONGO_USER'],
      os.environ['MONGO_PASSWORD'],
      os.environ['MONGO_HOST'],
      os.environ['MONGO_DBNAME'],
   )
   client = MongoClient(CONNECTION_STRING)
   return client[ os.environ['MONGO_DBNAME'] ]

db = get_database()