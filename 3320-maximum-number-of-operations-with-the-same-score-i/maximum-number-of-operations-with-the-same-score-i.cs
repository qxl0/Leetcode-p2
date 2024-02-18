public class Solution {
    public int MaxOperations(int[] nums) {
        int ret = 1;
        int i = 2;
        int n = nums.Length;
        int score = nums[0]+nums[1];
        while (i<n) {
            if (i+1<n && score == nums[i]+nums[i+1]) {
                ret += 1;
                i += 2;
            }
            else {
                break;
            }
        }

        return ret;
    }
}