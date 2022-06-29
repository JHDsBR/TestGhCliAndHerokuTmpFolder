from flask import Flask
import os
from random import randint

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


@app.route("/check-my-tmp")
def CheckMyTmp():
    a = ["./MyTmp","/MyTmp","MyTmp"]
    res = []
    for c in a:
        res.append(str(os.path.isdir(c)))
    return {"res":res}




@app.route("/create-file/<name>/<cont>")
def CreateFile(name, cont):
    try:
        with open(f"/tmp/{name}.txt", "w") as file:
            file.write(str(cont))
        return "ok"
    except:
        return "deu erro meu patrão"



@app.route("/read-file/<name>")
def ReadFile(name):
    try:
        with open(f"/tmp/{name}.txt", "r") as file:
            return file.read()
    except:
        return "consegui não meu patrão"




@app.route("/get-all-in-dir")
def GetAllDir():
    return str([x[0] for x in os.walk(".")])


@app.route("/my-path")
def MyPath():
    return str(os.getcwd())


@app.route("/get-all-in-path")
def GetAllPath():
    return str([x[0] for x in os.walk(os.getcwd())])


@app.route("/get-all-in-path-2")
def GetAllPath2():
    return str([x for x in os.walk("."+os.getcwd())])
