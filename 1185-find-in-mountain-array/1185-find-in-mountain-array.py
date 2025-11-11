# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, A: 'MountainArray') -> int:
        # find mountain peak
        l, r = 0, A.length()-1
        while l<r:
            mid = l + (r - l)//2
            if A.get(mid)>A.get(mid+1):
                r = mid
            else:
                l = mid+1
        # l is peak
        # print(f'p={l}')
        p = l
        # search first part
        l, r = 0, p
        while l<r:
            mid = r - (r-l)//2
            if A.get(mid)<= target:
                l = mid
            else:
                r = mid-1
        # print(f'at 2: {l}')
        if A.get(l)==target:
            return l
        l, r = p, A.length()-1
        while l<r:
            mid = l + (r-l)//2
            if A.get(mid)> target:
                l = mid+1
            else:
                r = mid
        if A.get(l)==target:
            return l
        return -1


        # search second part
