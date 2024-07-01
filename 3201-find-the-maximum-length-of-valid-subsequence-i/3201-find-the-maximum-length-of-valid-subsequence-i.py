class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [x%2 for x in nums]

        def getevenodd(x): # x==0 or 1        
            i=0
            while i<n and nums[i]!=x:
                i += 1
            # when stop nums[i]==0
            ret = 1
            j = i+1
            val = 1-x
            while j<n:
                while j<n and nums[j]!=val:
                    j += 1
                # stop nums[j]==val or j>=n 
                if j>=n: break 
                ret += 1
                j += 1
                val = 1-val
            return ret 

        
        # all even, odd, even->odd, odd->even
        ret = sum(1 for x in nums if x==0)
        ret = max(ret, sum(x for x in nums if x==1))
        ret = max(ret, getevenodd(0))
        ret = max(ret, getevenodd(1))
        return ret
        
        
                
