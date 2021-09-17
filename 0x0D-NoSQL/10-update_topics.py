#!/usr/bin/env python3
"""
func that change topics of school doc
"""


def update_topics(mongo_collection, name, topics):
    """update topics """
    st = {"name": name}
    ch = {"$set": {"topics": topics}}
    mongo_collection.update_many(st, ch)
