class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)        
        reach = 0
        for i,x in enumerate(nums):
            if reach>=i:
                reach = max(reach, i+nums[i])
            if reach >=n-1:
                return True
        return False