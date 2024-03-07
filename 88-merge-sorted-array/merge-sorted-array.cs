public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int k = m+n-1;
        int i = m-1,j=n-1;

        while (i>=0 && j>=0) {
            if (nums1[i]>=nums2[j]) {
                nums1[k] = nums1[i];
                i -= 1;                
            } else {
                nums1[k] = nums2[j];
                j -= 1;
            }
            k -= 1;
        }

        while (i>=0) {
            nums1[k] = nums1[i];
            i -= 1;
            k -= 1;
        }

        while (j>=0) {
            nums1[k] = nums2[j];
            j -= 1;
            k -= 1;
        }
    }
}