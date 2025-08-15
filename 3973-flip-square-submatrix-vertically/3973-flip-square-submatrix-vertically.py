class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m, n = len(grid),len(grid[0])

        for i in range(k//2):            
            for j in range(k):
                ip = k-1-i + x
                jp = j+y
                # jp = k-1-j + y
                # exchange                 
                tmp = grid[i+x][j+y]
                grid[i+x][j+y] = grid[ip][jp]
                grid[ip][jp] = tmp
        return grid
