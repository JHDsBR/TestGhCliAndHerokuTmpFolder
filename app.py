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
    return str(os.path.isdir("./tmp"))

@app.route("/get-all-in-dir")
def GetAllDir():
    return str([x[0] for x in os.walk(".")])



@app.route("/my-path")
def MyPath():
    return str(os.getcwd())
