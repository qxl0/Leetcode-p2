class Solution:
    index = 0
    def decodeString(self, s: str) -> str:        
        ret = []
        while self.index < len(s) and s[self.index] != ']':
            if not s[self.index].isdigit():
                ret.append(s[self.index])
                self.index += 1
            else:
                k = 0
                while self.index < len(s) and s[self.index].isdigit():
                    k = k * 10 + int(s[self.index])
                    self.index += 1
                self.index += 1  #ignore [
                decodestr = self.decodeString(s)

                self.index += 1   #ignore ]
                ret.append(decodestr*k)
        return "".join(ret)
        