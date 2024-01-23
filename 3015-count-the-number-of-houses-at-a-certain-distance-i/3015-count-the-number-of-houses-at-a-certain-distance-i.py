class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        dp = [[inf]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):            
            dp[i][i] = 0
            if i!=n:
                dp[i][i+1] = 1
            if i>1:
                dp[i][i-1] = 1
        dp[x][y] = 1
        dp[y][x] = 1
        
        for k in range(1,n+1):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if dp[i][k] != inf and dp[k][j]!=inf:
                        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
        
        ret = [0]*n
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dp[i][j] == inf: continue
                if i==j: continue
                k = int(dp[i][j])
                ret[k-1] += 1
        return ret 
        