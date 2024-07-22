class Solution {
    public int minChanges(int n, int k) {
        int ret = 0;
        for (int i=0;i<32;i++) {
            if (((n>>i) & 1) == 1) {
                if (((k>>i)&1) == 0) {
                    ret += 1;
                }
            }
            else {
                if (((k>>i)&1)==1) {
                    return -1;
                }
            }
        }

        return ret;
    }
}