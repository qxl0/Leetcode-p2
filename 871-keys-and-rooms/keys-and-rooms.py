class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        count = 0
        n = len(rooms)
        dq = deque([0])
        vis = set([0])
        while dq:
            cur = dq.popleft()            
            count += 1
            for k in rooms[cur]:
                if k not in vis:
                    vis.add(k)
                    dq.append(k)
        return len(vis)==n