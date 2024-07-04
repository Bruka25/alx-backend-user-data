#!/usr/bin/env python3
"""Module for hashing passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password with a salt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
