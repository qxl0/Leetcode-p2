class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # find the length of the longest sequential, and the start
        """
        count = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+= nums[i]
            else:
                break
        while True:
            if count not in nums:
                return count
            else:
                count+=1
        """
        ret = nums[0]
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                ret += nums[i]
            else:
                break
        while True:
            if ret not in nums:
                return ret
            ret += 1
        