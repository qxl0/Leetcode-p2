class Solution {
    char[][] _grid;
    int[] d1 = new int[]{-1,0,1,0};
    int[] d2 = new int[]{0,-1,0,1};
    int m,n;
    public int numIslands(char[][] grid) {
        m=grid.length;
        n=grid[0].length;
        this._grid = grid;
        int ret = 0;
        boolean[][] vis = new boolean[m][n];
        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {
                if (grid[i][j]=='1' && !vis[i][j]) {
                    ret += 1;
                    bfs(i,j, vis);
                }

            }
        }
        return ret;
    }
    private void bfs(int i,int j, boolean[][] vis) {
        Queue<int[]> q = new LinkedList<int[]>();
        
        q.add(new int[] {i,j} );
        while (!q.isEmpty()) {
            int qsize = q.size();

            for (int k=0;k<qsize;k++) {
                int[] cur = q.poll();
                int x = cur[0], y=cur[1];                

                for (var p=0;p<4;p++) {
                    int nx = x+d1[p];
                    int ny = y+d2[p];
                    if (nx<0 || nx>=m || ny<0 || ny>=n) continue;
                    if (!vis[nx][ny] && _grid[nx][ny]=='1') {
                        vis[nx][ny] = true;
                        q.add(new int[] {nx, ny});
                    }
                }
            }
        }

    }
}