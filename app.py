from flask import Flask,render_template,redirect
app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("Login.html")

@app.route("/signup")
def signup():
    return render_template("Signup.html")

@app.route("/todo",methods=["post","get"])
def todo():
    return render_template("Todo.html")


@app.route("/logout",methods=["post","get"])
def logout():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)