from sortedcontainers import SortedList
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        sl = SortedList(nums[1:dist+1])
        n = len(nums)
        cur,ret = sum(sl[:k-2]),float('inf')
        for i in range(dist+1,n):
            if sl.bisect(nums[i])<=k-2:
                cur+=nums[i]
            else:
                cur+=sl[k-2]
            ret = min(ret, cur)
            sl.add(nums[i])
            if sl.bisect(nums[i-dist])<=k-2:
                cur -= nums[i-dist]
            else:
                cur -= sl[k-2]
            sl.remove(nums[i-dist])
        return ret+nums[0]