class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        # [0,1,2,.. n-1 ]
        MOD=10**9+7
        mp = {e+1:c for e,c in requirements}

        dp = [[0]*401 for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(401):
                for k in range(i):
                    if j>=k:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-k])%MOD
            if i in mp:
                tmp = mp[i]
                for j in range(401):
                    if j!=tmp:
                        dp[i][j] = 0
        ans = 0
        for i in range(401):
            ans += dp[n][i]
            ans %=MOD
        return ans
