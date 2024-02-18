public class Solution {
    int m,n;
    public int OrangesRotting(int[][] grid) {
        m = grid.Length;
        n = grid[0].Length;
        int[][] dirs = new int[][]{new int[]{-1,0},new int[]{1,0}, new int[] {0,1}, new int[]{0,-1}};
        Queue<int[]> dq = new Queue<int[]>();
        int good = 0;
        for (int i=0;i<m;i++){
            for (int j=0;j<n;j++) {
                if (grid[i][j] == 2)
                    dq.Enqueue([i,j]);
                else if (grid[i][j] == 1)
                    good += 1;
            }
        }
        int time = 0;
        while (dq.Count > 0 && good>0) {
            int qsize = dq.Count;
            for (int i=0;i<qsize;i++) {
                int[] cur = dq.Dequeue();
                int x = cur[0];
                int y = cur[1];

                foreach (var dir in dirs) {
                    int newx = x + dir[0];
                    int newy = y + dir[1];

                    if (newx>=0 && newx<m && newy>=0 && newy<n && grid[newx][newy]==1) {
                        grid[newx][newy] = 2;
                        good -= 1;
                        dq.Enqueue([newx,newy]);
                    } 
                }
            }
            time += 1;            
        }
        return good==0? time: -1;

    }
}