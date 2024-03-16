class Solution {
    int m;
    int n;
    class UnionFind {
        int count;
        int[] father;
        int[] rank;
        
        public UnionFind(int n) {
            father = new int[n];
            rank = new int[n];
            for (int i=0;i<n;i++) {
                this.father[i] = i;
                this.rank[i] = 1;                
            }
        }

        public UnionFind(char[][] grid) {
            int m = grid.length,n = grid[0].length;
            father = new int[m*n];
            rank = new int[m*n];
            for (int i=0;i<m;i++) {
                for (int j=0;j<n;j++) {
                    if (grid[i][j]=='1') {
                        this.father[i*n+j] = i*n+j;                        
                        count += 1;              
                    }
                    this.rank[i*n+j] = 1;  
                }
            }
        }
        public int findFather(int x) {
            int px = this.father[x];
            if (px!=x) {
                this.father[x] = this.findFather(px);
            }
            return this.father[x];
        }

        public boolean union(int x, int y) {
            int px = this.findFather(x);
            int py = this.findFather(y);

            if (px==py) return false;

            if (rank[px]<rank[py]) {
                this.rank[py]+= this.rank[px];
                this.father[py] = px;
            }
            else {
                this.rank[px]+= this.rank[py];
                this.father[px] = py;
            }
            count -= 1;
            // System.out.println(count);
            return true;
        }

        public int getCount() {
            return count;
        }
    }
    public int numIslands(char[][] grid) {
        m = grid.length;
        n = grid[0].length;        

        UnionFind uf = new UnionFind(grid);

        for (int i=0;i<m;i++) {
            for (int j=0;j<n;j++) {
                if (grid[i][j]=='1') {
                    grid[i][j] = '0';
                    if (i-1>=0 && grid[i-1][j]=='1') {
                        uf.union(getId(i,j), getId(i-1,j));
                    }
                    if (i+1<m && grid[i+1][j]=='1') {
                        uf.union(getId(i,j), getId(i+1,j));
                    }
                    if (j-1>=0 && grid[i][j-1]=='1') {
                        uf.union(getId(i,j), getId(i,j-1));
                    }
                    if (j+1<n && grid[i][j+1]=='1') {
                        uf.union(getId(i,j), getId(i,j+1));
                    }
                }
            }
        }

        return uf.getCount();
    }

    private int getId(int x, int y) {
        return (x)*n + y;
    }
}