public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        PriorityQueue<int,int> minHeap = new PriorityQueue<int,int>();
        foreach (var x in nums) {
            minHeap.Enqueue(x, x);
            if (minHeap.Count>k){
                minHeap.Dequeue();
            }
        }
        return minHeap.Peek();
    }
}