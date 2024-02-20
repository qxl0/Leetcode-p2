public class Solution {
    public long MaxScore(int[] nums1, int[] nums2, int k) {
        // sort nums2 desc
        int n = nums1.Length;
        (int,int)[] arr = nums1.Zip(nums2, (n1,n2)=>(n1,n2)).ToArray();

        Array.Sort(arr, (x,y)=>y.Item2.CompareTo(x.Item2));

        long runningSum = 0;
        long ret = 0;
        PriorityQueue<int,int> dq = new PriorityQueue<int,int>();

        for (int i=0; i<n;i++) {
            runningSum += arr[i].Item1;
            dq.Enqueue(arr[i].Item1, arr[i].Item1);

            if (dq.Count>k) runningSum -= dq.Dequeue();

            if (dq.Count==k) ret = Math.Max(ret, arr[i].Item2 * runningSum);            
        }

        return ret;
    }
}