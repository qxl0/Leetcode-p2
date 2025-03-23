class UnionFind:
    def __init__(self, n):
        self.Father = [i for i in range(n + 1)]

    def findFather(self, x):
        if self.Father[x] != x:
            self.Father[x] = self.findFather(self.Father[x])
        return self.Father[x]

    def Union(self, x, y):
        px, py = self.findFather(x), self.findFather(y)
        if px < py:
            self.Father[py] = px
        else:
            self.Father[px] = py

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        pSet = [set(properties[i]) for i in range(n)]
        def isintersect(i,j):
            return len(pSet[i].intersection(pSet[j]))>=k
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1,n):
                if isintersect(i,j):
                    uf.Union(i, j)
        ans = 0
        Set = set()
        for i in range(n):
            f = uf.findFather(i)
            if f not in Set:
                ans += 1
                Set.add(f)
        return ans
        