class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def findlps(s):
            n = len(s)
            lps = [0]*n
            for i in range(1,n):
                j = lps[i-1]
                while j>0 and s[j]!=s[i]:
                    j = lps[j-1]
                # stop 
                lps[i] = j+(1 if s[j]==s[i] else 0)
            return lps
        lps = findlps(needle)
        
        n,m = len(haystack),len(needle)
        dp = [0]*n
        dp[0] = (1 if haystack[0]==needle[0] else 0)
        for i in range(1,n):
            j = dp[i-1]
            while j>0 and (j==m or haystack[i]!=needle[j]):
                j = lps[j-1]
            dp[i] = j + (1 if haystack[i]==needle[j] else 0)
        for i in range(n):
            if dp[i]==m:
                return i-m+1
        return -1
