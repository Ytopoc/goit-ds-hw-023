from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test
# Створення БД

db.cats.insert_many([
    {
        'name': 'Lama',
        'age': 2,
        'features': ['ходить в лоток', 'не дає себе гладити', 'сірий'],
    },
    {
        'name': 'Liza',
        'age': 4,
        'features': ['ходить в лоток', 'дає себе гладити', 'білий'],
    },
    {
       'name': 'Boris',
        'age': 12,
        'features': ['ходить в лоток', 'не дає себе гладити', 'сірий'],
    },
    {
        'name': 'Oleg',
        'age': 1,
        'features': ['ходить в лоток', 'дає себе гладити', 'чорний'],
    }
])
