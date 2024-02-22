public class Solution {
    public IList<IList<int>> CombinationSum3(int k, int n) {
        IList<IList<int>> ret = new List<IList<int>>();
        List<int> cur = new();
        helper(k,n,1, cur, ret);
        return ret;
    }

    private void helper(int k, int n, int start, List<int> cur, IList<IList<int>> ret) {
        if (k==0) {
            if (n==0) {
                ret.Add(new List<int>(cur));
                return;
            }
        }

        for (int i = start; i<=9; i++) {
            if (i>n) return;
            cur.Add(i);
            helper(k-1, n-i, i+1, cur, ret);
            cur.RemoveAt(cur.Count-1);
        }
    }
}