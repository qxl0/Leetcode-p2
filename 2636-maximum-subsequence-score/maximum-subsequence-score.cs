public class Solution {
    public long MaxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.Length;
        (int,int)[] arr = nums1.Zip(nums2, (x,y)=>(x,y)).ToArray();
        Array.Sort(arr, (x,y)=>y.Item2.CompareTo(x.Item2));

        PriorityQueue<int,int> dq = new PriorityQueue<int,int>();
        long ret = 0, runningSum = 0;
        for (int i=0;i<n;i++) {
            runningSum += arr[i].Item1;
            dq.Enqueue(arr[i].Item1, arr[i].Item1);

            if (dq.Count > k) {
                int removed = dq.Dequeue();
                runningSum -= removed;
            }

            if (dq.Count==k) {
                ret = Math.Max(ret, runningSum * arr[i].Item2);
            }            
        }
        
        return ret;
    }
}