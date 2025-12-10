class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        for x,xc in [(a,'a'),(b,'b'),(c,'c')]:
            if x>0: 
                heappush(q,(-x,xc))
        ans = ''
        while len(q)>=2:
            x,xc = heappop(q)
            y,yc = heappop(q)
            k = min(2, -x)
            ans += xc*k
            ans += yc
            if -x>k:
                heappush(q, (x+k,xc))
            if -y>1:
                heappush(q, (y+1,yc))
        if q:
            x,xc = heappop(q)
            if -x>=3:
                ans += xc*2
            else:
                ans += xc*(-x)
        
        return ans
        