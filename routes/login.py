from flask import Blueprint, render_template
login = Blueprint('login', __name__, url_prefix="/Login")
@login.route("/", methods=["POST", "GET"])
def login_view():
    return render_template("Login.html")
