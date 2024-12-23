class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl,pl = list(s),list(p)
        m,n = len(s),len(p)
        dp = [[0]*(n+1) for _ in range(m+1)]
        def isMatch(lst, pst, i, j):
            # return True if lst[i..] matches pst[j..]
            if dp[i][j]>0:
                return dp[i][j]==1
            ans = False
            if i>=len(sl):
                if j>=len(pl):                    
                    ans = True
                else:
                    ans = j+1<len(pl) and pl[j+1]=='*' and isMatch(sl,pl,i,j+2)                    
            elif j>=len(pl):
                ans = False
            else: # i,j, both left 
                if j+1==len(pl) or pl[j+1]!='*':
                    ans = (sl[i]==pl[j] or pl[j]=='.') and isMatch(sl,pl,i+1,j+1)
                else:
                    ret1 = (sl[i]==pl[j] or pl[j]=='.') and isMatch(sl,pl,i+1,j)
                    ret2 = isMatch(sl,pl,i,j+2)
                    ans = ret1 or ret2                    
            dp[i][j] = 1 if ans else 2
            return ans
        return isMatch(sl,pl,0,0)