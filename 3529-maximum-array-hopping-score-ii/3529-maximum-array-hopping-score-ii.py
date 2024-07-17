class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        mx = 0
        for i in range(n-1,0,-1):
            if nums[i]>mx:
                mx = nums[i]
            ret += mx
        return ret 