class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ret = inf
        nums.sort()
        n = len(nums)
        i,j = 0,n-1
        while i<j:
            mn,mx = nums[i], nums[j]
            ret = min(ret, (mn+mx)/2)
            i += 1
            j -= 1
        return ret
