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
        if not root: return ""
        q = deque()
        q.append(root)
        ret = []
        while q:
            cur = q.popleft()
            if not cur:
                ret.append('null')
                continue
            ret.append(str(cur.val))
            q.append(cur.left)
            q.append(cur.right)
        return ','.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="": return None
        q = deque()
        lst = data.split(',')
        root = TreeNode(int(lst[0]))
        
        q.append(root)
        i = 1
        while i<len(lst):
            cur = q.popleft()
            if lst[i]!='null':
                cur.left = TreeNode(int(lst[i]))
                q.append(cur.left)
            i += 1
            if lst[i]!='null':
                cur.right = TreeNode(int(lst[i]))
                q.append(cur.right)
            i += 1
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))