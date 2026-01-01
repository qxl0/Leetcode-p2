class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []        
        def dfs(i, path):
            if len(path)==k:
                ret.append(path.copy())
                return 
            if i>n:
                return
            for j in range(i,n+1):
                dfs(j+1, path+[j])
        dfs(1,[])
        return ret