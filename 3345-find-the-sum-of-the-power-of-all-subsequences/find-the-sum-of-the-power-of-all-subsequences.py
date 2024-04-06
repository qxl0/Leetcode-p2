class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        """
        sum of power: power of an array: # of subsequence sum()==k 
        return: sum of power of all subsequences of nums   
        dp[i][s][j]: # of subsequences up to nums[:i] with sum==s len==j  
        """
        MOD=10**9+7
        if sum(nums)<k: return 0
        n = len(nums)
        dp = [[[0]*(n+1) for _ in range(k+1)] for _ in range(n+1)]
        
        dp[0][0][0] = 1
        for i in range(1,n+1):              
            for s in range(k+1):                                
                for j in range(i+1):                      
                    dp[i][s][j] = dp[i-1][s][j]
                    if nums[i-1]<=s and j>0:
                        dp[i][s][j] += dp[i-1][s-nums[i-1]][j-1]
                    dp[i][s][j] %= MOD
        ret = 0
        for j in range(1,n+1):
            ret += dp[n][k][j]*pow(2,n-j,MOD)
            ret %= MOD   
        
        return ret 