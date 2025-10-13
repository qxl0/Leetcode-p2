class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c,x = 0, None
        for n in nums:
            if x == n:
                c += 1
            elif c == 0:
                c = 1
                x = n
            else:
                c -= 1
        if nums.count(x) >= len(nums)//2:
            return x
            