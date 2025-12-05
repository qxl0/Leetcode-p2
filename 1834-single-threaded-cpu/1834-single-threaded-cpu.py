class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ret = []
        tt = [(t,dur,id) for id, (t,dur) in enumerate(tasks)]
        tt.sort()
        q = []
        heapify(q)
        cur = tt[0][0]
        i = 0
        while i<len(tt) or q:
            while i<len(tt) and tt[i][0]<=cur:
                t,dur,id = tt[i]
                heappush(q,(dur,id, t))
                i += 1  
            if not q: break                      
            d,id,s = heappop(q)
            if cur>=s:
                cur += dur
                ret.append(id)
            else:
                cur = s+dur
                ret.append(id)
                
        return ret
