class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        
        vals = sorted(count.keys())
        n = len(vals)
        dp = [0]*n

        dp[0] = vals[0]*count[vals[0]]
        for i in range(1,n):
            cur = vals[i]
            freq = count[cur]
            curpower = cur*freq

            dp[i] = dp[i-1]
            # find prev with no conflict with cur 
            j = i-1
            while j>=0 and vals[j] in [cur-1,cur-2,cur+1,cur+2]:
                j -= 1
            if j>=0:
                dp[i] = max(dp[i], dp[j]+curpower)
            else:
                dp[i] = max(dp[i], curpower)
        return dp[n-1]