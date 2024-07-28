class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def getprimes(n):
            dp = [0]*(n+1)
            for i in range(2, int(sqrt(n))+1):
                if dp[i]==1:
                    continue
                j = i*2
                while j<=n:
                    dp[j] = 1
                    j += i          
            primes = []  
            for i in range(2,n+1):
                if dp[i]==0:
                    primes.append(i)
            return primes
        primes = getprimes(int(sqrt(10**9)))
        ret = 0
        for p in primes:
            if p>=sqrt(l) and p<=sqrt(r):
                ret += 1
        return r-l+1-ret