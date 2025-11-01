class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, n-1
        while l<r:
            mid = r-(r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else: # nums[mid]>target
                r = mid-1
        if l<n and nums[l]<target:
            return l+1
        return l