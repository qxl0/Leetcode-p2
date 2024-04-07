class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        if median==k:
            return 0
        else:
            if median>k:
                ret = 0
                for i in range(n//2,-1,-1):
                    if nums[i]<=k: 
                        return ret   
                    ret += nums[i]-k                
                return ret 
            else:  # median<k   
                ret = 0
                for i in range(n//2,n,1):
                    if nums[i]>=k:
                        return ret 
                    ret += k-nums[i]
                return ret 