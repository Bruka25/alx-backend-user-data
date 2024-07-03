#!/usr/bin/env python3

"""Module for returning log message obfuscated"""
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscates specified fields in a log message."""
    pattern = f"({'|'.join(fields)})=.+?{separator}"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}",
                  message)
