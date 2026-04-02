class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms),len(rooms[0])
        EMPTY = 2**31 - 1
        gates = deque([(0, i,j) for i in range(m) for j in range(n) if rooms[i][j]==0])
        
        while gates:
            d, x, y = gates.popleft()
            
            rooms[x][y] = min(rooms[x][y], d)
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = x+dx, y+dy
                if nx<0 or nx>=m or ny<0 or ny>=n: continue
                if rooms[nx][ny] == EMPTY:
                    gates.append((d+1, nx, ny))
        