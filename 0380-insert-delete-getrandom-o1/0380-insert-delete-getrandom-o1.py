class RandomizedSet:

    def __init__(self):
        self.data = []
        self.map = {}        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.map)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        
        val2 = self.data[-1]
        self.data[idx] = val2
        self.map[val2] = idx
        
        del self.map[val]
        self.data.pop()
        
        return True

    def getRandom(self) -> int:
        return choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()