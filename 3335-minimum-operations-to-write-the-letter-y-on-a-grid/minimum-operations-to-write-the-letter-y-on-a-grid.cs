public class Solution {
    public int MinimumOperationsToWriteY(int[][] grid) {
        Dictionary<int,int> Y = new() {{0,0},{1,0},{2,0}};
        Dictionary<int,int> NonY = new() {{0,0},{1,0},{2,0}};

        int n = grid.Length;

        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                NonY[grid[i][j]]+= 1;
            }
        }
        int center = n/2;
        for (int i=0;i<center;i++) {
            Y[grid[i][i]] += 1;
            Y[grid[i][n-1-i]] += 1;
        }
        for (int i=center;i<n;i++) {
            Y[grid[i][center]]+=1;
        }

        // NonY-Y
        foreach (var key in NonY.Keys.ToList()) {
            NonY[key] -= Y[key];
        }

        int ans = int.MaxValue;
        for (int x=0;x<=2;x++) {
            for (int y=0;y<=2;y++) {
                if (x==y) 
                    continue;
                // change Y to x, NonY to y 
                int ops = calculate(Y, x) + calculate(NonY, y);
                ans = Math.Min(ans, ops);
            }
        }
        return ans;
    }

    private int calculate(Dictionary<int,int> count, int x) {
        // calculate total ops needed to change count to have only x : 0,1,2
        int totalops = 0;
        foreach (var item in count) {
            int key = item.Key;
            int freq = item.Value;
            if (key!=x) {
                totalops += freq;
            }
        }
        return totalops;
    }
}