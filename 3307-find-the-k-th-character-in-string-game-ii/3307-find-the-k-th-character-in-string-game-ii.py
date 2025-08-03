class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        shift = 0
        t = 0
        length = 1        
        while length < k:
            length *= 2
            t += 1
        # now we know we need 
        for i in range(t-1,-1,-1):
            if k > length//2:
                if operations[i]==0:
                    k -= length//2
                else:
                    k -= length//2
                    shift += 1
            length //= 2
        return chr(ord('a') + shift%26)