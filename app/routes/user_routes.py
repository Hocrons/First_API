from flask import Blueprint, jsonify, request
from app.services import user_service

user_bp = Blueprint("users", __name__)

@user_bp.route("/", methods = ["GET"])
def get_users():

    return jsonify(user_service.get_all_users()), 200

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):

    user = user_service.get_user_by_id(user_id)

    if user: 
        
        return jsonify(user), 200
    
    return jsonify({"erro": "Usuário não encontrado"}), 404

@user_bp.route('/', methods=['POST'])
def create_user():

    data = request.json
    user, erro = user_service.create_user(data)

    if erro:
        return jsonify(erro), 400
    return jsonify(user), 201

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user, erro = user_service.update_user(user_id, data)

    if erro:
        return jsonify(erro), 400
    return jsonify(user), 200

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    response, erro = user_service.delete_user(user_id)

    if erro:
        return jsonify(erro), 404
    return jsonify(response), 200