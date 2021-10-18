#!/usr/bin/env python3
"""web module"""
from typing import Callable
import requests
import redis
from functools import wraps

redis_object = redis.Redis()


def count_req(method: Callable) -> Callable:
    """Count Request"""

    @wraps(method)
    def wrapper(link):
        """Wrapper method"""
        redis_object.incr("count:{}".format(link))
        c = redis_object.get("cached:{}".format(link))
        if c:
            return c.decode('utf-8')
        r = method(link)
        redis_object.setex("cached:{}".format(link), 10, r)
        return r

    return wrapper


@count_req
def get_page(url: str) -> str:
    """get_page"""
    request = requests.get(url)
    return request.text
