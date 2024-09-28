class Solution:
    def minNumberOfSeconds(self, H: int, T: List[int]) -> int:
        def times(t, h):
            ret = 0
            for i in range(1,h+1):
                ret += t*i
            return ret
        def depth(t, total):
            # t, total time -> x   t + t*2 + .. + t*x <=total
            a, b = 1,1
            c = -2*total/t
            x2 = (-b + sqrt(b*b-4*a*c))/(2*a)
            return floor(x2)
        def checkok(mid): # check if using mid s to reach H
            total = 0
            for t in T:
                total += depth(t, mid)
                if total>=H:
                    return True
            if total<H:
                return False
            return True
        mn = min(T)
        mxT = times(mn, H)

        l,r = 0, mxT
        while l<r:
            mid= l+(r-l)//2  # mid -> second
            if checkok(mid):
                r = mid
            else:
                l = mid+1
        return l