class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        # dp[l][msk]: total number of arrays with length l, set of number is the bit pos that's set
        # dp[n][B-1]
        B = 1<<n
        dp = [[0]*B for _ in range(n+1)]
        dp[0][0]=1
        for l in range(1,n+1):
            for msk in range(B):
                dp[l][msk] = 0
                for b in range(n):
                    if msk&(1<<b) and gcd(b+1,l)==1:
                        dp[l][msk] += dp[l-1][msk&~(1<<b)]
        return dp[n][B-1]