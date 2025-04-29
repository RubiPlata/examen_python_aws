from flask import Blueprint, request, jsonify
from controllers.userController import get_all_user, get_user_by_id, create_user, update_user, delete_user

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def index():
    users = get_all_user()
    return jsonify(users)

@user_bp.route('/<int:user_id>', methods=['GET'])
def show(user_id):
    user = get_user_by_id(user_id)
    return jsonify(user)

@user_bp.route('/', methods=['POST'])
def store():
    data = request.json
    user = create_user(data)
    return jsonify(user), 201

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update(user_id):
    data = request.json
    user = update_user(user_id, data)
    return jsonify(user)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def destroy(user_id):
    response = delete_user(user_id)
    return jsonify(response)



