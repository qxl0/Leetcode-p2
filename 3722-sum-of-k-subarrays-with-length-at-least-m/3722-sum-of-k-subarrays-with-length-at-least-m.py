class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        pre = list(accumulate(nums,initial=0))
        @cache
        def dp(i,k, canextend): # max sum
            if n-i<k*m:
                return -inf
            if i==n:
                return 0 if k==0 else -inf
            ans = dp(i+1, k, False)
            if canextend:
                ans = max(ans, dp(i+1,k, True) + nums[i])
            if k>0 and i+m<=n:
                ans = max(ans, dp(i+m,k-1,True) + pre[i+m]-pre[i])
            return ans
        ans= dp(0,k,False)
        dp.cache_clear()
        return ans
