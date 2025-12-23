class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr = [(c,p) for c,p in zip(capital, profits)]
        arr.sort()
        hq = []
        ret = w
        i = 0
        while k:
            while i<len(arr) and arr[i][0]<=w:
                heappush(hq, -arr[i][1])
                i += 1
            if not hq:
                break
            p = heappop(hq)
            ret += (-p)
            w += (-p)
            k -= 1
        return ret 