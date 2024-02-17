class UnionFind:
    def __init__(self,n):
        self.father = [i for i in range(n)]
    def findFather(self,x):
        px = self.father[x]
        if px != x:
            self.father[x] = self.findFather(px)
        return self.father[x]
    def union(self,x,y):
        px,py = self.findFather(x), self.findFather(y)
        if px == py: return False
        if px<py:
            self.father[py] = px
        else:
            self.father[px] = py
        return True
    def __str__(self):
        return f"UF:{self.father}"
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        ret = 0
        for i in range(n):
            if uf.father[i] == i:
                ret += 1
        return ret
        