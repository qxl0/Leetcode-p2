from sortedcontainers import SortedList
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        l = []
        def key(x,y):
            return abs(x)+abs(y)
        ans = []
        for x,y in queries:
            heappush(l, -key(x,y))    
            if len(l)<k:
                ans.append(-1)
            elif len(l)>k:
                heappop(l)
                ans.append(-l[0])
            else:               
                ans.append(-l[0])
            
        return ans