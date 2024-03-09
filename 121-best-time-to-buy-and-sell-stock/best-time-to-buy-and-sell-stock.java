class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int ret = 0;

        int min = Integer.MAX_VALUE;
        for (var price : prices) {
            ret = Math.max(ret, price-min);
            min = Math.min(min, price);
        }

        return ret;
    }
}