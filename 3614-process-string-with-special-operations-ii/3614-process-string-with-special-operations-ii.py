class Solution:
    def processStr(self, s: str, k: int) -> str:
        # append '#' to make index : 1....n
        n = len(s)
        s = '#' + s        
        length = [0]*(n+1)
        for i in range(1,n+1):
            c = s[i]
            if 'a'<=c and c<='z':                
                length[i] = length[i-1] + 1
            elif c == '*':
                length[i] = 0 if length[i-1]==0 else length[i-1]-1
            elif c == '#':
                length[i] = length[i-1]*2
            elif c == '%':
                length[i] = length[i-1]
        k += 1
        if k>length[n] or k==0: return '.'

        for t in range(n, 0, -1):
            c = s[t]
            before = length[t-1]
            after = length[t]
            if 'a'<=c and c<='z':                
                if k == after: return c
            elif c == '*':
                k = k
            elif c == '#':
                if k > before:
                    k = k - before
            elif c == '%':
                k = before + 1 -k
        return '.'