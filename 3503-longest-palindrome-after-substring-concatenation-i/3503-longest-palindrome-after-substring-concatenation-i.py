class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:        
        def ispalin(ns):
            i,j = 0, len(ns)-1
            while i<j and ns[i]==ns[j]:
                i += 1
                j -= 1
            if i>=j: return True
            return False
        ans = 1
        m,n = len(s),len(t)
        for i in range(m+1):                        
            for j in range(i,m+1):
                for k in range(n+1):
                    for l in range(k,n+1):                        
                        ns = s[i:j]+t[k:l]
                        if ispalin(ns):
                            ans = max(ans,len(ns))                
        return ans
