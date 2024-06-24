class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        addResult,subResult = nums[0],nums[0]
        for x in nums[1:]:
            temp_add = max(addResult, subResult) + x
            temp_sub = addResult - x

            addResult,subResult = temp_add,temp_sub
        return max(addResult,subResult)
