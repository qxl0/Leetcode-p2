class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:x[0])
        maxDay = max(events[i][1] for i in range(len(events)))
        heap = []
        ans = 0
        i = 0
        for day in range(events[0][0], maxDay+1):
            # add end day in
            while i<len(events) and day==events[i][0]:
                heappush(heap, events[i][1])
                i += 1
            # remove 
            while len(heap)>0 and heap[0]<day:
                heappop(heap)
            # 
            if len(heap)>0:
                ans += 1
                heappop(heap)
        return ans