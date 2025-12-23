class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        sm = 0
        def gen(pos, path):
            nonlocal sm
            if pos == n:
                sm += path
                return
            gen(pos+1, path)
            gen(pos+1, path^nums[pos])
        gen(0,0)
        return sm