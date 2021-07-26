#!/usr/bin/python3
""" fifocache """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """fifoache class"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """adding an item cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            ItemToDiscard = sorted(self.cache_data)[0]
            print('DISCARD: {}'.format(ItemToDiscard))
            self.cache_data.pop(ItemToDiscard)
        self.cache_data[key] = item

        def get(self, key):
            """ gettingGet item with key"""
            if key is None or key not in self.cache_data.keys():
                return None
            return self.cache_data[key]
