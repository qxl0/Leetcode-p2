from sortedcontainers import SortedDict
class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def add(self, i, x):        
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res
class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        MOD=10**9+7
        mx = max(nums)
        g_idx = [[] for _ in range(mx+1)]
        for i in range(len(nums)):
            j = 1
            while j*j<=nums[i]:
                if nums[i]%j==0:
                    g_idx[j].append(i)
                    if j*j != nums[i]:
                        g_idx[nums[i]//j].append(i)
                j += 1
        seq = [0]*(mx+1)
        for g in range(1, mx+1):            
            
            unique_vals = sorted(set(nums[idx] for idx in g_idx[g]))
            val_to_rank = {val: i+1 for i,val in enumerate(unique_vals)}
            arr = []
            for idx in g_idx[g]:
                arr.append(val_to_rank[nums[idx]])
            bit = BIT(len(arr))
            for x in arr:
                tmp = (bit.sum(x-1) + 1)%MOD
                bit.add(x, tmp)
                seq[g] = (seq[g]+tmp)%MOD
        # seq, --> 
        dp = [0]*(mx+1)
        for g in range(mx, 0, -1):
            j = g*2
            dp[g] = seq[g]
            while j<=mx:
                dp[g] = (dp[g] - dp[j] + MOD) %MOD
                j += g 
        ret = 0
        for g in range(1, mx+1):
            ret += g*dp[g]
            ret %= MOD
        return ret

