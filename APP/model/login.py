import json
from pymongo import MongoClient

keys = json.load(open('keys.json'))
client = MongoClient(f"mongodb+srv://hugo:{keys['mongodb_pass']}@cluster0.uimyf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test