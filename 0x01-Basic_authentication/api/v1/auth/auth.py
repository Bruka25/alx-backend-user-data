#!/usr/bin/env python3
"""Authentication module for the API."""
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication.
        Args:
          - path: The path to check.
          - excluded_paths: A list of paths that do not require auth.
        Return:
          - False: Authentication is not required.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Gets the authorization header field from the request.
        Args:
          - request: The request object.
        Return:
          - None: No authorization header found.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user from the request.
        Args:
          - request: The request object.
        Return:
          - None: No current user found.
        """
        return None
