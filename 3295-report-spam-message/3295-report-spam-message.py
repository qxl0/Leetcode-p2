class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = Counter(bannedWords)
        ret = 0
        for word in message:
            if count[word]>0:
                ret += 1
            if ret >= 2:
                return True
        return False
