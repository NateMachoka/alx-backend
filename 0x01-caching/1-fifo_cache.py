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

        if key not in self.cache_data and len(
                self.cache_data) >= BaseCaching.MAX_ITEMS:
            # FIFO: remove the first item added
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD {first_key}")

        # If key already exists, remove it from `order`, reinsert it at the end
        if key in self.cache_data:
            self.order.remove(key)

        # Add or update the item in cache
        self.cache_data[key] = item
        self.order.append(key)  # Append key to maintain order

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
