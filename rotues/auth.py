from flask import Blueprint,render_template
authbp = Blueprint('auth',__name__,url_prefix="/auth")

@authbp.route("/login")
def login():
    return render_template("Login.html")

@authbp.route("/signup")
def signup():
    return render_template("Signup.html")

@authbp.route("/logout",methods=["post","get"])
def logout():
    return render_template("index.html")

