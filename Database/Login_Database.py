import pymongo
class Login_Database:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Students"]["Practice"]
    def __init__(self):
        pass

    def checkUser(self,name,password):
        if(self.checkname(name)):
            if self.db.count_documents({"uname":name,"passw":password})==1:
                return "True"
            else:
                return "Password is incorrect"
        else:
            return "Username is not found"
    
    def checkname(self,name):
        return self.db.count_documents({"uname":name})==1

    