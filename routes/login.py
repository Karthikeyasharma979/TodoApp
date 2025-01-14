from flask import Blueprint, render_template,request
from Database.Login_Database import Login_Database
login = Blueprint('login', __name__, url_prefix="/Login")
@login.route("/", methods=["POST", "GET"])
def login_view():
    if (request.method=="POST"):
        s1 = Login_Database()
        name = request.form["username"]
        password = request.form["password"]
        res = s1.checkUser(name,password)
        if(res!="True"):
            return render_template("Login.html",res=res)
        else:
            return render_template("todo.html")
    return render_template("Login.html")
