class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # dp[i]: the maximum points you can earn for the exam up to questions[:i]
        n = len(questions)
        ans = 0
        @lru_cache(None)
        def dp(i):
            nonlocal ans            
            if i>=n: return 0
            return max(questions[i][0] + dp(i+questions[i][1]+1), dp(i+1))
        return dp(0)


