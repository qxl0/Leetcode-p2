/**
 * Definition for an infinite stream.
 * class InfiniteStream {
 *     public InfiniteStream(int[] bits);
 *     public int Next();
 * }
 */
public class Solution {
    public int FindPattern(InfiniteStream stream, int[] pattern) {
        int[] lps = preprocess(pattern);
        int n = pattern.Length;

        int i = 0, j = 0;
        int cur = stream.Next();
        
        while (i<n) {
            if (cur == pattern[i])
            {
                i += 1;
                cur = stream.Next();
                j += 1;
            }
            else {
                if (i==0){
                    cur = stream.Next();
                    j += 1;
                }
                else {
                    i = lps[i-1];
                }
            }
            if (i==n)
                return j-n;
        }
        return 0;
    }

    private int[] preprocess(int[] pattern) {
        int n = pattern.Length;
        int[] lps = new int[n];
        lps[0] = 0;
        for (int i=1;i<n;i++) {
            int j = lps[i-1];
            while (j>0 && pattern[i]!=pattern[j]) {
                j = lps[j-1];
            }
            lps[i] = j + (pattern[i]==pattern[j] ? 1:0);
        }

        return lps;
    }
}