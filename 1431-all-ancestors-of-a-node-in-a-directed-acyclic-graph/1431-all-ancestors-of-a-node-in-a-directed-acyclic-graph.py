class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        adj = [[] for _ in range(n)]
        indeg = [0]*n
                
        for u,v in edges:
            adj[u].append(v)
            indeg[v] += 1
        
        for i in range(n):
            pq = deque()
            pq.append(i)
            while pq:
                cur = pq.popleft()                
                for child in adj[cur]:                             
                    if len(ans[child])==0 or ans[child][-1]!=i:
                        ans[child].append(i)
                        pq.append(child)
        return ans
