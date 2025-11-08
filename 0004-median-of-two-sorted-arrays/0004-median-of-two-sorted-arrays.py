class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        m,n = len(nums1),len(nums2)
        half = (m+n)//2
        l, r = 0, m-1
        while True:
            mid = l+(r-l)//2 # mid starts at 0
            #  
            #
            j = half-mid-2 # Bl starts at 0
            Al,Ar = (nums1[mid] if mid>=0 else -inf), (nums1[mid+1] if mid+1<m else inf)
            Bl,Br = (nums2[j] if j>=0 else -inf), (nums2[j+1] if j+1<n else inf)
            if Al<=Br and Bl<=Ar:
                if (m+n)%2==1:
                    return max(max(Al,Bl),min(Ar, Br))
                else:
                    return (max(Al, Bl)+min(Ar, Br))/2
            elif Al > Br:
                r = mid-1
            else:
                l = mid+1
        

