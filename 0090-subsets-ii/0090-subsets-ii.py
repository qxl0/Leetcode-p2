class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i==0 or nums[i]!=nums[i-1]:
                l = len(ans)
            for j in range(len(ans)-l, len(ans)):
                ans.append(ans[j]+[nums[i]])
        return ans