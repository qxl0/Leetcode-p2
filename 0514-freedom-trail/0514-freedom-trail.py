class Solution:
    def findRotateSteps(self, r: str, k: str) -> int:
        MAXN = 101
        MAXC = 26
        size = [0]*MAXC
        ring = [-1]*MAXN
        key = [-1]*MAXN
        where = [[0]*MAXN for _ in range(MAXC)]
        dp = [[-1]*MAXN for _ in range(MAXN)]
        M, N = len(r), len(k)
        def clock(i,v):
            # find pos clockwize 
            sorted_l = where[v]
            l, r = 0, size[v]-1
            find = -1
            while l<=r:
                mid = l + (r-l)//2
                if sorted_l[mid] > i:
                    find = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return sorted_l[find] if find != -1 else sorted_l[0]
        def counterclock(i, v):
            # find < i 
            sorted_l = where[v]
            l,r = 0, size[v]-1
            find = -1
            while l<=r:
                mid = r - (r-l)//2
                if sorted_l[mid] < i:
                    find = mid
                    l = mid+1
                else:
                    r = mid-1
            return sorted_l[find] if find != -1 else sorted_l[size[v]-1]
        def build():
            # build up structure so f can be called
            for i in range(M):
                cur = ord(r[i])-ord('a')
                ring[i] = cur
                where[cur][size[cur]] += i
                size[cur] += 1
            for i in range(N):
                cur = ord(k[i]) - ord('a')
                key[i] = cur                
        def f(i,j):
            # cur pos = i, return minimal number of steps to spell all chars in the key
            if j==N:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            ans = 0
            # ring[i]==key[j]
            if ring[i]==key[j]:
                ans = 1+f(i, j+1)
            else:
                jump1 = clock(i, key[j])
                dist1 = jump1 - i if i<jump1 else M-i+jump1
                jump2 = counterclock(i,key[j])
                dist2 = i-jump2 if i>jump2 else i+M-jump2
                ans = min(dist1 + f(jump1, j), dist2 + f(jump2, j))
            dp[i][j] = ans
            return ans
        build()
        return f(0,0)