class Solution:
    def closestFair(self, n: int) -> int:
        def helper(m, count): # check m, with count digits to compensate
            t = m
            odd,even = 0,0
            while t>0:
                if t%2==0:even+=1
                else: odd += 1
                t //= 10
            diff = odd - even  
            if (count+diff)%2!=0: return -1
            a = (count+diff)//2
            b = (count-diff)//2
            if a<0 or b<0: 
                return -1
            # '0'*a + '1'*b
            return int(str(m)+'0'*a+'1'*b)
        # loop
        ret = helper(n,0)
        if ret!=-1:
            return ret
        count = 0
        while n>=0:
            ret = helper(n+1,count)
            if ret != -1:
                return ret
            ret = helper(n+2, count)
            if ret != -1:
                return ret
            n //=10
            count += 1
        return -1
            
            