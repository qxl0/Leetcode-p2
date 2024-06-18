class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hours = [x%24 for x in hours] 
        Map = Counter()
        ret = 0
        for x in hours:
           ret += Map[(24-x)%24]
           Map[x]+=1
        return ret
