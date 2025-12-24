class Solution:
    def maxProduct(self, s: str) -> int:
        maxCenter,maxRight = -1,-1
        N = len(s)
        P = [1]*N
        for i in range(N):
            r = 1
            if maxRight>i:
                j = 2*maxCenter - i
                r = min(P[j], maxRight - i)
            while i-r>=0 and i+r<N and s[i-r]==s[i+r]:
                r += 1
            P[i] = r-1
            if i+P[i]>maxRight:
                maxCenter = i
                maxRight = i+P[i]
        print(P)
        left = [0]*N
        right = [0]*N
        left[0] = 1
        j = 0
        for i in range(1,N):
            while j<N and j+P[j]<i:
                j += 1
            left[i] = max(left[i-1], (i-j)*2+1)
        j = N-1
        right[N-1] = 1
        for i in range(N-2,-1,-1):
            while j>=0 and j-P[j]>i:
                j -= 1
            right[i] = max(right[i+1], (j-i)*2+1)
        ans = -1
        for i in range(0, N-1):
            print(f"i={i},l={left[i]},r={right[i+1]}")
            ans = max(ans, left[i]*right[i+1])
        return ans






# x x x x x x x x | x x x x x x x x 
#               i
# L[i]: length of max palindromic string s[0:i]
# R[i]: length of max palindromic string s[i:n-1]

# L[i]*R[i+1]

# 2 <= s.length <= 10**5
# O(n*logn)
# ------------
# 1. P[i]: max radius s[i] center palindromic string 
# 2. L[i]: 
# x x x x x x x x i} x x x x x x x
#       ----- j -----
# L[i]: 
#    max(L[i-1], (i-j)*2+1)

#    for i in range(N):
#      while j<N and j+P[j]>i:
#         L[i] = max(L[i-1], (i-j)*2+1) 
# 3. loop through i:
#   ans = max(ans, L[i]*R[i+1])