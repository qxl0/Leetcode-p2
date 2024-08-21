class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        ret = 0
        n = len(energyDrinkA)
        dp0,dp1 = 0,0
        # dp[i][0]: max boost from ... len: i, last one is from A
        # dp[i][1]: max boost from ... len: i, last one is from B
        
        for i in range(1,n+1):
            dp0_new = max(dp0+energyDrinkA[i-1], dp1)
            dp1 = max(dp1+energyDrinkB[i-1], dp0)
            dp0 = dp0_new

        return max(dp0,dp1)
            
        
