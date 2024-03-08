class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        n = len(nums)
        cur = 1
        i = 0
        while i<n:
            j = i+1
            while j<n and nums[j]==nums[i]:
                j += 1
            if j==n: break
            nums[cur] = nums[j]
            cur += 1

            i = j
        return cur
            
