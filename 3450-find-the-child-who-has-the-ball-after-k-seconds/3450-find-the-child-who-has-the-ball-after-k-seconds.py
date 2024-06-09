class Solution:
    def numberOfChild(self, n: int, k: int) -> int:        
        # (n-1)*2 -> 0 again 
        k = k % (2*(n-1))
        if k<n:
            return k
        if k>=n:
            k -= n-1
            return n-1-k

