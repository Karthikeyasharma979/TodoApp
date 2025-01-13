from flask import Flask,render_template,redirect
from routes.login import login  # This is where the blueprint is imported
from routes.signup import signup
app = Flask(__name__)

# Register the blueprint
app.register_blueprint(login)
app.register_blueprint(signup)

@app.route("/")
def welcome():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
