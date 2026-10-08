#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    """welcome page"""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    """return list of usernames"""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """endpoint status"""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """return user data"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

@app.route("/add_user", methods=["POST"])
def add_user():
    """add new user with POST"""
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400
    
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in data or not data["username"]:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", ""),
    }

    users[username] = user

    response = {
        "message": "User added",
        "user": user,
    }

    return jsonify(response), 201


if __name__ == "__main__":
    app.run()