class Solution {
    public String longestPrefix(String s) {
        int n = s.length();
        int[] dp = new int[n];
        
        dp[0] = 0;
        for (int i = 1; i<n; i++) {
            int j = dp[i-1];
            while (j>0 && s.charAt(j)!=s.charAt(i)) 
                j = dp[j-1];
            dp[i] = j + (s.charAt(j)==s.charAt(i) ? 1:0);
        }
        return s.substring(0, dp[n-1]);
    }
}