class Solution:
    def canIWin(self, n: int, m: int) -> bool:
        if m==0:
            return True
        if (n*(n+1)/2<m):
            return False
        def f(status, remaining, dp):
            if remaining<=0:
                return False 
            if dp[status]!=0:
                return dp[status]==1
            ans = False
            for i in range(1, n+1):
                if (status&(1<<i)!=0) and not f((status^(1<<i)), remaining - i, dp):
                    ans = True
                    break
            dp[status] = 1 if ans else -1
            return ans         
        # n = 4, 4,3,2,1,0
        #        1 1 1 1  
        dp = [0]*(1<<(n+1))
        # 0->not set, 1->true, -1->false 
        return f(((1<<(n+1))-1), m, dp)
        