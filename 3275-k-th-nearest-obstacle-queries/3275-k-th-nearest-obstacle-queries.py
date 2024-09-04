from sortedcontainers import SortedList
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        l = SortedList()
        def key(x,y):
            return abs(x)+abs(y)
        ans = []
        for x,y in queries:
            l.add((key(x,y),x,y))    
            if len(l)<k:
                ans.append(-1)
            else:
                ans.append(l[k-1][0])
            
        return ans