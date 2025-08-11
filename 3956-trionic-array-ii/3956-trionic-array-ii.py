class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        lst = list(accumulate(nums))
        decArr = []
        i = 0
        while i<n:
            j = i
            while j+1<n and nums[j+1]<nums[j]:
                j += 1
            # stop
            if j>i:
                decArr.append((i,j))
            i = j+1 
        ans = -inf
        for s,e in decArr:
            if s-1<0 or e+1>=n:continue
            if nums[e+1]<=nums[e]: continue
            if nums[s-1]>=nums[s]: continue
            
            maxSum1 = nums[s-1]
            ls = nums[s-1]
            for j in range(s-2, -1, -1):
                if nums[j]>=nums[j+1]:break
                ls += nums[j]
                maxSum1 = max(maxSum1, ls)
            
            maxSum2 = nums[e+1]
            rs = nums[e+1]
            for j in range(e+2, n):
                if nums[j]<=nums[j-1]:break
                rs += nums[j]
                maxSum2 = max(maxSum2, rs)
            sum = lst[e]-lst[s-1]
            ans = max(ans, maxSum1 + maxSum2 + sum)
        return ans
            

            