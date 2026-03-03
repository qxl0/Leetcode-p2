class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        Set = set(wordDict)
        ans = []
        def dfs(i, path):
            if i==n:
                ans.append(' '.join(path))
            for j in range(i, n):
                if s[i:j+1] in Set:
                      dfs(j+1, path + [s[i:j+1]])
        dfs(0, [])
        return ans