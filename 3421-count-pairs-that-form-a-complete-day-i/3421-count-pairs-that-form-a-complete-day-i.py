class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ret = 0
        n = len(hours)
        for i in range(n):
            for j in range(i+1,n):
                if (hours[i]+hours[j])%24==0:
                    ret += 1
        # print(ret)
        return ret