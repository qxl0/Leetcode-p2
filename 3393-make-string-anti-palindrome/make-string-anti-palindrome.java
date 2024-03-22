class Solution {
    public String makeAntiPalindrome(String s) {
        char[] ans = s.toCharArray();
        Arrays.sort(ans);

        int n = ans.length;
        int j = n/2;
        for (int i=n/2-1;i>=0;i--) {
            if (ans[i]!=ans[n-1-i])
                break;
            // swap n-1-i with j
            while (j<n && ans[j]==ans[n-1-i]) {
                j++;
            }
            if (j>=n) return "-1";
            // swap 
            char tmp = ans[j];
            ans[j] = ans[n-1-i];
            ans[n-1-i] = tmp;
            j += 1;
        }

        return new String(ans);
    }
}