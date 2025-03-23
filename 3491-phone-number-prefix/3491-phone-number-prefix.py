class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        def isprefix_word(t,s):
            w = numbers[t]
            word = numbers[s]
            i,j=0,0
            while i<len(w) and j<len(word) and w[i]==word[j]:
                i += 1
                j += 1
            if i==len(w):
                return True
            return False
        def isprefix(i):
            for j in range(len(numbers)):
                if j==i:continue
                if isprefix_word(i,j):
                    return True
            return False
        for i in range(len(numbers)):
            if isprefix(i):
                return False
        return True