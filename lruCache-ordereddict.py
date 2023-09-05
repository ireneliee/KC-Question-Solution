
from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        self.library = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.library:
            self.library.move_to_end(key)
            return self.library[key]
        else:
            return -1
        
    def put(self, key, value):
        self.library[key] = value
        self.library.move_to_end(key)
        if len(self.library) > self.capacity:
            self.library.popitem(last = False)

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))