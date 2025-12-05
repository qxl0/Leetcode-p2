class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ret = []
        tt = [(t,dur,id) for id, (t,dur) in enumerate(tasks)]
        tt.sort()
        q = []        
        cur = tt[0][0]
        i = 0
        while i<len(tt) or q:
            if not q and cur<tt[i][0]:
                cur = tt[i][0]
            while i<len(tt) and tt[i][0]<=cur:                
                heappush(q,(tt[i][1], tt[i][2]))
                i += 1                                  
            d,id = heappop(q)            
            cur += d
            ret.append(id)
            
                
        return ret
