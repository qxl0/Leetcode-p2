class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ret = []
        def dfs(i,path,s):            
            if s==target:
                ret.append(path.copy())
                return
            if i==n:
                return
            pre = -1
            for j in range(i,n,1):
                if s+candidates[j]>target:
                    continue
                if pre==candidates[j]:
                    continue 
                pre = candidates[j]
                dfs(j+1,path+[candidates[j]], candidates[j]+s)
        candidates.sort()
        dfs(0,[],0)
        return ret 