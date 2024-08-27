class SegTreeNode:
    def __init__(self, a, b, val):  # init [a,b] with val
        self.tag = 0
        self.start = a
        self.end = b
        self.delta=0
        self.left = self.right = None
        if a == b:
            self.info = val
            return
        mid = (a + b) // 2
        if not self.left:
            self.left = SegTreeNode(a, mid, val)
            self.right = SegTreeNode(mid + 1, b, val)
            self.info = self.left.info + self.right.info

    def pushDown(self):
        if self.tag == 1 and self.left:
            self.left.info += self.delta*(self.left.end-self.left.start+1)
            self.left.delta += self.delta
            self.right.info += self.delta*(self.right.end-self.right.start+1)
            self.right.delta += self.delta
            self.left.tag = 1
            self.right.tag = 1
            self.tag = 0
            self.delta = 0

    def updateRange(self, a, b, val):  # increase range [a,b] with val
        if b < self.start or self.end < a:
            return
        if a <= self.start and self.end <= b:
            self.info += val * (self.end - self.start + 1)
            self.delta += val
            self.tag = 1
            return

        if self.left:
            self.pushDown()
            self.left.updateRange(a, b, val+self.delta)
            self.right.updateRange(a, b, val+self.delta)
            self.delta=0
            self.tag=0
            self.info = self.left.info + self.right.info

    def queryRange(self, a, b):  # query sum over [a,b]
        if b < self.start or a > self.end:
            return 0
        if a <= self.start and self.end <= b:
            return self.info

        if self.left:
            self.pushDown()
            ret = self.left.queryRange(a, b) + self.right.queryRange(a, b)
            self.info = self.left.info + self.right.info
            return ret
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        root = SegTreeNode(0, n-1, 0)

        end = [n]*n
        count0,count1 = 0,0
        j=0
        for i in range(n):
            while j<n and ((count0+(1 if s[j]=='0' else 0))<=k or (count1+(1 if s[j]=='1' else 0))<=k):
                count0 += (1 if s[j]=='0' else 0)
                count1 += (1 if s[j]=='1' else 0)
                j += 1
            # when stop, 
            end[i] = j-1
            count0 -= (1 if s[i]=='0' else 0)
            count1 -= (1 if s[i]=='1' else 0)
        
        q = [(l,r,i) for i,(l,r) in enumerate(queries)]
        q.sort(reverse=True)
        # print(q)
        ret = [0]*len(q)
        i = n-1
        for l,r,idx in q:
            while i>=l:
                root.updateRange(i, end[i], 1)
                i -= 1
            ret[idx] = root.queryRange(l, r)
        return ret 


        