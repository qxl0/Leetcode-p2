class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # 4^15 =  10 ^9
        def count(l,r):
            ret = 0
            for i in range(1,16,1):
                # find # from [4^(i-1), 4^i)
                p0,p1 = pow(4,i-1),pow(4,i)-1
                if p0 > r:break
                if p1 < l: continue
                k,j = max(p0,l), min(p1,r)
                ret += (j-k+1)*i
            return (ret+1)//2
        ans = 0
        for l,r in queries:
            ans += count(l,r)
        return ans