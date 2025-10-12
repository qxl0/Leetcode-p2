class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(arr,l,r):
            nonlocal first, last
            if l>=r:
                return arr
            
            x = nums[randint(l,r)]
            partition(arr,l, r, x)
            left, right = first, last
            quicksort(arr,l,left-1)
            quicksort(arr,right+1, r)
            return arr
        def partition(arr,l, r, x):
            nonlocal first,last
            i = l
            first,last = l,r
            while i <= last:
                if nums[i] == x:
                    i += 1
                elif nums[i] < x:
                    swap(nums, first, i)
                    first += 1
                    i += 1
                else: # nums[i] > X
                    swap(nums, i, last)
                    last -= 1
        def swap(arr, i, j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
        first,last = -1,-1
        return quicksort(nums,0,len(nums)-1)
        
        