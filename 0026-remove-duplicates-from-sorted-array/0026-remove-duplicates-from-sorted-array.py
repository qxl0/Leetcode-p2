class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        n = len(nums)
        if n<2: return n
        k = 1
        i = 0
        while i < n:
            j = i+1
            while j<n and nums[i]==nums[j]:
                j += 1
            # when stop, j -> next val in nums
            if j >= n:
                break
            nums[k] = nums[j]
            k += 1
            i = j
            
        return k