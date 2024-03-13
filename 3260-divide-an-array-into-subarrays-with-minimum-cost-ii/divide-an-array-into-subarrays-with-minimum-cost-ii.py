from sortedcontainers import SortedList
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n =len(nums)
        sl = SortedList(nums[1:dist+1])
        ret,cur = float("inf"), sum(sl[:k-2])
        for i in range(dist+1,n):
            if sl.bisect(nums[i])<=k-2:
                cur+=nums[i]
            else:
                cur+=sl[k-2]
            ret = min(ret, cur)
            sl.add(nums[i])
            # remove i-dist 
            if sl.bisect(nums[i-dist])<=k-2:
                cur -= nums[i-dist]
            else:
                cur -= sl[k-2]
            sl.remove(nums[i-dist])
        return ret+nums[0]