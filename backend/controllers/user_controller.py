from flask import jsonify
from utils.db import users

def get_users():
    return jsonify(users)