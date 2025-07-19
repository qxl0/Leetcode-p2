class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        res = 0
        adj = defaultdict(set)
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
        MAXM=(2**n)
        dp = [[[False]*15 for _ in range(15)] for _ in range(MAXM)]
        def dfs(i,j,mask,vis):
            nonlocal res
            mask |= (1<<i)|(1<<j)
            if dp[mask][i][j]:
                return
            dp[mask][i][j] = True
            vis[i]=vis[j]=True
            res = max(res, mask.bit_count())
            for x in adj[i]:
                if not vis[x]:
                    for y in adj[j]:
                        if not vis[y] and x!=y and label[x]==label[y]:
                            dfs(x,y,mask,vis)
            vis[i]=vis[j]=False
        
        for i in range(n):
            dfs(i,i,0,[False]*n)
            for j in adj[i]:
                if i<j and label[i]==label[j]:
                    dfs(i,j,0,[False]*n)
        return res