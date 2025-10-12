class NumMatrix:
    data = []
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])        
        self.data = [list(accumulate(row)) for row in matrix]
        self.presum = [[0]*n for _ in range(m)]        
        for j in range(n):
            for i in range(m):
                self.presum[i][j] = (self.presum[i-1][j] if i>0 else 0) + self.data[i][j]
        # print(self.presum)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret = self.presum[row2][col2]-(self.presum[row2][col1-1] if col1>0 else 0) - (self.presum[row1-1][col2] if row1>0 else 0) + (self.presum[row1-1][col1-1] if row1>0 and col1>0 else 0)
        return ret


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)