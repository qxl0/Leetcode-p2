class Solution {
    private long base = 411;
    private long[] pow;
    private int n, m;
    public int strStr(String s1, String s2) {
        this.n = s1.length();
        this.m = s2.length();
        long hash_s2 = hash(s2, 0, m);

        // loop through s1
        for (int i=0; i < n - m + 1; i++) {
            var tmp = hash(s1, i, i + m);
            if (tmp == hash_s2) {
                return i;
            }
        }

        return -1;
    }

    private long hash(String s, int l, int r) {
        // calculate hash of s
        long ans = 0;
        for (int i=l; i<r; i++) {
            ans = ans * base + s.charAt(i) - 'a' + 1;
        }
        return ans;
    }

}