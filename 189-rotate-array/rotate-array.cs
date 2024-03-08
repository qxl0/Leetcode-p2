public class Solution {
    public void Rotate(int[] nums, int k) {
        int n = nums.Length;
        k %= n;

        int start = 0, count = 0;   
        while (count<n) {
            int current = start;
            int current_v = nums[start];

            while (true) {
                int next = (current+k)%n;
                int temp = nums[next];

                nums[next] = current_v;
                count += 1;

                current = next;
                current_v = temp;

                if (current == start) {
                    break;
                }
            }

            start += 1;
        }
    }
}