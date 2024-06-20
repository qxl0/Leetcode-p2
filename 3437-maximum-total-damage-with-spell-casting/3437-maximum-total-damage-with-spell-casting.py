class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        max_dp = 0
        power.sort()
        n = len(power)
        dp = [0]*(n+1)

        j = 0
        for i in range(n):
            if power[i]==power[max(0,i-1)]:
                dp[i+1] = dp[i]+power[i]
            else:                
                while j<n and power[j]+2<power[i]:
                    max_dp = max(max_dp, dp[j+1])
                    j += 1
                # when stop power[j]+2<power[i]
                dp[i+1]=max_dp + power[i]
        return max(dp)