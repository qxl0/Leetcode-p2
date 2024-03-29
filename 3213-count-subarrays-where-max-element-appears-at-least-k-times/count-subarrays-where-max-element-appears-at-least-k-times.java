class Solution {
    public long countSubarrays(int[] nums, int k) {
        int mx = Arrays.stream(nums).max().orElseThrow();
        long ret = 0;
        int count = 0;
        int i=0;
        for (var j = 0; j < nums.length; j++) {
            if (nums[j]==mx) {
                count += 1;
            }
            while (count>=k) {
                if (nums[i]==mx) {
                    count -= 1;                    
                }
                i += 1;
            }
                         
            ret += i;
            
        }

        return ret;
    }
}