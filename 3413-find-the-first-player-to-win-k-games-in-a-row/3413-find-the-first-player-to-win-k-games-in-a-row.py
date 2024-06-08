class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        mx = max(skills)
        if k>=n: 
            for i in range(n):
                if skills[i]==mx:
                    return i
        arr = deque()
        arr.extend(range(n))
        Map = [k]*n
        while len(arr)>=2:
            p1,p2 = arr.popleft(), arr.popleft()
            if skills[p1]>skills[p2]:
                arr.appendleft(p1)
                arr.append(p2)
                Map[p1]-=1
                if Map[p1]==0:
                    return p1
            else:
                arr.append(p1)
                arr.appendleft(p2)
                Map[p2] -= 1
                if Map[p2]==0:
                    return p2 

