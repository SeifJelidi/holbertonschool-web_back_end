#!/usr/bin/env python3
"""
list all documents using Python
"""


def list_all(mongo_collection):
    """list all doc of collection"""
    return mongo_collection.find()
