class DSU:
    def __init__(self,n):
        self.fathers = [i for i in range(n+1)]
        self.components = n

    def findFather(self,x):
        px = self.fathers[x]
        if x==px:
            return px
        self.fathers[x] = self.findFather(px)
        return self.fathers[x]
    def union(self, x, y):
        px,py = self.findFather(x), self.findFather(y)
        if px==py: return False 
        if px<py:
            self.fathers[py] = px 
        else:
            self.fathers[px] = py
        self.components -= 1
        return True
    def isconnected(self):
        return self.components == 1
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsuA = DSU(n)
        dsuB = DSU(n)
        edges.sort(key=lambda x:x[0], reverse=True)
        needed = 0
        for tp,u,v in edges:
            if tp==3:
                retA = dsuA.union(u, v)
                retB = dsuB.union(u, v)
                needed += (1 if retA or retB  else 0)
        for tp,u,v in edges:
            if tp==1:
                needed += (1 if dsuA.union(u, v) else 0)
            elif tp==2:
                needed += (1 if dsuB.union(u, v) else 0)
        if dsuA.isconnected() and dsuB.isconnected():
            return len(edges)-needed
        return -1
