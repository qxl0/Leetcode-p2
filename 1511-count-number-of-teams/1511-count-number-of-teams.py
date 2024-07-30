class FenwickTree:
    def __init__(self,n):
        self.sums = [0]*(n+1)
    def update(self, i, delta):
        while i<len(self.sums):
            self.sums[i]+= delta
            i += self.lowbit(i)
    def lowbit(self, x):
        return x&(-x)
    def query(self,i):
        ret = 0
        while i>0:
            ret += self.sums[i]
            i -= self.lowbit(i)
        return ret 
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        mx = max(rating)
        left = FenwickTree(mx+1)
        right = FenwickTree(mx+1)
        for x in rating:
            right.update(x, 1)
        ret = 0
        for i in range(n):
            val = rating[i]
            right.update(val,-1)  # remove             
            ret += left.query(val-1)*(right.query(mx)-right.query(val))
            ret += (left.query(mx)-left.query(val))*right.query(val-1)

            left.update(val,1)
        return ret 
