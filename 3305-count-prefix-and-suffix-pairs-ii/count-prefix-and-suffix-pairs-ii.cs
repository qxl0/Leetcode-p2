public class TrieNode {
    public TrieNode[] next = new TrieNode[26];
    public int count;        
    public TrieNode() {
        for (int i=0;i<26;i++){
            this.next[i] = null;
        }
        count = 0;
    }
    }
public class Solution {
    
    TrieNode root = new TrieNode();
    public long CountPrefixSuffixPairs(string[] words) {        
        long ret = 0;
        for (int i=words.Length-1;i>=0;i--){
            ret += find(root, words[i]);

            int n = words[i].Length;
            int[] lcp = LongestPrefix(words[i]);
            HashSet<int> set = new HashSet<int>();
            int len = lcp[n-1];
            while (len!=0) {
                set.Add(len);
                len = lcp[len-1];
            }
            set.Add(n);

            add(root, words[i], set);
        }
        return ret;
    }

    private void add(TrieNode root, string word, HashSet<int> set) {
        TrieNode node = root;
        int n = word.Length;

        for (int i=0;i<n;i++) {
            if (node.next[word[i]-'a'] == null) {
                node.next[word[i]-'a'] = new TrieNode();            
            }
            node = node.next[word[i]-'a'];
            if (set.Contains(i+1)) {
                node.count += 1;
            }
        }
    }
    private int find(TrieNode root, string word) {
        // 
        TrieNode node = root;
        int n = word.Length;

        for (int i=0;i<n;i++) {
            if (node.next[word[i]-'a'] == null) {
                return 0;
            }
            node = node.next[word[i]-'a'];
        }
        return node.count;
    }

    private int[] LongestPrefix(string word) {
        int n = word.Length;
        int[] dp = new int[n];

        dp[0] = 0;

        for (int i=1;i<n;i++) {
            int j = dp[i-1];
            while (j>0 && word[i]!=word[j]) {
                j = dp[j-1];
            }
            dp[i] = j + (word[i]==word[j]?1:0);
        }
        return dp;
    }
}