class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        """ dfs(cur,invcnt): 
            number of perms of cur distinct elements that satisfy the requirements and have exactly invcnt inversions 
        """
        DistinctElement2Cnt = {end+1:n for end,n in requirements}

        @cache
        def dfs(cur, invcnt):
            if invcnt<0: 
                return 0
            if cur in DistinctElement2Cnt and DistinctElement2Cnt[cur]!=invcnt:
                return 0
            if cur==1:
                return 1 if invcnt==0 else 0
            
            ret = 0
            for i in range(1,cur+1):
                invs = cur - i
                ret += dfs(cur-1, invcnt - invs)
            return ret 
        return dfs(n, DistinctElement2Cnt[n])%(10**9+7)