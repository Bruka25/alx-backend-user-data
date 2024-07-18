#!/usr/bin/env python3
"""Basic Flask app
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome() -> str:
    """GET route to return a welcome message

    Returns:
        str: JSON payload with a welcome message
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)