class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        ret = 0
        nums = [i for i in range(1,n+1)]
        def dfs(i, avail, cur):
            nonlocal ret 
            if i == n:
                ret += 1
                return
            for j in range(len(avail)):
                # chose jth element in avail, add to cur 
                if gcd(avail[j], len(cur)+1)==1:
                    dfs(i+1,avail[:j]+avail[j+1:], cur+[avail[j]])
                
        dfs(0,nums,[])
        return ret
        
        