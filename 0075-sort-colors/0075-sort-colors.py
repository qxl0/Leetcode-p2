class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(arr, i, j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
        
        x = 1
        n = len(nums)
        l, r = 0, n-1
        first,last = l, r
        i = 0
        while i <= last:
            if nums[i] == x:
                i += 1
            elif nums[i] < x:
                swap(nums, first, i)
                first += 1
                i += 1
            else:
                swap(nums, i, last)
                last -= 1
        return nums


        