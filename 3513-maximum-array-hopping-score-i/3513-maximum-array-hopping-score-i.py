class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n

        for i in range(n):
            for j in range(i):
                dp[i] = max(dp[i], (i-j)*nums[i] + dp[j])
        return dp[n-1]