"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""


class LRUCache:

    def __init__(self, capacity):
        self.cache = {}  # the LRU cache
        self.cap = capacity  # initialising the cache with the given capacity
        self.recently_used = {}  # a dictionary for maintaining the record of recently used elements of cache

    def put(self, key, val):  # Function for putting the key value pair in the cache
        cur_cap = len(self.cache)
        if key in self.cache:
            self.cache[key] = val
            self.recently_used.pop(key)
            self.recently_used[key] = None
        else:
            if cur_cap < self.cap:
                self.cache[key] = val
                self.recently_used[key] = None
            else:
                least_used = list(self.recently_used)[0]
                # popping out the least used from recently used
                self.recently_used.pop(least_used)

                # and also popping out the least used from recently used
                self.cache.pop(least_used)

                self.cache[key] = val
                self.recently_used[key] = None

    def get(self, key):  # Function for getting the value from the cache for the given key
        if key in self.cache:
            self.recently_used.pop(key)
            self.recently_used[key] = None
            return self.cache[key]
        else:
            return -1
