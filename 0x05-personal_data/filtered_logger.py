#!/usr/bin/env python3
"""Regex-ing"""
import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Log formatter"""
        form = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION, form, self.SEPARATOR)


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


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    sh = logging.StreamHandler()
    sh.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(sh)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', "root")
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', "")
    host = os.getenv('PERSONAL_DATA_DB_HOST', "localhost")
    name = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connect(user=username, password=password,
                                   host=host,
                                   database=name)


def main():
    """main function"""
    db_connection = get_db()
    q = connect.cursor()
    q.execute("SELECT * FROM users")
    data = q.fetchall()
    logger = get_logger()

    for r in data:
        m = "name=" + r[0] + "; " + "email=" + r[1] + "; "
        + "phone=" + r[2] + "; " + "ssn=" + r[3] + "; "
        + "password=" + r[4] + "; " + "ip=" + r[5] + "; "
        + "last_login=" + r[6] + "; " + "user_agent=" + r[7] + ";"
        logger.info(m)

    q.close()


if __name__ == "__main__":
    main()
