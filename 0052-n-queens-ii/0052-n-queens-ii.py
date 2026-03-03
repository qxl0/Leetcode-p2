class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        def dfs(queens,pdiff,psum):
            nonlocal ans
            p=len(queens)
            if p==n:
                ans += 1            
            for q in range(n):
                if q not in queens and p-q not in pdiff and p+q not in psum:
                    dfs(queens+[q], pdiff+[p-q], psum+[p+q])
        dfs([],[],[])
        return ans