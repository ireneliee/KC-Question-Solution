class Node(object):
    def __init__(self, k = None, v = None):
        self.k = k
        self.v = v
        self.next = None
        self.prev = None
    

class LRUCache(object):

    def __init__(self, capacity):
        self.library = {}
        self.capacity = capacity
        self.currCapacity = 0
        
        # most left
        self.oldest = Node("Oldest")
        # most right
        self.latest = Node("Latest")

        # linking oldest and latest together
        self.oldest.next = self.latest
        self.latest.prev = self.oldest
        

    def get(self, key):
        if key in self.library:
            node = self.library[key]
            # before returning must update the 'history' first
            res = node.v
            self.update_to_latest(key)
            return res
        else:
            return -1
        
        

    def put(self, key, value):
        if key in self.library:
            self.update_to_latest(key)
            node = self.library[key]
            node.v = value
        else:
            node = Node(key, value)
            self.insert_to_latest(node)

            self.library[key] = node
            if self.currCapacity == self.capacity:
                oldest_k = self.oldest.next.k
                self.remove(oldest_k)
                self.library.pop(oldest_k)
            else:
                self.currCapacity = self.currCapacity + 1

    def update_to_latest(self, k):
        self.remove(k)
        self.move_to_latest(k)
    
    def remove(self, k):
        node_to_remove = self.library[k]
        previous_node = node_to_remove.prev
        after_node = node_to_remove.next

        previous_node.next = after_node
        after_node.prev = previous_node
    
    def move_to_latest(self, k):
        node_to_move = self.library[k]
        self.insert_to_latest(node_to_move)
    
    def insert_to_latest(self, node):
        latest_node = self.latest.prev
        latest_pointer = self.latest
        latest_node.next = node
        node.prev = latest_node
        latest_pointer.prev = node
        node.next = latest_pointer
    
    def print_node(self):
        res = ""
        node = self.oldest
        while node != None:
            res = res + " -> " + str(node.k)
            node = node.next
        
        print(res)

cache = LRUCache(2)
cache.put(1, 1)
print('Post putting 1')
cache.print_node()
cache.put(2, 2)
print('Post putting 2')
cache.print_node()
print(cache.get(1))
print('Post retrieving 1')
cache.print_node()
cache.put(3, 3)
print('Post putting 3, evicting 2')
cache.print_node()
print(cache.get(2))
print('Post getting 2')
cache.put(4, 4)
print('Post putting 4, evict 1')
cache.print_node()
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

