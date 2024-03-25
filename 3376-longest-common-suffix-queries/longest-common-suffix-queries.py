class TrieNode:
    def __init__(self):
        self.children = dict()
        self.cur = (inf,None)        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, i,word):
        node = self.root
        node.cur = (-1,None)
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if not node.cur[1] or len(node.cur[1])>len(word) or len(node.cur[1])==len(word) and node.cur[0]>i:
                node.cur = (i,word)

    def get(self, prefix: str):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return node.cur[0]
            node = node.children[c]
        return node.cur[0]
    
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = Trie()
        shortest_len = min(len(w) for w in wordsContainer)
        idx_shortest = -1
        for i in range(len(wordsContainer)):
            if len(wordsContainer[i])==shortest_len:
                idx_shortest = i
                break 
        for i,word in enumerate(wordsContainer):
            root.insert(i,word[::-1])
        ans = []
        for q in wordsQuery:
            idx = root.get(q[::-1]) 
            ans.append(idx if idx!=-1 else idx_shortest)
        return ans 