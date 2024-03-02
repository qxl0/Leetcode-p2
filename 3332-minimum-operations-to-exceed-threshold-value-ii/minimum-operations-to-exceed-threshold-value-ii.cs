public class Solution {
    int MOD = int.MaxValue;
    public int MinOperations(int[] nums, int k) {
        int n = nums.Length;
        PriorityQueue<long,long> pq = new PriorityQueue<long,long>();
        for (int i=0;i<n;i++) {
            pq.Enqueue(nums[i],nums[i]);
        }
        int ops = 0;

        while (pq.Count>=2) {
            long f1 = pq.Dequeue();
            if (f1>=k) {
                return ops;
            }
            long f2 = pq.Dequeue();
            ops += 1;

            long nf = (f1*2+f2);
            pq.Enqueue(nf, nf);
        }

        return ops;
    }
}