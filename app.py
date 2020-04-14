# app.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/other")
def other():
    return "Hello Other World!"