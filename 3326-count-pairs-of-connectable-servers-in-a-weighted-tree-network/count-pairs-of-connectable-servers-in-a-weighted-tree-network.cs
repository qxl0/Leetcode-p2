public class Solution {
    int[] nodes;
    Dictionary<int,List<(int,int)>> adj;
    public int[] CountPairsOfConnectableServers(int[][] edges, int signalSpeed) {
        adj = new();
        foreach (var edge in edges) {
            var u = edge[0];
            var v = edge[1];
            var w = edge[2];

            if (!adj.ContainsKey(u)) {
                adj[u] = new List<(int,int)>();
            }
            adj[u].Add((v,w));

            if (!adj.ContainsKey(v)) {
                adj[v] = new List<(int,int)>();
            }
            adj[v].Add((u,w));
        }
        int n = edges.Length+1;
        int[] ret = new int[n];
        
        for (int i=0;i<n;i++) {
            double[] nums = new double[adj[i].Count];
            for (int j=0;j<adj[i].Count;j++) {
                var (chld,w) = adj[i][j];
                int delta = w%signalSpeed;
                if (delta==0) 
                    nums[j] = 1;
                nums[j] += dfs(chld, i, signalSpeed, delta);
            }
            ret[i] = getTotal(nums);   
        }

        /*
        If the root has m children named c1, c2, …, cm that respectively have num[c1], num[c2], …, num[cm] nodes 
        in their subtrees whose distance is divisible by signalSpeed. Then, there are 
        ((S - num[ci]) * num[ci]) / 2
        that are connectable through the root that we have fixed, where S is the sum of num[ci].
        */
       
        return ret;
    }

    private int getTotal(double[] nums) {
        double ret = 0;
        double S = nums.Sum();

        for (int i=0;i<nums.Length;i++) {
            ret += (S-nums[i])*nums[i]/2;
        }

        return (int)ret;
    }

    private int dfs(int root, int parent, int signalSpeed,int delta) {
        // find the number of nodes its dist from root is divisble by signalSpeed
        
        int ret = 0;        
        foreach (var (nei, weight) in adj[root]) {
            if (nei==parent)
                continue;
            if ((weight+delta)%signalSpeed==0) {
                ret += 1;
            }
            int newdelta = (delta+weight)%signalSpeed;
            ret += dfs(nei, root, signalSpeed, newdelta);
                        
        }

        return ret;
    }
}