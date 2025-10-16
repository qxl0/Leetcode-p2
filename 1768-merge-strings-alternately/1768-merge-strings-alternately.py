class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = []
        i,j = 0, 0
        n1,n2 = len(word1),len(word2)
        while i<n1 and j<n2:
            ret.append(word1[i])
            ret.append(word2[j])
            i += 1
            j += 1
        while i<n1:
            ret.append(word1[i])
            i += 1
        while j<n2:
            ret.append(word2[j])
            j += 1
        return ''.join(ret)