public class Solution {
    public long TotalCost(int[] costs, int k, int candidates) {
        PriorityQueue<int,int> left = new PriorityQueue<int,int>();
        PriorityQueue<int,int> right = new PriorityQueue<int,int>();

        for (int i=0;i<candidates;i++) {
            left.Enqueue(costs[i], costs[i]);
        }

        int n = costs.Length;
        for (int i=n-1;i>=Math.Max(candidates, n-candidates);i--) {
            right.Enqueue(costs[i], costs[i]);
        }

        long ret = 0;
        int l = candidates, r = n-1-candidates;
        while (k>0) {
            if (right.Count==0 || (left.Count>0 && left.Peek()<=right.Peek())) {
                ret += left.Dequeue();
                if (l<=r) {
                    left.Enqueue(costs[l], costs[l]);
                    l += 1;
                }
            }
            else {
                ret += right.Dequeue();
                if (l<=r) {
                    right.Enqueue(costs[r], costs[r]);
                    r -= 1;
                }
            }
            k -= 1;
        }

        return ret;
    }
}