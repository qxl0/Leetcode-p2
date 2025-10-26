class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ret = []
        for ch in operations:
            if ch == '+':
                ret.append(ret[-1] + ret[-2])
            elif ch == 'D':
                ret.append(ret[-1]*2)
            elif ch == 'C':
                ret.pop()
            else:
                ret.append(int(ch))
        return sum(ret)