class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], L: int, R: int) -> int:
        presum = list(accumulate(nums))
        n = len(nums)
        ans = 0
        lmax = 0
        for i in range(n-L-R+1):            
            lmax = max(lmax, presum[i+L-1]-(presum[i-1] if i>0 else 0))
            ans = max(ans, lmax+presum[i+L+R-1]-presum[i+L-1])
        rmax = 0
        for i in range(n-L-R+1):
            rmax = max(rmax, presum[i+R-1]-(presum[i-1] if i>0 else 0))
            ans = max(ans, rmax + presum[i+L+R-1]-presum[i+R-1])
        return ans