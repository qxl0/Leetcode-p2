class Solution:
    def makeAntiPalindrome(self, s: str) -> str:        
        n = len(s)
        ans = sorted(ch for ch in s)
        i=j=n//2 
        while j<n and ans[j]==ans[i]:
            j += 1
        while ans[i]==ans[n-1-i]:
            if j==n: return "-1"
            ans[i],ans[j]=ans[j],ans[i]
            i+=1
            j+=1
        
        return "".join(ans)

    