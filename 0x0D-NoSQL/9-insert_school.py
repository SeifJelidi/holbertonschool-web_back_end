#!/usr/bin/env python3
"""
insert a document using Python
"""


def insert_school(mongo_collection, **kwargs):
    """ insert document into collection"""
    return mongo_collection.insert_one(kwargs).inserted_id
