public class Solution {
    int[][] memo;
    int m,n;
    public int MinDistance(string word1, string word2) {
        m = word1.Length;
        n = word2.Length;
        memo = new int[m][];
        for (int i=0;i<m;i++) {
            memo[i] = new int[n];
            Array.Fill(memo[i], int.MaxValue);
        }
            
        return minDistanceRecur(word1,word2,word1.Length-1,word2.Length-1);
    }

    private int minDistanceRecur(string w1, string w2, int idx1, int idx2) {        
        if (idx1<0) {
            return idx2+1;
        }
        else if (idx2 < 0) {
            return idx1+1;
        }
        
        if (memo[idx1][idx2]!=int.MaxValue) 
            return memo[idx1][idx2];

        if (w1[idx1]!=w2[idx2]) {
            int x = minDistanceRecur(w1,w2, idx1-1, idx2-1);
            int y =  minDistanceRecur(w1,w2, idx1, idx2-1);
            int z =  minDistanceRecur(w1,w2, idx1-1, idx2);
            memo[idx1][idx2] =  Math.Min(x, Math.Min(y,z)) + 1;
            return memo[idx1][idx2];
        }
        else {
            memo[idx1][idx2] = minDistanceRecur(w1,w2,idx1-1,idx2-1);
            return memo[idx1][idx2];
        }
        
    }
}