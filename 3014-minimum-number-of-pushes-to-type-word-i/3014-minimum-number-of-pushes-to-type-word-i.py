class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        lst = count.most_common()
        ret = 0
        i = 0
        for ch,freq in lst:
            ret += (1+i//8)*freq
            i += 1
        return ret 
