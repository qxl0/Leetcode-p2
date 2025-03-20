class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        MAXN = 1<<20
        lsum = [0]*MAXN
        rsum = [0]*MAXN
        def collect(nums, i, e, s, sum): 
            nonlocal fill           
            if i==e:
                sum[fill] = s  
                fill += 1
            else:
                j = i + 1
                while j<e and nums[j]==nums[i]:
                    j += 1
                # stop 
                for k in range(j-i+1):
                    collect(nums, j, e, s+k*nums[i], sum) 
        n = len(nums)
        mn,mx = 0,0
        for x in nums:
            if x >=0:
                mx += x
            else:
                mn += x
        if mx<goal:
            return abs(mx-goal)
        if mn>goal:
            return abs(mn-goal)
        nums.sort()
        fill=0
        collect(nums,0,n>>1,0, lsum)
        lsize = fill
        fill=0
        collect(nums,n>>1,n,0, rsum)
        rsize = fill
        lsum = sorted(lsum[0:lsize])
        rsum = sorted(rsum[0:rsize])
        ans = abs(goal)
        i,j = 0, rsize-1
        while i<lsize:
            while j>0 and abs(goal-lsum[i]-rsum[j-1]) <= abs(goal-lsum[i]-rsum[j]):
                j -= 1
            ans = min(ans, abs(goal-lsum[i]-rsum[j]))
            i += 1
        return ans

