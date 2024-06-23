class Solution:
    def minOperations(self, nums: List[int]) -> int:        
        ret = 0
        n = len(nums)
        flipbit = 0
        
        i = 0
        while i<n:
            cur = nums[i]^flipbit
            if cur==1:
                i += 1
                continue            
            ret += 1
            flipbit ^=1
            i += 1
        
        return ret 
