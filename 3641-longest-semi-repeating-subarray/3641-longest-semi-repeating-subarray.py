class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        ret = 1
        count = Counter()
        repeating = 0
        for j in range(n):
            count[nums[j]] += 1
            if count[nums[j]] == 2: repeating += 1
            while i<n and repeating >k:                
                count[nums[i]] -= 1
                if count[nums[i]]==0:
                    del count[nums[i]]
                if count[nums[i]]==1:
                    repeating -= 1
                i += 1
            if repeating<=k:
                ret = max(ret, j-i+1)
        return ret
