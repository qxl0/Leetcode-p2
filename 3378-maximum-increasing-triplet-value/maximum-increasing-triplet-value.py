from sortedcontainers import SortedList
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n =len(nums)
        right = [-inf]*n
        mx = nums[n-1]
        for i in range(n-2,-1,-1):
            if nums[i]<mx:
                right[i] = mx
            mx = max(mx, nums[i])
        
        Set = SortedList()
        Set.add(nums[0])
        ret = 0
        for i in range(1,n-1,1):
            pos = Set.bisect_left(nums[i])
            if pos>0:
                ret = max(ret, Set[pos-1]+right[i]-nums[i])
            Set.add(nums[i])
        return ret
