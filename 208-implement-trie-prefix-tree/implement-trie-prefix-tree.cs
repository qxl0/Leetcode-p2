public class Trie {
    public class TrieNode {
        public TrieNode[] next = new TrieNode[26];        
        public bool isword = false;
        public TrieNode() {
            Array.Fill(next, null);
        }
    }
    
    TrieNode root;
    public Trie() {
        root = new TrieNode();
    }
    
    public void Insert(string word) {
        TrieNode node = root;
        foreach (var ch in word) {
            if (node.next[ch-'a'] == null) {
                node.next[ch-'a'] = new TrieNode();
            }
            node = node.next[ch-'a'];
        }
        node.isword = true;
    }
    
    public bool Search(string word) {
        TrieNode node = root;
        foreach (var ch in word) {
            if (node.next[ch-'a'] == null){
                return false;
            }
            node = node.next[ch-'a'];
        }
        return node.isword;
    }
    
    public bool StartsWith(string prefix) {
        TrieNode node = root;
        foreach (var ch in prefix) {
            if (node.next[ch-'a']==null) {
                return false;
            }
            node = node.next[ch-'a'];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.Insert(word);
 * bool param_2 = obj.Search(word);
 * bool param_3 = obj.StartsWith(prefix);
 */