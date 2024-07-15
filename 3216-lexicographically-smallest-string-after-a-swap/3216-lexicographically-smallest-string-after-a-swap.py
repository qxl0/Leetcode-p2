class Solution:
    def getSmallestString(self, s: str) -> str:
        ret = [int(c) for c in s]
        n = len(s)
        for i in range(n-1):
            if ret[i]%2==ret[i+1]%2 and ret[i]>ret[i+1]:
                ret[i],ret[i+1] = ret[i+1],ret[i]
                break
        return "".join([str(c) for c in ret])

        