class Solution {
    int m,n;
    char[][] _board;
    int[][] dt = new int[][]{ {-1,0}, {1,0}, {0,-1}, {0, 1}};    
    public boolean exist(char[][] board, String word) {
        m = board.length;
        n = board[0].length;
        _board = board;

        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {
                if (board[i][j]==word.charAt(0)) {
                    boolean[][] vis = new boolean[m][n];
                    vis[i][j] = true;
                    if (dfs(i,j,word, 0, vis)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private boolean dfs(int row, int col, String word, int idx, boolean[][] vis) {
        if (_board[row][col]!= word.charAt(idx)) {
            return false;
        }
        if (idx == word.length()-1) {
            return true;
        }

        // move 
        for (var di : dt) {            
                int ii = row+di[0];
                int jj = col+di[1];

                if (ii<0 || ii>=m || jj<0 || jj>=n) continue;
                if (vis[ii][jj]) continue;
                vis[ii][jj] = true;  // visited 

                if (dfs(ii,jj, word, idx+1, vis)) {
                    return true;
                }

                vis[ii][jj] = false; // backtrack

        }
        
        return false;
    }
}