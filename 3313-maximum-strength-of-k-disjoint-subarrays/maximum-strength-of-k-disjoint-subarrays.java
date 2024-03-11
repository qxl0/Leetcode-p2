class Solution {
    public long maximumStrength(int[] nums, int k) {
        int n = nums.length;
        long[][] dp = new long[k+1][n+1];
        for (long[] row : dp)
            Arrays.fill(row, 0l);
        
        for (int i=1;i<=k;i++) {
            long maxsum = Long.MIN_VALUE/2;
            long curr = Long.MIN_VALUE/2;
            long multiplier = i%2==1 ? k+1-i : i-k-1;
            for (int j=i-1;j<n;j++) {
                curr = Math.max(curr+nums[j]*multiplier, dp[i-1][j]+nums[j]*multiplier);
                maxsum = Math.max(maxsum, curr);
                dp[i][j+1] = maxsum;
            }
        }

        return dp[k][n];
    }
}