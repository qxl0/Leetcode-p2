class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0]*(n+1)
        for i in range(1, n+1):
            arr[i] = nums[i-1]
        arr[1:n+1] = sorted(arr[1:n+1])
        m = 1
        for i in range(2,n+1): # remove duplicate
            if arr[m] != arr[i]:
                m += 1
                arr[m] = arr[i]
                
        # 2,3,3,3,4,4,5
        # 2,3,4,5
        # m = 4
        # index tree set up
        treeMaxLen = [0]*(m+1)
        treeMaxLenCnt = [0]*(m+1)
        maxLen,maxLenCnt = 0,0        
        def rank(x): # x -> index
            ans = 0
            l,r = 1,m
            while l<=r:
                mid = (l+r)//2
                if arr[mid]>=x:
                    ans = mid
                    r = mid-1
                else:
                    l = mid+1
            return ans
        def lowbit(x):
            return x & -x
        def query(i): # return maxLen, maxLenCnt global veriables
            nonlocal maxLen, maxLenCnt
            maxLen=maxLenCnt=0
            while i>0:
                if maxLen==treeMaxLen[i]:
                    maxLenCnt += treeMaxLenCnt[i]
                elif maxLen<treeMaxLen[i]:
                    maxLen = treeMaxLen[i]
                    maxLenCnt = treeMaxLenCnt[i]
                i -= lowbit(i)
        def add(i, len, cnt):
            while i<= m:
                if treeMaxLen[i] == len:
                    treeMaxLenCnt[i] += cnt
                elif treeMaxLen[i] < len:
                    treeMaxLen[i] = len
                    treeMaxLenCnt[i] = cnt
                i += lowbit(i)    
        for num in nums:
            i = rank(num)
            query(i-1)
            if maxLen==0:
                add(i, 1, 1)
            else:
                add(i, maxLen+1, maxLenCnt)
        query(m)
        return maxLenCnt
