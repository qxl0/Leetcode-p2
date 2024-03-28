class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k<=1) return 0;
        int n = nums.length;
        int count = 0;
        int i = 0;
        int product = 1;
        for (var j=0;j<n;j++) {
            product *= nums[j];
            while (i<=j && product>=k) {
                product /= nums[i];
                i += 1;
            }
            // System.out.println(String.format("j: %d, ret: %d",j, (j-i+1)));
            count += j-i+1;
        }

        return count;
    }
}

// 10,5,2,6
//    ^   ^
// 1  3 5 8