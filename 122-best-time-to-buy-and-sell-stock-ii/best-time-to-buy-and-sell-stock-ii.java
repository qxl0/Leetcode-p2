class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int sold = 0;
        int hold = -prices[0];
        int ret = 0;

        for (int i=1;i<n;i++) {
            int oldsold=sold;
            sold = Math.max(sold, hold + prices[i]);
            hold = Math.max(hold, oldsold - prices[i]);
            ret = Math.max(ret, sold);
        }

        return ret;
    }
}