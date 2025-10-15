class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        def ispar(l,r):
            while l<r:
                if s[l]!=s[r]: return False
                l += 1
                r -= 1
            return True 
        i,j = 0, n-1
        while i<j:
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                return ispar(i+1, j) or ispar(i,j-1)
        return True