class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        x = 0
        for y in nums:
            x ^=y
        x ^=k
        return bin(x).count('1')
            