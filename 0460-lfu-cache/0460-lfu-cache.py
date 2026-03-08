class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = self.next = None
        self.freq = 1
class DLinkedList:
    def __init__(self):
        self.sentinel = Node()
        # prev: head, next: end
        self.sentinel.prev = self.sentinel.next = self.sentinel
        self.size = 0

    def append(self, node):
        # add to the end 
        # set node
        node.next = self.sentinel.next
        node.prev = self.sentinel
        # point to node
        self.sentinel.next.prev = node
        self.sentinel.next = node

        self.size += 1

    def pop(self, node = None):
        # pop from head
        if not node:
            node = self.sentinel.prev
        # remove node
        # [p] <-> node <-> [n]
        # node.prev, node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.freq2list = defaultdict(DLinkedList)
        self.key2node = {}
        self.minFreq = 0
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        self.update(node)
        return node.val
    
    

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return 
        # check key 
        if key in self.key2node:
            node = self.key2node[key]
            self.update(node)
            node.val = value
            return 
        # check cap reached?
        if self.size == self.cap:
            node = self.freq2list[self.minFreq].pop()
            del self.key2node[node.key]
            self.size -= 1
        # create node
        node = Node(key, value)
        self.key2node[key] = node
        self.freq2list[1].append(node)
        self.minFreq = 1
        self.size += 1
    def update(self, node):
        # 
        freq = node.freq
        self.freq2list[freq].pop(node)
        if self.minFreq == freq and self.freq2list[freq].size == 0:
            self.minFreq += 1
        node.freq += 1
        freq = node.freq
        self.freq2list[freq].append(node)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)