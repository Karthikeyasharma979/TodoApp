from flask import Blueprint, render_template

todo_bp = Blueprint('todo', __name__, url_prefix="/todo")

@todo_bp.route("/", methods=["POST", "GET"])
def todo():
    return render_template("Todo.html")
