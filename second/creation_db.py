from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = "mongodb+srv://Ytopoc:228402vovan@ytopoc.3txgotu.mongodb.net/?retryWrites=true&w=majority&appName=Ytopoc"


client = MongoClient(uri, server_api=ServerApi('1'))

# Файл для сторення БД за допомогою json файлів. ПРАЦЮЄ ПІСЛЯ ВИКОНАННЯ СКРИПТУ В ФАЙЛІ "parsing.py"!
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.book
try:
    with open('quotes.json', 'r') as fh:
        data_quotes = json.load(fh)
        db.quotes.insert_many(data_quotes)

    with open('authors.json', 'r') as fh:
        data_authors = json.load(fh)
        db.authors.insert_many(data_authors)
except Exception as e :
    print(e)


