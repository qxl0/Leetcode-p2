public class Solution {
    int n;    
    int[][] dp;
    public int MaxOperations(int[] nums) {
        n = nums.Length;
        dp = new int[n+1][];
        for (int j=0;j<n+1;j++) {
            dp[j] = new int[n+1];
            Array.Fill(dp[j], -1);
        }
        int ops = 0;
        ops = Math.Max(ops, helper(nums, 2, n-1, nums[0]+nums[1])+1);        
        ops = Math.Max(ops, helper(nums, 0, n-3, nums[n-1]+nums[n-2])+1);
        ops = Math.Max(ops, helper(nums, 1, n-2, nums[0]+nums[n-1])+ 1);

        return ops;
    }

    private int helper(int[] nums, int start,int end, int score) {
        if (start>=end)
            return 0;
        if (dp[start][end]!=-1)
            return dp[start][end];
            
        int ops = 0;
        if (nums[start]+nums[start+1] == score) {
            ops = Math.Max(ops, helper(nums, start+2, end, score) + 1);
        }
        if (nums[end]+nums[end-1] == score) {
            ops = Math.Max(ops, helper(nums, start, end-2, score)+1);
        }
        if (nums[start]+nums[end] == score) {
            ops = Math.Max(ops, helper(nums, start+1, end-1, score)+1);
        }
        
        dp[start][end] = ops;        
        return ops;
        
    }
}