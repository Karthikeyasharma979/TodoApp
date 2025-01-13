from flask import Blueprint, render_template,request
from Database.User import User
from Database.SignUp_Database import SignUp_Database
signup = Blueprint('signup', __name__, url_prefix="/signup")
@signup.route("/", methods=["POST", "GET"])
def signup_view():
    if request.method=="POST":
        name = str(request.form["fullName"])
        email = str(request.form["email"])
        uname = str(request.form["username"])
        passw = str(request.form["password"])
        cpassw = str(request.form["confirmPassword"])
        if passw!=cpassw:
            return render_template("Signup.html",result="Password and Confirm Password are not same")
        else:
            u1 = User(name,email,uname,passw,cpassw)
            s1 = SignUp_Database()
            msg = s1.add(u1)
            if msg=="True":
                return render_template("Todo.html")
            return render_template("Signup.html",result=msg)
    return render_template("Signup.html")
    