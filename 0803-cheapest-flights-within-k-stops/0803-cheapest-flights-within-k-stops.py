class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:        
        graph = defaultdict(list)
        for a,b,w in flights:
            graph[a].append((b,w))    
        distance = [inf]*n
        distance[src]=0
        queue = deque()
        queue.append(src)
        for i in range(k+1):
            quelne = len(queue)
            nxt = distance.copy()
            for _ in range(quelne):
                cur = queue.popleft()                
                for nei,w in graph[cur]:
                    if distance[cur] + w < nxt[nei]:                        
                        nxt[nei] = distance[cur]+w
                        queue.append(nei)
            distance = nxt
        return distance[dst] if distance[dst]!=inf else -1
