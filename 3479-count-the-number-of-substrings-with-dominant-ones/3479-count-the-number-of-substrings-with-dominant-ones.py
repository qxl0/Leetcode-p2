class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        right = [0]*n
        def findright():
            right[n-1] = (1 if s[n-1]=='1' else 0)
            for i in range(n-2,-1,-1):
                if s[i]=='0':continue
                right[i] = right[i+1] + (1 if s[i]=='1' else 0)
        findright()
        # print(right)
        ret = 0
        for m in range(1,int(sqrt(n))+1):
            # m: # of 0 in the sliding window            
            count = 0
            j=0
            for i in range(n):                                                           
                while j<n and count<m:
                    if s[j]=='0':
                        count += 1
                    j += 1
                # when stop, x x x x 0]j
                if count!=m: break  # we can't find m 0
                one = j-i-m
                if one+(right[j] if j<n else 0)>=count*count:
                    extra = (right[j] if j<n else 0) - max(0,m*m-one)  # right[j]: # of 1 from j pos including j
                    ret += max(0,extra + 1)
                count -= (1 if s[i]=='0' else 0)
        # m == 0
        for i in range(n):
            if s[i]=='0':continue
            ret += right[i]
        
        return ret 



