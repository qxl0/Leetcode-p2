public class FenwickTree {
    private int[] _data;
    public FenwickTree(int n) {
        this._data = new int[n];        
    }

    public void update(int i, int delta) {        
        while (i<_data.Length) {
            this._data[i] += delta;
            i += lowbit(i);
        }
    }

    public int query(int i) {
        int sum = 0;
        while (i>0) {
            sum += this._data[i];
            i -= lowbit(i);
        }

        return sum;
    }

    private int lowbit(int x) {
        return x & (-x);
    }
}
public class NumArray {
    private FenwickTree tree;
    private int[] _nums;
    public NumArray(int[] nums) {
        _nums = nums;
        int n = nums.Length;
        tree = new FenwickTree(n+1);
        for (int i=0;i<n;i++) {
            tree.update(i+1, nums[i]);
        }
    }
    
    public void Update(int index, int val) {
        tree.update(index+1, val-this._nums[index]);
        this._nums[index] = val;
    }
    
    public int SumRange(int left, int right) {
        return tree.query(right+1)-tree.query(left);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.Update(index,val);
 * int param_2 = obj.SumRange(left,right);
 */