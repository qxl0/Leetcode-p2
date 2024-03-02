public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.Length, n = nums2.Length;
        if (m>n) {
            // exchange nums1 with nums2 
            int[] tmp = nums2;
            nums2 = nums1;
            nums1 = tmp;
            m = nums1.Length;
            n = nums2.Length;
        }
        int total = (m+n);
        int half = total/2;

        int l = 0, r = m-1;
        while (true) {
            int i = r - (r-l)/2;
            int j = half - i - 2;

            double Al = i>=0 ? nums1[i]:int.MinValue;
            double Ar = (i+1)<m ? nums1[i+1]:int.MaxValue;
            double Bl = j>=0 ? nums2[j]:int.MinValue;
            double Br = j+1<n ? nums2[j+1]:int.MaxValue;

            if (Al<=Br && Bl<=Ar) {
                if (total%2==1) {
                    return Math.Min(Br,Ar);
                }
                else {
                    return (Math.Max(Al,Bl) + Math.Min(Br,Ar))/2;
                }
            }
            else if (Al>Br) {
                r = i-1;
            } 
            else {
                l = i+1;
            }
        }
    }
}