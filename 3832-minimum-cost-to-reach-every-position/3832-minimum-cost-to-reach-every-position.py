class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        # find min before or at i
        n = len(cost)
        ans = [0]*n
        mn = cost[0]
        for i in range(n):
            mn = min(mn, cost[i])
            ans[i] = mn
        return ans