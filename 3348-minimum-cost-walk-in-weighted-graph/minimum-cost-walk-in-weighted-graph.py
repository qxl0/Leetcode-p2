class UnionFind:
    def __init__(self,n):
        self.n = n
        self.data = [i for i in range(n+1)]        
        self.result = [(1<<32)-1 for i in range(n+1)]

    def find(self,x):
        px = self.data[x]
        if px!=x:
            self.data[x] = self.find(px)
        return self.data[x]
    def union(self,x,y,w):
        px,py = self.find(x),self.find(y)
        if px==py: 
            self.result[px] = self.result[px]&w if self.result[px]!=-1 else w 
            return False 
        if px<py:
            self.data[py] = px
            self.result[py] &=w               
            self.result[px] &= self.result[py]
        else:
            self.data[px] = py
            self.result[px] &= w            
            self.result[py] &= self.result[px]
        return True 
    def get(self,x):
        px = self.find(x)
        return self.result[px]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        for x,y,w in edges:
            uf.union(x,y,w)
        ans = [-1]*len(query)
        for i, (u,v) in enumerate(query):
            if u==v: 
                ans[i]=0
                continue
            pu = uf.find(u)
            pv = uf.find(v)
            if pu==pv:
                ans[i] = uf.get(pu)
        return ans 