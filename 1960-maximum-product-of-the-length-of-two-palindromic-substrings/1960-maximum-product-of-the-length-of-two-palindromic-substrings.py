class Solution:
    def maxProduct(self, s: str) -> int:
        N = len(s)
        
        # P[i]
        P = [1]*N
        maxRight, maxCenter = -1,-1
        for i in range(N):
            r = 1
            if i<maxRight:
                j = maxCenter*2-i
                r = min(P[j], maxRight-i)
            while i-r>=0 and i+r<N and s[i-r] == s[i+r]:
                r += 1
            P[i] = r-1
            if i+P[i] > maxRight:
                maxRight = i+P[i]
                maxCenter = i
                
        # left[i], right[i]
        left = [0]*N
        right = [0]*N        
        left[0] = 1        
        j = 0
        for i in range(1, N):
            while j<N and j+P[j]<i:
                j += 1
            left[i] = max(left[i-1], (i-j)*2+1)
        j = N-1
        right[N-1] = 1
        for i in range(N-2, -1, -1):
            while j>=0 and j-P[j]>i:
                j -= 1
            right[i] = max(right[i+1], (j-i)*2+1)
        
        ans = -1
        print(left)
        print(right)
        for i in range(0,N-1):
            ans = max(ans, left[i]*right[i+1])
        return ans
            