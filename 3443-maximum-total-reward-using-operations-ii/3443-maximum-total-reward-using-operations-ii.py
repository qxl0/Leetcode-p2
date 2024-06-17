
class Solution:
    def maxTotalReward(self, A: List[int]) -> int:        
        b = 1<<0
        for v in sorted(set(A)):
            b |= (b&((1<<v)-1))<<v
        return b.bit_length()-1

        