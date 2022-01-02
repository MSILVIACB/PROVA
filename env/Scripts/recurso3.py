from flask import Flask, Blueprint, request, jsonify
import sqlite3


usuario = Blueprint('usuario', __name__)

def conectar():
    return sqlite3.connect('database/data.db')


app = Flask ("Desktop")

@app.route('/',  methods = ['PUT'])
def update():
    cliente = request.get_json()

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE tb_usuario SET nome=?, email=?, senha=? WHERE id=?",
                    (usuario['nome'], usuario['email'], usuario['senha'], usuario['id']) )
        conn.commit()
        mensagem = jsonify({'mensagem':'Operacao realizada com sucesso'})

    except Exception as e:
        conn.rollback()
        mensagem = jsonify({'erro' : str(e)})
    finally:
        conn.close()

    return mensagem 

    app.run(debug=True)

