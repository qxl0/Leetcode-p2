class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        """
        dp[i][j]: max strength i subarrays, up to j index 
        """
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(k+1)]

        for i in range(1,k+1):
            multiplier = k+1-i if i%2==1 else i-k-1
            maxsum,cur = -inf,-inf
            for j in range(i-1,n):
                cur = max(cur+nums[j]*multiplier, dp[i-1][j]+nums[j]*multiplier)
                maxsum = max(maxsum, cur)
                dp[i][j+1] = maxsum

        return dp[k][n]