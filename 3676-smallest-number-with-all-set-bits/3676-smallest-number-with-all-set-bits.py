class Solution:
    def smallestNumber(self, n: int) -> int:
        h = 0
        for i in range(31,-1,-1):
            if (n>>i)&1==1:
                h = i
                break
        # h stands for the highest bit pos where n at it -> 1
        return 2**(i+1)-1