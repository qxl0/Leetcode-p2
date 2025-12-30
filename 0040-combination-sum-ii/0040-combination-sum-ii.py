class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ret = []
        candidates.sort()
        def dfs(i, path, sm):
            if sm == target:
                ret.append(path.copy())
                return
            if i >= n or sm > target:
                return
            
            for j in range(i, n):
                # Skip duplicates at same recursion level
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if sm + candidates[j] > target:
                    break
                dfs(j+1, path+[candidates[j]], sm+candidates[j])
                        
        dfs(0,[], 0)
        return ret