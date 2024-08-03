class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        player = [[0]*11 for _ in range(n)]
        count = set()        
        for p, color in pick:
            player[p][color]+=1
            if player[p][color]>p:
                count.add(p)
        return len(count)