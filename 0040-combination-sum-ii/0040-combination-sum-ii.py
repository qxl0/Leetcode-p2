class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ret = []
        candidates.sort()
        def dfs(i,path,sm):            
            if sm == target:
                ret.append(path.copy())
                return
            if i>=n:
                return
            pre = -1
            for j in range(i,n,1):
                if sm+candidates[j]>target:
                    continue
                if pre == candidates[j]:
                    continue                
                pre = candidates[j]                
                dfs(j+1, path+[candidates[j]], candidates[j]+sm)
                
        dfs(0,[], 0)
        return ret