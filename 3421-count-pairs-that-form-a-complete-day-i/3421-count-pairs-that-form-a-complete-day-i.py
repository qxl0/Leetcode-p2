class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        n = len(hours)
        Map = Counter()
        ret = 0
        for x in hours:
            x %=24
            ret+= Map[(24-x)%24]
            Map[x%24]+=1
        return ret 


            