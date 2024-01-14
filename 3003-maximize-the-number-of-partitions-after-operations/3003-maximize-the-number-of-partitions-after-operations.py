class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        @lru_cache(None)
        def dfs(i,mask,canchange): # max number of resulting partitions after ops on s up to i index
            if i==n: return 1
            res = 0
            # add ith bit
            ichar=ord(s[i])-ord('a')
            newmask = mask|(1<<ichar)
            if newmask.bit_count()>k:
                res = 1+dfs(i+1, (1<<ichar), canchange)
            else:
                res = dfs(i+1, newmask, canchange)
            if canchange:
                # change to what???
                for j in range(26):
                    newmask = mask|(1<<j)
                    if newmask.bit_count()>k:
                        res = max(res, 1+dfs(i+1,(1<<j), False))
                    else:
                        res = max(res, dfs(i+1, newmask, False))
                        
            return res
        return dfs(0,0,True)