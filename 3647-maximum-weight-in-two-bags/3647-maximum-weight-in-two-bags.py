class Solution:
    
    def maxWeight(self, weights: List[int], w1: int, w2: int) -> int:
        dp = [[0]*(w2+1) for _ in range(w1+1)]
        for w in weights:                      # process each item once
            for i in range(w1, -1, -1):        # descend to prevent reuse in bag1
                for j in range(w2, -1, -1):    # descend to prevent reuse in bag2
                    if i >= w:
                        dp[i][j] = max(dp[i][j], dp[i - w][j] + w)   # put in bag1
                    if j >= w:
                        dp[i][j] = max(dp[i][j], dp[i][j - w] + w)   # put in bag2
        return dp[w1][w2]
        