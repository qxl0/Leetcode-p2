class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:        
        def isamediag(e,f,c,d):
            return e+f==c+d or e-f==c-d
        def isbetween(e,f,c,d,a,b):
            if e+f==c+d==a+b or e-f==c-d==a-b: 
                if e<a<c or c<a<e: return True
            return False
        def issamevertorhorz(e,f,a,b):
            if e==a or f==b: return True
            return False
        def isbetweenrook(e,f,a,b,c,d):
            if not issamevertorhorz(e,f,c,d): return False
            if e<c<a or a<c<e or f<d<b or b<d<f: return True
            return False
        def rookmove(e,f,c,d):
            if e%2==c%2 or f%2==d%2: return True
            return False
        if isamediag(e,f,c,d):
            if not isbetween(e,f,c,d,a,b): return 1
            return 2
        else:
            if issamevertorhorz(e,f,a,b):
                if not isbetweenrook(e,f,a,b,c,d): return 1                    
            return 2
                