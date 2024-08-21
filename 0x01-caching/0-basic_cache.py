#!/usr/bin/python3
""" BaseCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BaseCache Completes BaseCaching and retrieves items and adds them"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
        return

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
