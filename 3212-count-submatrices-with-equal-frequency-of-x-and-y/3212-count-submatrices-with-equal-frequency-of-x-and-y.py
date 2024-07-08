class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        presum_X = [[0]*n for _ in range(m)]
        presum_Y = [[0]*n for _ in range(m)]
        def calpresum(presumX, isX=0):            
            for i in range(m):
                for j in range(n):                    
                    presumX[i][j] = (presumX[i-1][j] if i>0 else 0) + (presumX[i][j-1] if j>0 else 0)-(presumX[i-1][j-1] if i>0 and j>0 else 0) + (1 if (grid[i][j]=='X' and isX or not isX and grid[i][j]=='Y') else 0)
        calpresum(presum_X, 1)
        calpresum(presum_Y, 0)

        ret = 0
        for i in range(m):
            for j in range(n):
                if presum_X[i][j]==presum_Y[i][j] and presum_X[i][j]!=0:
                    ret += 1
        return ret 