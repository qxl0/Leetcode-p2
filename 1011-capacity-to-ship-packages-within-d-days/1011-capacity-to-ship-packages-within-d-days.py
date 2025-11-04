class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)        
        def days2ship(x):            
            c = 0
            ship = 0
            for w in weights:                
                if ship+w>x:
                    c += 1
                    ship =0                
                ship += w
            return c+1
        l,r = max(weights), sum(weights)
        while l<r:
            m = l+(r-l)//2
            d = days2ship(m)
            if d > days:
                l = m+1
            else:
                r = m
        return l