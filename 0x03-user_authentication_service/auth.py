#!/usr/bin/env python3

"""Module for hashing passwords for authentication"""

# auth_utils.py
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password string with bcrypt

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted hash of the password.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
