class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ret = 1
        cur = 1
        mode = -1  # -1: not decided, 0: down, 1: up 
        n = len(nums)
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                if mode == 0:
                    ret = max(ret, cur)      
                    cur = 1
                mode = 1  
                cur += 1  
            elif nums[i]<nums[i-1]:
                if mode==1: 
                    ret = max(ret, cur)
                    cur = 1
                mode = 0 
                cur += 1
            else:
                ret = max(ret, cur)
                cur = 1
        ret = max(ret, cur)
        return ret   

                 
                