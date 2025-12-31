class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort() # [1,2,2,2,5] --> target = 5
        def dfs(i, path, t): # i.., find newpath st. sum(newpath)==t, 
            if t==0:
                ret.append(path.copy())
                return
            if i>len(candidates):
                return
            for j in range(i, len(candidates)):     
                if j>i and candidates[j]==candidates[j-1]:
                    continue           
                if candidates[j]>t:
                    continue 
                dfs(j+1, path+[candidates[j]], t-candidates[j])
        dfs(0, [], target)
        return ret