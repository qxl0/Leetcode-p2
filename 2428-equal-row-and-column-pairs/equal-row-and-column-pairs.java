class Solution {
    private int[][] grid;
    private int m,n;
    public int equalPairs(int[][] grid) {
        this.grid = grid;
        
        int count = 0;
        m = grid.length;
        n = grid[0].length;
        
        for (var row : grid) {
            for (int c = 0; c<n; c++) {
                var col = getCol(c);
                if (Arrays.equals(col, row))
                    count += 1;
            }
        }

        return count;
    }

    private int[] getCol(int c) {
        int[] cols = new int[n];
        for (int i = 0; i<m; i++)
            cols[i] = grid[i][c];
        return cols;
    }
}