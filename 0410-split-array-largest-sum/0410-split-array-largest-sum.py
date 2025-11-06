class Solution:
    def splitArray(self, nums: List[int], K: int) -> int:
        n = len(nums)
        presum = list(accumulate(nums))
        dp = [[0]*(K+1) for _ in range(n)]
        for k in range(1,K+1):
            for i in range(n):
                if k == 1:
                    dp[i][k] = presum[n-1]-(presum[i-1] if i>0 else 0)
                    continue
                mn = presum[n-1]
                for j in range(i,n-k+1):
                    cur = presum[j]-(presum[i-1] if i>0 else 0)
                    mx = max(cur, dp[j+1][k-1])
                    mn = min(mn, mx)
                    if cur >=mn:
                        break
                dp[i][k] = mn
        return dp[0][K]

                    