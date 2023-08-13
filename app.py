from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios = []

@app.route('/post_usuario', methods=['POST'])
def post_usuario():
    data = request.json

    if 'cpf' not in data or 'nome' not in data or 'data_nascimento' not in data:
        return jsonify({'message': 'Dados incompletos'}), 400

    usuarios.append(data)

    return jsonify(data), 201

@app.route('/get_usuario/<int:cpf>', methods=['GET'])
def get_usuario(cpf):
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'message': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
