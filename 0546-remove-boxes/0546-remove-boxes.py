class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[-1]*n for _ in range(n)] for _ in range(n)]
        def f(l,r,k):
            # max points boxes[l...r] with k prefix boxes which same color as boxes[l]
            if l>r:
                return 0            
            if dp[l][r][k]!=-1:
                return dp[l][r][k]            
            start = l
            while start+1<n and boxes[start+1]==boxes[l]:
                start += 1
            # when stop
            # 
            cnt = k+start-l+1
            ans = cnt*cnt + f(start+1, r, 0)
            for m in range(start+2, r+1, 1):
                if boxes[m]==boxes[l] and boxes[m-1]!=boxes[m]:
                    ans = max(ans, f(start+1, m-1,0) + f(m, r, cnt))
            dp[l][r][k] = ans

            return ans
        return f(0,n-1,0)