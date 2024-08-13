class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def isleaf(node,parent):
            if node and len(adj[node])==1 and adj[node][0]==parent:
                return True
            return False

        def dfs(node,parent):
            nonlocal ret
            if isleaf(node,parent):
                ret +=1
                return 1
            sl = []
            for kid in adj[node]:
                if kid == parent: continue
                sl.append(dfs(kid, node))
            if max(sl) == min(sl):
                ret += 1
            return sum(sl)+1
        ret = 0
        dfs(0, -1)
        return ret