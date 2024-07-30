class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def findlsp(s):
            n = len(s)
            dp = [0]*n
            for i in range(1,n):
                j = dp[i-1]
                while j>0 and s[i]!=s[j]:
                    j = dp[j-1]
                dp[i] = j+(1 if s[i]==s[j] else 0)
            return dp
        lsp = findlsp(needle)
        m,n = len(needle),len(haystack)
        dp = [0]*n # dp[i]: length of max substring in haystack[:i] which is prefix of needle
        dp[0] = (1 if haystack[0]==needle[0] else 0)
        for i in range(1,n):
            j = dp[i-1]
            while j>0 and (j==m or haystack[i]!=needle[j]):
                j = lsp[j-1]
            dp[i] = j + (1 if haystack[i]==needle[j] else 0)
        for i in range(n):
            if dp[i]==m:
                return i-m+1
        return -1