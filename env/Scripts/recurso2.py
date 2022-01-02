from flask import Flask, request 

from main import insertUsuario 

app = Flask ("Desktop")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola": "mundo"}

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():

    body = request.get_json()

    usuario = insertUsuario(body["nome"], body["email"], body["senha"])

    return usuario 

app.run() 