class MinStack:

    def __init__(self):
        self.data = []        

    def push(self, val: int) -> None:        
        cur = self.data[-1][1] if self.data else inf
        self.data.append((val, min(cur,val)))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()