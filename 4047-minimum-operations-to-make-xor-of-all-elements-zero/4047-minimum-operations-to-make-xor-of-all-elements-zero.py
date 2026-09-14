class Solution:
    def minOperations(self, nums: list[int]) -> int:
        xor = 0
        for x in nums:
            xor ^= x
        if xor == 0:
            return 0
        dn = list(set(nums))
        if len(dn)==1: return -1
        N = 2048
        dp = [inf]*N
        dp[0] = 0
        for x in dn:
            for v in range(N-1,-1,-1):
                dp[v^x] = min(dp[v^x], dp[v]+1)
        return dp[xor] if dp[xor]<=len(nums)-1 else -1
            
        