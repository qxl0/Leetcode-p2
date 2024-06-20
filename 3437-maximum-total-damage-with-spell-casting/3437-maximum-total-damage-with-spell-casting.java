class Solution {
    public long maximumTotalDamage(int[] power) {
        // dp[i]: max possible total damage cast from 0..i   
        int n = power.length;
        // sort 
        Arrays.sort(power);
        long[] dp = new long[n+1];
        long max_p = 0;

        int j=0;
        long ret = 0;
        for (var i=0; i<n; i++) {
            // power[i] 
            if (power[i]==power[Math.max(0, i-1)]) 
                dp[i+1] = dp[i]+power[i];
            else {
                while (j<n && power[j]+2<power[i]) {
                    max_p = Math.max(max_p, dp[++j]);
                }

                dp[i+1] = Math.max(dp[i+1], max_p + power[i]);                
            }            
            ret = Math.max(ret, dp[i+1]);
        }

        return ret;
    }
}