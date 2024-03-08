class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur = 0
        n = len(nums)
        for i in range(n):
            if nums[i]!=val:
                nums[cur] = nums[i]
                cur += 1
        return cur
        