from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
     return "Hello world"

@app.route("/user/<username>")
def show_user(username):
    return "User: %s" %username
