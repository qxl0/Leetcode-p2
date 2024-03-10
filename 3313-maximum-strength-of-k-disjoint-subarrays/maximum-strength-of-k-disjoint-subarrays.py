class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[[-1,-1] for _ in range(k+1)] for _ in range(n)]
        def helper(i,j,skip):
            # return Max strength of j disjoint subarrays based on nums[i:] include nums[i] based on skip 
            # x x x x x x x x x x x
            # i
            # nums[i], 
            # j%2==1, add, otherwise minus 
            if j<0: return -inf 
            if (i==n):
                if j==0: return 0
                else: return -inf
            if dp[i][j][skip]!=-1: return dp[i][j][skip]

            op1 = -inf 
            op2 = -inf 
            if skip:
                op1 = helper(i+1,j,skip)
            if j&1==1:
                op2 = max(helper(i+1,j,0)+nums[i]*j, helper(i+1,j-1,1)+nums[i]*j)
            else:
                op2 = max(helper(i+1,j,0)-nums[i]*j, helper(i+1,j-1,1)-nums[i]*j)
            
            dp[i][j][skip] = max(op1,op2)
            return dp[i][j][skip]

        return max(helper(0,k,0),helper(0,k,1))