class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.left = self.right = None

    def __repr__(self) -> str:
        return f"max:{self.count},start:{self.start},end:{self.end}, {self.left},{self.right}"


class SegmentTree:
    root = None
    p = None
    nums = None 
    def __init__(self, nums):
        self.p = self.build(nums)
        self.nums = nums
        self.root = self.buildHelper(0, len(nums) - 1, nums)
        

    def build(self,nums):
        n = len(nums)
        ret = [False]*n
        for i in range(1,n-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                ret[i] = True
        return ret

    def __repr__(self):
        return self.root

    def buildHelper(self, start, end, nums):
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end, (1 if self.p[start] else 0))
        # root has Child
        root = SegmentTreeNode(start, end, 0)
        mid = start + (end - start) // 2
        root.left = self.buildHelper(start, mid, nums)
        root.right = self.buildHelper(mid + 1, end, nums)

        # maximum
        if root.left:
            root.count += root.left.count
        if root.right:
            root.count += root.right.count

        return root

    def query(self, start, end):
        ret = self._query(self.root, start, end)
        if self.p[start]:
            ret -= 1
        if self.p[end]:
            ret -= 1
        return max(0,ret) 

    def _query(self, node, start, end):
        if start <= node.start and node.end <= end:
            return node.count
        mid = node.start + (node.end - node.start) // 2
        leftRet = 0
        rightRet = 0
        if start <= mid:
            leftRet += self._query(node.left, start, end)
        if mid < end:
            rightRet += self._query(node.right, start, end)

        return leftRet+rightRet

    def modify(self, index, value):
        self._modify(self.root, index, value)

    def _modify(self, root: SegmentTreeNode, index: int, value: int):
        # exit
        if root.start == root.end and root.start == index:            
            # index-1,index, index+1
            self.updatep(index, value)
            root.count =( 1 if self.p[index] else 0)
            return

        mid = root.start + (root.end - root.start) // 2

        # left root.start, mid
        if index <= mid:
            self._modify(root.left, index, value)
        else:
            self._modify(root.right, index, value)

        # maintain max
        root.count = root.left.count + root.right.count
        return
    def updatep(self, i, value):
        # i-1,i,i+1
        nums = self.nums
        p = self.p 
        n = len(nums)
        if p[i]:
            if i-1>=0 and i+1<n and value<=nums[i+1] or value <= nums[i-1]:
                p[i] = False             
        else:     
            if i+1<n and i-1>=0 and value>nums[i+1] and value > nums[i-1]:
                p[i] = True 
        
        nums[i] = value

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ret = []
        tree = SegmentTree(nums)
        for tpe,p1,p2 in queries:
            if tpe==2:
                tree.modify(p1,p2)
                if p1-1>=0:
                    tree.modify(p1-1,nums[p1-1])
                if p1+1<len(nums):
                    tree.modify(p1+1,nums[p1+1])
            else:
                ret.append(tree.query(p1,p2))
        return ret 
