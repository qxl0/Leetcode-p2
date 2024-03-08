class Solution {
    public int removeDuplicates(int[] nums) {        
        int n = nums.length;
        if (n<3) return n;
        int l = 2, r = 2;

        while (r<n) {
            if (nums[l-2] ==nums[r])
                r += 1;
            else {
                nums[l] = nums[r];
                l++;
                r++;
            }
        }

        return l;
    }
}