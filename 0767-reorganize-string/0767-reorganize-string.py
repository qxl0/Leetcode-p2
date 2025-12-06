class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        n = len(s)
        ans = ['']*n
        q = []
        i =0
        for ch,freq in count.most_common():            
            while freq:
                ans[i] = ch
                if i>=1 and ans[i]==ans[i-1]:
                    return ''
                i += 2
                if i>=n and i%2==0:
                    i = 1
                freq -= 1
        return "".join(ans)

                
