class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l<r:
            mid = r-(r-l)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                r = mid-1
            else:
                l = mid
        return l