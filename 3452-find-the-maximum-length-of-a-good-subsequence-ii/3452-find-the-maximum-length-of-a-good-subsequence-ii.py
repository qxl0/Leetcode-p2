class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:        
        """
        res[i]: max length of subsequence with i nonequals 
        dp[i][a]: max length of subsequence ending in a with i nonequals  
        """
        dp = [Counter() for _ in range(k+1)]
        res = [0]*(k+1)
        for a in nums:
            for i in range(k,-1,-1):
                dp[i][a] = max(dp[i][a]+1, (res[i-1] if i>0 else 0)+1)
                res[i] = max(res[i], dp[i][a])
        return res[k]
