from flask import Blueprint, jsonify

auth_bp = Blueprint('auth',__name__)

@auth_bp.post('/register')
def registration():
    return jsonify({"message" : "User Created"})