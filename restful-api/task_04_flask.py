#!/usr/bin/python3

from flask import FLASK, jsonify, request

app = Flask(__name__)
users = {}

@app.rout("/")
def home():
    return "Welcome to the Flask API!"

@app.rout("/data")
def get_data():
    return jsonfi(list(users.keys()))

@app.rout("/status")
def status():
    return "OK"

@app.rout("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.rout("/add_user", methods=["POST"])
def add_user:
    if not request.is_json:
        return jsonify({"error":"Invalid JSON"}), 400
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error":"Username is required"}), 400
    username = data["username"]
    if username in users:
        return jsonify({"error":"Username already exists"}), 409
    users[username] = data
    return jsonify({
        "message": "User added",
        "User": data
        }), 201

if __name__ == "__main__":
    app.run()
