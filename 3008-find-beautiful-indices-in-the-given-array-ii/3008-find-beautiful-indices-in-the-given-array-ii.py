class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(s):
            n = len(s)
            dp = [0]*n
            for i in range(1,n):
                cur = dp[i-1]
                while cur and s[cur]!=s[i]:
                    cur = dp[cur-1]
                dp[i] = cur + (s[cur]==s[i])
            return dp
        v1 = kmp(a+'#'+s)
        v2 = kmp(b+'#'+s)
        al,bl = len(a),len(b)
        ii = [i-al-al for i,v in enumerate(v1) if v>=al]
        jj = [i-bl-bl for i,v in enumerate(v2) if v>=bl]
        
        ret = []
        j = 0
        for i in ii:
            while j<len(jj) and jj[j]<i-k:
                j += 1
            # when stop
            if j<len(jj) and jj[j]<=i+k:
                ret.append(i)
        return ret 