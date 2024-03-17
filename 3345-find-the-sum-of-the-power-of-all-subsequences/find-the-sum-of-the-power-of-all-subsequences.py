class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        if sum(nums)<k: return 0
        n = len(nums)
        MOD=10**9+7
        dp = [[[-1]*(k+1) for _ in range(k+1)] for _ in range(n+1)]        
        def dfs(i, path, sm):            
            if sm<0: return 0
            if i>=n and sm!=0: return 0
            if sm==0:
                return pow(2, n-path, MOD)
            if dp[i][path][sm]!=-1: return dp[i][path][sm]         
            nottake=dfs(i+1, path,sm)            
            take=dfs(i+1, path+1, sm-nums[i])
            dp[i][path][sm] = (take+nottake)%MOD 
            return dp[i][path][sm]
        return dfs(0, 0, k)
        



        
        