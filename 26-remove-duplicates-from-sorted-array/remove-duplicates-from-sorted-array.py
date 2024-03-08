class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur=1
        n = len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]:continue
            nums[cur] = nums[i]
            cur += 1
        return cur