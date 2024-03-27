class Solution {
    public int firstMissingPositive(int[] nums) {
        // use idx i -> i+1 is availble if we visit (mark to negative)
        // 
        int n = nums.length;
        for (var i=0;i<n;i++){
            if (nums[i]<0) {
                nums[i]=0;
            }
        }

        for (var i=0;i<n;i++) {
            int val = Math.abs(nums[i]);
            // check if val-1 
            if (val>n || val<1) continue;            
            if (nums[val-1]<0) continue;
            if (nums[val-1]>0) {
                nums[val-1] *= -1;
            }
            if (nums[val-1]==0) nums[val-1] = -(n+1);            
        }

        // we use idx 
        for (var i=0;i<n;i++) {
            if (nums[i]>=0) return i+1;
        }

        return n+1;
    }
}