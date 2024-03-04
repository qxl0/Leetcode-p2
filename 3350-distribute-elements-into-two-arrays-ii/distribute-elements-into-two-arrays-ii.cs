public class SegmentTreeNode {    
    public SegmentTreeNode left,right;
    public SegmentTreeNode(int start, int end, int count) {
        this.start = start;
        this.end = end;
        this.count = count;
        this.left = null;
        this.right = null;
    }
    public int count {get;set;}
    public int start {get;set;}
    public int end {get;set;}
}
public class SegmentTree {
    SegmentTreeNode root = null;
    public SegmentTree(int length) {
        root = buildHelper(0, length-1);
    }
    private SegmentTreeNode buildHelper(int start, int end) {
        if (start>end) return null;
        if (start==end) return new SegmentTreeNode(start,end,0);

        SegmentTreeNode node = new SegmentTreeNode(start, end, 0);
        int mid = start + (end-start)/2;
        node.left = buildHelper(start, mid);
        node.right = buildHelper(mid+1, end);

        if (node.left!=null)
            node.count += node.left.count;
        if (node.right!=null)
            node.count += node.right.count;
        return node;
    }
    public int queryCount(int start, int end) {
        return _queryCount(root, start, end);
    }
    private int _queryCount(SegmentTreeNode node, int start, int end) {
        if (node==null || start>end) return 0;
        if (node.start>=start && node.end<=end)
            return node.count;
        int mid = node.start + (node.end-node.start)/2;

        int leftRet = 0;
        int rightRet = 0;

        if (start <= mid) 
            leftRet = _queryCount(node.left, start, end);
        if (mid+1<=end) 
            rightRet = _queryCount(node.right, start, end);
        
        return leftRet+rightRet;
    }
    public void modify(int index, int value) {
        _modify(root, index, value);
    }
    private void _modify(SegmentTreeNode node, int index, int value) {
        if (node.start==node.end && node.start == index) {
            node.count += value;
            return;
        }
        int mid = node.start + (node.end-node.start)/2;
        if (index<=mid) 
            _modify(node.left, index, value);
        else
            _modify(node.right, index, value);
        node.count = node.left.count + node.right.count;
        return;
    }
}
public class Solution {
    Dictionary<int,int> Map = new();
    Dictionary<int,int> Map_inverse = new();
    public int[] ResultArray(int[] nums) {
        nums = compress(nums);

        List<int> arr1=new(), arr2 = new();

        arr1.Add(nums[0]);
        arr2.Add(nums[1]);
        
        if (nums.Length==1) return nums;        
        int mx = nums.Max() + 1;

        SegmentTree tree1 = new SegmentTree(mx), tree2 = new SegmentTree(mx);
        tree1.modify(nums[0], 1);
        tree2.modify(nums[1], 1);
        for (int i=2;i<nums.Length;i++) {
            int target = nums[i]; // strictly greater than, but our tree is >=
            int t1 = tree1.queryCount(target+1, int.MaxValue);
            int t2 = tree2.queryCount(target+1, int.MaxValue);

            if (t1<t2) {
                arr2.Add(target);
                tree2.modify(target,1);
            } else if (t1>t2) {
                arr1.Add(target);
                tree1.modify(target, 1);
            } else {
                if (arr1.Count<arr2.Count) {
                    arr1.Add(target);
                    tree1.modify(target,1);
                } else if (arr1.Count>arr2.Count) {
                    arr2.Add(target);
                    tree2.modify(target,1);
                } else {
                    arr1.Add(target);
                    tree1.modify(target,1);
                }
            }
        }

        List<int> ret = new();
        foreach (var item in arr1) {
            ret.Add(Map_inverse[item]);
        }

        foreach (var item in arr2) {
            ret.Add(Map_inverse[item]);
        }

        return ret.ToArray();
    }

    private int[] compress(int[] nums) {
        int[] nums2 = new int[nums.Length];
        Array.Copy(nums, nums2, nums.Length);

        Array.Sort(nums2);
        
        int id = 1;
        foreach (var x in nums2) {
            if (Map.ContainsKey(x)) continue;
            Map[x] = id;
            Map_inverse[id] = x;
            id += 1;
        }
        
        for (int i=0;i<nums.Length;i++) {
            nums[i] = Map[nums[i]];
        }

        return nums;
    }
}