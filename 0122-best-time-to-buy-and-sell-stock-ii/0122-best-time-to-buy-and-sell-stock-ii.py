class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy, max profit after brought at time i, last action must be sell
        # sell, max profit after sold at time i, last action must be buy
        buy,sell = -inf, 0
        for i in range(len(prices)):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i])
        return max(buy, sell)