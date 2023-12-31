from pymongo import MongoClient

client = MongoClient('localhost' ,27017)
print(client.list_database_names())
db = client['news_db']
print(db.list_collection_names())