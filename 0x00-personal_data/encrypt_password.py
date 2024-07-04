#!/usr/bin/env python3
"""Module for hashing passwords and validating them"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password with a salt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates that the provided password matches the hashed password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
