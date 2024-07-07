class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ret = []
        n = len(s)
        for i in range(n):
            ret.append(s[(i+k)%n])
        return "".join(ret)