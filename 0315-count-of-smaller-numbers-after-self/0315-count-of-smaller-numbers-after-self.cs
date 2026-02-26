public class FenwickTree {
    private int[] _data;
    private int n;
    public FenwickTree(int n) {
        this.n = n;
        _data = new int[n+1];
    }

    public void update(int index, int delta) {
        while (index<=n) {
            _data[index] += delta;
            index += lowbit(index);
        }
    }
    public int query(int index) {
        int sum = 0;
        while (index>0) {
            sum += _data[index];
            index -= lowbit(index);
        }
        return sum;
    }
    private int lowbit(int x) {
        return x &(-x);
    }
}
public class Solution {
    public IList<int> CountSmaller(int[] nums) {
        HashSet<int> Set = new HashSet<int>(nums);
        List<int> nums2 = Set.ToList();
        nums2.Sort();
        Dictionary<int,int> ranks = new();
        int rank = 0;
        foreach (var x in nums2) {
            ranks[x] = ++rank;
        }

        int n = nums.Length;

        FenwickTree tree = new FenwickTree(n+1);

        int[] ans = new int[n];
        for (int i=n-1;i>=0;i--) {
            ans[i] = tree.query(ranks[nums[i]]-1);
            tree.update(ranks[nums[i]], 1);
        }
        return ans;
    }
}