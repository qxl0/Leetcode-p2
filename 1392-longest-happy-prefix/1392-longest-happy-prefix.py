class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        dp = [0]*n
        
        for i in range(1,n):
            j = dp[i-1]
            while j>=1 and s[j]!=s[i]:
                j = dp[j-1]
            dp[i] = j + (1 if s[j]==s[i] else 0)
        l = dp[n-1]
        if l>=1:
            return s[:l]
        return ""