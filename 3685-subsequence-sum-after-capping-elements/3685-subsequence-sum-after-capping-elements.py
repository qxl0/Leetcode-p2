class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        dp = [False]*(k+1)
        nums.sort()  # sorted
        ret = [False]*n
        dp[0] = True
        i = 0
        for x in range(1, n+1):
            while i<n and nums[i]<x:
                for c in range(k, 0, -1):
                    if c<nums[i]: break
                    dp[c] = dp[c] | dp[c-nums[i]]                    
                i += 1
            for j in range(n-i+1):
                if k>=x*j and dp[k-x*j]:
                    ret[x-1] = True
                    break            
        return ret


                