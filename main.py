from pymongo import MongoClient

client = MongoClient()

db = client.labbd

print(db)
