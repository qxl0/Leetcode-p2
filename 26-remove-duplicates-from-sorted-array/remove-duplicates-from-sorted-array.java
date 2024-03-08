class Solution {
    public int removeDuplicates(int[] nums) {
        int cur = 1;
        int n = nums.length;

        for (int i=1;i<n;i++) {
            if (nums[i]==nums[i-1])
                continue;
            nums[cur] = nums[i];
            cur +=1;
        }

        return cur;
    }
}