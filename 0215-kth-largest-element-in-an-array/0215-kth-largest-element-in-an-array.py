class Solution:
    def findKthLargest(self, nums: List[int], K: int) -> int:
        n = len(nums)
        def swap(x,y):
            nums[x],nums[y] = nums[y], nums[x]
        def quickpartition(l,r,k):            
            # x x x x v v v y y y y 
            #         i   j   <--- return (i,j) st 
            # < i, [i,j] >j ....
            if l>=r: return nums[l]
            idx = randint(l,r)
            x = nums[idx]
            a, b = l, r 
            i = l
            while i<=b:
                if nums[i]<x:
                    swap(a, i)
                    i += 1
                    a += 1
                elif nums[i] == x:
                    i += 1
                else:
                    swap(b, i)
                    b -= 1
            if a-l >= k:
                return quickpartition(l, a-1, k)
            elif b+1-l < k:
                return quickpartition(b+1, r, l+k-b-1)
            return x
        
        return quickpartition(0,n-1,n-K+1)
