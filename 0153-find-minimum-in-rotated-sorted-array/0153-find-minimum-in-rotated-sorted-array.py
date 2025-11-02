class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, n-1
        if nums[r]>=nums[l]:
            return nums[l]
        while l<r:
            mid = l+(r-l)//2
            v = nums[mid]
            if v >= nums[0]: # left  
                l = mid+1
            else: # right
                r = mid
        return nums[l]