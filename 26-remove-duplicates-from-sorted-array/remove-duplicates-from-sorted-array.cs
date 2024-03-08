public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int cur = 1;
        int n = nums.Length;

        for (int i=1;i<n;i++) {
            if (nums[i]==nums[i-1])
                continue;
            // find first unique element
            nums[cur] = nums[i];
            cur += 1;
        }
        return cur;
    }
}