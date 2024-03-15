# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def bfs(node):
            # level order traversal
            q = deque()
            q.append(node)
            while q:
                qsize = len(q)
                for _ in range(qsize):
                    cur = q.popleft()
                    if not cur:                        
                        ans.append('N')
                        continue
                    ans.append(str(cur.val))
                    q.append(cur.left)                    
                    q.append(cur.right)
        if not root: return ""
        bfs(root)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="": return None
        lst = data.split(',')        
        
        root = TreeNode(int(lst[0]))
        q = deque()
        q.append(root)
        i = 1
        while i<len(lst):
            parent = q.popleft()            
            if lst[i]!='N':
                parent.left = TreeNode(int(lst[i]))
                q.append(parent.left)
            i += 1
            if lst[i]!='N':
                parent.right = TreeNode(int(lst[i]))
                q.append(parent.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))