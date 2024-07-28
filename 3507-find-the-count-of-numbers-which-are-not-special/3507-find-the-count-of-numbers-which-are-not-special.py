class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def eratosthenes(n):
            q = [0] * (n + 1)
            primes = []

            for i in range(2, int(sqrt(n)) + 1):
                if q[i] == 1:
                    continue
                j = i * 2
                while j <= n:
                    q[j] = 1
                    j += i
            for i in range(2, n + 1):
                if q[i] == 0:
                    primes.append(i)
            return primes

        p = eratosthenes(int(sqrt(10**9)))

        ret = 0
        for x in p:
            # if i==2: continue
            if x>=sqrt(l) and x<=sqrt(r):
                ret += 1
        return r-l+1-ret


        