class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        sets = set()
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
            sets.add((u,v))
        ans = 0
        def dfs(i,p):
            nonlocal ans
            for nei in adj[i]:
                if nei==p:continue
                ans += (i,nei) in sets
                dfs(nei,i)
        dfs(0,-1)
        return ans
