class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l,r = 0, n-1
        while l<r:
            mid = l + (r-l)//2
            v = nums[mid]
            if v == target:
                return True
            
            if nums[l] > v: # mid is on right side
                # target 
                if v < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[l] < v: # mid is on left side
                if nums[l] <= target < v:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # nums[l] == v
                l -= 1
        return nums[l]==target