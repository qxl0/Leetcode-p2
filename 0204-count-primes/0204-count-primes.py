class Solution:
    def countPrimes(self, n: int) -> int:
        n -=1
        visit = [False]*(n+1)
        prime = [0]*((n//2) +1)
        cnt = 0

        for i in range(2, n+1):
            if not visit[i]:
                prime[cnt] = i
                cnt += 1
            for j in range(cnt):
                if i*prime[j]>n:
                    break
                visit[i*prime[j]] = True
                if i%prime[j]==0:
                    break
                

        return cnt