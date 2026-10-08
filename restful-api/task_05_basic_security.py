#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# ----------------------------
# Configuration
# ----------------------------

app.config["JWT_SECRET_KEY"] = "change-me-to-a-strong-secret-key"
# En production : utiliser une vraie clé forte, idéalement via variable d'environnement.

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# ----------------------------
# Utilisateurs en mémoire
# ----------------------------

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


# ----------------------------
# Basic Auth : vérification
# ----------------------------

@auth.verify_password
def verify_password(username, password):
    """Vérifie le mot de passe pour Basic Auth."""
    if username not in users:
        return None
    user = users[username]
    if check_password_hash(user["password"], password):
        return username  # identité retournée
    return None


# ----------------------------
# JWT : gestion des erreurs (401)
# ----------------------------

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


# ----------------------------
# Endpoints - Basic Auth
# ----------------------------

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protégée par Basic Auth."""
    return "Basic Auth: Access Granted"


# ----------------------------
# Endpoints - JWT Auth
# ----------------------------

@app.route("/login", methods=["POST"])
def login():
    """
    Login JWT.
    Corps attendu : {"username": "...", "password": "..."}
    Retourne un access_token si les identifiants sont valides.
    """
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users[username]
    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # On inclut le rôle dans le token
    additional_claims = {"role": user["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protégée par JWT."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route réservée aux admins."""
    identity = get_jwt_identity()
    # Récupérer les claims du token
    from flask_jwt_extended import get_jwt
    claims = get_jwt()

    role = claims.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ----------------------------
# Lancement
# ----------------------------

if __name__ == "__main__":
    app.run()