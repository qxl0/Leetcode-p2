from bisect import bisect, bisect_left
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        presum = [0]*(n+1)
        for i in range(n):
            presum[i+1] = presum[i]+nums[i]
        
        def helper(presum, a, b, lower,upper):
            nonlocal ret
            if a>=b:return
            mid = a + (b-a)//2
            helper(presum, a, mid, lower, upper)
            helper(presum, mid+1, b, lower, upper)
            x,y = 0,0
            for i in range(a, mid+1):
                x = bisect_left(presum, presum[i]+lower, mid+1, b+1)
                y = bisect(presum, presum[i]+upper, mid+1, b+1)
                ret += y-x
            
            temp = [0]*(b-a+1)
            p = 0
            i = a
            j = mid+1
            while i<=mid and j<=b:
                if presum[i]<=presum[j]:
                    temp[p] = presum[i]
                    i += 1
                else:
                    temp[p] = presum[j]
                    j += 1
                p += 1
            while i<=mid:
                temp[p] = presum[i]
                i += 1
                p += 1
            while j<=b:
                temp[p] = presum[j]
                j += 1
                p += 1
            for i in range(b-a+1):
                presum[i+a] = temp[i]
            
        ret = 0
        helper(presum, 0, n, lower, upper)
        
        return ret