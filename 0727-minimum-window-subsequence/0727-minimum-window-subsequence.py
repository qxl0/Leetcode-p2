class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slen, tlen = len(s),len(t)
        dp = [[-1]*tlen for _ in range(slen)]
        for i in range(slen):
            if s[i] == t[0]:
                dp[i][0] = i
            else:
                if i != 0:
                    dp[i][0] = dp[i-1][0]
        # dp
        for i in range(1, slen):
            for j in range(1, tlen):
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        # 
        begin, minlen = -1, float('inf')
        for i in range(slen):
            if dp[i][tlen-1] != -1:
                k = dp[i][tlen-1]
                if k != -1:
                    if minlen>i-k+1:
                        begin,minlen = k, i-k+1
        if begin == -1:
            return ""
        return s[begin:begin+minlen]