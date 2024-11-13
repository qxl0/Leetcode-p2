class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        up,pre = 1,0
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                up += 1
            else:
                pre = up
                up = 1
            res = max(res, max(up//2, min(pre,up)))
        return res
        