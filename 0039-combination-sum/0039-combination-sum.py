class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        n = len(candidates)
        def dfs(cur, path, sm):
            if sm>target or cur>=n:
                return
            if sm==target:
                ret.append(path.copy())
                return
            dfs(cur, path+[candidates[cur]], sm+candidates[cur])
            dfs(cur+1, path, sm)
        dfs(0,[],0)
        return ret