#!/usr/bin/env python3
"""Basic authentication module for the API.
"""
from .auth import Auth
import re


class BasicAuth(Auth):
    """Basic authentication class."""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header for Basic Auth.
        Args:
          - authorization_header: The full authorization header string.
        Return:
          - The Base64 encoded part of the header or None if not found.
        """
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'  # Pattern to match Basic token
            field_match = re.fullmatch(pattern, authorization_header.strip())
            # Match pattern against stripped authorization header
            if field_match is not None:
                return field_match.group('token')  # Return captured token part
        return None  # Return None if not a valid Basic Auth header
