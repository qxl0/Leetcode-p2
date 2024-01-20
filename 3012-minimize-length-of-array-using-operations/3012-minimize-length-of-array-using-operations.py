class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        """ if the min of nums occurs only once, then return 1
        
        """
        count = Counter(nums)
        mn = min(nums)
        if count[mn]==1: return 1
        
        for v1 in count:        
            if v1!=mn and v1%mn != 0 and v1%mn not in count: 
                return 1
        
        return ceil(count[mn]/2)
        
        
        