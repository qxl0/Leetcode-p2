class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        lastgrouphigh = 0
        high = nums[0]
        bitchange = False
        for i in range(1,len(nums)):
            # check if cross group??
            bitchange = (nums[i].bit_count()!=high.bit_count())
            if bitchange:
                lastgrouphigh = high
            # maintain high
            high = max(high, nums[i])
            # check if not sortable 
            if nums[i]<lastgrouphigh:
                return False
        return True 


                