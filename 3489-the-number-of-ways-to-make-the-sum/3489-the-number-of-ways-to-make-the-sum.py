class Solution:
    def numberOfWays(self, n: int) -> int:
        coins = [1,2,6]
        dp = [[0]*(n+1) for _ in range(3)]
        MOD = 10**9+7
        
        for i in range(3):
            dp[i][0]=1
        for i in range(3):  # coin  1,2,6
            for j in range(1,n+1): # capacity 
                dp[i][j] += (dp[i-1][j] if i>0 else 0)
                if j>=coins[i]:
                    dp[i][j] += (dp[i][j-coins[i]] if i>0 else 1)
            # print(f'i={i}', dp[i])
        res = dp[2][n]
        if n-4>=0:
            res += dp[2][n-4]
        if n-8>=0:
            res += dp[2][n-8]
        
        return res%MOD