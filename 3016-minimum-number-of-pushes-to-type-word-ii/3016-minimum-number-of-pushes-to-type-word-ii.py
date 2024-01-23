class Solution:
    def minimumPushes(self, word: str) -> int:
        ret = 0
        i = 0
        for ch,freq in Counter(word).most_common():
            ret += (1+i//8)*freq
            i += 1
        return ret
            