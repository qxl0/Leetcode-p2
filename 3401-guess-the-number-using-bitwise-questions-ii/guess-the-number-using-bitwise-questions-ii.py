# Definition of commonBits API.
# def commonBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:
        base = commonBits(0)
        ret = 0
        i = 0
        while i<30:
            count = commonBits(1<<i)
            if count>base:
                ret |= (1<<i)            
            commonBits(1<<i)
            i += 1
        return ret

