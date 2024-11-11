class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        count = Counter()
        res,i,j,n=0,0,0,len(nums)

        # [a-k,a+k]
        for a in nums:            
            while j<n and nums[j]<=a+k:
                count[nums[j]] += 1
                j += 1
            while i<n and nums[i]<a-k:
                count[nums[i]] -= 1
                i += 1
            cur = min(j-i, count[a] + numOperations)
            res = max(res, cur)
        # [a, a+k+k]
        i,j=0,0
        while j<n:
            while nums[i]+k+k<nums[j]:
                i += 1
            res = max(res, min(j-i+1, numOperations))
            j += 1
            
        return res