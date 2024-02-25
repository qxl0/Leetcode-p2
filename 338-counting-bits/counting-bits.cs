public class Solution {
    public int[] CountBits(int n) {
        int[] ans = new int[n+1];

        for (int i=0;i<=n;i++) {
            ans[i] = checkbits(i);
        }

        return ans;
    }

    private int checkbits(int x) {
        int ret = 0;
        while (x>0) {
            ret += (x%2);
            x /= 2;
        }
        return ret;
    }
}