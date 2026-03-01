class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm%4!=0:
            return False
        n = len(nums)
        target = sm//4
        def dfs(pos, tmpSum, grpId, vis):
            if grpId==4: return True
            if  tmpSum == target: return dfs(0, 0, grpId+1, vis)
            if tmpSum>target: return False

            for i in range(pos, n):
                if vis[i]: continue
                if i>0 and nums[i]==nums[i-1] and not vis[i-1]: continue
                vis[i] = 1
                if dfs(i+1, tmpSum + nums[i], grpId, vis):
                    return True
                vis[i] = 0
            return False

        nums.sort()
        vis = [0]*n
        return dfs(0, 0, 0, vis)