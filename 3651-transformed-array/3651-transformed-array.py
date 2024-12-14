class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]*n
        for i,x in enumerate(nums):
            if x>0:
                arr[i] = nums[(i+x)%n]
            elif x<0:
                arr[i] = nums[(i+x+n)%n]
            else:
               arr[i] = nums[i] 
            
        return arr