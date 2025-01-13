class User:
    def __init__(self,name,email,username,password,cpassword):
        self.name =name
        self.email =email
        self.uname =username
        self.passw =password
        self.cpassw =cpassword

    def getAll(self):
        res={
            "name":self.name,
            "email":self.email,
            "uname":self.uname,
            "passw":self.passw,
            "cpassw":self.cpassw,
        }
        return res
    
    def getUser(self):
        return self.uname