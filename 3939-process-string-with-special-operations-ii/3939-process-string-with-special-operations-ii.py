class Solution:
    def processStr(self, s: str, k: int) -> str:
        """
        recursion from n to 0
        """
        n = len(s)
        s = '#'+ s # 1 to n
        l = [0]*(n+1)
        for i in range(1,n+1):
            c = s[i]
            if 'a'<= c and c <= 'z':
                l[i] = l[i-1] + 1                
            elif c == '#':
                l[i] = l[i-1]*2
            elif c == '%': 
                l[i] = l[i-1]
            elif c == '*':
                l[i] = (l[i-1]-1 if l[i-1]>0 else 0)
        k += 1
        if k > l[n] or k == 0:
            return '.'
        for i in range(n,0,-1):
            c = s[i]
            before,after = l[i-1], l[i]
            if 'a'<= c and c <= 'z':
                if k == after: return c
            elif c == '#':
                if k>before:
                    k -= before
            elif c == '%':
                k = before + 1 - k
        return '.'

