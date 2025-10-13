class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        M = {0:1}
        ret = 0
        presum = list(accumulate(nums))
        for x in presum:
            target = x - k
            if target in M:
                ret += M[target]
            if x in M:
                M[x] += 1
            else:
                M[x] = 1
        return ret