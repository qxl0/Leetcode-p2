class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        ret = inf
        def process(i,j,k,l):
            i0,j0 = inf,inf
            i1,j1 = -inf,-inf
            for row in range(i,k+1):
                for col in range(j,l+1):
                    if grid[row][col]==1:
                        i0=min(i0,row)
                        j0=min(j0,col)
                        i1=max(i1,row)
                        j1=max(j1,col)
            return (j1-j0+1)*(i1-i0+1)
        # 1
        for i in range(1,m):
            for k in range(i+1,m):
                area1 = process(0,0,i-1,n-1)
                area2 = process(i,0,k-1,n-1)
                area3 = process(k,0,m-1,n-1)
                ret = min(ret, area1+area2+area3)
        # 2 
        for i in range(1,m):
            for j in range(1,n):
                area1 = process(0,0,i-1,j-1)
                area2 = process(0,j,i-1,n-1)
                area3 = process(i,0,m-1,n-1)
                ret = min(ret, area1+area2+area3)
        # 3 
        for i in range(1,m):
            for j in range(1,n):
                area1 = process(0,0,i-1,n-1)
                area2 = process(i,0,m-1,j-1)
                area3 = process(i,j,m-1,n-1)
                ret = min(ret, area1+area2+area3)
        # 4
        for j in range(1,n):
            for l in range(j+1,n):
                area1 = process(0,0,m-1,j-1)
                area2 = process(0,j,m-1,l-1)
                area3 = process(0,l,m-1,n-1)
                ret = min(ret, area1+area2+area3)
        # 5
        for i in range(1,m):
            for j in range(1,n):
                area1 = process(0,0,i-1,j-1)
                area2 = process(i,0,m-1,j-1)
                area3 = process(0,j,m-1,n-1)
                ret = min(ret, area1+area2+area3)
        # 6
        for i in range(1,m):
            for j in range(1,n):
                area1 = process(0,0,m-1,j-1)
                area2 = process(0,j,i-1,n-1)
                area3 = process(i,j,m-1,n-1)
                ret = min(ret, area1+area2+area3)
        return ret 
        