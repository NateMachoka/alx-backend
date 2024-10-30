#!/usr/bin/env python3
"""LFUCache module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache defines a Least Frequently Used (LFU) caching system."""

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.frequency = {}  # Track the frequency of each key
        self.order = []  # Track the order of keys with the same frequency

    def put(self, key, item):
        """Add an item in the cache using the LFU policy."""
        if key is None or item is None:
            return

        # Update the item if the key already exists
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1  # Increase the frequency count
            self.order.remove(key)  # Update order to mru
            self.order.append(key)
        else:
            # If cache is full, we need to remove the lfu item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item(s)
                min_freq = min(self.frequency.values())
                lfu_keys = [
                    k for k, v in self.frequency.items() if v == min_freq]

                # Use LRU among the least frequently used keys
                lfu_key = lfu_keys[0]
                for k in lfu_keys:
                    if k in self.order:
                        lfu_key = k
                        break

                # Discard the least frequently used item
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add the new item to cache
            self.cache_data[key] = item
            self.frequency[key] = 1  # Initialize frequency
            self.order.append(key)  # Mark as most recently used

    def get(self, key):
        """Get an item by key and mark it as recently used."""
        if key is None or key not in self.cache_data:
            return None

        # Increase frequency and mark as recently used
        self.frequency[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
