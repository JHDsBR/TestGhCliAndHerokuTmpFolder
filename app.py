from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def Home():
    return "Está no ar"

# @app.route("/tmp1")
# def Tmp():
#     with open("Temp/", "w")
#     return "Está no ar"

@app.route("/checktmp")
def CheckTmp():
    return str(os.path.isdir("tmp"))
