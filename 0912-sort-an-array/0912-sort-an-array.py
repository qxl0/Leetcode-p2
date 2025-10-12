class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            l = len(arr)
            if l <= 1:
                return arr
            ll, rr = mergesort(arr[:l//2]), mergesort(arr[l//2:])
            return merge(ll, rr)
        def merge(l, r):
            ln, rn = len(l), len(r)
            ret,i,j = [], 0,0
            while i<ln and j <rn:
                if l[i] <= r[j]:
                    ret.append(l[i])
                    i += 1                    
                else:
                    ret.append(r[j])
                    j += 1
            ans = ret + (l[i:] if j == rn else r[j:])
            return ans

        return mergesort(nums)