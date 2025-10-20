class Solution:
    def maxTotalValue(self, nums: List[int], K: int) -> int:
        n = len(nums)
        MX = 5*10**4 + 5
        D = 20
        # mn = [[inf]*32 for _ in range(MX)]
        # mx = [[-inf]*32 for _ in range(MX)]
        mn = defaultdict(lambda: defaultdict(lambda: inf))
        mx = defaultdict(lambda: defaultdict(lambda: -inf))
        for i in range(n):
            mn[i][0] = mx[i][0] = nums[i]
        for k in range(1, D):
            i = 0
            while i+(1<<k)-1<n:
                mn[i][k] = min(mn[i][k-1], mn[i+(1<<(k-1))][k-1])
                mx[i][k] = max(mx[i][k-1], mx[i+(1<<(k-1))][k-1])
                i += 1
        def getVal(l, r):
            if l>r: return 0
            k = floor(log(r-l+1, 2))
            return max(mx[l][k], mx[r-(1<<k)+1][k])-min(mn[l][k], mn[r-(1<<k)+1][k])
        def countVal(v):
            # count subarray with value >= v
            count = 0
            j = 0
            for i in range(n):
                while j<n and getVal(i,j)<v:
                    j += 1
                count += n-j
            return count
        pq = []
        for i in range(n):
            v = getVal(i,n-1)
            pq.append([-v, i, n-1])
        heapify(pq)
        ans = 0
        for _ in range(K):
            nv, i, j = heappop(pq)
            ans -= nv
            if j-1 >= i:
                v2 = getVal(i,j-1)
                heappush(pq, [-v2, i, j-1])
        return ans
        

