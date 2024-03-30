class Solution:
    def minimumSubarrayLength(self, nums: List[int], K: int) -> int:
        ret = inf                 
        n = len(nums)
        def isspecial(start,end):
            runningsum = 0
            for k in range(start,end+1):
                runningsum |= nums[k] 
            return runningsum>=K 
        for j in range(n):
            for i in range(j,n):
                if isspecial(j,i):
                    ret = min(ret, i-j+1)
        return ret if ret<inf else -1
        
             
            