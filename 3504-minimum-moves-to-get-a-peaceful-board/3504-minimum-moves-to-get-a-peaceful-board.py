class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        rooks.sort(key=lambda x:x[0])
        ret = 0
        n = len(rooks)
        for i in range(n):
            ret += abs(rooks[i][0]-i)
            rooks[i][0] = i
        
        rooks.sort(key=lambda x:x[1])
        for j in range(n):
            ret += abs(rooks[j][1]-j)
            rooks[j][1] = j
        
        return ret
        
        