class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        # kmp algorithm?        
        m = len(pattern)
        dp = [0]*m
        for i in range(1,m):
            j = dp[i-1]
            while j>0 and pattern[j]!=pattern[i]:
                j = dp[j-1]
            dp[i] = j + (1 if pattern[j]==pattern[i] else 0)
        # kmp 
        nums2 = []
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                nums2.append(1)
            elif nums[i]>nums[i+1]:
                nums2.append(-1)
            else:
                nums2.append(0)
        # find how many pattern in nums2
        n = len(nums2)
        dp2 = [0]*n # dp2[i]: j => pattern[0:j-1]==nums2[i-j+1:i] all inclusive
        dp2[0] = 1 if (nums2[0]==pattern[0]) else 0
        for i in range(1,n):
            j = dp2[i-1]
            while j>0 and (j==m or nums2[i]!=pattern[j]):
                j = dp[j-1]
            dp2[i] = j + (1 if nums2[i]==pattern[j] else 0)
        # get dp2 
        ret = 0
        for x in dp2:
            if x==m:
                ret += 1
        return ret


        

        