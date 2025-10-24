class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        ans = n+1
        sm = 0
        for i in range(n):
            sm += nums[i]
            while j<n and sm >= target:
                ans = min(ans, i-j+1)
                sm -= nums[j]
                j += 1
        return ans if ans < n+1 else 0

        