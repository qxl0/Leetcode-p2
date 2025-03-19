class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:        
        m,n = len(nums),len(queries)
        dp = [[False]*1001 for _ in range(m)]
        def isok(nums):
            for i in range(len(nums)):
                if not dp[i][nums[i]]:
                    return False
            return True
        
        for i in range(m):
            dp[i][0] = True

        if isok(nums): return 0

        for k in range(n):
            l,r,v = queries[k]
            for i in range(l,r+1):
                for t in range(1000,0,-1):                    
                    if t>=v and dp[i][t-v]:
                        dp[i][t] = True
            # check
            if isok(nums):
                return k+1
        return -1
                