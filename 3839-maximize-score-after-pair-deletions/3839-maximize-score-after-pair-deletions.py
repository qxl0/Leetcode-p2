class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n%2==1:
            return sum(nums)-min(nums)
        mn = inf
        for i in range(n-1):
            mn = min(mn, nums[i]+nums[i+1])
        return sum(nums)-mn