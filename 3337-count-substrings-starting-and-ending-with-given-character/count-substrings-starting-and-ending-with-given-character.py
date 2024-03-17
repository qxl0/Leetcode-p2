class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        n= len(s)
        cloc = [i for i in range(n) if s[i]==c]
        ret = 0
        for i,ch in enumerate(s):
            if ch==c: 
                # find how many in cloc st. >=i       
                pos = bisect_left(cloc, i)
                ret += len(cloc)-pos 
        return ret 