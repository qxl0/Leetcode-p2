class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        arr = [1]*n
        while k:
            k -=1
            arr = list(accumulate(arr))
        return arr[n-1]%(10**9+7)
            