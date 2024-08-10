class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        def shortestpath(adj):
            dq = [(0,0)]
            dist = [inf]*n
            dist[0]=0            
            while dq:
                d,cur = heappop(dq)
                if d > dist[cur] or cur==n-1:continue
                for w, nei in adj[cur]:
                    if dist[cur] + w < dist[nei]:
                        dist[nei] = dist[cur] + w
                        heappush(dq, (dist[nei], nei))
            return dist[n-1]
        adj = {i:[(1,i+1)] for i in range(n-1)}
        for u,v in queries:
            adj[u].append((1,v))
            ans.append(shortestpath(adj))
        return ans