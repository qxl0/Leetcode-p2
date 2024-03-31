class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ret = numBottles
        emptyBottles = numBottles
        while emptyBottles>=numExchange:
            ret += 1
            emptyBottles -= numExchange
            emptyBottles += 1 
            numExchange += 1
        return ret 