#!/usr/bin/envv python3
"""FIFOcache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """

    def __init__(self):
        """ Initialize the FIFO cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using FIFO policy """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # FIFO: remove the first item added
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD {first_key}")

        # add new key and item
        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
