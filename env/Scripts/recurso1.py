from flask import Flask

app = Flask ("Desktop")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola": "mundo"}

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():

    return{"id": 0}

app.run() 