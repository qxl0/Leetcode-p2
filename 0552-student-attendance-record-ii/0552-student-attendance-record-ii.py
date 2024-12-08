class Solution:
    def checkRecord(self, n: int) -> int:
        MOD=10**9+7
        def multiply(a, b):
            n,k = len(a),len(a[0])
            m = len(b[0])
            ans = [[0]*m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    for c in range(k):
                        ans[i][j] = (a[i][c]*b[c][j]+ans[i][j])%MOD
            return ans
        def power(m, p):
            n = len(m)
            ans = [[0]*n for _ in range(n)]
            for i in range(n):
                ans[i][i] = 1            
            while p!=0:
                if (p&1) !=0:
                    ans = multiply(ans, m)
                m = multiply(m,m)
                p >>=1
            return ans
        start = [[1,1,0,1,0,0]]
        base = [[1,1,0,1,0,0], 
                [1,0,1,1,0,0],
                [1,0,0,1,0,0],
                [0,0,0,1,1,0],
                [0,0,0,1,0,1],
                [0,0,0,1,0,0]
                ]
        ans = multiply(start, power(base,n-1))
        ret = 0
        for a in ans[0]:
            ret = (ret+a)%MOD
        return ret
