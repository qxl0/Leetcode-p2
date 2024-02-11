class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        def checkok(i):
            # check i,i+1,...i+m
            for k in range(m):
                if pattern[k]==1 and nums[i+k+1]<=nums[i+k]:
                    return False
                if pattern[k]==0 and nums[i+k+1]!=nums[i+k]:
                    return False
                if pattern[k]==-1 and nums[i+k+1]>=nums[i+k]:
                    return False
            return True
        count = 0
        for i in range(n-m):
            if checkok(i):
                count += 1
        return count