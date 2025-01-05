class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD=10**9+7
        n = len(hats) # how many persons 
        m = max(max(x) for x in hats)
        hat2p = [0]*(m+1)
        for pi in range(n):
            for hat in hats[pi]:
                hat2p[hat] |= (1<<pi)

        dp = [[-1]*(1<<n) for _ in range(m+1)]
        def f(status, curColor):
            # status: x x x x x x x
            #         1 or 0, 1 -> hashat, 0, no hat
            # curColor: cur color hat to work on 
            if status == (1<<n)-1:
                return 1
            if curColor>m:
                return 0
            if dp[curColor][status]!=-1:
                return dp[curColor][status]

            cur = hat2p[curColor] # curColor -> int (xxxxxxxxxxx) if 1, means 
            ans = f(status, curColor+1)
            while cur != 0:
                right = cur & (-cur)
                if status & right == 0:
                    ans = (ans + f(status|right, curColor+1))% MOD
                cur ^= right
            dp[curColor][status] = ans
            return ans
        return f(0, 1)