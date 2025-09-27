class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def hhmm_diff(t1,t2):
            t1_lst =  t1.split(':')
            t2_lst = t2.split(':')
            h1, m1 = int(t1_lst[0]),int(t1_lst[1])
            h2, m2 = int(t2_lst[0]),int(t2_lst[1])
            mm1 = h1*60+m1
            mm2 = h2*60+m2
            ans= mm2-mm1 
            return ans if ans >=0 else ans+1440

        timePoints.sort()

        ret = 24*60
        for t1,t2 in zip(timePoints, timePoints[1:]+[timePoints[0]]):
            ret = min(ret, hhmm_diff(t1,t2))
        return ret
