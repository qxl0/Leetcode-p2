class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        for x,xc in [(a,'a'),(b,'b'),(c,'c')]:
            if x>0: 
                heappush(q,(-x,xc))
        ans = ''
        while q:
            if len(q)==1:
                x,xc = heappop(q)
                ans += xc*min(2, -x)
                return ans
            x,xc = heappop(q)
            y,yc = heappop(q)
            k = min(2, 1-x+y)
            ans += xc*k
            ans += yc
            if -x>k:
                heappush(q, (x+k,xc))
            if -y>1:
                heappush(q, (y+1,yc))
        
        return ans
        