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
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@auth.error_handler
def basic_auth_error():
    return jsonify({"error": "Unauthorized"}), 401

@jwt.unautherized_loader
def jwt_missing_token(err_msg):
    return jsonify({"error": "Missing or invalid token"}), 401
@jwt.invalid_token_loader
def jwt_invalid_token(err_msg):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def jwt_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def jwt_revoked_token(jwt_header,jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def jwt_fresh_required(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 401
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401
    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]["role"]}
            )
    return jsonify({"access_token": token})

@app.route("/jwt-protected", method=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"
if __name__ == "__main__":
    app.run()
