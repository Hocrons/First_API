from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/users', methods=['GET'])

def getUsers():
    dados = { 'mensagem': 'OLA MUNDO!'}
    return jsonify(dados), 200
if __name__ == '__main__':
    app.run(debug=True, port=5001)