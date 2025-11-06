class Solution:
    def splitArray(self, nums: List[int], K: int) -> int:
        n = len(nums)
        presum = list(accumulate(nums))
        dp = [[-1]*(K+1) for _ in range(n)]
        def dfs(i,k): # i....n-1,  minimized largest sum of the split, 
            if k==1:
                return presum[n-1]-(presum[i-1] if i>0 else 0)
            if dp[i][k]!=-1:
                return dp[i][k]
            # find the cut from i....n-1
            ret = presum[n-1]
            for j in range(n-k+1):
                cur = presum[j]-(presum[i-1] if i>0 else 0)
                if cur >= ret:
                    break
                largest = max(cur, dfs(j+1, k-1))
                ret = min(ret, largest)
                
            dp[i][k] = ret
            return ret

        return dfs(0, K)