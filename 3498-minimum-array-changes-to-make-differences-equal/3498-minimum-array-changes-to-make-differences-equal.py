class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter(abs(nums[i]-nums[n-1-i]) for i in range(n//2))
        freqlst = count.most_common(2)
        maxdiff1 = freqlst[0][0]
        maxdiff2 = k
        if len(freqlst)>=2:
            maxdiff2 = freqlst[1][0]
        ret = 2*n
        for x in [maxdiff1, maxdiff2]:
            cur = 0
            for i in range(n//2):
                left,right=nums[i], nums[n-1-i]
                if left>right:
                    left,right=right,left  # make sure left<right
                d = right-left 
                mxd = max(right-0, k-left)
                if d==x:
                    continue
                if x <= mxd:
                    cur += 1
                else:
                    cur += 2
            ret = min(ret, cur)
        return ret 


