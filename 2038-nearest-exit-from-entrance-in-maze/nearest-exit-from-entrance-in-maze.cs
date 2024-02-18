public class Solution {
    int m,n;
    public int NearestExit(char[][] maze, int[] entrance) {
        m = maze.Length;
        n = maze[0].Length;
        int[][] dirs = new int[][]{new int[]{-1,0}, new int[]{1,0}, new int[]{0,-1}, new int[]{0,1}};
        Queue<int[]> dq = new Queue<int[]>();
        
        bool[][] vis = new bool[m][];
        for (int i=0;i<m;i++)
        {
            vis[i] = new bool[n];
        }
        dq.Enqueue(entrance);
        int steps = 0;
        while (dq.Count != 0) {
            int qsize = dq.Count;
            for (int i=0;i<qsize;i++ ) {
                int[] cur = dq.Dequeue();
                int x = cur[0], y = cur[1];
                if ((x != entrance[0]||y!=entrance[1]) && isBoundry(cur)) {
                    return steps;
                }

                foreach (var dir in dirs) {
                    int newx = x + dir[0];
                    int newy = y + dir[1];
                    if (newx>=0 && newx<m && newy>=0 && newy<n && maze[newx][newy]=='.' && vis[newx][newy] != true) {
                        vis[newx][newy] = true;
                        dq.Enqueue(new int[]{newx,newy});
                    }
                }
            }
            steps += 1;   
        }
        return -1;
    }

    private bool isBoundry(int[] pos) {
        if (pos[0] == 0 || pos[0] == m-1 || pos[1] == 0 || pos[1]==n-1)
            return true;
        return false;
    }
}