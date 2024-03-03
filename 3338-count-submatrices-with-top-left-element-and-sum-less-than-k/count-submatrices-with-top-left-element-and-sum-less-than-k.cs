public class Solution {
    public int CountSubmatrices(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;

        int[][] presum = new int[m][];
        for (int i=0;i<m;i++) {
            presum[i] = new int[n];
            for (int j=0;j<n;j++) {
                presum[i][j] = (j>0? presum[i][j-1] : 0)+grid[i][j];
            }
        }        
        for (int j=0;j<n;j++) {
            for (int i=0;i<m;i++) {
                presum[i][j] = (i>0? presum[i-1][j] : 0) + presum[i][j];
            }
        }        
        
        int ret = 0;        
        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {
                if (presum[i][j]<=k) {
                    ret += 1;
                }        
            }
        }
        return ret;
    }
}