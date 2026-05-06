class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ret = 0
        def dfs(cur, parent):
            nonlocal ret
            
            total = values[cur]
            for nei in adj[cur]:
                if nei == parent:
                    continue
                total += dfs(nei, cur)
            if total%k==0:
                ret += 1
            return total
        dfs(0, -1)
        return ret