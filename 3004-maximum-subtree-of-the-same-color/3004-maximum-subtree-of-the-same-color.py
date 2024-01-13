class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        n = len(edges)+1
        ans = 0
        nxt = [[] for _ in range(n)]
        for u,v in edges:
            nxt[u].append(v)
            nxt[v].append(u)
        def dfs(node,parent): # return: (current cnt,global cnt)
            maxNodes,cur = -1,1
            for v in nxt[node]:
                if v == parent: continue
                c,cnt = dfs(v, node)
                if c!=-1 and colors[v]==colors[node] and cur!=-1:
                    cur += c
                else:
                    cur = -1
                maxNodes = max(maxNodes, cnt)
            return cur,max(cur,maxNodes)
        return dfs(0, -1)[1]
                    
                
            
        