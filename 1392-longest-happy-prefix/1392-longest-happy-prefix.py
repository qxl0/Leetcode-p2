class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        dp = [0]*n
        for i in range(1,n):
            j = dp[i-1]
            while j and s[j]!=s[i]:
                j = dp[j-1] # 
            dp[i] = j +(s[j]==s[i])
        return s[0:dp[n-1]]