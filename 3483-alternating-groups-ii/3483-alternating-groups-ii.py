class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        A = colors + colors
        ret = 0        
        i = 0
        while i<n:
            c = A[i]
            j = i+1            
            while j<n+k-1 and A[j]==1-c:
                j += 1
                c = 1-c 
            # when stop 
            # i.... j
            if j-i>=k:
                ret += j-i-k+1
            i = j
        return ret 
        


