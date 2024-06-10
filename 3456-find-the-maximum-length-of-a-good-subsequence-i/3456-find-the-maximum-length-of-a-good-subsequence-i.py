class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def dfs(k,i):
            if k<0 or i>=n: return 0
            ans = 0
            for j in range(i+1,n):
                if nums[j]==nums[i]:
                    ans = max(ans, dfs(k,j))
                else:
                    ans = max(ans, dfs(k-1,j))
            return 1+ans
        ret = 0
        for i in range(n):
            ret = max(ret, dfs(k,i))
        
        return ret