class Solution:
    def kInversePairs(self, n: int, K: int) -> int:
        M=10**9+7
        dp = [[0]*(K+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(1,K+1):                
                if j>=i:
                    dp[i][j] = dp[i-1][j] +dp[i][j-1] - dp[i-1][j-i]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n][K]%M