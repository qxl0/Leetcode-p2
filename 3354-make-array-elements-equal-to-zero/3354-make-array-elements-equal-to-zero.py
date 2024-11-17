class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        presum = list(accumulate(nums))
        ret = 0
        n = len(nums)
        for i in range(n):
            if nums[i]!=0:
                continue
            # calculate left sum, and right sum
            left = presum[i-1] if i>=1 else 0
            right = presum[n-1]-presum[i]
            if left==right:
                ret += 2
            elif abs(left-right)<=1:
                ret += 1
        return ret