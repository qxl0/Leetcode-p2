class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        s1 = '#' + s1
        s2 = '#' + s2

        # dp[i][j]: minimum length k such that s2[1:j] is subsequence of s1[i-k+1:i] 
        dp = [[inf]*(n+1) for _ in range(m+1)]
        for i in range(m):
            dp[i][0]=0
        for j in range(n):
            dp[0][j] = inf
        dp[0][0] = 0
        for i in range(1,m+1):
            for j in range(1, n+1):
                if s1[i]==s2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i-1][j] + 1
        
        # ans, dp[][n]  
        l = inf
        pos = 0
        for i in range(1,m+1):
            if dp[i][n] < l:
                l = dp[i][n]
                pos = i
        if l == inf:
            return ""
        return s1[pos-l+1:pos+1]
                
        