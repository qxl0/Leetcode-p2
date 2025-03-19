class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isok(dp):
            for i in range(len(nums)):
                if not dp[i][nums[i]]:
                    return False
            return True
        m,n = len(nums),len(queries)
        dp = [[False]*1001 for _ in range(m)]
        if m==1 and nums[0]==0: return 0
        for i in range(m):
            dp[i][0] = True
        for k in range(n):
            l,r,v = queries[k]
            for i in range(l,r+1):
                for t in range(1000,0,-1):                    
                    if t>=v and dp[i][t-v]:
                        dp[i][t] = True
            # check
            if isok(dp):
                return k+1
        return -1
                