#!/usr/bin/env python3
"""Regex-ing"""
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        search = field + "=" + ".*?" + separator
        replace = field + "=" + redaction + separator
        message = re.sub(search, replace, message)
    return message
