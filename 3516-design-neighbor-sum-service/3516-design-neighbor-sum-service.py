class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.Map = {grid[i][j]:(i,j) for i in range(len(grid)) for j in range(len(grid[0]))}        

    def adjacentSum(self, value: int) -> int:
        i,j = self.Map[value]
        sm = 0
        if j-1>=0:
            sm = self.grid[i][j-1]
        if j+1<len(self.grid):
            sm += (self.grid[i][j+1])
        if i-1>=0:
            sm += (self.grid[i-1][j])
        if i+1<len(self.grid):
            sm += (self.grid[i+1][j])
        return sm

    def diagonalSum(self, value: int) -> int:
        i,j = self.Map[value]
        m,n = len(self.grid),len(self.grid[0])
        sm = 0
        if j-1>=0 and i-1>=0:
            sm = (self.grid[i-1][j-1])
        if i+1<m and j-1>=0:
            sm += (self.grid[i+1][j-1])
        if i-1>=0 and j+1<n:
            sm += (self.grid[i-1][j+1])
        if i+1<m and j+1<n:
            sm += (self.grid[i+1][j+1])
        return sm

        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)