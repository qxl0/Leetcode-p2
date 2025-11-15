class FreqStack:

    def __init__(self):
        self.data = Counter()
        self.stacks = defaultdict(list)
        self.max = 0

    def push(self, val: int) -> None:
        self.data[val] += 1
        freq = self.data[val]
        if freq>self.max:
            self.max = freq            
        self.stacks[freq].append(val)

    def pop(self) -> int:
        val = self.stacks[self.max].pop()
        self.data[val] -= 1
        if not self.stacks[self.max]:
            self.max -= 1

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()