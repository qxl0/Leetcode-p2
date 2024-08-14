class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l,r = 0, nums[n-1] 
        while l<r:
            mid = l + (r-l)//2
            # check 
            j=0
            count = 0
            for i in range(n):
                while j<n and nums[j]-nums[i]<=mid:
                    j += 1
                # when stop 
                count += j-i-1
            if count<k:
                l = mid+1
            else:
                r = mid
        return l
