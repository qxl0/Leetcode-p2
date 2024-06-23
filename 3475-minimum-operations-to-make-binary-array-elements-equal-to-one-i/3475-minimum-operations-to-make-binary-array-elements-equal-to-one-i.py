class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        def flip(i):
            for k in range(i,i+3,1):
                if k<n:
                    nums[k] ^=1
        i = 0
        while i<n:
            if nums[i]==1:
                i += 1
                continue
            if n-1-i<2: return -1
            ret += 1
            flip(i)
            i += 1
        
        return ret 

