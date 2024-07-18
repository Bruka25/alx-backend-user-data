#!/usr/bin/env python3
"""Basic Flask app with user registration
"""
from flask import Flask, request, jsonify, abort, make_response, redirect
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


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user() -> str:
    """POST route to register a new user

    Returns:
        str: JSON payload with registration status
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """POST route to login a user"""
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = make_response(
        jsonify({"email": email, "message": "logged in"})
    )
    response.set_cookie("session_id", session_id)
    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """Handle logout functionality.

    Method:
        DELETE

    Description:
        Logs out the user by destroying their session.

    Returns:
        Redirects to the home route ("/").

    Raises:
        403 Forbidden: If the session ID is invalid or user is not
                       authenticated.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """Handle profile retrieval for authenticated users.

    Method:
        GET

    Description:
        Retrieves and returns the profile information of the authenticated user
        based on the session ID stored in the cookies.

    Returns:
        JSON: User's profile information including their email address.

    Raises:
        403 Forbidden: If the session ID is invalid or user is not
                       authenticated.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
