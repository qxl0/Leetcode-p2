class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        used = [0]*len(nums)
        def dfs(path):
            if len(path)==len(nums):
                ans.append(path.copy())
                return
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1] and not used[i-1] or used[i]:
                    continue
                path.append(nums[i])
                used[i]=1
                dfs(path)
                path.pop()
                used[i]=0
        dfs([])
        return ans