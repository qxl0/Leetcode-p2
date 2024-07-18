class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        i,j=1,1
        bq = [(-x,1) for x in horizontalCut]+[(-x,0) for x in verticalCut]
        heapify(bq)
        ret = 0
        while bq:
            x,isH = heappop(bq)
            x = -x
            if isH:
                ret += x*j
                i += 1
            else:
                ret += x*i
                j += 1
        return ret