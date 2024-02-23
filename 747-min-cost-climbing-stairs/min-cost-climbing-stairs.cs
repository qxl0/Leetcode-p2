public class Solution {
    int[] _cost;
    Dictionary<int,int> memo = new();
    public int MinCostClimbingStairs(int[] cost) {
        this._cost = cost;
        return helper(cost.Length);
    }

    private int helper(int idx) {
        if (idx<=1) 
            return 0;
        if (memo.ContainsKey(idx)) {
            return memo[idx];
        }

        int downOne = _cost[idx-1] + helper(idx-1);
        int downTwo = _cost[idx-2] + helper(idx-2);

        memo[idx] = Math.Min(downOne,downTwo);
        return memo[idx];
    }
}