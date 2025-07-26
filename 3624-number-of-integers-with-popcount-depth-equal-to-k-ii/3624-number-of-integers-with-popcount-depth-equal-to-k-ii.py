class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1) # 1,2,...n

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l-1)
class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def getDepth(x):
            ret = 0
            while x!=1:
                x = x.bit_count()
                ret +=1
            return ret
        n = len(nums)
        trees = [FenwickTree(n) for _ in range(64)]
        for i in range(n):
            dep = getDepth(nums[i])
            trees[dep].add(i+1, 1)
        rets = []
        for [op,*args] in queries:
            if op==1:
                l,r,k = args
                rets.append(trees[k].range_sum(l+1, r+1))
            else: # op=2
                idx,val = args
                olddep = getDepth(nums[idx])
                newdep = getDepth(val)
                trees[newdep].add(idx+1, 1)
                trees[olddep].add(idx+1,-1)
                nums[idx] = val
        return rets

        
