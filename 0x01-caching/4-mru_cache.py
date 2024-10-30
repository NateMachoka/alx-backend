#!/usr/bin/env python3
"""MRUCache module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache defines a Most Recently Used (MRU) caching system."""

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()
        self.order = []  # List to keep track of the access order of keys

    def put(self, key, item):
        """Add an item in the cache using the MRU policy."""
        if key is None or item is None:
            return

        # If the key is already in cache, update the item
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # If the cache is at its limit, remove the most recently used item
            mru_key = self.order.pop()  # mru item is at the end of the list
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add the new item and mark it as the most recently used
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key and mark it as recently used."""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the order list to mark it as mru
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
