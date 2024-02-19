public class Solution {
    public int MaxSelectedElements(int[] nums) {
        Array.Sort(nums);
        // 1,1,1,2,5
        int n = nums.Length;
        int[][] dp = new int[n][]; 
        for (var i=0;i<n;i++) {
            dp[i] = new int[2];
        }
        // dp[i]: length of the longest consecutive elements ending at element i 
        // dp[i][0]: length of the longest consecutive sequence without self-increasing 1
        // dp[i][1]:
        //  x x x x x i-1, i x x x 
        //             a   b
        // initial value: by itself
        // dp[i][0] = dp[i][1] = 1
        // 1. b-a==2, a+1, b+0
        //  dp[i][0] = dp[i-1][1]+1
        // 2. b-a==1,
        //  dp[i][0] = dp[i-1][0]+1
        //  dp[i][1] = dp[i-1][1]+1
        // 3. b-a==0
        //  dp[i][0] = dp[i-1][0]
        //  dp[i][1] = dp[i-1][1]
        //  dp[i][1] = dp[i-1][0]+1
        int ret = 1;
        dp[0][0] = 1;
        dp[0][1] = 1;
        for (int i=1;i<n;i++) {
            dp[i][0] = 1;
            dp[i][1] = 1;
            if (nums[i]==nums[i-1]) {
                dp[i][1] = Math.Max(dp[i][1], dp[i-1][0]+1);
                dp[i][0] = Math.Max(dp[i][0], dp[i-1][0]);
                dp[i][1] = Math.Max(dp[i][1], dp[i-1][1]);
            } 
            else if (nums[i]-nums[i-1]==1) {
                dp[i][0] = Math.Max(dp[i][0], dp[i-1][0] + 1);
                dp[i][1] = Math.Max(dp[i][1], dp[i-1][1] + 1);
            }
            else if (nums[i]-nums[i-1]==2) {
                dp[i][0] = Math.Max(dp[i][0], dp[i-1][1] + 1);                
            }

            ret = Math.Max(ret, dp[i][0]);
            ret = Math.Max(ret, dp[i][1]);
        }

        return ret;
    }
}
