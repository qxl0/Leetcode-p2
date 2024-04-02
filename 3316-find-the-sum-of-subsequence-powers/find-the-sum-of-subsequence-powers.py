class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD=10**9+7
        n = len(nums)
        # dp = [[[[0]*51 for _ in range(52)] for _ in range(52)] for _ in range(52)]
        nums.sort()
        @lru_cache(None)
        def dfs(i,count,diff,last):
            if count==k: return diff
            if i>=n: return 0 
            # if dp[i][count][diff][last]>0:
            #     return dp[i][count][diff][last]
            newdiff=diff if last==-1 else min(diff,abs(nums[last]-nums[i]))
            take=dfs(i+1,count+1,newdiff,i)
            nottake=dfs(i+1,count,diff,last)
            # dp[i][count][diff][last] = (take+nottake)%MOD
            # return dp[i][count][diff][last]
            return (take+nottake)%MOD

        return dfs(0,0,MOD,-1)