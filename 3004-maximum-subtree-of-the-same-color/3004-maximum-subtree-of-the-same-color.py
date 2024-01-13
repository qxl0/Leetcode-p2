class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        n = len(edges)+1
        ans = 0
        nxt = [[] for _ in range(n)]
        for u,v in edges:
            nxt[u].append(v)
            nxt[v].append(u)
        def dfs(node,parent): # return: max(color,#ofnodes) among tree rooted at node
            nonlocal ans            
            ret = defaultdict(int)
            for nei in nxt[node]:
                if nei == parent: continue
                clr,num = dfs(nei,node)
                ret[clr]+=num
            # check if there is only one clr
            node_color = colors[node]
             
            if  len(ret)==1 and node_color in ret:  # best case
                ans = max(ans, ret[node_color] + 1)
                return node_color, ret[node_color]+1
            else:
                if len(ret)==0:
                    ans = max(ans,1)
                    return node_color,1
                else:
                    return 0,0
        dfs(0,-1)
        return ans 
                    
                
            
        