class FenwickTree:
    def __init__(self,n):
        self.n = n
        self.data = [0]*(n+1)
    def lowbit(self,x):
        return x & (-x)
    def update(self,i,t):
        while i <= self.n:
            self.data[i] += t
            i += self.lowbit(i)
    def query(self,i):
        ret = 0
        while i>0:
            ret += self.data[i]
            i -= self.lowbit(i)
        return ret
    def rangesum(self, l, r):
        if l>r: return 0
        return self.query(r)-self.query(l-1)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        lower<=P[i]-P[j]<=upper
        P[i]-upper<=P[j]<=P[i]-lower
        scan P[i], find P[j] in range [P[i]-upper, P[i]-lower]
        '''
        n = len(nums)        
        # 1. get presum
        P = [0]*(n+1)
        for i in range(n):
            P[i+1] = P[i] + nums[i]
        # 2. Coordinate compression over values
        vals = []
        for v in P:
            vals.append(v)
            vals.append(v-lower)
            vals.append(v-upper)
        Map = {x:(i+1) for i,x in enumerate(sorted(set(vals)))}
        # x=>index from 1
        N = len(Map)
        tree = FenwickTree(N)
        tree.update(Map[P[0]], 1)
        ans = 0
        for i in range(1,n+1):
            k = Map[P[i]]
            print(f'{i}: {k-upper}, {k-lower}')
            ans += tree.rangesum(Map[P[i]-upper], Map[P[i]-lower])
            tree.update(k, 1)
        return ans
