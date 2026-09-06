class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mx_l,mn_l = [],[]
        n= len(nums)
        mx = -1
        mn = inf
        
        for i in range(n):
            mx = max(mx, nums[i])
            mx_l.append(mx)
        for i in range(n-1,-1,-1):
            mn = min(mn, nums[i])
            mn_l.append(mn)
        
        for i in range(n):
            if mx_l[i]-mn_l[n-1-i]<=k:
                return i
        
        return -1
