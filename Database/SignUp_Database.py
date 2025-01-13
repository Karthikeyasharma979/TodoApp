import pymongo
from Database.User import User
class SignUp_Database:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Students"]["Practice"]
    def __init__(self):
        pass
    def add(self, user: User):
        if isinstance(user, User):
            uname = user.getUser()
            if self.isUname(uname):
                res  = user.getAll()
                self.db.insert_one(res)
                return "True"
            else:
                return "Username Exist"
        else:
            # raise TypeError("The argument must be an instance of the User class.")
            return "Error Please try Again"

    def isUname(self,name):
        c = self.db.count_documents({"uname":name})
        # print(c)
        return c==0
    

