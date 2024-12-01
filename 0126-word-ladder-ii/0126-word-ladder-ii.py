class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:                    
        def bfs(start,end):
            find = False
            curLevel = [start]
            nextLevel = []
            while len(curLevel)>0:
                dict.difference_update(curLevel)
                for word in curLevel:
                    newword = list(word)
                    for i in range(len(word)):
                        old = newword[i]
                        for ch in "abcdefghijklmnopqrstuvwxyz":
                            newword[i] = ch
                            nw = "".join(newword)
                            if nw in dict and nw != word:
                                if nw == end:
                                    find = True
                                graph[nw].append(word)
                                if nw not in nextLevel:
                                    nextLevel.append(nw)
                        newword[i] = old
                if find:
                    return True                
                curLevel = nextLevel.copy()
                nextLevel.clear()
            return False

            
        def dfs(word, end):
            path.insert(0, word)
            if word == end:
                ans.append(path.copy())
            if word in graph:
                for nxt in graph[word]:
                    dfs(nxt, end)
            path.remove(word)
        
        ans = []
        graph = defaultdict(list)
        path = []
        dict = set(wordList)
        
        if (endWord not in dict):
            return ans
        if (bfs(beginWord, endWord)):
            dfs(endWord, beginWord)
        return ans