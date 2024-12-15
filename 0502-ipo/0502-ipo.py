class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap1,heap2 = [(c,p) for p,c in zip(profits,capital)], []
        heapify(heap1)
        
        while k>0:
            while len(heap1)>0 and heap1[0][0]<=w:
                c,p = heappop(heap1)
                heappush(heap2, (-p, c))
            if len(heap2)>0:
                p,_ = heappop(heap2)
                w += -p
                k -= 1
            else:
                break
        return w