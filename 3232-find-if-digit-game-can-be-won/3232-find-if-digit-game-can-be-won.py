class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sd_sum = sum(x for x in nums if x<=9)
        dd_sum = sum(x for x in nums if x>=10)
        if sd_sum==dd_sum:
            return False
        return True