import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb['custumers']

myd = {"name": "", "password": "", "prefLang": ""}
#mycol.insert_one(myd)

def insert_to_db (Uname, password, prefLang):
    collist = mydb.list_collection_names()
    if not "customers" in collist:
        mydict = {"name": Uname,"password": password ,"prefLang": prefLang}
        mycol.insert_one (mydict)
        return "inserted"
    else:
        for i in mycol.find({},{"name"}):
            if (i['name'] != Uname):
                mydict = {"name": Uname,"password": password ,"prefLang": prefLang}
                mycol.insert_one (mydict)
                return "inserted"
            else:
                return "Username already in use"

def delete_from_db (name):
    myquery= {"name": name}
    mycol.delete_one(myquery)

def findName (name):
    for i in mycol.find():
        if (i['name'] == name):
            return i

#insert_to_db("John","******", "English")
#delete_from_db("Ale")
#print (findName("John"))

# for i in mycol.find():
#     print(i)
