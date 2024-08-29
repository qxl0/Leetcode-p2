class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def findmin(nums,x):
            for i in range(len(nums)):
                if nums[i]==x:
                    return x,i
        i = 0
        while i<k:
            # find the smallest one 
            mn = min(nums)
            x,idx = findmin(nums,mn)
            nums[idx] = x*multiplier
            i += 1
        return nums
            


            
