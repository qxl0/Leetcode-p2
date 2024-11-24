class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        MAXL = 10**5+1
        deque = [0]*MAXL # big ... small queue
        h = t = 0;  # deque head-> h, tail -> t
        # k-1 window
        for i in range(k-1):
            while (h<t and nums[deque[t-1]]<=nums[i]):
                t -= 1
            deque[t] = i
            t += 1
        ans = [0]*(n-k+1) # n=3,k=3
        # window on nums, l, r   
        l,r = 0, k-1
        while l<n-k+1:
            # add a new one at r to deque
            while (h<t and nums[deque[t-1]]<=nums[r]):
                t -= 1
            deque[t] = r
            t += 1
            # 
            ans[l] = nums[deque[h]]
            # 
            if (l==deque[h]):
                h += 1
            l,r = l+1,r+1
        return ans
        
