class SGT:
    def __init__(self, n):
        self.seg = [0]*(4*n+1)
    def build(self, index, low,high,arr):
        # build sgt rooted at index 
        if low==high:
            self.seg[index] = arr[low]
            return
        mid=(low+high)//2
        self.build(2*index+1, low, mid, arr)
        self.build(2*index+2, mid+1, high, arr)

        self.seg[index] = self.seg[2*index+1] + self.seg[2*index+2]

    def query(self, index, low,high,l,r):
        # query sgt rooted at index 
        if r<low or l>high: 
            return 0
        if low>=l and r>=high:
            return self.seg[index]
        
        mid = (low+high)//2
        left = self.query(2*index+1, low, mid, l, r)
        right = self.query(2*index+2, mid+1, high, l, r)

        return left + right 

    def update(self,index, low,high,i,val):
        if low==high:
            self.seg[index] = val
            return 
        
        mid = (low+high)//2
        if i<=mid:
            self.update(2*index+1, low, mid, i, val)
        else:
            self.update(2*index+2, mid+1, high, i, val)
        
        self.seg[index] = self.seg[2*index+1]+self.seg[2*index+2]
        

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n  = len(nums)
        peak = [0]*n
        def maintain(x):
            if nums[x]>nums[x-1] and nums[x]>nums[x+1]:
                tree.update(0,0,n-1,x,1)
                peak[x] = 1
            else:
                tree.update(0,0,n-1,x,0)
                peak[x] = 0

        for i in range(1,n-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                peak[i] =1
        tree = SGT(n)
        tree.build(0,0,n-1,peak)
        ans = []

        for i in range(len(queries)):
            tp1 = queries[i][0]
            if tp1==2:
                # update tree 
                _, p, x = queries[i]
                nums[p] = x
                if p-1>=0 and p+1<n: # check 
                    maintain(p)
                if p-2>=0 and p<n: # p-1
                    maintain(p-1)
                if p>=0 and p+2<n: # p+1
                    maintain(p+1)
            else: # query
                _, l, r = queries[i]
                if l==r:
                    ans.append(0)
                    continue
                res = tree.query(0,0,n-1,l,r)
                if peak[l]==1: res -= 1
                if peak[r]==1: res -= 1
                ans.append(res)
        return ans 

        