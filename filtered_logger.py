#!/usr/bin/env python3
"""Module for returning log message obfuscated"""
import re; def filter_datum(fields, redaction, message, separator): return re.sub(f"({'|'.join(fields)})=.+?{separator}", lambda m: f"{m.group(1)}={redaction}{separator}", message)

