#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
        JWTManager, create_access_token,
        jwt_required, get_jwt
        )
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

auth = HTTPBasicAuth()
jwt = JWTManager(app)
users = {
        "user1": {
            "username": "user1",
            "password": generate_password_hash("password"),
            "role": "user"
            },
        "admin1": {
            "username": "admin1",
            "password": generate_password_hash("password"),
            "role": "admin"
            }
        }
@auth.verify_password
def verify_password(username, password):
    if username in useres and check_password_hash(users[username]["password"], password):
        return username
    return None

@auth.error_handler
def basic_auth_error():
    return jsonify({"error": "Unathorized"}), 401

@jwt.unautherized_loader
def jwt_missing_token(err_msg):
    return jsonify({"error": "Missing or invalid token"}), 401
@jwt.invalid_token_loader
def jwt_invalid_token(err_msg):
    return jsoify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def jwt_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401
