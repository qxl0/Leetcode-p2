public class Solution {
    public int MinDistance(string word1, string word2) {
        int m = word1.Length,n=word2.Length;
        int[][] dp = new int[m+1][];
        for (int i=0;i<m+1;i++){
            dp[i] = new int[n+1];
            Array.Fill(dp[i], int.MaxValue);
        }
        
        for (int i=0;i<m+1;i++) {            
            dp[i][0]=i;
        }
        for (int j=0;j<n+1;j++) {
            dp[0][j]=j;
        }
        for (int i=1;i<m+1;i++) {
            for (int j=1;j<n+1;j++) {
                if (word1[i-1]==word2[j-1])
                    dp[i][j] = dp[i-1][j-1];
                else {
                    dp[i][j] = Math.Min(dp[i][j], dp[i-1][j] + 1);
                    dp[i][j] = Math.Min(dp[i][j], dp[i][j-1] + 1);
                    dp[i][j] = Math.Min(dp[i][j], dp[i-1][j-1] + 1);
                }
            }
        }

        return dp[m][n];
    }
}