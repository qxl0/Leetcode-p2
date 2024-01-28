class Solution:
    def countKeyChanges(self, s: str) -> int:
        ret = 0
        for i in range(1,len(s)):
            if s[i].lower()!=s[i-1].lower():
                ret += 1
        return ret 
            