class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        count = Counter(s)
        ret = []
        for ch in s:
            if count[ch]>=k:
                continue
            ret.append(ch)
        return "".join(ret)