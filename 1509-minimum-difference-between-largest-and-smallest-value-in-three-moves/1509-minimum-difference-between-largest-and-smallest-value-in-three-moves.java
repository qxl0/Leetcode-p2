class Solution {
    public int minDifference(int[] nums) {
        int n = nums.length;
        if (n<=4)
            return 0;
        // sort
        Arrays.sort(nums);

        int ret = Integer.MAX_VALUE;
        // all 3 from left 
        ret = Math.min(ret, nums[n-1]-nums[3]);
        // all 3 from right
        ret = Math.min(ret, nums[n-4]-nums[0]);
        // 1, 2
        ret = Math.min(ret, nums[n-3]-nums[1]);
        // 2, 1
        ret = Math.min(ret, nums[n-2]-nums[2]);
        
        
        return ret;
    }
}