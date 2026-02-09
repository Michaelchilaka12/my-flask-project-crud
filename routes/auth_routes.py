from flask import Blueprint
from controllers.auth_controller import register, login

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.route("/register", methods=["POST"])
def register_user():
    return register()

@auth_routes.route("/login", methods=["POST"])
def login_user():
    return login()
