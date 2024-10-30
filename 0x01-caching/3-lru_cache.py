#!/usr/bin/env python3
""" LRUCache module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache defines a Least Recently Used (LRU) caching system."""

    def __init__(self):
        """ Initialize the LRU cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using the LRU policy."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key, and mark it as recently used."""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
