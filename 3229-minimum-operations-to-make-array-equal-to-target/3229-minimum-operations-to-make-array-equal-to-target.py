class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        ret = 0
        prev = 0
        for i in range(n):
            cur = nums[i]-target[i]
            if cur>0 and prev<0 or cur<0 and prev>0:
                ret += abs(cur)
            elif abs(cur)-abs(prev)>0:
                ret += abs(cur-prev)
            prev = cur 
        return ret