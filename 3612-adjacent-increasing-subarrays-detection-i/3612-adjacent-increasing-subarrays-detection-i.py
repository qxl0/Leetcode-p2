class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if k==1: return True     
        def issorted(i):
            if i+k>n:
                return False
            j = i
            while j<i+k-1 and nums[j]<nums[j+1]:
                j += 1
            return j==i+k-1
        for i in range(n):
            if issorted(i) and issorted(i+k):
                return True
        return False