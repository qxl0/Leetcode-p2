class Solution:
    def minimumCost(self, m: int, n: int, H: List[int], V: List[int]) -> int:
        pq = [(-h,1) for h in H]+[(-v,0) for v in V]
        heapify(pq)

        ret = 0
        i,j = 1,1
        while pq:
            x,isH = heappop(pq)
            x = -x
            if isH:
                ret += j*x
                i+=1
            else: # isV
                ret += i*x
                j+=1
        return ret 