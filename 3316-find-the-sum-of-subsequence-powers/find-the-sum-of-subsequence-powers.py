class Solution:
    def sumOfPowers(self, nums: List[int], K: int) -> int:
        MOD=10**9+7
        n = len(nums)
        nums.sort()

        def helper(a,b,d):
            dp1 = [[0]*(K+1) for _ in range(n)]
            dp2 = [[0]*(K+1) for _ in range(n)]

            for i in range(n):
                dp1[i][1] = 1
                dp2[i][1] = 1 
            # x x x x x k x x x i .... 
            for i in range(a+1):
                for j in range(2,K+1):
                    for k in range(i):
                        if nums[i]-nums[k]>d:
                            dp1[i][j] += dp1[k][j-1]
            # x x x i x x x x k x x    
            for i in range(n-1,b-1,-1):
                for j in range(2,K+1):
                    for k in range(n-1,i,-1):
                        if nums[k]-nums[i]>=d:
                            dp2[i][j] += dp2[k][j-1]
            ret = 0
            for t in range(K):
                ret+=dp1[a][t]*dp2[b][K-t]
                ret%=MOD   
            return ret * d  
        ret = 0
        for a in range(n):
            for b in range(a+1,n):
                ret += helper(a,b,nums[b]-nums[a])
                ret %= MOD   
        return ret 