class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ret = 0
        seen = {}
        for r in range(len(s)):
            if s[r] in seen and seen[s[r]]>=l:
                l = seen[s[r]]+1
            else:
                ret = max(ret, r-l+1)
            seen[s[r]] = r 
        return ret 
