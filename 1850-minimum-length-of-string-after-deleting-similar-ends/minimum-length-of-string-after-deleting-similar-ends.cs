public class Solution {
    public int MinimumLength(string s) {
        int i=0,j=s.Length-1;

        while (i<j) {
            if (s[i]!=s[j])
                return j-i+1;
            int k = i+1;
            while (k<j && s[k]==s[j]) {
                k += 1;
            }

            i = k;
            
            int t = j-1;
            while (t>i && s[t]==s[j]) {
                t -= 1;
            }

            j = t;
        }

        return j-i+1;
    }
}