class Solution:
    def minOperations(self, k: int) -> int:
        if k==1: return 0
        if k==2: return 1
        ret = inf 
        for x in range(2,ceil(k/2)+1):
            y=ceil(k/x)
            if x*y>=k: 
                ret = min(ret, x+y-2)
        return ret 
