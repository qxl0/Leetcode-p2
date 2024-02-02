# Definition for an infinite stream.
# class InfiniteStream:
#     def next(self) -> int:
#         pass
class Solution:
    def findPattern(self, stream: Optional['InfiniteStream'], pattern: List[int]) -> int:        
        def kmp(p):
            n = len(p)
            dp = [0]*n
            for i in range(1,n):
                j = dp[i-1]
                while j>0 and p[j]!=p[i]:
                    j = dp[j-1] # not equal, so we j'=dp[j-1], and try the same
                dp[i] = j + (p[j]==p[i])
            return dp
        N = 10**5+1
        if len(pattern)==0: return 0
        
        lp = kmp(pattern)
        dp = [0]*N
        if pattern[0]==stream.next():
            dp[0] = 1
            if len(pattern)==1:
                return 0
        for i in range(1,N):
            j = dp[i-1]
            si = stream.next()
            while j>0 and pattern[j]!=si:
                j = lp[j-1]
            dp[i] = j+(pattern[j]==si)
            if dp[i]==len(pattern):
                return i-len(pattern)+1
        return 99999
            
            
                
            
            
            
            