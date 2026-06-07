class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m, n = len(workers), len(bikes)
        dist = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dist[i][j] = abs(workers[i][0]-bikes[j][0]) + abs(workers[i][1]-bikes[j][1])
        pq = [(0,0)]
        visited = [0]*(1<<n)  # state -> 00011  bikes[3], bikes[4] are taken
        while pq:
            cost,state = heappop(pq)
            if visited[state]: continue
            visited[state] = 1

            i = state.bit_count()
            if i == m:
                return cost
            for j in range(n):
                if (state>>j)&1==1: continue
                newState = state + (1<<j)
                if visited[newState] == 1: continue
                heappush(pq, (cost + dist[i][j], newState))
        return -1
            
        