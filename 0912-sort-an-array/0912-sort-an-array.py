class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort1(arr, l, r):
            if l >= r:
                return
            x = arr[randint(l, r)] # [a, b) 
            mid = partition1(arr, l, r, x)
            quicksort1(arr, l, mid-1)
            quicksort1(arr, mid+1, r)   
            return arr         
        def swap(arr, a, b):
            tmp = arr[a]
            arr[a] = arr[b]
            arr[b] = tmp
        def partition1(arr, l, r, x):
            a = l
            xi = 0
            for i in range(l, r+1, 1):
                if arr[i] <= x:
                    swap(arr, a, i)
                    if arr[a] == x:
                        xi = a
                    a += 1
            swap(arr, xi, a-1)
            return a-1
        def quicksort2(arr, l, r):
            nonlocal first,last
            if l >= r: return
            x = arr[randint(l, r)]
            partion2(arr, l, r, x)
            left, right = first, last
            quicksort2(arr, l, left-1)
            quicksort2(arr, right+1, r)
            return arr
        def partion2(arr, l, r, x):
            nonlocal first, last
            first,last = l, r
            i = l
            while i <= last:
                if arr[i] == x:
                    i += 1
                elif arr[i] < x:
                    swap(arr, first, i)
                    first += 1
                    i += 1
                else:
                    swap(arr, i, last)
                    last -= 1
        first,last = -1,-1
        if len(nums)>1:
            return quicksort2(nums, 0, len(nums)-1)
        return nums