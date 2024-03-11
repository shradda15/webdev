from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# Create a new client and connect to the server
client = MongoClient("mongodb+srv://shradda:shradda@cluster0.mfvlisk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Send a ping to confirm a successful connection
db=client["shopping"]
col=db["items"]
# mylist = [
#   { "name": "cube", "price": 1999},
#   { "name": "kite", "price": 1199},
#   { "name": "sunglass", "price": 6000},
#   { "name": "perfume", "price": 1797},
#   {"name":"chocolates","price":5196},
#   {"name":"samsung","price":41999}
# ]
# documents=list(col.find({"name":"chocolates"}))
# print(documents[0]["price"])

# x = col.find_one()
# print(x)

x=col.find()
print(list(x))
