class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD=10**9+7
        arr = [1]*n

        while k:
            presum = list(accumulate(arr))
            cur = [(arr[i]+(presum[i-1] if i>0 else 0))%MOD for i in range(n)]

            arr = cur
            k -= 1
        
        return arr[n-1]