class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        last = 0
        for i in range(n-2,-1,-1):
            x = nums[i] + last 
            if x == nums[n-1]:
                continue
            ret += 1
            last += nums[n-1] - x
        return ret