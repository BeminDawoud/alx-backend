#!/usr/bin/python3
""" BaseCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """BaseCache Completes BaseCaching and retrieves items and adds them"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

        return

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
