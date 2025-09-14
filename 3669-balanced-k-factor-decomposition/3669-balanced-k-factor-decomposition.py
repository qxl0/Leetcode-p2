class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        factors = []
        for i in range(1,floor(sqrt(n))+1):
            if n%i==0:
                factors.append(i)
                if n//i <=i:
                    continue
                factors.append(n//i)
        factors.sort()
        ret = []
        bestDiff,diff=inf,inf
        cur = []
        def dfs(idx, n, k):
            nonlocal bestDiff,ret
            if k==1:
                cur.append(n)
                diff = cur[-1]-cur[0]
                if diff<bestDiff:
                    bestDiff=diff
                    ret = cur.copy()
                cur.pop()
                return
            for i in range(idx, len(factors)):
                d = factors[i]
                if n%d!=0:continue
                if n//d < d: break
                cur.append(d)
                dfs(i,n//d, k-1)
                cur.pop()
        dfs(0,n,k)
        return ret

