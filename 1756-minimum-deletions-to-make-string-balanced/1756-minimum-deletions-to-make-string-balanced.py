class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        Bleft = [0]*n
        Bcount = 0
        for i in range(n):
            Bleft[i] = Bcount
            Bcount += (1 if s[i]=='b' else 0)
        Aright = [0]*n
        Acount = 0
        for i in range(n-1,-1,-1):
            Aright[i] = Acount
            Acount += (1 if s[i]=='a' else 0)
        ret = inf
        for i in range(n):
            ret = min(ret, Bleft[i]+Aright[i])
        return ret
