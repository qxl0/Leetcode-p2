class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        dp = [[inf/2]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=0
        for u,v,w in edges:
            dp[u][v] = w
            dp[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
        ans = -1
        cnt = inf/2
        for i in range(n):
            cur = 0
            for j in range(n):
                if i==j: continue
                if dp[i][j]<=distanceThreshold:
                    cur += 1
            if cur<=cnt:
                cnt = cur
                ans = i
        return ans