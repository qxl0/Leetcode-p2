public class Solution {
    public int Jump(int[] nums) {
        int l=0,r=0;
        int n = nums.Length;
        if (n==1) return 0;

        int ret = 0;

        while (true) {
            int nxt = 0;
            for (int i=l;i<r+1;i++) {
                nxt = Math.Max(nxt, i+nums[i]);
            }
            ret += 1;
            if (nxt >= n-1) {
                break;    
            }
            
            l = r+1;
            r = nxt;
        }

        return ret;
    }
}