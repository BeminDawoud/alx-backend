#!/usr/bin/python3
""" BaseCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """BaseCache Completes BaseCaching and retrieves items and adds them"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                self.cache_data.pop(first_key)
        return

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
