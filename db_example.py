# import pymongo
#
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb['custumers']
#
# # mydict = {"name": "John", "prefLang": "English"}
# # x = mycol.insert_one (mydict)
# #if only one is inserted
# # print(x)
# # print(x.inserted_id)
#
# # #ids can be specified by "_id"=1 field
# # mylist = [
# #   { "name": "Amy", "prefLang": "English"},
# #   { "name": "Hannah", "prefLang": "English"},
# #   { "name": "Michael", "prefLang": "English"},
# #   { "name": "Sandy", "prefLang": "English"},
# #   { "name": "Betty", "prefLang": "English"},
# #   { "name": "Richard", "prefLang": "English"},
# #   { "name": "Susan", "prefLang": "English"},
# #   { "name": "Vicky", "prefLang": "English"},
# #   { "name": "Ben", "prefLang": "English"},
# #   { "name": "William", "prefLang": "Spanish"},
# #   { "name": "Chuck", "prefLang": "French"},
# #   { "name": "Viola", "prefLang": "Spanish"}
# # ]
# # #if multiple are inserted
# # y = mycol.insert_many(mylist)
# # print(y.inserted_ids)
# # #finds first reoccurance
# # z = mycol.find_one()
# # print(z)
# #
# # #finds all in selection
# # for i in mycol.find():
# #     print (i)
#
# #choose fields to display
# # for i in mycol.find({},{"name"}):
# #     print(i['name'])
#
# #find with specifics
# # myquery = {"prefLang": "Spanish"}
# # mydoc = mycol.find(myquery)
#
# # for x in mydoc:
# #     print(x)
# #
# # #sorting
# # mydoc = mycol.find().sort("name")
# #
# # for x in mydoc:
# #     print(x)
#
# #delete
# # myquery= {"name": "John"}
# # #mycol.delete_one(myquery)
# # #deletes all {}
# x = mycol.delete_many({})
# print (x.deleted_count)
