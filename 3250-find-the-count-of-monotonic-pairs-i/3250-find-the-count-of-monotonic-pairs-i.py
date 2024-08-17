class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)
        MOD=10**9+7
        dp = [[0]*(mx+1) for _ in range(n+1)]  # dp[i][s]: # of mon pairs of len i with arr1[i-1]=s

        for s in range(nums[0]+1):            
            dp[1][s] = 1
        for i in range(2,n+1):
            for s in range(nums[i-1]+1):
                # arr1[i-1]=s,arr2[i-1]=nums[i-1]-s
                # nums[i], arr1[i]:s,s+1,... arr2[i]=nums[i]-s                
                for p in range(s+1):
                    arr2_s = nums[i-1]-s
                    arr2_p = nums[i-2]-p
                    if arr2_s<=arr2_p:
                        dp[i][s] += dp[i-1][p]
                        
        # print(dp)
        return sum(dp[-1])%MOD