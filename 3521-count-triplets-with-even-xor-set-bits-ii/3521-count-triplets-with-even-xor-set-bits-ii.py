class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def bitsets(arr):
            return [1 if bin(x)[2:].count('1')%2==1 else 0 for x in arr]
        ap = bitsets(a)
        bp = bitsets(b)
        cp = bitsets(c)
        odd_bp = sum(y==0 for y in bp)
        even_bp = sum(y for y in bp)
        odd_cp = sum(z==0 for z in cp)
        even_cp = sum(z for z in cp)
        # 3 arrs:          
        ret = 0        
        for x in ap:
            if x==0: # even
                ret += odd_bp*odd_cp  # odd, odd 
                ret += even_bp*even_cp
            else: # odd --> odd,even, or even,odd
                ret += odd_bp*even_cp
                ret += even_bp*odd_cp
        return ret
