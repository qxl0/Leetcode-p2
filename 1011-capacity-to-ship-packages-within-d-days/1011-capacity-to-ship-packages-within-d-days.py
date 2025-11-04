class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:        
        n = len(weights)
        def checkok(mid):            
            count = 0
            i = 0
            while i<n:
                sm = weights[i]
                j = i+1
                while j<n and sm+weights[j]<=mid:
                    sm += weights[j]
                    j += 1
                count += 1
                if count > days:
                    return False
                i = j
            return True

        l, r = max(weights), sum(weights)
        while l<r:
            mid = l+(r-l)//2
            if checkok(mid):
                r = mid
            else:
                l = mid+1
        return l