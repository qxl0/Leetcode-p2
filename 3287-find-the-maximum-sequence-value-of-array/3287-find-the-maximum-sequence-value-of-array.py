class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def helper(nums):
            dp = [[set() for _ in range(k+1)] for _ in range(n+1)]  # dp[i][j]: set of values taking j elements from nums[..j] (up to nums[j-1])
            for i in range(n+1):    # dp[i][1]: set of elements: nums[0]... nums[i-1]        
                for l in range(i):  
                    dp[i][1].add(nums[l])
            for i in range(1,n+1):
                for j in range(1,min(i,k)+1):
                    dp[i][j] |= dp[i-1][j] # union operator  # not take nums[i-1]
                    for ele in dp[i-1][j-1]: # take nums[i-1]
                        dp[i][j].add(ele|nums[i-1])
            return dp
        left = helper(nums)
        right = [[set() for _ in range(k+1)] for _ in range(n+1)]
        for i in range(n+1):    # dp[i][1]: set of elements: nums[0]... nums[i-1]        
            for l in range(i,n):  
                right[i][1].add(nums[l])
        for i in range(n-1,-1,-1):
            for j in range(1, min(n-i, k) + 1):
                right[i][j] |= right[i+1][j]
                for t in right[i+1][j-1]:
                    right[i][j].add( t|nums[i])
        
        # print(right)
        # loop throught i
        ret = 0
        for i in range(k, n-k+1):
            for l in left[i][k]:
                for r in right[i][k]:
                    ret = max(ret, l^r)
        return ret


