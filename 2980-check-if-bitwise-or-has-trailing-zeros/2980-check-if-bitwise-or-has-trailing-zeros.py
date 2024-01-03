class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        arr = [(1 if x%2==0 else 0) for x in nums]
        return sum(arr)>=2