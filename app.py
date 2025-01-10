from flask import Flask,render_template,redirect
from rotues.auth import authbp

app = Flask(__name__)

#Registration
app.register_blueprint(authbp)



@app.route("/")
def welcome():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)