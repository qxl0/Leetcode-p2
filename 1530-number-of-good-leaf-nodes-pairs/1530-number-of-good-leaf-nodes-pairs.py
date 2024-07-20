# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        adj = defaultdict(list)
        bq = []
        def traverseTree(node,parent=None):
            if not node: return            
            # add 
            if node.left:
                adj[node.left].append(node)
                adj[node].append(node.left)
                traverseTree(node.left, node)            
            if node.right:
                adj[node.right].append(node)
                adj[node].append(node.right)
                traverseTree(node.right,node)
            if not node.left and not node.right:
                bq.append(node)
        traverseTree(root)

        # bfs        
        ret = 0                
        for leaf in bq:
            q = deque()
            q.append(leaf)
            vis = set()
            vis.add(leaf)
            for _ in range(distance+1):
                size = len(q)
                for _ in range(size):
                    cur = q.popleft()                    
                    if cur!=leaf and not cur.left and not cur.right:
                        ret += 1
                    for nei in adj[cur]:
                        if nei in vis:
                            continue 
                        vis.add(cur)                   
                        q.append(nei)            
        return ret//2
