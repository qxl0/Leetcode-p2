class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        MAXN = 1<<20
        lsum,rsum = [0]*MAXN,[0]*MAXN
        def collect(nums, i, e, s, sum):
            nonlocal fill
            if i == e:
                sum[fill] = s
                fill += 1
            else:
                j = i + 1
                while j<e and nums[i]==nums[j]:
                    j += 1
                for k in range(j-i+1):
                    collect(nums, j, e, s+nums[i]*k, sum)
        mx,mn = 0,0
        for x in nums:
            if x > 0:
                mx += x
            else:
                mn += x
        if mx < goal:
            return abs(mx-goal)
        if mn > goal:
            return abs(mn-goal)
        n = len(nums)
        nums.sort()
        fill=0
        collect(nums,0, n>>1, 0, lsum)
        lsize = fill
        fill=0
        collect(nums,n>>1, n, 0, rsum)
        rsize = fill
        # get possible subset sums in lsum, rsum
        lsum = sorted(lsum[:lsize])
        rsum = sorted(rsum[:rsize])
        ans = abs(goal)
        i,j = 0, rsize-1
        while i<lsize:
            while j > 0 and abs(goal - lsum[i] - rsum[j-1]) <= abs(goal - lsum[i] - rsum[j]):
                j -= 1
            ans = min(ans, abs(goal-lsum[i]-rsum[j]))
            i += 1
        return ans
            