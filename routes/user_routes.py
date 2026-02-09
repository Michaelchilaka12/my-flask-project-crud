from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from controllers.user_controller import get_users, get_user, update_user, delete_user

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/users", methods=["GET"])
@jwt_required()
def all_users():
    return get_users()

@user_routes.route("/users/<int:user_id>", methods=["GET"])
@jwt_required()
def single_user(user_id):
    return get_user(user_id)


@user_routes.route("/users/<int:user_id>", methods=["PATCH"])
@jwt_required()
def modify_user(user_id):
    data = request.json
    return update_user(user_id, data)

@user_routes.route("/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
def remove_user(user_id):
    return delete_user(user_id) 


