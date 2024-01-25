class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        """
        o ... o -> x ...  y -> * ... *
        A            C           B
        AA, BB, AB, AC, BC, CC
        """
        if x>y:
            tmp = y
            y = x
            x = tmp
        ret = [0]*n
        if abs(x-y)<=1:
            
            for t in range(1,n):
                ret[t-1] = ((n-t)*2)
            return ret
        
        a = x-1
        b = n-y
        d = y-x+1
        def f1(t,a):
            # AA, BB
            start = 1
            end = a-t
            return max(0,end-start+1)
        def f2(t, a, b):
            # AB: 
            start = max(1,a+3-t)
            end = min(a, a+2+b-t)
            return max(0,end-start+1)
        def f3(t,a, p, q):
            # AC:
            ret = 0
            start = max(1,a+2-t)
            end = min(a, a+1+p-t)
            ret += end-start+1
            
            end2 = min(a,a+1+q-t)
            ret += end2-start+1
            
            if a>=t:
                ret += 1
            return max(0,ret) 
        def f4(t, d):
            # CC
            ret = 0
            if t<d-t:
                ret = d
            elif t == d-t:
                ret = d//2
            return max(0,ret)
        for t in range(1, n):
            ret[t-1] += f1(t,a)
            ret[t-1] += f1(t,b)
            ret[t-1] += f2(t,a,b)
            ret[t-1] += f3(t,a, (d-1)//2, d-1-(d-1)//2)
            ret[t-1] += f3(t,b, (d-1)//2, d-1-(d-1)//2)
            ret[t-1] += f4(t, d)
            ret[t-1] *= 2
        return ret
        
        
        
        