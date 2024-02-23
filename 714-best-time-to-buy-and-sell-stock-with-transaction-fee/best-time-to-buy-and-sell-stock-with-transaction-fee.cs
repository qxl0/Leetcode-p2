public class Solution {
    public int MaxProfit(int[] prices, int fee) {
        int n = prices.Length;
        int sold=0,hold=-prices[0]-fee;

        for (int i=1;i<n;i++) {
            int oldhold = hold;
            hold = Math.Max(hold, sold-prices[i]-fee);
            sold = Math.Max(sold, oldhold+prices[i]);
        }

        return sold>0?sold:0;
    }
}