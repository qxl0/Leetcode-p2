class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        if median==k:
            return 0
        else:
            ret = 0
            if median>k:            
                for i in range(n//2,-1,-1):
                    if nums[i]<=k: 
                        return ret   
                    ret += nums[i]-k                                
            else:  # median<k               
                for i in range(n//2,n,1):
                    if nums[i]>=k:
                        return ret 
                    ret += k-nums[i]
            return ret 