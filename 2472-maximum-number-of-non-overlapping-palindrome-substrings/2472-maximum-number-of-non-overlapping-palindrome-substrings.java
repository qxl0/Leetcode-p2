class Solution {
    char[] ss;
    char[] s;
    public int MAXN = 2001;
    public int[] p = new int[MAXN<<1];
    public int N;
    public int maxPalindromes(String str, int k) {
        // convert abaczazccc to #a#b#a#....
        this.s = str.toCharArray();
        int n = s.length;
        N = 2*n+1;
        ss = new char[N+1];
        for (int i=0; i<n; i++) {
            ss[2*i] = '#';
            ss[2*i+1] = s[i];
        }
        ss[2*n] = '#';

        // do manacher
        int ans = 0, next = 0;
        while ((next = find(next, k)) != -1) {
            ans++;
        }

        return ans;
    }

    private int find(int l, int k) {
        // from l, ss[l] = '#'
        // once find palindrome radius >=k , return -1 otherwise 
        // 1. #a#b#a#a#a#  k=2
        //       3  ^  --> return 6(#) rather than 5(a)
        // 2. #a#a#a#b#a#a#, k=2
        //      2 ^   --> return 4(#) directly
        for (int i=l, c=l, r=l, len; i<N; i++) {
            len = r>i ? Math.min(p[2*c-i], r-i) : 1;
            while (i+len<N && i-len>=l && ss[i+len] == ss[i-len]) {
                if (++len>k) {
                    return i+k+(ss[i+k]!='#'? 1:0);
                }
            }

            if (i + len > r) {
                r = i + len;
                c = i;
            }      
            p[i] = len;      
        }
        return -1;
    }
}