class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [0] + nums
        # add a element, so we know index from 1... n
        # if nums[i] > 0, i is missing 
        for i in range(1, n+1):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(1, n+1):
            val = abs(nums[i])
            if val>n or val<1:
                continue
            if nums[val] > 0:
                nums[val] *= -1
            if nums[val]==0:
                nums[val] = -(n+1)
        for i in range(1,n+1):
            if nums[i] >= 0:
                return i
        return n+1
