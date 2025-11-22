class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        def maxprofitwithfee(fee):
            # return maxprofit,count
            sold = [0]*(n+1)
            hold = [0]*(n+1)
            hold[0] = -inf
            soldcount,holdcount = 0,0
            for i in range(1,n+1):
                if sold[i-1] >= hold[i-1]+prices[i-1]:
                    sold[i] = sold[i-1]
                else:
                    sold[i] = hold[i-1]+prices[i-1]
                    soldcount = holdcount
                if hold[i-1] >= sold[i-1]-prices[i-1]-fee:
                    hold[i] = hold[i-1]
                else:
                    hold[i] = sold[i-1]-prices[i-1]-fee
                    holdcount = soldcount + 1
            return sold[n], soldcount 
        l, r = 0, 1000
        # find optimal fee 
        while l<r:
            mid = l + (r - l)//2
            if maxprofitwithfee(mid)[1]>k:
                l = mid + 1
            else:
                r = mid 
        # l == r
        return maxprofitwithfee(l)[0] + l*k


