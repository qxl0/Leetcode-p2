class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp0 = [[0]*n for _ in range(n+1)]
        dp1 = [[0]*n for _ in range(n+1)]
        presum = [[0]*n for _ in range(n+1)]

        for j in range(n):
            for i in range(1,n+1):
                presum[i][j] = presum[i-1][j] + grid[i-1][j]
        
        for j in range(1,n): # col
            for i in range(n+1):  # row 
                for black in range(n+1): # black row 
                    pv = presum[i][j-1]-presum[black][j-1] if i > black else 0
                    cv = presum[black][j] - presum[i][j] if i < black else 0
                    dp1[i][j] = max(dp1[i][j], pv+dp1[black][j-1], dp0[black][j-1])
                    dp0[i][j] = max(dp0[i][j], cv+pv+dp1[black][j-1], cv+dp0[black][j-1])
        return max(row[-1] for row in dp0)