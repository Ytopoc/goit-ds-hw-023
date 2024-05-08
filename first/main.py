
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Ytopoc:228402vovan@ytopoc.3txgotu.mongodb.net/test?retryWrites=true&w=majority&appName=Ytopoc"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test

#Реалізуйте функцію для виведення всіх записів із колекції.
def read_all(database):

    result = database.cats.find({})
    for el in result:
        print(el)
#Реалізуйте функцію, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота.
def read_by_name(database):
    name= input('Введіть ім\'я кота: ')

    result = database.cats.find_one({"name":name})
    if result:
        print(result)
    else:
        print('Такого кота не існує')

#Створіть функцію, яка дозволяє користувачеві оновити вік кота за ім'ям.
def update_by_name(database):
    name = 'Lama'
    check= database.cats.find_one({"name":name})
    if check:
        database.cats.update_one({"name": name}, {"$set": {"age": 3}})
        print('Документ оновлено')
    else:
        print('Такого кота не існує')


#Створіть функцію, яка дозволяє додати нову характеристику до списку features кота за ім'ям.
def update_features_by_name(database):
    name = 'Lama'
    check= database.cats.find_one({"name":name})
    if check:
        database.cats.update_one({'name':name},{"$push": {"features": 'new_feature'}} )
        print('Документ оновлено')

    else:
        print('Такого кота не існує')



#Реалізуйте функцію для видалення запису з колекції за ім'ям тварини.
def delete_by_name(database):
    name = 'Lama'
    check= database.cats.find_one({"name":name})
    if check:
        database.cats.delete_one({'name':name})
        print('Запис видалено')
    else:
        print('Такого кота не існує')

#Реалізуйте функцію для видалення всіх записів із колекції.

def delete_all(database):
    check=input('Введіть \"+\" якщо бажаєте видалити всі записи:')
    if check == '+':
        database.cats.delete_many({})
        print('Записи видаленно')
        pass
    else:
        print('Записи НЕ видаленно')

if __name__ == '__main__':
    delete_all(db)