class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        
        n  = len(rewardValues)
        dp = [defaultdict(int) for _ in range(n+1)]
        def dfs(i,cur):        
            if i>=n:
                return cur 
            if cur in dp[i]: return dp[i][cur]
            # take, no take
            ans = 0
            if cur<rewardValues[i]:
                ans = max(ans,dfs(i+1, cur+rewardValues[i]))
                ans = max(ans, dfs(i+1, cur))
            else:
                ans = max(ans, dfs(i+1, cur))
            dp[i][cur]= ans 
            return ans 
        return dfs(0,0)
        