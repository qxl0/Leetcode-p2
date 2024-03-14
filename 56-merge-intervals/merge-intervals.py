class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ret = []
        a,b = intervals[0]
        for c,d in intervals[1:]:
            if b<c:
                ret.append([a,b])
                a,b = c,d
            else:
                b = max(b, d)
        ret.append([a,b])
        return ret 