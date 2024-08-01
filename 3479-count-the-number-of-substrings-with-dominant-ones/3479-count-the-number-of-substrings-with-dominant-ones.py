class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)  
        ret = 0      
        for k in range(1,int(sqrt(n))+1):
            ones = 0
            lastzero = -1
            zeros = deque()
            for right in range(n):
                if s[right]=='0':
                    zeros.append(right)
                    while len(zeros)>k:
                        ones -= (zeros[0]-lastzero-1)
                        lastzero = zeros.popleft()                    
                else:
                    ones += 1
                if len(zeros)==k and ones>=k**2:
                    ret += min(ones-k**2+1, zeros[0]-lastzero)
        i = 0
        while i<n:
            if s[i]=='0':
                i += 1
                continue
            sz = 0
            while i<n and s[i]=='1':
                sz += 1
                i += 1
            ret += (sz*(sz+1))//2

        return ret

                    