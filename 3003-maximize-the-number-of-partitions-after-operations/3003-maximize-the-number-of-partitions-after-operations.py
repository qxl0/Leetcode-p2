class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        @lru_cache(None)
        def dfs(idx,mask,canChange):
            # return the max partitions from idx to end in string s 
            if idx == n: return 0
            
            res = 0
            curCharIdx = ord(s[idx])-ord('a')
            newMask = mask | (1<<curCharIdx)
            distinctCount = newMask.bit_count()
            if distinctCount>k:
                res = 1 + dfs(idx+1, 1<<curCharIdx, canChange)
            else:
                res = dfs(idx+1, newMask, canChange)
            if canChange:
                # try change curChar to any of the 26
                for i in range(26):
                    if i==curCharIdx:continue
                    newMask = mask | (1<<i)
                    distinctCount = newMask.bit_count()
                    if distinctCount>k:
                        res = max(res, 1 + dfs(idx+1,1<<i,False))
                    else:
                        res = max(res, dfs(idx+1,newMask,False))
            return res
        return dfs(0,0,True)+1
                
            
                
            
            