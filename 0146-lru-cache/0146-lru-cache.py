class LRUCache:

    def __init__(self, capacity: int):
        self.data = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.data: return -1
        ret = self.data.pop(key)
        self.data[key] = ret  # add it to the end, most recently used
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.data: # already in cache
            self.data.pop(key)
        if len(self.data)==self.capacity:
            # remove first one
            self.data.popitem(last=False)  # remove first one
        
        self.data[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)