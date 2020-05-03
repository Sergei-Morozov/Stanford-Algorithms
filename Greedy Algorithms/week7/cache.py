"""
The optimal cache
LRU
- least frequently stack - FIFO queue
- hash to check for keys
"""

class LRU:
    def __init__(self):
        self.size = 2
        self.hash = {}
        self.queue = []

    def set(self, key, item):
        """
        insert item in cache
        """
        if key in self.hash:
            self.hash[key] = item
            return

        if len(self.queue) >= self.size:
            least_key = self.queue.pop()
            self.hash.pop(least_key)
        self.hash[key] = item
        self.queue.insert(0, key)

    def get(self, key):
        """
        check if cache contains item
        """
        if key in self.hash:
            print(self.hash[key])
            self.queue.remove(key)
            self.queue.insert(0, key)
            return
        print(-1)

cache = LRU()
cache.set(1, 10); # it will store a key (1) with value 10 in the cache.
cache.set(2, 20); # it will store a key (2) with value 20 in the cache.
cache.get(1); # returns 10
cache.set(3, 30); # evicts key 2 and store a key (3) with value 30 in the cache.
cache.get(2); # returns -1 (not found)
cache.set(4, 40); # evicts key 1 and store a key (4) with value 40 in the cache.
cache.get(1); # returns -1 (not found)
cache.get(3); # returns 30
cache.get(4); # returns 40
