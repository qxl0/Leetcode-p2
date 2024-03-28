class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        HashMap<Integer,Integer> Map = new HashMap<>();
        int ret = 0;
        int i = 0;
        for (var j=0;j<nums.length;j++) {
            Map.put(nums[j], Map.getOrDefault(nums[j], 0)+1);
            while (i<j && Map.get(nums[j])>k) {
                Map.put(nums[i], Map.getOrDefault(nums[i], 0)-1);
                i += 1;
            }
            ret = Math.max(ret, j-i+1);
        }

        return ret;
    }
}