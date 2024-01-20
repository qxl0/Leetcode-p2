class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ret = nums[0]
        arr = sorted(nums[1:])
        ret += sum(arr[:2])
        return ret
        