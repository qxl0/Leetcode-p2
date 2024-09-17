class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)        
        trie = Trie()
        for word in words:
            trie.add(word)
        # dp(i): minimum cost to form target i to end 
        dp = [inf]*(n+1)
        dp[n]=0
        for i in range(n-1,-1,-1):
            node = trie.root
            for j in range(i,n):
                if target[j] in node.children:
                    node = node.children[target[j]]
                else:
                    break
                dp[i] = min(dp[i], 1 + dp[j+1])
        return dp[0] if dp[0]<inf else -1
        
