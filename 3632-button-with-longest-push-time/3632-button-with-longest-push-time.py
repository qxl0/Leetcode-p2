class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        ret = events[0][0]
        t = events[0][1]
        for p1,p2 in zip(events, events[1:]):
            if p2[1] - p1[1] > t or (p2[1] - p1[1] == t and ret>p2[0]):
                t =  p2[1] - p1[1]
                ret = p2[0]
        return ret 
            