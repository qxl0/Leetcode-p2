class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dp = [[-inf]*5 for _ in range(n)]
        def dfs(i,alen):
            if alen==0:
                return 0
            if i==n:
                return -inf
            if dp[i][alen]!=-inf:
                return dp[i][alen]
            
            take = b[i]*a[4-alen] + dfs(i+1, alen-1)
            notake = dfs(i+1, alen)

            dp[i][alen] = max(take,notake)
            return dp[i][alen]
        return dfs(0,4)

                
        