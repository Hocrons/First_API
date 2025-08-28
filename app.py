from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []
proximo_id = 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(usuarios), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            return jsonify(usuario), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/users', methods=['POST'])
def criar_usuario():
    global proximo_id
    dados = request.json
    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return jsonify({"erro": "Nome e email são obrigatórios"}), 400

    usuario = {
        "id": proximo_id,
        "nome": nome,
        "email": email
    }

    usuarios.append(usuario)
    proximo_id += 1

    return jsonify(usuario), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
