class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        nums = [i for i, val in enumerate(nums) if val != 0]
        n = len(nums)
        prefix_sum = [0] + list(accumulate(nums))
        res = inf
        for m in range(max(0, k-maxChanges), min(n, max(0, k-maxChanges)+3, k) + 1):
            for i in range(n - m + 1):
                cur = (prefix_sum[i + m] - prefix_sum[i + m - m // 2]) - (prefix_sum[i + m // 2] - prefix_sum[i])
                res = min(res, cur + (k - m) * 2)
        return res
        
        