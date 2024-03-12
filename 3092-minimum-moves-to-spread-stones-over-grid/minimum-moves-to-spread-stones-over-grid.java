class Solution {
    int ret = Integer.MAX_VALUE;
    int[][] _grid;
    public int minimumMoves(int[][] grid) {
        _grid  = grid;
        dfs(0,0);
        return ret;
    }

    private void dfs(int cur, int moves) {
        if (moves>ret) return;
        if (cur==9) {
            ret = Math.min(ret, moves);
            return;
        }
        int i = cur/3;
        int j = cur%3;

        if (_grid[i][j]!=0) {
            dfs(cur+1, moves);
            return;
        }
        else {
            // loop through x,y
            for (int x=0;x<3;x++) {
                for (int y=0;y<3;y++) {
                    if (_grid[x][y]<=1) continue;
                    _grid[x][y] -= 1;
                    _grid[i][j] += 1;
                    dfs(cur+1,moves+Math.abs(y-j)+Math.abs(x-i));
                    _grid[x][y] += 1;
                    _grid[i][j] -= 1;
                }
            }
        }
    }
}