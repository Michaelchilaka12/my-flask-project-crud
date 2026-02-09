from flask import request, jsonify
from flask_jwt_extended import create_access_token
from models.user_model import User
from extensions import db

def register():
    data = request.json

    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"]  # will hash later
    )

    db.session.add(user)
    db.session.commit()
    token = create_access_token(identity=str(user.id))

    return jsonify({"message": "User registered successfully", "access_token": token}), 201

def login():
    data = request.json
    

    user = User.query.filter_by(email=data["email"]).first()

    if not user or user.email != data["email"]:
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user.id))
    return jsonify(access_token=token)
