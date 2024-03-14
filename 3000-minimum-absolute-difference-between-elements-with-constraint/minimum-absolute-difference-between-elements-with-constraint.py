from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:        
        sl = SortedList()
        ret = inf
        n = len(nums)
        for i in range(x,n):
            sl.add(nums[i-x])
            pos = sl.bisect_left(nums[i])
            if pos==len(sl):
                ret = min(ret, abs(nums[i]-sl[pos-1]))                
            else:                
                ret = min(ret, abs(nums[i]-sl[pos]))
                if pos>0:
                    ret = min(ret, abs(nums[i]-sl[pos-1]))
                
            # print(f'i={i}, ret={ret},sl={sl}')
            
        return ret 

