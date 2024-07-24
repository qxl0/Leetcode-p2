class Solution:
    def maxOperations(self, s: str) -> int:
        ret = 0
        cur = 0
        cancount = True
        for i,ch in enumerate(s):
            if ch=='1':
                cur += 1
                cancount = True
            elif cancount:
                ret += cur
                cancount = False
        return ret
