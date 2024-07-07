class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n

        for i in range(n):
            for j in range(i+1,n):
                dp[j] = max(dp[j], (j-i)*nums[j] + dp[i])
        return dp[n-1]