#!/usr/bin/env python3
"""
End-to-End integration test module for a Flask application.
Uses requests library to simulate HTTP requests and tests various endpoints.
"""

from requests import get, put, post, delete


# Function to register a new user
def register_user(email: str, password: str) -> None:
    """Test user registration."""
    # New user successfully created
    request = post("http://0.0.0.0:5000/users",
                   data={'email': email, "password": password})
    response = request.json()
    assert response == {"email": email, "message": "user created"}
    assert request.status_code == 200

    # Email already associated with user
    request = post("http://0.0.0.0:5000/users",
                   data={'email': email, "password": password})
    response = request.json()
    assert response == {"message": "email already registered"}
    assert request.status_code == 400


# Function to test logging in with wrong password
def log_in_wrong_password(email: str, password: str) -> None:
    """Test login with wrong password."""
    request = post("http://0.0.0.0:5000/sessions",
                   data={'email': email, "password": password})
    assert request.status_code == 401
    assert request.cookies.get("session_id") is None


# Function to test logging in
def log_in(email: str, password: str) -> str:
    """Test user login. Returns session_id."""
    request = post("http://0.0.0.0:5000/sessions",
                   data={'email': email, "password": password})
    response = request.json()
    session_id = request.cookies.get("session_id")
    assert request.status_code == 200
    assert response == {"email": email, "message": "logged in"}
    assert session_id is not None
    return session_id


# Function to test accessing profile without logging in
def profile_unlogged() -> None:
    """Test accessing profile without logging in."""
    request = get("http://0.0.0.0:5000/profile")
    assert request.status_code == 403


# Function to test accessing profile after logging in
def profile_logged(session_id: str) -> None:
    """Test accessing profile after logging in."""
    request = get("http://0.0.0.0:5000/profile",
                  cookies={"session_id": session_id})
    response = request.json()
    assert request.status_code == 200
    assert response == {"email": EMAIL}


# Function to test logging out
def log_out(session_id: str) -> None:
    """Test user logout."""
    request = delete("http://0.0.0.0:5000/sessions",
                     cookies={"session_id": session_id},
                     allow_redirects=True)
    response = request.json()
    history = request.history
    assert request.status_code == 200
    assert len(history) == 1
    assert history[0].status_code == 302
    assert response == {"message": "Bienvenue"}


# Function to test obtaining reset token for password reset
def reset_password_token(email: str) -> str:
    """Test obtaining password reset token. Returns reset_token."""
    request = post("http://0.0.0.0:5000/reset_password",
                   data={"email": email})
    response = request.json()
    reset_token = response.get("reset_token")
    assert request.status_code == 200
    assert isinstance(reset_token, str)
    return reset_token


# Function to test updating password using reset token
def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test updating password using reset token."""
    request = put("http://0.0.0.0:5000/reset_password",
                  data={"email": email, "new_password": new_password,
                        "reset_token": reset_token})
    response = request.json()
    assert request.status_code == 200
    assert response == {"email": email, "message": "Password updated"}


# Test data
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    # Execute the tests sequentially
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
