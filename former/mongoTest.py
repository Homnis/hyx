import pymongo

client=pymongo.MongoClient()
db=client.test
collection=db.stu
print(db)
result = collection.find_one()
results = collection.find().sort('age',pymongo.DESCENDING)
print(type(result))
for result in results:
    print(result)
    print(result['name'])
count = collection.find({'age': {'$gte': 20}}).count()
print(count)
