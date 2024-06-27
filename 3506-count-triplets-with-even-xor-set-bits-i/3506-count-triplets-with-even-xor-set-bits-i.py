class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        return sum(1 if bin(x^y^z).count('1')%2==0 else 0 for x in a for y in b for z in c)
