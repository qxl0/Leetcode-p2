class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        ret = 0
        nums = [i for i in range(1,n+1)]
        def dfs(cur,idx):
            nonlocal ret 
            if idx == n+1:
                ret += 1
                return
            for num in nums:
                # chose jth element in avail, add to cur 
                if num not in cur and gcd(num, idx)==1:
                    dfs(cur+[num], idx+1)
                
        dfs([], 1)
        return ret
        
        