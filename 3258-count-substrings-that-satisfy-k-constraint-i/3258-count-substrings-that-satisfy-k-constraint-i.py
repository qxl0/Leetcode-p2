class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ret = 0
        for i in range(n):
            count0 = 0
            count1 = 0
            for j in range(i,n):
                count0 += (1 if s[j]=='0' else 0)
                count1 += (1 if s[j]=='1' else 0)
                if count0<=k or count1 <=k:
                    ret += 1
        return ret 

