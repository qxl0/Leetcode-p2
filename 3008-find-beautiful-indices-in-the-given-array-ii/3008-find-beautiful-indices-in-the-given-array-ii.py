class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # use kmp algorithm 
        def kmp(s):
            dp = [0]*len(s)
            for i in range(1,len(s)):
                cur = dp[i-1]
                while cur and s[i]!=s[cur]:
                    cur = dp[cur-1]
                dp[i] = cur + (s[i]==s[cur])
            return dp
        v1 = kmp(a+'#'+s)
        v2 = kmp(b+'#'+s)
        ii = [i-len(a)*2 for i,v in enumerate(v1) if v1[i]>=len(a)]
        jj = [i-len(b)*2 for i,v in enumerate(v2) if v2[i]>=len(b)]
        print(ii,jj)
        ret = []
        jdx = 0
        for i in ii:
            while jdx<len(jj) and jj[jdx]<i-k:
                jdx += 1
            if jdx<len(jj) and jj[jdx]<=i+k:
                ret.append(i)
        return ret 
                
        