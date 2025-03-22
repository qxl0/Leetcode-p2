class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cur = [inf]*n
        cur[src]=0
        for i in range(k+1):
            next = cur.copy()
            for a,b,w in flights:
                if cur[a]!= inf:
                    next[b] = min(next[b], cur[a]+w)
            cur = next
        return cur[dst] if cur[dst]!=inf else -1
