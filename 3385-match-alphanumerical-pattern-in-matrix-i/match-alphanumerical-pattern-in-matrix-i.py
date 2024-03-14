class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
        m,n = len(board),len(board[0])
        t,s = len(pattern),len(pattern[0])
        def check(i,j):
            Map = {}
            rMap = {}
            for l in range(t):
                for k in range(s):
                    if pattern[l][k].isdigit():
                        if int(pattern[l][k])!=board[i+l][j+k]:
                            return False 
                        else:
                            continue
                    if pattern[l][k] in Map:
                        if Map[pattern[l][k]]!=board[i+l][j+k]:
                            return False
                    if board[i+l][j+k] in rMap:
                        if rMap[board[i+l][j+k]]!=pattern[l][k]:
                            return False
                    Map[pattern[l][k]] = board[i+l][j+k]
                    rMap[board[i+l][j+k]] = pattern[l][k]
            return True

        for i in range(m-t+1):
            for j in range(n-s+1):
                if check(i,j):
                    return [i,j]
        return [-1,-1]