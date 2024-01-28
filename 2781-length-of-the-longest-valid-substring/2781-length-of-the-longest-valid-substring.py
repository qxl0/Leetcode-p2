class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        fset = set(forbidden)
        n = len(word)
        ret = 0
        left = 0
        for i in range(n):
            for j in range(max(i-10,left),i+1):
                if word[j:i+1] in fset:
                    left = j+1
            ret = max(ret, i-left+1)
        return ret 
                