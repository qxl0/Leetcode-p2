class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        MAXL = 10**5+2
        # MAXL = 9
        n = len(nums)
        dq = [0]*MAXL
        h=t=0
        
        # add k-1 elements to dq
        for i in range(k-1):
            while h<t and nums[dq[t-1]] < nums[i]:
                t -= 1
            dq[t] = i
            t += 1
        # main loop
        ans = [0]*(n-k+1)
        for i in range(k-1, n):
            # add i to dq
            while h<t and nums[dq[t-1]] < nums[i]:
                t -= 1
            dq[t] = i
            t += 1
            # get ans
            ans[i-k+1] = nums[dq[h]]
            # remove element at i-k
            if dq[h] == i-k+1:
                h += 1
        return ans