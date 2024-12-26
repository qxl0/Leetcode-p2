class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        arr = [0] + sorted(cuts) + [n]
        m = len(cuts)
        dp = [[-1]*(m+2) for _ in range(m+2)]        
        def f(l,r):
            # return the minCost between [l, r]
            if l>r: 
                return 0
            if l==r: 
                return arr[r+1]-arr[l-1]
            if dp[l][r]!=-1: 
                return dp[l][r]
            ans = inf
            for k in range(l, r+1): # l+1,l+2, ... r-1
                ans = min(ans, f(l, k-1)+f(k+1, r))
            ans += arr[r+1]-arr[l-1]
            dp[l][r] = ans
            return ans
        
        return f(1,m)