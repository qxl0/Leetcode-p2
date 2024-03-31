class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        p = nums[0]
        ret = 1
        cur = 1
        for x in nums[1:]:            
            if x!=p:
                cur +=1
            else: 
                cur = 1
            ret += cur 
            p = x      
        return ret 