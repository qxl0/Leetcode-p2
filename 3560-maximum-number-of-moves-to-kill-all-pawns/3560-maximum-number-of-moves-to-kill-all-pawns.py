class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:    
        n = len(positions)
        dist = [[0 for _ in range(n)] for _ in range(n + 1)]
        positions.append([kx, ky])
        def bfs(i: int) -> int:
            dq = collections.deque([positions[i]])
            seen = set()
            step = 0
            while dq:
                l = len(dq)
                for _ in range(l):
                    x, y = dq.popleft()
                    if [x, y] == positions[j]: return step
                    for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                                   (1, -2), (1, 2), (2, -1), (2, 1)]:
                        cx, cy = x + dx, y + dy
                        if cx < 0 or cx > 49 or cy < 0 or cy > 49 or (cx, cy) in seen: continue
                        dq.append([cx, cy])
                        seen.add((cx, cy))
                step += 1

        for i in range(n + 1):
            for j in range(n):
                if i == j: continue
                dist[i][j] = bfs(i)
        # dp[state]: max number of moves 
        final = (1<<n) - 1
        @cache
        def dfs(cur,mask,alice): # cur: 0,..n mask:0..final-1 alice:0,1
            if mask==final:
                return 0
            ret = -10**7 if alice else 10**7
            for i in range(n):
                if mask&(1<<i) == 0: # mask[i bit]==0
                    cost = dist[cur][i]
                    if alice:
                        ret = max(ret, cost + dfs(i, mask|(1<<i), 1-alice))
                    else:
                        ret = min(ret, cost + dfs(i, mask|(1<<i), 1-alice))
            return ret


        return dfs(n,0,1)


