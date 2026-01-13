class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        vis = [[0]*n for _ in range(m)]
        k = len(word)
        def dfs(i,j,cur):            
            if cur==k:
                return True
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x,y = i+dx,j+dy
                if x<0 or x>=m or y<0 or y>=n:
                    continue
                if vis[x][y] == 1:
                    continue
                if board[x][y]==word[cur]:
                    vis[x][y] = 1
                    if dfs(x,y,cur+1):
                        return True
                    vis[x][y] = 0
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    vis[i][j]=1
                    if dfs(i,j,1):
                        return True
                    vis[i][j]=0
        return False