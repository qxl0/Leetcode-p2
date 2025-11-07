class TimeMap:

    def __init__(self):
        self.time = {}
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
            self.time[key] = []
        self.data[key].append(value)
        self.time[key].append(timestamp)        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        possible = self.time[key]
        pos = bisect_right(possible, timestamp)-1
        if pos>=0:
            return self.data[key][pos]
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)