class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        ret = 0
        n = len(energyDrinkA)
        dp = [[0]*2 for _ in range(n+1)] 
        # dp[i][0]: max boost from ... len: i, last one is from A
        # dp[i][1]: max boost from ... len: i, last one is from B
        
        for i in range(1,n+1):
            dp[i][0] = max(dp[i-1][0] + energyDrinkA[i-1], dp[i-1][1])
            dp[i][1] = max(dp[i-1][1]+energyDrinkB[i-1], dp[i-1][0])

        return max(dp[n])
            
        
