from flask import request, jsonify
from utils.db import users
import uuid

def register():
    data = request.json

    # check if user exists
    for user in users:
        if user["email"] == data.get("email"):
            return jsonify({"message": "User already exists"}), 400

    new_user = {
        "id": str(uuid.uuid4()),
        "name": data.get("name"),
        "email": data.get("email"),
        "password": data.get("password")
    }

    users.append(new_user)

    return jsonify({
        "message": "User registered successfully",
        "user": new_user
    })


def login():
    data = request.json

    for user in users:
        if user["email"] == data.get("email") and user["password"] == data.get("password"):
            return jsonify({
                "message": "Login successful",
                "user": user
            })

    return jsonify({"message": "Invalid credentials"}), 401