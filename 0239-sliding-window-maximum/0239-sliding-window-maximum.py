class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        MAXL = 100003
        n = len(nums)
        dq = [0]*MAXL
        h=t=0
        for i in range(k-1):  # add k-1 elements
            while h<t and nums[dq[t-1]]<=nums[i]:
                t -= 1
            dq[t] = i
            t += 1
        # start loop
        j = 0
        ans = [0]*(n-k+1)   
        for i in range(k-1, len(nums)):
            # add element at i
            while h<t and nums[dq[t-1]]<=nums[i]:
                t -= 1
            dq[t] = i            
            t += 1
            # ans got 
            ans[i-k+1] = nums[dq[h]]
            # remove element at j
            if dq[h]==j:
                h += 1
            j += 1
        return ans