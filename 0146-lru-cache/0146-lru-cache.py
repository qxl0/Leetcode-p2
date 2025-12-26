class Node:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.Map = {} # key -> Node
        self.left,self.right = Node(0,0),Node(0,0) # left: LRU, right: most recently visited
        self.left.next = self.right  
        self.right.prev = self.left

    def remove(self, node):
        # 
        k = node.key
        if k not in self.Map:
            return 
        # in Map 
        del self.Map[k]
        # in duble linked list 
        p = node.prev 
        n = node.next 
        p.next = n 
        n.prev = p
    def add(self,node):
        # add to head 
        temp = self.right.prev
        temp.next = node 
        node.next = self.right        
        node.prev = temp
        self.right.prev = node  
        self.Map[node.key] = node 
    def get(self, key: int) -> int:
        if key not in self.Map:
            return -1
        cur = self.Map[key]
        self.remove(cur)
        self.add(cur)
        return cur.val

    def put(self, key: int, value: int) -> None:
        if key in self.Map:
            cur = self.Map[key]
            cur.val = value
            self.remove(cur)             
        else:
            cur = Node(key, value)
        # check if capcacity 
        if len(self.Map)>=self.cap:
            self.remove(self.left.next)            
        self.add(cur)
        self.Map[key] = cur
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)