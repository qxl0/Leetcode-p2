class Solution:
    def maxScore(self, nums: List[int]) -> int:        
        n = len(nums)
        @cache
        def dfs(i):                        
            if i==n-1:
                return 0
            ret = 0
            for j in range(i+1,n):
                # i->j
                ret = max(ret, (j-i)*nums[j]+dfs(j))
            return ret 
        return dfs(0) 