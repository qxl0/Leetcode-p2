class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//2
        L,R = nums[:n], nums[n:]
        total = sum(nums)

        left_sum = [[] for _ in range(n+1)]
        right_sum = [[] for _ in range(n+1)]

        for mask in range(1<<n):
            cnt = 0
            sL,sR = 0,0
            for i in range(n):
                if (mask>>i)&1==1:
                    cnt += 1
                    sL += L[i]
                    sR += R[i]
            left_sum[cnt].append(sL)
            right_sum[cnt].append(sR)
        for k in range(n+1):
            right_sum[k].sort()
        
        ans = inf
        for k in range(n+1):
            rlist = right_sum[n-k]
            for sL in left_sum[k]:
                target = total/2 - sL
                idx = bisect_left(rlist, target)
                if idx<len(rlist):
                    sA = sL + rlist[idx]
                    ans = min(ans, abs(total-2*sA))
                if idx>0:
                    sA = sL + rlist[idx-1]
                    ans = min(ans, abs(total-2*sA))
        return ans

