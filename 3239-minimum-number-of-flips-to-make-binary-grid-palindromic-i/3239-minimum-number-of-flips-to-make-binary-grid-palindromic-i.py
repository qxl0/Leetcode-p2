class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        def makepalin_row(row):
            ret = 0
            i,j=0,len(row)-1
            while i<j:
                if row[i]!=row[j]:
                    ret += 1
                i += 1
                j -= 1
            return ret 
        def makepalin(grid):
            ret = sum(makepalin_row(row) for row in grid)
            return ret 
        ret = m*n

        ret = min(ret, makepalin(grid))
        ret = min(ret, makepalin(zip(*grid)))
        return ret 