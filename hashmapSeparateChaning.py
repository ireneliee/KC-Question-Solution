class HashMap:
    
    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0


    def put(self, key, value):                                     
        bucket_index = self.get_bucket_index(key)   

        new_node = LinkedListNode(key, value)                       
        head = self.bucket_array[bucket_index]             


        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        
       
        head = self.bucket_array[bucket_index]
        new_node.next = head                                         
        self.bucket_array[bucket_index] = new_node                  
        self.num_entries += 1
        
    def get(self, key):
        bucket_index = self.get_bucket_index(key) 
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
        
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index
    
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                      
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   

        return hash_code % num_buckets                                
    
    def size(self):
        return self.num_entries
    
    # Helper function to see the hashmap
    def __repr__(self):
        output = "\nLet's view the hash map:"

        node = self.bucket_array
        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next
                    
        return output