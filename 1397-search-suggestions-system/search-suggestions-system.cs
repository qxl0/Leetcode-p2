public class TrieNode {
    public TrieNode[] next = new TrieNode[26];        
    public bool isword = false;
    public List<string> wordlist = new();
    public TrieNode() {
        Array.Fill(next, null);
    }    
    
    public void Insert(string word) {
        TrieNode node = this;
        foreach (var ch in word) {
            if (node.next[ch-'a'] == null) {
                node.next[ch-'a'] = new TrieNode();
            }                      
            node = node.next[ch-'a'];

            // add word to List            
            node.wordlist.Add(word);  
            // sort 
            node.wordlist.Sort();

            // remove if over 3
            if (node.wordlist.Count>3)
                node.wordlist.RemoveAt(node.wordlist.Count-1);
        }
        node.isword = true;
    }
}

public class Solution {
    public IList<IList<string>> SuggestedProducts(string[] products, string searchWord) {
        TrieNode root = new TrieNode();
        foreach (var word in products) {
            root.Insert(word);
        }
        List<IList<string>> ans = new();
        TrieNode node = root;
        for (var i=0;i<searchWord.Length;i++) {
            char ch = searchWord[i];
            if (node.next[ch-'a']==null){
                for (int j=i;j<searchWord.Length;j++) {
                    ans.Add(new List<string>());
                }
                break;
            }
            node = node.next[ch-'a'];

            List<string> lst= new List<string>(node.wordlist);
            ans.Add(lst);
        }

        return ans;
    }
}