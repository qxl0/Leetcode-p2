class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        n = len(nums)
        for i in range(n):
            if i-1>=0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    # avoid duplicate
                    while l+1<n and nums[l] == nums[l+1]:
                        l += 1
                    while r>i and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ret
