class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        count = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]<=nums[j]:
                    continue
                if dp[i]<dp[j]+1:
                    dp[i] = dp[j]+1
                    count[i] = count[j]
                elif dp[i]==dp[j]+1:
                    count[i] += count[j]
        maxLen = 0
        res = 0
        print(count)
        for i in range(n):
            if maxLen<dp[i]:
                maxLen=dp[i]
                res = count[i]
            elif maxLen == dp[i]:
                res += count[i]
        return res
            
                    
                    
                
                    
        