#!/usr/bin/env python3
"""Basic authentication module for the API.
"""
from .auth import Auth
import re
import base64
import binascii


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

    def decode_base64_authorization_header(
           self,
           base64_authorization_header: str) -> str:
        """Decodes a base64-encoded authorization header.
        Args:
          - base64_authorization_header: The base64-encoded header string.
        Return:
          - Decoded header as a UTF-8 string or None if decoding fails.
        """
        if type(base64_authorization_header) == str:
            try:
                res = base64.b64decode(base64_authorization_header,
                                       validate=True)
                return res.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None  # Return None if decoding fails
