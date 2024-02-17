public class Solution {
    int count = 0;
    public int MinReorder(int n, int[][] connections) {
        // node->[(v, sign), ...]  sign = 0, 1  original, artificial
        Dictionary<int,List<List<int>>> adj = new Dictionary<int,List<List<int>>>();

        foreach (int[] conn in connections) {
            int u = conn[0], v = conn[1];
            if (!adj.ContainsKey(u)) {
                adj.Add(u, new List<List<int>>());
            }
            adj[u].Add(new List<int>{v, 1});
            if (!adj.ContainsKey(v)) {
                adj.Add(v, new List<List<int>>());                
            }
            adj[v].Add(new List<int>{u,0});
        }

        dfs(0, -1, adj);

        return count;
    }

    private void dfs(int node, int parent, Dictionary<int,List<List<int>>> adj) {
        if (!adj.ContainsKey(node)) {
            return;
        }

        foreach (List<int> nei in adj[node]) {
            int neighbor = nei[0];
            int sign = nei[1];
            if (neighbor != parent) {
                this.count += sign;
                dfs(neighbor, node, adj);
            }
        }
    }
}