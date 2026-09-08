class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        q = [] # c,i,j,t,dir
        heappush(q, ([grid[0][0],0,0,0,-1]))
        seen = set()
        # dir:-1,0,1,2,3
        while q:
            cost, i,j,t,dir = heappop(q)
            if i==m-1 and j==n-1 and t<=k:
                return cost
            if (i,j,dir,t) in seen:
                continue
            seen.add((i,j,dir,t))
            for d,(di,dj) in enumerate([(-1,0),(0,1),(1,0),(0,-1)]): #0,1,2,3
                ni,nj = i+di,j+dj
                if ni<0 or ni>m-1 or nj<0 or nj>n-1:
                    continue                                
                nt = t+(1 if dir != -1 and dir != d else 0)                     
                if nt <=k:
                    heappush(q, (cost+grid[ni][nj], ni,nj,nt,d))
                
        return -1
                
        
