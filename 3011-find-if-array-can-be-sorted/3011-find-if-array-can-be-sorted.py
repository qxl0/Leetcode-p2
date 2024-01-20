class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        
        prevc = None        
        curmax = 0
        prevmax = -inf
        for i,x in enumerate(nums):
            bc = x.bit_count()
            if not prevc:
                prevc = bc
                curmax = x
            elif bc == prevc:
                curmax = max(curmax, x)
                if x < prevmax: return False
            else: # new section
                prevmax = curmax # cache prev max 
                curmax = x
                if x<prevmax: 
                    return False
                prevc = bc
                
        return True
                
            
            
        