public class Solution {
    public int CountSubmatrices(int[][] grid, int k) {
        int m=grid.Length,n=grid[0].Length;
        int ret = 0;
        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {
                grid[i][j] += (i>0?grid[i-1][j]:0) + (j>0?grid[i][j-1]:0) - ((i>0 && j>0 )? grid[i-1][j-1]:0);

                if (grid[i][j]<=k) 
                    ret += 1;
            }
        }

        return ret;
    }
}