class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x<y: return y-x
        # ops to decrease x so it will equal to y
        U = x + (x-y)
        q = deque()
        vis = set()
        q.append((x,0))        
        while q:
            cur, steps = q.popleft()
            if cur == y:
                return steps
            vis.add(cur)
            if cur%11==0:
                if cur//11 not in vis:
                    q.append((cur//11, steps+1))
            if cur%5==0:
                if cur//5 not in vis:
                    q.append((cur//5, steps+1))
            if cur<U:
                if cur+1 not in vis:
                    q.append((cur+1, steps+1))
            if cur-1 not in vis:
                q.append((cur-1, steps+1))
        return x-y
        