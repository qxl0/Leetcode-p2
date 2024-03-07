public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int n = nums.Length;
        int i = 0, j=0;

        while (j<n) {
            if (nums[j]!=val) {
                nums[i] = nums[j];
                i += 1;
            }
            j += 1;
        }

        return i;
    }
}