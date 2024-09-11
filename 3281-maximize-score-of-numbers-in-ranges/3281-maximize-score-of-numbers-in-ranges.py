class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        n = len(start)
        def checkok(mid):
            # check if mid can be a solution  max of the min   
            last = start[0]
            for i in range(1,n):
                if last+mid>start[i]+d:
                    return False
                last = max(last+mid, start[i])
            return True
        l,r = 0,2*10**9
        while l<r:
            mid = r - (r-l)//2
            if checkok(mid):
                l = mid
            else:
                r = mid -1
        return l