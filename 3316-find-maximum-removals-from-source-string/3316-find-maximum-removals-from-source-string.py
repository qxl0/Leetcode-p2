class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        m,n = len(source),len(pattern)
        T = set(targetIndices)
        dp = [[0]*(n+1) for _ in range(m+1)]
        # dp[i][j]: result from source[i:] and pattern[j:]

        dp[m][n]=0
        for j in range(n):
            dp[m][j] = -inf
        for i in range(m-1,-1,-1):
            dp[i][n] = dp[i+1][n] + (1 if i in T else 0)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = dp[i+1][j] + (1 if i in T else 0)
                if source[i]==pattern[j]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j+1])
        return dp[0][0]
