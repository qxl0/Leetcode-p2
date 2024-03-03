public class Solution {
    public long MaximumValueSum(int[] nums, int k, int[][] edges) {
        int n = nums.Length;
        long S = 0;
        foreach(var x in nums){
            S += x;
        }
        int[] nums2 = Array.ConvertAll(nums, x=>(x^k)-x);
        Array.Sort(nums2, (x,y)=>y-x);
        
        int i=0;
        while (i<n) {
            if (i+1<n && nums2[i]+nums2[i+1]>0) {
                S += nums2[i]+nums2[i+1];
            }
            i += 2;
        }
        
        return S;
    }
}