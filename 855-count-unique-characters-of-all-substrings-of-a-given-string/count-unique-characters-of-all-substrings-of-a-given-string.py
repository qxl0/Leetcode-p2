class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        seen = [-1]*26
        prefix = []
        for i,ch in enumerate(s):
            prefix.append(seen[ord(ch)-ord('A')])
            seen[ord(ch)-ord('A')] = i
        seen = [n]*26
        suffix = []
        for i in range(n-1,-1,-1):
            ch = s[i]
            suffix.append(seen[ord(ch)-ord('A')])
            seen[ord(ch)-ord('A')] = i
        suffix = suffix[::-1]
        ret = 0
        for i in range(n):
            ret += (i-prefix[i])*(suffix[i]-i)
        return ret 