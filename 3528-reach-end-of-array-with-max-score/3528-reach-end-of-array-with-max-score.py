class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        #dp[i]: max score from i->n-1
        #return dp[0]
        #dp[n-1]:0
        ans,cur = 0,nums[0]
        n = len(nums)
        for i in range(1,n):
            ans += cur
            if nums[i]>cur:
                cur = nums[i]
        return ans
            
        
        