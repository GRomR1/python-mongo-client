
import pymongo
from pymongo import MongoClient

# соединяемся с сервером базы данных
# (по умолчанию подключение осуществляется на localhost:27017)
conn = pymongo.Connection()

client = MongoClient('mongodb://root:mMrGevR75bGcBKqg@localhost:27017/')

answers = {'qwe': ['Audi', 'price'],
           'wer': ['Mercedes', 'price']}

answers = {'qwe': ['Audi', 'price'],
           'wer': ['Mercedes', 'price'],
           'wer2': ['Mercedes', 'price']}
import json
from bson import json_util

with client:
    db = client.honorcup
    coll = db.iot_base
    coll.save(answers)
    # выводим все документы из коллекции coll
    for a in coll.find():
        print(a)

if __name__ == 'main':
    pass