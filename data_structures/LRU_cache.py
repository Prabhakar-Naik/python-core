"""
LRU Cache Implementation
Use OrderedDict or LinkedHashMap to maintain insertion order and efficiently remove least recently used items.

Input: cache = LRU_Cache(2), operations = [get(2), put(2,6), get(1), put(1,5), put(1,2), get(1), get(2)]
Output: [-1, -1, 5, 2, -1]

Approach: Use a dictionary to store key-value pairs and a list to maintain access order.
When cache is full, remove the least recently used item (from the front of the list).

Design and implement an LRU (Least Recently Used) Cache.
The cache should support the following operations:
get(key): Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value): Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
The LRUCache class must support both get and put in O(1) time complexity.

"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # 1
lru.put(3, 3)
print(lru.get(2))  # -1