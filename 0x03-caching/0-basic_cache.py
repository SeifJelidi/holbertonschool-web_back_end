#!/usr/bin/python3
"""basiccache module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def put(self, key, item):
        """adding item in cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """getting item with key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
