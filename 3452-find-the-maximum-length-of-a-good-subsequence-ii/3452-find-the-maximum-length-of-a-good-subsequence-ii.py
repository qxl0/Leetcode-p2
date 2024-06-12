class Solution:
    def maximumLength(self, nums: List[int], K: int) -> int:
        n = len(nums)
        dp = [[-1]*(K+1) for _ in range(n+1)]
        
        prevmax = [0]*n
        for k in range(K+1):
            Map = defaultdict(int)
            curmax = [0]*n

            for i in range(n-1,-1,-1):
                dp[i][k] = max(1+Map[nums[i]], 1+ (prevmax[i+1] if i+1<n else 0) )
                
                Map[nums[i]] = max(Map[nums[i]], dp[i][k])
                # save to Map   
                curmax[i] = max(dp[i][k], (curmax[i+1] if i+1<n else 0))
            prevmax = curmax 
        ret = 0
        for i in range(n):
            ret = max(ret, dp[i][k])

        return ret 