class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0]*(k) for _ in range(n)]
        Map = defaultdict(int)
        
        for i in range(n):
            for t in range(k):
                d = (t-nums[i]%k+k)%k
                if d in Map:
                    j=Map[d]
                    dp[i][t] = dp[j][t] + 1
                else:
                    dp[i][t]=1
            Map[nums[i]%k] = i
        ret = 0
        for row in dp:
            ret = max(ret, max(row))
        return ret 