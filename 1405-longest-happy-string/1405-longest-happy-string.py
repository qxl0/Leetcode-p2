class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        if a > 0:
            heapq.heappush(q,(-a, 'a'))
        if b > 0:
            heapq.heappush(q,(-b, 'b'))
        if c > 0:
            heapq.heappush(q,(-c, 'c'))
        
        
        ans = ''
        while q:
            if len(q) == 1:
                z,zc = heapq.heappop(q)
                k = min(-z, 2)
                ans += zc*k
                return ans
            x,xc = heapq.heappop(q)
            y,yc = heapq.heappop(q)
            
            k = min(2, 1+(-x)-(-y))
            ans += xc*k
            ans += yc
            
            nx = (-x)-k
            ny = (-y)-1
            if nx>0:
                heapq.heappush(q, (-nx, xc))
            if ny>0:
                heapq.heappush(q, (-ny, yc))
            # print(ans)
        return ans
            