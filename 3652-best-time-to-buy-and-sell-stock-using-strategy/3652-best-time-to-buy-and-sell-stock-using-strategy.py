class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        def getwindow(prices, i):
            # i, ..., i+k-1
            # 0,..i+k//2
            return opre[i+k-1] - opre[i+k//2-1]

        prod = [a*b for a, b in zip(prices,strategy)]
        base = sum(prod)
        presum = list(accumulate(prod))
        opre = list(accumulate(prices))
        ans = base
        n = len(prices)
        i = 0
        while i<=n-k:
            left = (presum[i-1] if i>0 else 0)
            right = presum[n-1]-presum[i+k-1]
            window = getwindow(prices, i)
            ans = max(ans, left+window+right)
            i += 1
        return ans
