#!/usr/bin/env python3
"""Basic Flask app with user registration
"""
from flask import Flask, request, jsonify
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome() -> str:
    """GET route to return a welcome message

    Returns:
        str: JSON payload with a welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user() -> str:
    """POST route to register a new user

    Returns:
        str: JSON payload with registration status
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
