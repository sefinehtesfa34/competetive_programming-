from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self.hashmap[key] = self.hashmap.pop(key)
        return self.hashmap[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            if len(self.hashmap) == self.capacity:
                self.hashmap.popitem(last = False)
        else:
            self.hashmap.pop(key)
            
        self.hashmap[key] = value
        
        
        
                
        
        
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)