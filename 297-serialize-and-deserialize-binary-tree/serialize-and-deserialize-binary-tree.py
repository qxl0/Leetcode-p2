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
        def dfs(node):
            if not node: 
                ans.append('N')
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(",".join(ans))
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        lst = data.split(",")
        n = len(lst)
        if not lst:
            return None
        i=0
        def dfs():
            nonlocal i
            if i==n: return
            if lst[i]=='N': return None
            root = TreeNode(int(lst[i]))
            i+= 1
            root.left = dfs()
            i+=1 
            root.right = dfs()
            return root
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))