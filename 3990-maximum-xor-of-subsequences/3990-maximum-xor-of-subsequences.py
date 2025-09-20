class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        basis = [0]*32        
        for x in nums:
            for i in range(31,-1,-1):
                if (x>>i)&1==0:
                    continue
                if basis[i]!=0:
                    x ^= basis[i]
                else:
                    basis[i] = x
                    break
        ret = 0
        for i in range(31,-1,-1):
            ret = max(ret, ret^basis[i])
        return ret
