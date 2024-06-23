class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        i0,i1 = 0,m-1
        for i in range(m):
            if all(x==0 for x in grid[i]):
                i0+=1
            else:
                break                
        for i in range(m-1,-1,-1):
            if all(x==0 for x in grid[i]):
                i1 -= 1
            else:
                break
        j0,j1 = 0,n-1
        for j in range(n):
            allzero = 1
            for i in range(m):
                if grid[i][j]==1:
                    allzero = 0
                    break
            if allzero==1:
                j0 += 1
            else:
                break
        for j in range(n-1,-1,-1):
            allzero = 1
            for i in range(m):
                if grid[i][j]==1:
                    allzero = 0
                    break
            if allzero==1:
                j1 -= 1
            else:
                break
        return (i1-i0+1)*(j1-j0+1)
