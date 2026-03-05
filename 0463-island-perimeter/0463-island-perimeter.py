class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 4
                    if j+1<n and grid[i][j+1]==1:
                        ans -= 2
                    if i+1<m and grid[i+1][j]==1:
                        ans -= 2
        return ans
